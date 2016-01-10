'''Explore matrices that respect rank

identity_matrices = RankMatrices(identity_rule)
>>> for n in range(2, 11):
...     for m in range(1, n):
...         if 2 * m <= n:
...             print(n, m, identity_matrices.product_stats(n - m, m))
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


>>> C_in_AAA = identity_matrices.C_rule

>>> for d in range(11):
...     counter = Counter(C_in_AAA[d].flatten())
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

>>> D_in_AAA = identity_matrices.D_rule

>>> for d in range(11):
...     counter = Counter(D_in_AAA[d].flatten())
...     print(d, sorted(counter.items()))
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
''

>>> str_expand_d(expand_d((0, 1, 2)))
',2,22 ,2,211 ,2,1111 ,11,22 ,11,211 ,11,1111'

>>> str_expand_d(expand_d((0, 2, 1)))
',22,2 ,22,11 ,211,2 ,211,11 ,1111,2 ,1111,11'

>>> expand_c((1, 0, 0))
((0, 0, 1), (0, 1, 0), (1, 0, 0))

>>> expand_c((0, 0, 1))
((0, 0, 1),)

>>> expand_c((2, 0, 0))
((0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0), (2, 0, 0))

>>> expand_c((1, 1, 0))
((0, 0, 2), (0, 1, 1), (0, 2, 0), (1, 0, 1), (1, 1, 0))
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

    def __init__(self, rule):
        self.rule = rule

        self.AAA_from_CDR = grow_list(
            lambda self_: _AAA_from_CDR(rule, len(self_))
        )

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

        self.doit = lambda n, m: change_product_basis(
            product_formula(n, m),
            self.IC_from_AAA[n],
            self.IC_from_AAA[m],
            self.AAA_from_FLAG[n+m]
        )

        self.product_stats = lambda n, m: sorted(
            Counter(self.doit(n, m).flatten()).items()
        )



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
    head = ((b'',),)            # Skip leading D's.
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


if __name__ == '__main__':


    if 0:
        tmp = _AAA_from_CDR(identity_rule, 5)
        print(tmp)

        print(identity_matrices.AAA_from_CDR[5])
        print(identity_matrices.stats(5, 3))


    import doctest
    print(doctest.testmod())
