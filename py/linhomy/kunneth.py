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


def print_rows(n, m):

    matrix = doit_G(n, m)

    for i, ind1 in enumerate(INDEXES[n]):
        for j, ind2 in enumerate(INDEXES[m]):
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

            print(lhs, '=', rhs)


for n in range(2, 11):
    for m in range(1, n):
        if 2 * m <= n:

            print(n, m)
            print_rows(n - m, m)
            print('\n')
