'''


>>> FLAG_from_IC[2]
array([[1, 1],
       [3, 4]])

The flag vector of ICC is [1, 6, 9].
>>> numpy.dot(FLAG_from_IC[3], [0, 0, 1])
array([1, 6, 9])

>>> FLAG_from_IC[3]
array([[1, 1, 1],
       [4, 5, 6],
       [6, 8, 9]])

>>> IC_from_FLAG[3]
array([[ 3,  1, -1],
       [ 0, -3,  2],
       [-2,  2, -1]])

>>> numpy.dot(FLAG_from_IC[3], IC_from_FLAG[3])
array([[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]])

Each column is an expansion, with power of 2 ones.
>>> CD_from_IC[3]
array([[1, 1, 1],
       [0, 1, 0],
       [0, 0, 1]])

Expansion of [ICIC is CCCC, CCD, DCC, DD].
>>> numpy.dot(CD_from_IC[4], [0, 0, 0, 0, 1])
array([1, 1, 0, 1, 1])


>>> C_in_CD[3]
array([[1, 0, 0],
       [0, 1, 0],
       [0, 0, 1],
       [0, 0, 0],
       [0, 0, 0]])

>>> D_in_CD[3]
array([[0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [0, 0, 0],
       [1, 0, 0],
       [0, 1, 0],
       [0, 0, 1]])
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import itertools
import numpy

from .fibonacci import FIBONACCI
from .fibonacci import FIB_WORDS
from .tools import grow_list
from .data import IC_flag


def linalg_int_inv(matrix):
    '''Compute the integer inverse of a matrix.'''

    shape = matrix.shape

    # Compute inverse and cast to integer matrix.
    tmp = numpy.linalg.inv(matrix)
    inverse = numpy.zeros(shape, int)
    inverse = numpy.rint(tmp, inverse)

    # Check we actually have the inverse.
    expect = numpy.eye(shape[0], dtype=int)
    actual = numpy.dot(matrix, inverse)
    if not numpy.array_equal(actual, expect):
        raise ValueError

    return inverse


def fib_zeros_array(*argv):
    '''Return array with shape (FIB[argv[0] + 1], ...).
    '''

    shape = tuple(FIBONACCI[n+1] for n in argv)
    value = numpy.zeros(shape, int)
    return value

def invert_grow_list(matrices):

    @grow_list
    def inverse(self):

        deg = len(self)
        matrix = matrices[deg]
        return linalg_int_inv(matrix)

    return inverse

@grow_list
def FLAG_from_IC(self):

    deg = len(self)
    value = fib_zeros_array(deg, deg)

    for i, line in enumerate(IC_flag[deg]):
        value[:,i] = list(map(int, line.split()[1:]))

    return value

IC_from_FLAG = invert_grow_list(FLAG_from_IC)


@grow_list
def CD_from_IC(self):

    # Prepare for the double loop.
    deg = len(self)
    value = fib_zeros_array(deg, deg)
    words = FIB_WORDS[deg]
    index = words.index

    # The columns give the CD expansion of an IC word.
    for j, ic_word in enumerate(words):

        # Compute factors needed for the expansion.
        factors = []
        for ones in ic_word.split(b'\x02'):
            if ones:
                factors.append((ones,))
            factors.append((b'\x01\x01', b'\x02'))
        del factors[-1]

        # Iterate of the product of the factors.
        for w in itertools.product(*factors):
            cd_word = b''.join(w)
            i = index(cd_word)
            value[i,j] += 1     # Record the contribution.

    return value

IC_from_CD = invert_grow_list(CD_from_IC)


@grow_list
def C_in_CD(self):

    # Prepare for the single loop.
    deg = len(self)
    value = fib_zeros_array(deg + 1, deg)
    words = FIB_WORDS[deg]
    index = FIB_WORDS[deg + 1].index

    # The columns give C in the CD basis.
    for j, word in enumerate(words):

        c_word = b'\x01' + word
        i = index(c_word)
        value[i,j] += 1     # Record the contribution.

    return value


@grow_list
def D_in_CD(self):

    # Prepare for the single loop.
    deg = len(self)
    value = fib_zeros_array(deg + 2, deg)
    words = FIB_WORDS[deg]
    index = FIB_WORDS[deg + 2].index

    # The columns give D in the CD basis.
    for j, word in enumerate(words):

        d_word = b'\x02' + word
        i = index(d_word)
        value[i,j] += 1     # Record the contribution.

    return value
