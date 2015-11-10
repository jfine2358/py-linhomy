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
7 1 [(0, 247), (1, 26)]
7 2 [(0, 305), (1, 31)]
7 3 [(-1, 1), (0, 271), (1, 41), (2, 2)]
8 1 [(-1, 1), (0, 670), (1, 43)]
8 2 [(-1, 1), (0, 830), (1, 53)]
8 3 [(-2, 1), (-1, 4), (0, 729), (1, 78), (2, 4)]
8 4 [(-2, 2), (-1, 6), (0, 765), (1, 69), (2, 8)]
9 1 [(-1, 2), (0, 1797), (1, 71)]
9 2 [(-1, 2), (0, 2222), (1, 86)]
9 3 [(-2, 3), (-1, 15), (0, 1978), (1, 142), (2, 6), (3, 1)]
9 4 [(-3, 1), (-2, 6), (-1, 18), (0, 2021), (1, 137), (2, 17)]
10 1 [(-1, 3), (0, 4778), (1, 114)]
10 2 [(-1, 6), (0, 5902), (1, 144)]
10 3 [(-4, 1), (-3, 1), (-2, 7), (-1, 42), (0, 5292), (1, 248), (2, 14), (3, 2)]
10 4 [(-4, 1), (-3, 1), (-2, 16), (-1, 64), (0, 5403), (1, 263), (2, 35), (3, 2)]
10 5 [(-4, 1), (-3, 2), (-2, 21), (-1, 57), (0, 5297), (1, 275), (2, 43)]
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
