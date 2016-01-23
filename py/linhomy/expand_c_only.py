'''
>>> matrices.print_C_stats(10)
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

>>> matrices.print_D_stats(10)
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

>>> matrices.print_product_stats(10)
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

import itertools

from .rankmatrices import RankMatrices
from .rankmatrices import candidate_rule_factory
from .rankmatrices import print_rule
from .rankmatrices import CD_from_word
from .rankmatrices import word_from_CD
from .rankmatrices import index_from_word
from .rankmatrices import slide_d
from .rankmatrices import expand_c
from .rankmatrices import expand_d


def expand_c_only(word):
    '''Generic rule.'''
    index = index_from_word(word)
    C_count, D_count = index

    new_Cs = tuple(expand_c(C_count))

    for aaa in new_Cs:
        ccc = zip(
            (b'\x01' * c for c in aaa),
            (b'\x02' * d for d in D_count),
        )

        value = b'\x01\x02'.join(
            hhh + ggg
            for (ggg, hhh) in ccc
        )

        yield value


matrices = RankMatrices(expand_c_only)


if __name__ == '__main__':

    import doctest
    print(doctest.testmod())
