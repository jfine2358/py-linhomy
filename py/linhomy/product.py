'''For computing flag vector of product in various bases


>>> product_formula(2,3)
array([[[  1,  12,  30,  34, 120,  21, 120, 180],
        [  1,  15,  39,  44, 159,  26, 159, 240],
        [  1,  18,  45,  48, 180,  27, 180, 270]],
<BLANKLINE>
       [[  1,  16,  40,  44, 160,  26, 160, 240],
        [  1,  20,  52,  57, 212,  32, 212, 320],
        [  1,  24,  60,  62, 240,  33, 240, 360]]])
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import numpy

from .fibonacci import FIB_WORDS
from .data import P_flag
from .matrices import fib_zeros_array


def word_from_IC(s):

    return b''.join(
        {'C': b'\x01', 'D': b'\x02'}[c]
        for c in s.replace('IC', 'D')
    )


def index_from_IC(s):

    return FIB_WORDS.index(word_from_IC(s))


def change_product_basis(product_triple, a, b, c):

    n_a, n_b, n_c = product_triple.shape
    value = numpy.zeros(product_triple.shape, int)
    rows = numpy.reshape(product_triple, (n_a * n_b, n_c))

    for i in range(n_a):
        for j in range(n_b):

            # Convolve the columns to get coefficients.
            coefficients = [
                r * s
                # White space is to slow reader - pay attention.
                for r in a[ :, i]
                for s in b[ :, j]
            ]

            join_ic = sum(
                c * r
                for (c, r) in zip(coefficients, rows)
            )

            join_cd = numpy.dot(c, join_ic)
            value[i, j, : ] = join_cd

    return value



# TODO: Check this - it only looks right.
def product_formula(n, m):

    value = fib_zeros_array(n, m, n + m)

    for line in P_flag[n + m]:

        pieces = line.split()
        keys, column = pieces[0], tuple(map(int, pieces[1:]))
        keys = keys[2:-1].split(',')

        i = index_from_IC(keys[0])[1]
        j = index_from_IC(keys[1])[1]

        if len(keys[0]) == n:
            value[i, j, : ] = column

        if len(keys[0]) == m:
            value[j, i, : ] = column


    return value
