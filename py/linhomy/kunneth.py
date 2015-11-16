'''Write Kunneth formula for current G to stdout

'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import sys

from .fibonacci import INDEXES
from .work import doit_G
from .six import iterbytes

product_format = '[{0}] * [{1}]'.format

def pretty_vector(vector):

    lookup = dict()
    lookup[True] = '[{value}]'.format
    lookup[False] = '{c}*[{value}]'.format

    return ' + '.join(
        lookup[c==1](c=c, value=value)
        for c, value in  vector
    )


def iter_rows(n, m, condition):

    matrix = doit_G(n, m)

    for i, ind1 in enumerate(INDEXES[n]):
        for j, ind2 in enumerate(INDEXES[m]):

            # Skip if condition not satisfied.
            if condition and not condition(ind1, ind2):
                continue

            lhs = product_format(
                str('').join(map(str, iterbytes(ind1))),
                str('').join(map(str, iterbytes(ind2))),
            )

            row = matrix[i, j]

            value = [
                (c, str('').join(map(str, iterbytes(ind3))))
                for c, ind3 in zip(row, INDEXES[n+m])
                if c
            ]

            rhs = pretty_vector(value)

            yield lhs, rhs


def doit(condition=None, file=sys.stdout):

    for n in range(2, 11):
        for m in range(1, n):
            if 2 * m <= n:

                rows = list(iter_rows(n-m, m, condition))
                if rows:
                    print(n, m, file=file)
                    for row in rows:
                        lhs, rhs = row
                        print(lhs, '=', rhs, file=file)
                    print('\n', file=file)


def simple(ind1, ind2):

    return len(ind1) == len(ind2) == 2


ZERO = b'\x00'[0]
def rank_1_2(ind1, ind2):

    # Skip the trivial cases.
    if ind1[0] == ind2[0] == ZERO:
        return {len(ind1), len(ind2)} == {2, 4}
    else:
        return False

def rank_1_3(ind1, ind2):

    # Skip the trivial cases.
    if ind1[0] == ind2[0] == ZERO:
        return {len(ind1), len(ind2)} == {2, 6}
    else:
        return False

def rank_2_2(ind1, ind2):

    # Skip the trivial cases.
    if ind1[0] == ind2[0] == ZERO:
        return {len(ind1), len(ind2)} == {4}
    else:
        return False


if __name__ == '__main__':

    import sys
    import os

    lookup = dict(
        simple = simple,
        rank_1_2 = rank_1_2,
        rank_1_3 = rank_1_3,
        rank_2_2 = rank_2_2,
    )

    pairs = [
        ('kunneth-' + key + '.txt', value)
        for (key, value)
        in lookup.items()
    ]

    pairs.append(('kunneth.txt', None))
    pairs.sort()

    for filename, value in pairs:

        with open(filename, 'w') as f:
            doit(value, f)
