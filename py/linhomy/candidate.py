'''
>>> candidate_matrices.print_C_stats(10)
0 [(1, 1)]
1 [(0, 1), (1, 1)]
2 [(0, 3), (1, 3)]
3 [(0, 11), (1, 4)]
4 [(0, 33), (1, 7)]
5 [(0, 92), (1, 12)]
6 [(0, 254), (1, 19)]
7 [(0, 681), (1, 33)]
8 [(0, 1815), (1, 55)]
9 [(0, 4808), (1, 87)]
10 [(-1, 5), (0, 12669), (1, 142)]


Puzzle: Why are these negatives arising?

Unexpected negatives for C-rule 9 investigated.
TODO: More negatives in C-rule 9.
>>> CD_from_word(FIB_WORDS[10][10])
'CCCCDCDC'
>>> for c, w in zip(candidate_matrices.C_rule[9][10], FIB_WORDS[9]):
...     if c: print(c, CD_from_word(w))
1 CCCDCDC

>>> CD_from_word(FIB_WORDS[10][11])
'CCCCDDCC'
>>> for c, w in zip(candidate_matrices.C_rule[9][11], FIB_WORDS[9]):
...     if c: print(c, CD_from_word(w))
1 CCCDDCC


As expected, all zeros and ones.
>>> candidate_matrices.print_D_stats(10)
0 [(0, 1), (1, 1)]
1 [(0, 2), (1, 1)]
2 [(0, 8), (1, 2)]
3 [(0, 21), (1, 3)]
4 [(0, 60), (1, 5)]
5 [(0, 160), (1, 8)]
6 [(0, 427), (1, 15)]
7 [(0, 1129), (1, 26)]
8 [(0, 2987), (1, 39)]
9 [(0, 7865), (1, 55)]
10 [(0, 20648), (1, 89)]


Some negatives, that must be removed. Good outcome for little input.
>>> candidate_matrices.print_product_stats(10)
2 1 [(1, 2)]
3 1 [(0, 3), (1, 3)]
4 1 [(0, 9), (1, 6)]
4 2 [(0, 14), (1, 6)]
5 1 [(0, 31), (1, 9)]
5 2 [(0, 37), (1, 11)]
6 1 [(0, 88), (1, 16)]
6 2 [(0, 112), (1, 18)]
6 3 [(0, 93), (1, 23), (2, 1)]
7 1 [(0, 247), (1, 26)]
7 2 [(0, 305), (1, 31)]
7 3 [(0, 275), (1, 38), (2, 2)]
8 1 [(0, 668), (1, 46)]
8 2 [(0, 828), (1, 56)]
8 3 [(0, 738), (1, 73), (2, 5)]
8 4 [(0, 780), (1, 64), (2, 6)]
9 1 [(0, 1795), (1, 75)]
9 2 [(0, 2211), (1, 99)]
9 3 [(0, 1998), (1, 138), (2, 8), (3, 1)]
9 4 [(0, 2057), (1, 129), (2, 14)]
10 1 [(-1, 1), (0, 4773), (1, 121)]
10 2 [(0, 5893), (1, 159)]
10 3 [(0, 5344), (1, 246), (2, 15), (3, 2)]
10 4 [(-2, 1), (-1, 6), (0, 5504), (1, 247), (2, 25), (3, 2)]
10 5 [(-2, 2), (-1, 1), (0, 5405), (1, 254), (2, 34)]


More about the negative coefficients in product 10 1.
>>> for n in [43]:
...     print('#', n, CD_from_word(FIB_WORDS[10][n]))
...     for c, w in zip(candidate_matrices.doit(9, 1)[n,0], FIB_WORDS[10]):
...          if c: print(c, CD_from_word(w))
# 43 CDCDCCD
1 DCCDCCD
1 DCDCCCD
-1 DCDCCDC


More about the negative coefficients in product 10 4.
>>> for n in [3, 4]:
...     print('#', n, CD_from_word(FIB_WORDS[10][n]))
...     for c, w in zip(candidate_matrices.doit(6, 4)[n,1], FIB_WORDS[10]):
...          if c: print(c, CD_from_word(w))
# 3 CCCCCCDCC
1 CCCDCCCD
1 CCCDCCDC
2 CCCDCDCC
1 CCCDDCCC
-1 CCDCCCDC
-1 CCDCCDCC
-2 CCDCDCCC
-1 CCDDCCCC
1 DCDCCCD
1 DCDCCDC
2 DCDCDCC
1 DCDDCCC
# 4 CCCCCCDD
1 CCCDCDD
1 CCCDDCD
1 CCCDDDC
-1 CCDCDDC
-1 CCDDCDC
-1 CCDDDCC
1 DCDCDD
1 DCDDCD
1 DCDDDC


More about the negative coefficients in product 10 5.
>>> CD_from_word(FIB_WORDS[5][2])
'CCDC'
>>> for c, w in zip(candidate_matrices.doit(5, 5)[2][2], FIB_WORDS[10]):
...     if c: print(c, CD_from_word(w))
...
2 CCCDCCDC
2 CCCDCDCC
1 CCCDDCCC
-2 CCDCCDCC
-2 CCDCDCCC
-1 CCDDCCCC
2 DCDCCDC
2 DCDCDCC
1 DCDDCCC
'''


# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import re

from .fibonacci import FIB_WORDS
from .rankmatrices import RankMatrices
from .rankmatrices import CD_from_word
from .cdr_matrices import b_empty
from .cdr_matrices import b1
from .cdr_matrices import b2
from .cdr_matrices import rules_factory
from .cdr_matrices import rule_matrices_from_rules
from .cdr_matrices import cdr_print

if b1 != 'C' or b2 != 'D':
    ddt                         # Binary variant not coded.

candidate_2_re = re.compile('(C+)(D+)(.*)')
def candidate_2_split(s):
    mo = candidate_2_re.match(s)
    if mo:
        return mo.groups()

candidate_12_re = re.compile('(D+)(.*)')
def candidate_12_split(s):
    mo = candidate_12_re.match(s)
    if mo:
        return mo.groups()

# Start as clone of basic_matrices.
def candidate_11(word):
    yield b1 + word


def candidate_12(word):
    yield b1 + word
    if 0:
        bits = candidate_12_split(word)
        if bits != None:
            n = len(bits[0])
            for i in range(1, n):
                yield b1 + b2 * (n - i) + b1 * (2*i) + bits[1]

def candidate_2(word):
    yield  b2 + word

    if word in {
            # Dimension 6 -> 8.
            'CDCD', 'CDDC',
            # Dimension 7 -> 9.
            'CCDCD', 'CCDDC',
            'CDCCD', 'CDCDC', 'CDDCC',
            # Dimension 8 -> 10.
            'CCCDCD', 'CCCDDC', 'CCDCCD', 'CCDCDC', 'CCDDCC',
    }:
        yield b1 + word + b1
    if 0:
        bits = candidate_2_split(word)
        if bits != None:
            yield b1 + bits[0] + bits[1] + b1 + bits[2]


candidate_rules = rules_factory(candidate_11, candidate_12, candidate_2)
candidate_rule_matrices = rule_matrices_from_rules(candidate_rules)
candidate_matrices = RankMatrices(matrices=candidate_rule_matrices)

if __name__ == '__main__':

    import doctest
    print(doctest.testmod())
