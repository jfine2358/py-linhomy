'''Explain product in terms of C and D rules

Usage: $ python3 -m linhomy.explain 0010 0001

'''

import numpy

from .fibonacci import FIBONACCI
from .fibonacci import FIB_WORDS
from .fibonacci import INDEXES
from .matrices import CD_from_G
from .matrices import G_from_CD
from .rules import C_rule
from .rules import D_rule
from .six import iterbytes
from .six import PY3
from .work import doit_G


FIBONACCI[20]                   # Grow to large enough.


def cd_inverse(d, g_row):
    '''Return C and D factors of g_row, in G basis.

    Parameter d is the dimension of g. We have
    g_row =  C(c_part) + D(d_part).
    '''
    cd_value = list(numpy.dot(CD_from_G[d], g_row))

    fib_d = FIBONACCI[d]        # Two off-by-ones cancel here.
    # Split into C and D parts.
    c_cd_part, d_cd_part = cd_value[:fib_d], cd_value[fib_d:]

    # Express the parts using the G basis.
    c_part = list(numpy.dot(G_from_CD[d-1], c_cd_part))
    d_part = list(numpy.dot(G_from_CD[d-2], d_cd_part))

    return c_part, d_part


def index_from_str(s):

    if PY3:
        return bytes(map(int, s))
    else:
        ddt


def deg_from_index(b):

    vals = tuple(iterbytes(b))
    rank = -1 + len(vals) // 2

    return 3 * rank + 2* sum(vals[0::2]) + sum(vals[1::2])


def str_from_index(i):

    return ''.join(map(str, iterbytes(i)))


def explain(s1, s2):

    # Compute indexes and their degrees.
    i1, i2 = map(index_from_str, (s1, s2))
    d1, d2 = map(deg_from_index, (i1, i2))
    d = d1 + d2

    # Compute the g-vector of the product.
    t1 = INDEXES[d1].index(i1)
    t2 = INDEXES[d2].index(i2)
    matrix = doit_G(d1, d2)
    row = matrix[t1, t2]

    # Compute the C and D parts.
    c_part, d_part = cd_inverse(d, row)

    #    print(row)
    #    print(c_part, d_part)

    print('Explaining [{s1}] * [{s2}]'.format(**locals()))


    for part, offset, rule, letter in [
            (c_part, 1, C_rule, 'C'),
            (d_part, 2, D_rule, 'D'),
    ]:

        print()
        print('Contribution from {letter}.'.format(letter=letter))

        for coeff, ind in zip(part, INDEXES[d - offset]):
            if coeff:
                sind = '[' + str_from_index(ind) + ']'

                aaa = ' + '.join(
                    '[' + str_from_index(val) + ']'
                    for val
                    in rule(tuple(iterbytes(ind)))
                )
                print('{coeff}: {sind} -> {aaa}'.format(**locals()))


if __name__ == '__main__':

    if 0:
        ind = index_from_str('1231')
        deg = deg_from_index(ind)

        print(ind, deg)

    import sys

    s1, s2 = sys.argv[1:]

    explain(s1, s2)
