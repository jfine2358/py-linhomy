'''Explore matrices that respect rank

identity_matrices = RankMatrices(identity_rule)

>>> identity_matrices.print_product_stats(10)
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

>>> identity_matrices.print_C_stats(10)
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

>>> identity_matrices.print_D_stats(10)
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


>>> for d in range(1, 7):
...    print(' '.join(map(CD_from_word, FIB_WORDS[d])))
C
CC D
CCC CD DC
CCCC CCD CDC DCC DD
CCCCC CCCD CCDC CDCC CDD DCCC DCD DDC
CCCCCC CCCCD CCCDC CCDCC CCDD CDCCC CDCD CDDC DCCCC DCCD DCDC DDCC DDD

>>> for d in range(1, 7):
...    for word in FIB_WORDS[d]:
...        if word != word_from_CD(CD_from_word(word)):
...            print(word, CD_from_word(word))


>>> for n in range(10):
...    for word in FIB_WORDS[n]:
...        index = index_from_word(word)
...        word2 = word_from_index(index)
...        if word != word2:
...            print(word, word2)


>>> EXPAND_D[0] == (b'',)
True
>>> EXPAND_D[1] == (b'\x02', b'\x01\x01')
True
>>> EXPAND_D[2] == (b'\x02\x02', b'\x02\x01\x01', b'\x01' * 4)
True
>>> EXPAND_D[3] == (b'\x02\x02\x02', b'\x02\x02\x01\x01',
... b'\x02' + b'\x01' * 4,  b'\x01' * 6)
True

>>> list(expand_d((0,))) == [(b'',)]
True

>>> str_expand_d(expand_d((0,)))
''

>>> str_expand_d(expand_d((1,)))
'2'

>>> str_expand_d(expand_d((2,)))
'22'

>>> str_expand_d(expand_d((0, 1, 2)))
',2,22 ,2,211 ,2,1111 ,11,22 ,11,211 ,11,1111'

>>> str_expand_d(expand_d((0, 2, 1)))
',22,2 ,22,11 ,211,2 ,211,11 ,1111,2 ,1111,11'

>>> str_expand_d(expand_d((1, 2, 1)))
'2,22,2 2,22,11 2,211,2 2,211,11 2,1111,2 2,1111,11'

>>> str_expand_d(expand_d((2, 2, 1)))
'22,22,2 22,22,11 22,211,2 22,211,11 22,1111,2 22,1111,11'

>>> expand_c((1, 0, 0))
((0, 0, 1), (0, 1, 0), (1, 0, 0))

>>> expand_c((0, 0, 1))
((0, 0, 1),)

>>> expand_c((2, 0, 0))
((0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0))

>>> expand_c((1, 1, 0))
((0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0))


>>> slide_d(((0,), (0,)))
(((0,), (0,)),)
>>> slide_d(((0,), (1,)))
(((0,), (1,)),)
>>> slide_d(((1,), (0,)))
(((1,), (0,)),)
>>> slide_d(((1,), (1,)))
(((1,), (1,)),)


>>> slide_d(((0, 0), (0, 0)))
(((0, 0), (0, 0)),)
>>> slide_d(((0, 0), (1, 0)))
(((0, 0), (1, 0)), ((1, 1), (0, 0)))
>>> slide_d(((0, 0), (2, 0)))
(((0, 0), (2, 0)), ((1, 1), (1, 0)), ((2, 2), (0, 0)))

>>> slide_d(((1, 0), (1, 0)))
(((1, 0), (1, 0)), ((2, 1), (0, 0)))
>>> slide_d(((1, 0), (2, 0)))
(((1, 0), (2, 0)), ((2, 1), (1, 0)), ((3, 2), (0, 0)))

>>> cm_1.print_C_stats(10)
0 [(1, 1)]
1 [(0, 1), (1, 1)]
2 [(0, 3), (1, 3)]
3 [(0, 11), (1, 4)]
4 [(0, 32), (1, 8)]
5 [(0, 90), (1, 14)]
6 [(0, 250), (1, 23)]
7 [(-1, 2), (0, 674), (1, 38)]
8 [(-1, 3), (0, 1801), (1, 66)]
9 [(-1, 14), (0, 4776), (1, 105)]
10 [(-1, 19), (0, 12616), (1, 181)]

>>> cm_1.print_D_stats(10)
0 [(0, 1), (1, 1)]
1 [(0, 2), (1, 1)]
2 [(0, 8), (1, 2)]
3 [(0, 19), (1, 5)]
4 [(0, 57), (1, 8)]
5 [(0, 154), (1, 14)]
6 [(0, 416), (1, 26)]
7 [(-1, 3), (0, 1110), (1, 42)]
8 [(-1, 1), (0, 2949), (1, 76)]
9 [(-1, 10), (0, 7784), (1, 126)]
10 [(-1, 11), (0, 20510), (1, 216)]

>>> cm_1.print_product_stats(10)
2 1 [(1, 2)]
3 1 [(0, 3), (1, 3)]
4 1 [(0, 9), (1, 6)]
4 2 [(0, 14), (1, 6)]
5 1 [(0, 29), (1, 11)]
5 2 [(0, 35), (1, 13)]
6 1 [(-1, 2), (0, 84), (1, 18)]
6 2 [(0, 106), (1, 24)]
6 3 [(0, 86), (1, 30), (2, 1)]
7 1 [(-1, 2), (0, 237), (1, 34)]
7 2 [(-1, 3), (0, 289), (1, 44)]
7 3 [(0, 251), (1, 62), (2, 2)]
8 1 [(-1, 10), (0, 648), (1, 56)]
8 2 [(-1, 3), (0, 803), (1, 78)]
8 3 [(-1, 11), (0, 689), (1, 112), (2, 4)]
8 4 [(0, 721), (1, 119), (2, 10)]
9 1 [(-1, 19), (0, 1751), (1, 100)]
9 2 [(-1, 19), (0, 2151), (1, 140)]
9 3 [(-1, 16), (0, 1895), (1, 227), (2, 6), (3, 1)]
9 4 [(-2, 6), (-1, 25), (0, 1921), (1, 232), (2, 16)]
10 1 [(-1, 38), (0, 4678), (1, 179)]
10 2 [(-1, 33), (0, 5771), (1, 248)]
10 3 [(-2, 4), (-1, 67), (0, 5127), (1, 396), (2, 11), (3, 2)]
10 4 [(-2, 7), (-1, 44), (0, 5226), (1, 471), (2, 35), (3, 2)]
10 5 [(-2, 27), (-1, 98), (0, 5078), (1, 438), (2, 55)]


This shows that candidate_rule_1 is wrong - transposition.
>>> for d in range(1, 4):
...     print_rule(candidate_rule_1, d)
1 C C
2 CC CC
2 D D
3 CCC CCC
3 CD DC
3 DC CD

Revise to create cm_2.  Revised rule is still wrong!  First error is
product (6, 1).

>>> cm_2.print_C_stats(10)
0 [(1, 1)]
1 [(0, 1), (1, 1)]
2 [(0, 3), (1, 3)]
3 [(0, 11), (1, 4)]
4 [(0, 32), (1, 8)]
5 [(0, 90), (1, 14)]
6 [(0, 250), (1, 23)]
7 [(-1, 2), (0, 674), (1, 38)]
8 [(-1, 3), (0, 1801), (1, 66)]
9 [(-1, 10), (0, 4780), (1, 105)]
10 [(-1, 19), (0, 12616), (1, 181)]

>>> cm_2.print_D_stats(10)
0 [(0, 1), (1, 1)]
1 [(0, 2), (1, 1)]
2 [(0, 8), (1, 2)]
3 [(0, 19), (1, 5)]
4 [(0, 57), (1, 8)]
5 [(0, 154), (1, 14)]
6 [(0, 416), (1, 26)]
7 [(0, 1113), (1, 42)]
8 [(0, 2950), (1, 76)]
9 [(0, 7794), (1, 126)]
10 [(0, 20521), (1, 216)]

>>> cm_2.print_product_stats(10)
2 1 [(1, 2)]
3 1 [(0, 3), (1, 3)]
4 1 [(0, 9), (1, 6)]
4 2 [(0, 14), (1, 6)]
5 1 [(0, 29), (1, 11)]
5 2 [(0, 35), (1, 13)]
6 1 [(-1, 2), (0, 84), (1, 18)]
6 2 [(0, 106), (1, 24)]
6 3 [(0, 86), (1, 30), (2, 1)]
7 1 [(-1, 2), (0, 237), (1, 34)]
7 2 [(-1, 3), (0, 289), (1, 44)]
7 3 [(0, 251), (1, 62), (2, 2)]
8 1 [(-1, 9), (0, 649), (1, 56)]
8 2 [(-1, 3), (0, 803), (1, 78)]
8 3 [(-1, 11), (0, 689), (1, 112), (2, 4)]
8 4 [(0, 721), (1, 119), (2, 10)]
9 1 [(-1, 16), (0, 1754), (1, 100)]
9 2 [(-1, 13), (0, 2157), (1, 140)]
9 3 [(-1, 15), (0, 1897), (1, 226), (2, 6), (3, 1)]
9 4 [(-2, 6), (-1, 24), (0, 1923), (1, 231), (2, 16)]
10 1 [(-1, 34), (0, 4687), (1, 174)]
10 2 [(-1, 25), (0, 5779), (1, 248)]
10 3 [(-1, 53), (0, 5147), (1, 394), (2, 11), (3, 2)]
10 4 [(-2, 7), (-1, 40), (0, 5234), (1, 467), (2, 35), (3, 2)]
10 5 [(-2, 25), (-1, 95), (0, 5090), (1, 431), (2, 55)]


The candidate_rule_2 should not here have CDCC.
    5 DCD CCDC CDCC DCD
There may be other errors.
>>> for d in range(1, 6):
...     print_rule(candidate_rule_2, d)
1 C C
2 CC CC
2 D D
3 CCC CCC
3 CD CD
3 DC DC
4 CCCC CCCC
4 CCD CCD CDC
4 CDC CDC
4 DCC DCC
4 DD DD
5 CCCCC CCCCC
5 CCCD CCCD CCDC CDCC
5 CCDC CCDC CDCC
5 CDCC CDCC
5 CDD CDCC CDD
5 DCCC DCCC
5 DCD CCDC CDCC DCD
5 DDC DDC

Create candidate_rule_3.  It has fewer negatives. First error is C
rule at d=7.

>>> cm_3.print_C_stats(10)
0 [(1, 1)]
1 [(0, 1), (1, 1)]
2 [(0, 3), (1, 3)]
3 [(0, 11), (1, 4)]
4 [(0, 32), (1, 8)]
5 [(0, 90), (1, 14)]
6 [(0, 250), (1, 23)]
7 [(-1, 1), (0, 673), (1, 40)]
8 [(-1, 2), (0, 1801), (1, 67)]
9 [(-1, 6), (0, 4778), (1, 111)]
10 [(-1, 12), (0, 12613), (1, 191)]

>>> cm_3.print_D_stats(10)
0 [(0, 1), (1, 1)]
1 [(0, 2), (1, 1)]
2 [(0, 8), (1, 2)]
3 [(0, 20), (1, 4)]
4 [(0, 58), (1, 7)]
5 [(0, 156), (1, 12)]
6 [(0, 421), (1, 21)]
7 [(0, 1120), (1, 35)]
8 [(0, 2966), (1, 60)]
9 [(0, 7820), (1, 100)]
10 [(0, 20569), (1, 168)]

>>> cm_3.print_product_stats(10)
2 1 [(1, 2)]
3 1 [(0, 3), (1, 3)]
4 1 [(0, 9), (1, 6)]
4 2 [(0, 14), (1, 6)]
5 1 [(0, 30), (1, 10)]
5 2 [(0, 36), (1, 12)]
6 1 [(0, 87), (1, 17)]
6 2 [(0, 108), (1, 22)]
6 3 [(0, 88), (1, 28), (2, 1)]
7 1 [(0, 244), (1, 29)]
7 2 [(0, 298), (1, 38)]
7 3 [(0, 260), (1, 53), (2, 2)]
8 1 [(0, 666), (1, 48)]
8 2 [(0, 816), (1, 68)]
8 3 [(-1, 3), (0, 711), (1, 98), (2, 4)]
8 4 [(0, 742), (1, 101), (2, 7)]
9 1 [(0, 1789), (1, 81)]
9 2 [(0, 2195), (1, 115)]
9 3 [(-1, 7), (0, 1946), (1, 185), (2, 6), (3, 1)]
9 4 [(-2, 1), (-1, 8), (0, 1987), (1, 191), (2, 13)]
10 1 [(0, 4761), (1, 134)]
10 2 [(0, 5852), (1, 200)]
10 3 [(-1, 21), (0, 5247), (1, 326), (2, 11), (3, 2)]
10 4 [(-2, 2), (-1, 22), (0, 5361), (1, 375), (2, 23), (3, 2)]
10 5 [(-2, 7), (-1, 37), (0, 5258), (1, 361), (2, 33)]

>>> print_rule(candidate_rule_3, 5)
5 CCCCC CCCCC
5 CCCD CCCD CCDC CDCC
5 CCDC CCDC CDCC
5 CDCC CDCC
5 CDD CDCC CDD
5 DCCC DCCC
5 DCD CCDC DCD
5 DDC DDC

>>> print_rule(candidate_rule_3, 6)
6 CCCCCC CCCCCC
6 CCCCD CCCCD CCCDC CCDCC CDCCC
6 CCCDC CCCDC CCDCC CDCCC
6 CCDCC CCDCC CDCCC
6 CCDD CCDCC CCDD CDCCC CDDC
6 CDCCC CDCCC
6 CDCD CDCD
6 CDDC CDCCC CDDC
6 DCCCC DCCCC
6 DCCD CCCDC CCDCC DCCD DCDC
6 DCDC CCDCC DCDC
6 DDCC DDCC
6 DDD DDD

>>> print_rule(candidate_rule_3, 7)
7 CCCCCCC CCCCCCC
7 CCCCCD CCCCCD CCCCDC CCCDCC CCDCCC CDCCCC
7 CCCCDC CCCCDC CCCDCC CCDCCC CDCCCC
7 CCCDCC CCCDCC CCDCCC CDCCCC
7 CCCDD CCCDCC CCCDD CCDCCC CCDDC CDCCCC CDDCC
7 CCDCCC CCDCCC CDCCCC
7 CCDCD CCDCD CDCCD CDCDC
7 CCDDC CCDCCC CCDDC CDCCCC CDDCC
7 CDCCCC CDCCCC
7 CDCCD CDCCD CDCDC
7 CDCDC CDCDC
7 CDDCC CDCCCC CDDCC
7 CDDD CDCCCC CDDCC CDDD
7 DCCCCC DCCCCC
7 DCCCD CCCCDC CCCDCC CCDCCC DCCCD DCCDC DCDCC
7 DCCDC CCCDCC CCDCCC DCCDC DCDCC
7 DCDCC CCDCCC DCDCC
7 DCDD CCDCCC CCDDC DCDCC DCDD
7 DDCCC DDCCC
7 DDCD CCCDCC DCCDC DDCD
7 DDDC DDDC
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type


from collections import Counter
import functools
import itertools
import numpy
from .fibonacci import FIB_WORDS
from .matrices import fib_zeros_array
from .matrices import invert_grow_list
from .matrices import C_in_CD
from .matrices import CDR_from_CD
from .matrices import CDR_from_FLAG
from .matrices import D_in_CD
from .matrices import IC_from_CDR
from .product import product_formula
from .product import change_product_basis
from .six import iterbytes
from .tools import grow_list

def identity_rule(word):
    yield word


def str_expand_d(items):
    return str(' ').join(
        str(',').join(
            str('').join(
                str(c) for c in iterbytes(word)
            )
            for word in item
        )
        for item in items
    )

def _AAA_from_CDR(rule, deg):

    value = fib_zeros_array(deg, deg)

    # Because rule(word) = matrix * e_{word}, each rule(word) gives a
    # column on the matrix.  And so a certain value of j.

    # Iterate over the (i, j) values.
    for j, j_word in enumerate(FIB_WORDS[deg]):
        for i_word in rule(j_word):
            i = FIB_WORDS[deg].index(i_word)

            value[i, j] += 1    # Assign to the matrix.

    return value


def C_in_AAA_factory(CD_from_AAA, AAA_from_CD):

    # Based on C_in_CDR.
    @grow_list
    def C_in_AAA(self):
        deg = len(self)
        value = fib_zeros_array(deg + 1, deg)

        tmp = numpy.dot(C_in_CD[deg], CD_from_AAA[deg])
        value = numpy.dot(AAA_from_CD[deg+1], tmp)
        return value

    return C_in_AAA


def D_in_AAA_factory(CD_from_AAA, AAA_from_CD):

    # Based on C_in_AAA_factory.
    @grow_list
    def D_in_AAA(self):
        deg = len(self)
        value = fib_zeros_array(deg + 2, deg)

        tmp = numpy.dot(D_in_CD[deg], CD_from_AAA[deg])
        value = numpy.dot(AAA_from_CD[deg+2], tmp)
        return value

    return D_in_AAA


class RankMatrices:

    def __init__(self, rule=None, matrices=None):
        self.rule = rule

        if rule != None:
            if matrices != None:
                raise ValueError
            else:
                self.AAA_from_CDR = grow_list(
                    lambda self_: _AAA_from_CDR(rule, len(self_))
                )
        else:
            if matrices == None:
                raise ValueError
            else:
                self.AAA_from_CDR = matrices

        self.CDR_from_AAA = invert_grow_list(self.AAA_from_CDR)

        # Needed for C_in_AAA and D_in_AAA matrices.
        self.AAA_from_CD = grow_list(
            lambda self_: numpy.dot(
                self.AAA_from_CDR[len(self_)],
                CDR_from_CD[len(self_)]
            )
        )
        self.CD_from_AAA = invert_grow_list(self.AAA_from_CD)

        # Needed for change_product_basis.
        self.IC_from_AAA = grow_list(
            lambda self_: numpy.dot(
                IC_from_CDR[len(self_)],
                self.CDR_from_AAA[len(self_)]
            )
        )

        # Needed for change_product_basis.
        self.AAA_from_FLAG = grow_list(
            lambda self_: numpy.dot(
                self.AAA_from_CDR[len(self_)],
                CDR_from_FLAG[len(self_)]
            )
        )

        self.C_rule = C_in_AAA_factory(
            self.CD_from_AAA,
            self.AAA_from_CD
        )

        self.D_rule = D_in_AAA_factory(
            self.CD_from_AAA,
            self.AAA_from_CD
        )


    def doit(self, n, m):
        return change_product_basis(
            product_formula(n, m),
            self.IC_from_AAA[n],
            self.IC_from_AAA[m],
            self.AAA_from_FLAG[n+m]
        )


    def product_stats(self, n, m):
        matrix = self.doit(n, m)
        counter = Counter(matrix.flatten())
        return sorted(counter.items())


    def print_product_stats(self, max):
        for n in range(2, max + 1):
            for m in range(1, n):
                if 2 * m <= n:
                    print(n, m, self.product_stats(n - m, m))


    def print_C_stats(self, max):
        C_rule = self.C_rule
        for d in range(max + 1):
            counter = Counter(C_rule[d].flatten())
            print(d, sorted(counter.items()))


    def print_D_stats(self, max):
        D_rule = self.D_rule
        for d in range(max + 1):
            counter = Counter(D_rule[d].flatten())
            print(d, sorted(counter.items()))


identity_matrices = RankMatrices(identity_rule)


def index_from_word(word):
    '''Here, indexes is pair of tuples, not tuple of pairs.
    '''
    # Split into parts.
    parts = word.split(b'\x01\x02')

    # Turn parts into pair of sequences of ints.
    C_count = tuple(item.count(b'\x01') for item in parts)
    D_count = tuple(item.count(b'\x02') for item in parts)

    index = C_count, D_count

    return index


def word_from_index(index):

    # Turn int into sequence of parts.
    C_count, D_count = index
    parts = tuple(
        b'\x02' * d + b'\x01' * c
        for (c, d) in zip(C_count, D_count)
    )

    # Join the parts.
    return b'\x01\x02'.join(parts)


@grow_list
def EXPAND_D(self):
    '''Return tuple of word generated from D * d.
    '''
    d = len(self)
    return tuple(
        b'\x02' * (d - i) + b'\x01' * (2 * i)
        for i in range(d + 1)
    )

def expand_d(ints):
    '''Yield results of applying D -> CC rule.

    Does not apply to the leading D's.
    '''
    head = ((b'\x02' * ints[0],),) # The leading D's.
    body = tuple(EXPAND_D[d] for d in ints[1:])

    # Return iterator over the product.
    return itertools.product(*(head + body))


def expand_c(ints):

    '''Return tuple of ints.

    Move C rightwards.  For example, CCCD contributes also to CCDC and
    CDCC.
    '''
    if len(ints) <= 1:
        return (ints,)

    head = ints[0]
    body = ints[1:]

    return tuple(sorted(
        # Create new tuple with possible decremented tail.
        tuple((head - i,) + item)
        # Iterate over the possible decrements.
        for i in range(head + 1)
        # For given decrement, recursively iterate over items.
        for item in expand_c((body[0] + i,) + body[1:])
    ))


def slide_d(index):
    '''Return indexes to obtained by d-sliding index.

    An index is C_count, D_count.
    '''

    C_count, D_count = index
    # First deal with special case - no change.
    if len(C_count) < 2:
        return (index,)

    # Split the data with have.
    (c_1, c_2), C_body = C_count[:2], C_count[2:]
    (d_1,), D_body = D_count[:1], D_count[1:]

    return tuple(sorted(
        (
            (c_1 + i, c_2 + i) + C_body,
            (d_1 - i,) + D_body
        )
        for i in range(d_1 + 1)
    ))


def candidate_rule_1(word):
    '''Rough first approximation, tests how things fit together.
    '''
    index = index_from_word(word)
    for C_count, D_count in slide_d(index):

        new_Cs = tuple(expand_c(C_count))
        new_Ds = tuple(expand_d(D_count))

        for mixed in itertools.product(new_Cs, new_Ds):

            aaa, bbb = mixed
            ccc = zip(
                (b'\x01' * c for c in aaa),
                bbb
            )

            # Oops - should be CD, not DC.
            yield b'\x02\x01'.join(
                ggg + hhh       # Oops - transposed.
                for (ggg, hhh) in ccc
            )
cm_1 = RankMatrices(candidate_rule_1)

def candidate_rule_factory(condition):

    def candidate_rule(word):
        '''Generic rule.'''
        index = index_from_word(word)
        for C_count, D_count in slide_d(index):

            new_Cs = tuple(expand_c(C_count))
            new_Ds = tuple(expand_d(D_count))

            for mixed in itertools.product(new_Cs, new_Ds):

                aaa, bbb = mixed
                ccc = zip(
                    (b'\x01' * c for c in aaa),
                    bbb
                )

                value = b'\x01\x02'.join(
                    hhh + ggg
                    for (ggg, hhh) in ccc
                )

                if condition(word, value):
                    yield value

    return candidate_rule

candidate_rule_2 = candidate_rule_factory(lambda *argv: True)
cm_2 = RankMatrices(candidate_rule_2)


def condition_3(src, value):

    src_head = src.split(b'\x01\x02', 1)[0]
    val_head = value.split(b'\x01\x02', 1)[0]

    d_diff = src_head.count(b'\x02') - val_head.count(b'\x02')
    c_count = val_head.count(b'\x01')
    return c_count >= d_diff

candidate_rule_3 = candidate_rule_factory(condition_3)
cm_3 = RankMatrices(candidate_rule_3)


def CD_from_word(word):

    d = {
        1: str('C'),
        2: str('D'),
    }
    return str('').join(d[c] for c in iterbytes(word))


def word_from_CD(s):

    d = {
        str('C'): b'\x01',
        str('D'): b'\x02',
    }
    return b''.join(d[c] for c in s)


def print_rule(rule, d):

    for word in FIB_WORDS[d]:
        src = CD_from_word(word)
        bits = sorted(map(CD_from_word, rule(word)))
        print(d, src, str(' ').join(bits))


if __name__ == '__main__':


    if 0:
        tmp = _AAA_from_CDR(identity_rule, 5)
        print(tmp)

        print(identity_matrices.AAA_from_CDR[5])
        print(identity_matrices.stats(5, 3))


    import doctest
    print(doctest.testmod())
