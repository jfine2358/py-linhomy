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
8 1 [(0, 669), (1, 45)]
8 2 [(0, 829), (1, 53), (2, 2)]
8 3 [(-1, 3), (0, 727), (1, 81), (2, 5)]
8 4 [(-2, 1), (-1, 2), (0, 766), (1, 73), (2, 8)]
9 1 [(-1, 4), (0, 1790), (1, 75), (2, 1)]
9 2 [(0, 2218), (1, 90), (2, 2)]
9 3 [(-2, 1), (-1, 9), (0, 1971), (1, 150), (2, 10), (3, 4)]
9 4 [(-2, 2), (-1, 12), (0, 2025), (1, 145), (2, 15), (3, 1)]
10 1 [(-2, 1), (-1, 3), (0, 4768), (1, 122), (2, 1)]
10 2 [(-2, 1), (-1, 5), (0, 5889), (1, 150), (2, 6), (3, 1)]
10 3 [(-4, 2), (-2, 5), (-1, 29), (0, 5271), (1, 272), (2, 22), (3, 5), (4, 1)]
10 4 [(-5, 1), (-3, 1), (-2, 5), (-1, 39), (0, 5414), (1, 280), (2, 36), (3, 6), (4, 3)]
10 5 [(-3, 2), (-2, 6), (-1, 43), (0, 5311), (1, 293), (2, 39), (3, 2)]
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
