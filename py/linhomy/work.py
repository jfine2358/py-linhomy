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
7 3 [(0, 273), (1, 40), (2, 2)]
8 1 [(0, 671), (1, 43)]
8 2 [(0, 831), (1, 53)]
8 3 [(-1, 2), (0, 735), (1, 75), (2, 4)]
8 4 [(-2, 1), (-1, 2), (0, 772), (1, 69), (2, 6)]
9 1 [(0, 1798), (1, 72)]
9 2 [(0, 2223), (1, 87)]
9 3 [(-1, 4), (0, 1998), (1, 136), (2, 6), (3, 1)]
9 4 [(-2, 2), (-1, 9), (0, 2045), (1, 132), (2, 12)]
10 1 [(0, 4778), (1, 117)]
10 2 [(0, 5902), (1, 150)]
10 3 [(-1, 12), (0, 5345), (1, 237), (2, 11), (3, 2)]
10 4 [(-2, 4), (-1, 24), (0, 5479), (1, 254), (2, 22), (3, 2)]
10 5 [(-2, 8), (-1, 29), (0, 5374), (1, 257), (2, 28)]


# Product in CDR is very nice - no negatives, many zeros, all entries
# small.

>>> for n in range(2, 11):
...     for m in range(1, n):
...         if 2 * m <= n:
...             print(n, m, stats_CDR(n - m, m))
...
2 1 [(1, 2)]
3 1 [(0, 3), (1, 3)]
4 1 [(0, 10), (1, 5)]
4 2 [(0, 14), (1, 6)]
5 1 [(0, 32), (1, 8)]
5 2 [(0, 39), (1, 9)]
6 1 [(0, 91), (1, 13)]
6 2 [(0, 115), (1, 15)]
6 3 [(0, 101), (1, 15), (2, 1)]
7 1 [(0, 252), (1, 21)]
7 2 [(0, 312), (1, 24)]
7 3 [(0, 288), (1, 26), (2, 1)]
8 1 [(0, 680), (1, 34)]
8 2 [(0, 845), (1, 39)]
8 3 [(0, 769), (1, 45), (2, 2)]
8 4 [(0, 803), (1, 44), (2, 3)]
9 1 [(0, 1815), (1, 55)]
9 2 [(0, 2247), (1, 63)]
9 3 [(0, 2066), (1, 76), (2, 2), (3, 1)]
9 4 [(0, 2116), (1, 80), (2, 4)]
10 1 [(0, 4806), (1, 89)]
10 2 [(0, 5950), (1, 102)]
10 3 [(0, 5472), (1, 129), (2, 5), (3, 1)]
10 4 [(0, 5639), (1, 139), (2, 6), (3, 1)]
10 5 [(0, 5542), (1, 144), (2, 10)]

# Cone in CDR has some negatives, otherwise many zeros and the rest
# ones.
# Number of negatives is probably Fibonacci numbers - 1 (A000071).
# Number of ones is probably Lucas numbers (A000032).

>>> for d in range(11):
...     counter = Counter(C_in_CDR[d].flatten())
...     print(d, sorted(counter.items()))
0 [(1, 1)]
1 [(0, 1), (1, 1)]
2 [(0, 3), (1, 3)]
3 [(-1, 1), (0, 10), (1, 4)]
4 [(-1, 2), (0, 31), (1, 7)]
5 [(-1, 4), (0, 89), (1, 11)]
6 [(-1, 7), (0, 248), (1, 18)]
7 [(-1, 12), (0, 673), (1, 29)]
8 [(-1, 20), (0, 1803), (1, 47)]
9 [(-1, 33), (0, 4786), (1, 76)]
10 [(-1, 54), (0, 12639), (1, 123)]
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

from .matrices import CDR_from_FLAG
from .matrices import C_in_CDR
from .matrices import IC_from_CDR

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

def doit_CDR(n, m):

    return change_product_basis(
        product_formula(n, m),
        IC_from_CDR[n],
        IC_from_CDR[m],
        CDR_from_FLAG[n+m]
    )

def stats_CDR(n, m):

    matrix = doit_CDR(n, m)
    counter = Counter(matrix.flatten())
    counts = sorted(counter.items())
    return counts
