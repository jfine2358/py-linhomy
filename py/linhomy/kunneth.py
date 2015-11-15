'''Write Kunneth formula for current G to stdout

'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

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

            if condition and not condition(ind1, ind2):
                break

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


def doit(condition=None):

    for n in range(2, 11):
        for m in range(1, n):
            if 2 * m <= n:

                rows = list(iter_rows(n-m, m, condition))
                if rows:
                    print(n, m)
                    for row in rows:
                        lhs, rhs = row
                        print(lhs, '=', rhs)
                    print('\n')


def simple(ind1, ind2):

    return len(ind1) == len(ind2) == 2




if __name__ == '__main__':

    import sys

    lookup = dict(
        simple = simple,
    )

    condition = None
    if len(sys.argv) == 2:
        condition = lookup[sys.argv[1]]

    doit(condition)
