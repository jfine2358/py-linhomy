'''Assemble what we have and try it out

Sadly we get an error.  But at n=6 so might be easy to fix.  In
winter 2014-15 calculations we got past 6.

>>> doit_G(2, 3)
array([[[1, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1]],
<BLANKLINE>
       [[0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1]]])

>>> doit_G(3, 3)
array([[[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1],
        [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0]],
<BLANKLINE>
       [[0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 2, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]],
<BLANKLINE>
       [[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]]])

>>> for n in range(2, 11):
...     for m in range(1, n):
...         if 2 * m <= n:
...             print(n, m, stats(n - m, m))
...
2 1 [(1, 2)]
3 1 [(0, 3), (1, 3)]
4 1 [(0, 9), (1, 6)]
4 2 [(0, 14), (1, 6)]
5 1 [(0, 31), (1, 9)]
5 2 [(0, 37), (1, 11)]
6 1 [(0, 88), (1, 16)]
6 2 [(0, 112), (1, 18)]
6 3 [(0, 92), (1, 24), (2, 1)]
7 1 [(0, 246), (1, 27)]
7 2 [(0, 305), (1, 31)]
7 3 [(0, 271), (1, 42), (2, 2)]
8 1 [(-1, 2), (0, 668), (1, 44)]
8 2 [(-1, 1), (0, 829), (1, 53), (2, 1)]
8 3 [(-2, 1), (-1, 2), (0, 729), (1, 80), (2, 4)]
8 4 [(-2, 2), (-1, 2), (0, 767), (1, 73), (2, 6)]
9 1 [(-1, 2), (0, 1796), (1, 72)]
9 2 [(-1, 4), (0, 2217), (1, 89)]
9 3 [(-4, 1), (-2, 3), (-1, 10), (0, 1976), (1, 146), (2, 8), (3, 1)]
9 4 [(-2, 6), (-1, 12), (0, 2024), (1, 144), (2, 14)]
10 1 [(-2, 1), (-1, 3), (0, 4776), (1, 114), (2, 1)]
10 2 [(-1, 7), (0, 5899), (1, 145), (2, 1)]
10 3 [(-4, 5), (-3, 1), (-2, 7), (-1, 38), (0, 5280), (1, 256), (2, 18), (3, 2)]
10 4 [(-5, 1), (-4, 2), (-3, 2), (-2, 15), (-1, 51), (0, 5403), (1, 274), (2, 33), (3, 4)]
10 5 [(-4, 1), (-2, 21), (-1, 45), (0, 5303), (1, 289), (2, 37)]

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
