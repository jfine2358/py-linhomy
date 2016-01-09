'''Explore matrices that respect rank

identity_matrices = RankMatrices(identity_rule)
>>> for n in range(2, 11):
...     for m in range(1, n):
...         if 2 * m <= n:
...             print(n, m, identity_matrices.stats(n - m, m))
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

'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type


from collections import Counter
import numpy
from .fibonacci import FIB_WORDS
from .matrices import fib_zeros_array
from .matrices import invert_grow_list
from .matrices import CDR_from_FLAG
from .matrices import IC_from_CDR
from .product import product_formula
from .product import change_product_basis
from .tools import grow_list

def identity_rule(word):
    yield word


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


class RankMatrices:

    def __init__(self, rule):
        self.rule = rule

        self.AAA_from_CDR = grow_list(
            lambda self_: _AAA_from_CDR(rule, len(self_))
        )

        self.CDR_from_AAA = invert_grow_list(self.AAA_from_CDR)

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

        self.doit = lambda n, m: change_product_basis(
            product_formula(n, m),
            self.IC_from_AAA[n],
            self.IC_from_AAA[m],
            self.AAA_from_FLAG[n+m]
        )

        self.stats = lambda n, m: sorted(
            Counter(self.doit(n, m).flatten()).items()
        )



identity_matrices = RankMatrices(identity_rule)


if __name__ == '__main__':


    if 0:
        tmp = _AAA_from_CDR(identity_rule, 5)
        print(tmp)

        print(identity_matrices.AAA_from_CDR[5])
        print(identity_matrices.stats(5, 3))


    import doctest
    print(doctest.testmod())
