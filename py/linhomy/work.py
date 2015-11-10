'''Assemble what we have and try it out

Sadly we get an error.  But at n=6 so might be easy to fix.  In
winter 2014-15 calculations we got past 6.

>>> doit_G(2, 3)
array([[[1, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1]],
<BLANKLINE>
       [[0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1]]])

>>> doit_G(3, 3)
array([[[ 1,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1],
        [ 0,  1,  1,  1,  0,  1,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0]],
<BLANKLINE>
       [[ 0,  1,  1,  1,  0,  1,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0, -2,  0,  1,  2,  1,  0,  0,  0,  0,  0],
        [ 0,  0,  1,  1,  0,  0,  0,  0,  0,  1,  1,  0,  0]],
<BLANKLINE>
       [[ 0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0],
        [ 0,  0,  1,  1,  0,  0,  0,  0,  0,  1,  1,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1]]])


>>> for n in range(2, 11):
...     for m in range(1, n):
...         if 2 * m <= n:
...             print(n, m, stats(n - m, m))
...
2 1 [(1, 2)]
3 1 [(0, 3), (1, 3)]
4 1 [(0, 9), (1, 6)]
4 2 [(0, 14), (1, 6)]
5 1 [(0, 30), (1, 10)]
5 2 [(0, 36), (1, 12)]
6 1 [(0, 87), (1, 17)]
6 2 [(0, 108), (1, 22)]
6 3 [(-2, 1), (0, 87), (1, 28), (2, 1)]
7 1 [(0, 244), (1, 29)]
7 2 [(0, 298), (1, 38)]
7 3 [(-2, 3), (0, 257), (1, 53), (2, 2)]
8 1 [(0, 668), (1, 46)]
8 2 [(0, 818), (1, 66)]
8 3 [(-2, 7), (-1, 5), (0, 699), (1, 100), (2, 5)]
8 4 [(-2, 10), (0, 731), (1, 101), (2, 8)]
9 1 [(0, 1790), (1, 80)]
9 2 [(0, 2202), (1, 108)]
9 3 [(-3, 2), (-2, 15), (-1, 18), (0, 1913), (1, 184), (2, 12), (3, 1)]
9 4 [(-4, 1), (-2, 23), (-1, 15), (0, 1944), (1, 197), (2, 19), (4, 1)]
10 1 [(0, 4773), (1, 122)]
10 2 [(0, 5868), (1, 184)]
10 3 [(-3, 5), (-2, 32), (-1, 51), (0, 5166), (1, 325), (2, 26), (3, 2)]
10 4 [(-4, 5), (-3, 7), (-2, 50), (-1, 52), (0, 5244), (1, 374), (2, 47), (3, 2), (4, 3), (6, 1)]
10 5 [(-4, 9), (-2, 59), (-1, 74), (0, 5096), (1, 392), (2, 57), (4, 8), (6, 1)]
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import itertools
import numpy
from collections import Counter

from .matrices import G_from_FLAG
from .matrices import IC_from_G

from .product import product_formula
from .product import change_product_basis



def doit_G(n, m):

    return change_product_basis(
        product_formula(n, m),
        IC_from_G[n],
        IC_from_G[m],
        G_from_FLAG[n+m]
    )


def stats(n, m):

    matrix = doit_G(n, m)
    counter = Counter(matrix.flatten())
    counts = sorted(counter.items())
    return counts
