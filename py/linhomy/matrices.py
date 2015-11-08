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

'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import numpy

from .fibonacci import FIBONACCI
from .tools import grow_list
from .data import IC_flag

def fib_zeros_array(*argv):
    '''Return array with shape (FIB[argv[0] + 1], ...).
    '''

    shape = tuple(FIBONACCI[n+1] for n in argv)
    value = numpy.zeros(shape, int)
    return value


@grow_list
def FLAG_from_IC(self):

    deg = len(self)
    value = fib_zeros_array(deg, deg)

    for i, line in enumerate(IC_flag[deg]):
        value[:,i] = list(map(int, line.split()[1:]))

    return value
