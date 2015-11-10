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
        [ 0,  0,  0, -2,  0,  1,  2,  1,  0,  0, -2,  0,  0],
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
6 3 [(-2, 2), (0, 86), (1, 28), (2, 1)]
7 1 [(0, 245), (1, 28)]
7 2 [(0, 298), (1, 38)]
7 3 [(-2, 5), (0, 255), (1, 53), (2, 2)]
8 1 [(0, 668), (1, 46)]
8 2 [(0, 820), (1, 64)]
8 3 [(-2, 11), (-1, 7), (0, 693), (1, 100), (2, 5)]
8 4 [(-4, 1), (-2, 12), (0, 728), (1, 101), (2, 8)]
9 1 [(0, 1795), (1, 75)]
9 2 [(0, 2204), (1, 106)]
9 3 [(-3, 1), (-2, 23), (-1, 19), (0, 1911), (1, 179), (2, 11), (3, 1)]
9 4 [(-4, 4), (-3, 1), (-2, 26), (-1, 18), (0, 1935), (1, 196), (2, 19), (4, 1)]
10 1 [(0, 4773), (1, 122)]
10 2 [(0, 5878), (1, 174)]
10 3 [(-3, 3), (-2, 46), (-1, 57), (0, 5153), (1, 320), (2, 26), (3, 2)]
10 4 [(-6, 1), (-5, 1), (-4, 8), (-3, 3), (-2, 62), (-1, 50), (0, 5246), (1, 363), (2, 45), (3, 2), (4, 3), (6, 1)]
10 5 [(-6, 1), (-4, 14), (-3, 2), (-2, 67), (-1, 88), (0, 5070), (1, 388), (2, 57), (4, 8), (6, 1)]
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
