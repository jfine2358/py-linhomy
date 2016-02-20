'''
>>> candidate_matrices.print_C_stats(10)
0 [(1, 1)]
1 [(0, 1), (1, 1)]
2 [(0, 3), (1, 3)]
3 [(0, 11), (1, 4)]
4 [(0, 33), (1, 7)]
5 [(0, 92), (1, 12)]
6 [(0, 254), (1, 19)]
7 [(0, 682), (1, 32)]
8 [(0, 1818), (1, 52)]
9 [(0, 4810), (1, 85)]
10 [(0, 12677), (1, 139)]

As expected, all zeros and ones.
>>> candidate_matrices.print_D_stats(10)
0 [(0, 1), (1, 1)]
1 [(0, 2), (1, 1)]
2 [(0, 8), (1, 2)]
3 [(0, 21), (1, 3)]
4 [(0, 60), (1, 5)]
5 [(0, 160), (1, 8)]
6 [(0, 429), (1, 13)]
7 [(0, 1134), (1, 21)]
8 [(0, 2992), (1, 34)]
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
8 1 [(0, 671), (1, 43)]
8 2 [(0, 831), (1, 53)]
8 3 [(0, 741), (1, 71), (2, 4)]
8 4 [(-2, 1), (-1, 1), (0, 778), (1, 64), (2, 6)]
9 1 [(0, 1799), (1, 71)]
9 2 [(0, 2223), (1, 87)]
9 3 [(0, 2011), (1, 127), (2, 6), (3, 1)]
9 4 [(-2, 2), (-1, 3), (0, 2061), (1, 122), (2, 12)]
10 1 [(0, 4779), (1, 116)]
10 2 [(0, 5905), (1, 147)]
10 3 [(0, 5374), (1, 220), (2, 11), (3, 2)]
10 4 [(-2, 4), (-1, 10), (0, 5519), (1, 228), (2, 22), (3, 2)]
10 5 [(-2, 6), (-1, 7), (0, 5419), (1, 236), (2, 28)]
'''


# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import re

from .rankmatrices import RankMatrices
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
