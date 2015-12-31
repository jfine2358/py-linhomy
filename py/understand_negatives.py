'''Calculations to understand the negative coefficients

This is a temporary working file.

The simplest rule to fix this is to have that C increments at any
available position.

In other words '1000' -> '1100' and '1001' (new).
And also '0101' -> '0201' and '0102' (new).
'''

import numpy

from linhomy.fibonacci import INDEXES
from linhomy.fibonacci import FIB_WORDS


def a(s):

    return numpy.array(
        list(map(int, s.split())),
        dtype = int
    )


if 1:
    ccc_ccc = a('1 16 48 68 240 56 320 480 28 240 480 408 1440')
    ccc_cic = a('1 20 62 88 316 71 424 638 34 316 638 536 1920')
    cic_cic = a('1 25 80 114 416 90 562 848 41 416 848 704 2560')
    cic_icc = a('1 30 93 127 474 96 636 957 42 474 957 772 2880')
    icc_icc = a('1 36 108 141 540 102 720 1080 43 540 1080 846 3240')

    # CD = CIC - CCC, so CD * CD is ...
    flag_value = ccc_ccc - 2 * ccc_cic + cic_cic

    print(list(flag_value))


    from linhomy.matrices import IC_from_FLAG

    ic_value = numpy.dot(IC_from_FLAG[6], flag_value)

    print(list(ic_value))

if 1:

    cccccc = a('1 7 21 35 105 35 140 210 21 105 210 210 630')
    ccccic = a('1 8 26 45 136 45 184 278 26 136 278 278 840')
    cccicc = a('1 9 30 51 156 49 207 315 27 150 312 309 945')
    cciccc = a('1 10 33 54 168 50 220 336 27 160 334 324 1008')
    ccicic = a('1 12 42 70 220 64 290 446 33 208 443 428 1344')
    cicccc = a('1 11 35 55 175 50 230 350 27 170 350 330 1050')
    ciccic = a('1 13 44 71 228 64 303 464 33 221 464 436 1400')
    cicicc = a('1 15 51 80 261 69 341 525 34 246 522 483 1575')
    iccccc = a('1 12 36 55 180 50 240 360 27 180 360 330 1080')
    icccic = a('1 14 45 71 234 64 316 477 33 234 477 436 1440')
    iccicc = a('1 16 52 80 268 69 356 540 34 260 536 483 1620')
    iciccc = a('1 18 57 84 288 70 380 576 34 280 574 504 1728')
    icicic = a('1 22 73 109 378 89 502 765 41 366 762 664 2304')

    flag_ic_value = (
        # cccccc
        - ccccic
        + cccicc
        + cciccc
        - ccicic
        - cicccc
    + 2 * ciccic
        - cicicc
        + iccccc
        - icccic
        # iciccc
        - iciccc
        + icicic
    )

    print(list(flag_ic_value))

# jfine@apricot:~/py-linhomy2/py$ python -i work2.py
# [0, 1, 4, 6, 24, 4, 34, 52, 1, 24, 52, 40, 160]
# [0, -1, 1, 1, -1, -1, 2, -1, 1, -1, 0, -1, 1]
# [0, 1, 4, 6, 24, 4, 34, 52, 1, 24, 52, 40, 160]

from linhomy.matrices import CD_from_IC

cd_value = list(numpy.dot(CD_from_IC[6], ic_value))

print(
    [
        (c, e)
        for (c, e) in zip(cd_value, FIB_WORDS[6])
        if c
    ])



from linhomy.product import product_formula
from linhomy.product import change_product_basis
from linhomy.matrices import IC_from_CD
from linhomy.matrices import CD_from_IC
from linhomy.matrices import CD_from_FLAG
from linhomy.matrices import CD_from_G

def doit_CD(n, m):

    return change_product_basis(
        product_formula(n, m),
        IC_from_CD[n],
        IC_from_CD[m],
        CD_from_FLAG[n+m]
    )

cd_dc_product = (
    + doit_CD(3, 3)[1, 1]
    + doit_CD(3, 3)[2, 2]
    - doit_CD(3, 3)[1, 2]
    - doit_CD(3, 3)[1, 2]
)

print(
    [
        (c, e)
        for (c, e) in zip(cd_dc_product, FIB_WORDS[6])
        if c
    ])

# [(2, '\x01\x02\x01\x02'), (-1, '\x01\x02\x02\x01'), (1, '\x02\x02\x02')]
# [(2, '\x01\x02\x01\x02'), (-1, '\x01\x02\x02\x01'), (-2, '\x02\x01\x01\x02'), (1, '\x02\x02\x01\x01')]


from linhomy.work import doit_G
from linhomy.matrices import G_from_CD


from linhomy.rules import C_rule
from linhomy.rules import D_rule


def C(indexes):

    return list(
        j
        for i in indexes
        for j in C_rule(i)
    )

def D(indexes):

    return list(
        j
        for i in indexes
        for j in D_rule(i)
    )

CDCD = tmp = C(D(C(D([(0,0)]))))
print(' '.join(''.join(map(str, index)) for index in tmp))

DCCD = tmp = D(C(C(D([(0,0)]))))
print(' '.join(''.join(map(str, index)) for index in tmp))

CDDC = tmp = C(D(D(C([(0,0)]))))
print(' '.join(''.join(map(str, index)) for index in tmp))

DDCC = tmp = D(D(C(C([(0,0)]))))
print(' '.join(''.join(map(str, index)) for index in tmp))

# 22 0011 0003 1100 000000 0201
# 22 1001 0102 1100 0201
# 22 0011 0003
# 22

DCD = tmp = D(C(D([(0,0)])))
print(' '.join(''.join(map(str, index)) for index in tmp))

# 21 1000 0101

# Applying coefficients +2, -2, -1, +1 to the above we really do get
# two negative values, at '1001' and '0102'.

# The simplest rule to fix this is to have that C increments at any
# available position.

# In other words '1000' -> '1100' and '1001' (new).
# And also '0101' -> '0201' and '0102' (new).

print(INDEXES[6].index(b'\x00' * 6))
# 6

tmp = [0] * 13
tmp[6] = 1

cd_vector = list(numpy.dot(CD_from_G[6], tmp))
print(cd_vector)
# [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

print(
    [
        (c, e)
        for (c, e) in zip(cd_vector, FIB_WORDS[6])
        if c
    ])
# [(1, b'\x01\x02\x01\x02'), (-1, b'\x01\x02\x02\x01'), (-1, b'\x02\x01\x01\x02'), (1, b'\x02\x02\x01\x01')]

# Compute (by hand) I applied to above (ie multiplication by C).

CCDCD = tmp = C(C(D(C(D([(0,0)])))))
print(' '.join(''.join(map(str, index)) for index in tmp))

CCDDC = tmp = C(C(D(D(C([(0,0)])))))
print(' '.join(''.join(map(str, index)) for index in tmp))

DCCCD = tmp = D(C(C(C(D([(0,0)])))))
print(' '.join(''.join(map(str, index)) for index in tmp))

DDCCC = tmp = D(D(C(C(C([(0,0)])))))
print(' '.join(''.join(map(str, index)) for index in tmp))

# 23 0012 0004 0111 0103 1200 000100 1101 000001 010000
# 23 0012 0004 0111 0103
# 23 1002 1101 1200
# 23

# Hand calculation of signed sum give
# (+) 000100 000001 010000
# (-) 1002


g_vector = list(doit_G(1, 6)[0][6])
print(g_vector)
# [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0]

# This agrees with the hand calculation.
print([index for (i, index) in zip(g_vector, INDEXES[7]) if i])
# [
#     b'\x00\x01\x00\x00\x00\x00',
#     b'\x00\x00\x00\x01\x00\x00',
#     b'\x00\x00\x00\x00\x00\x01',
#     b'\x01\x00\x00\x02'
# ]

# We apply D to this to get the negative.  It's straightforward.
CCCD = tmp = C(C(C(D([(0,0)]))))
print(' '.join(''.join(map(str, index)) for index in tmp))
# 13 0002 0101 0200


# We apply C to this to get the 'top' term.
CDCD = tmp = C(D(C(D([(0,0)]))))
print(' '.join(''.join(map(str, index)) for index in tmp))
# 22 0011 0003 1100 1001 000000


g_vector = list(doit_G(3, 4)[1][2])
print(g_vector)                                   #!!
# [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, -1, 0, 0, 0, 0]

cd_vector = list(numpy.dot(CD_from_G[7], g_vector))
print(cd_vector)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, -1, 0, 0, -1, -1, 0, 0, 1, 0, 0]

terms = [
    (c, ''.join(map(str, ind)))
    for (c, ind) in zip(cd_vector, FIB_WORDS[7])
    if c
]

print(terms)
# [
#     (1, '12112'),
#     (1, '12121'),
#     (-1, '12211'),
#     (-1, '21112'),
#     (-1, '21121'),
#     (1, '22111'),
# ]

tmp = C(D(C(C(D([(0,0)])))))
print(' '.join(''.join(map(str, index)) for index in tmp))

tmp = C(D(C(D(C([(0,0)])))))
print(' '.join(''.join(map(str, index)) for index in tmp))

tmp = C(D(D(C(C([(0,0)])))))
print(' '.join(''.join(map(str, index)) for index in tmp))

tmp = D(C(C(C(D([(0,0)])))))
print(' '.join(''.join(map(str, index)) for index in tmp))

tmp = D(C(C(D(C([(0,0)])))))
print(' '.join(''.join(map(str, index)) for index in tmp))

tmp = D(D(C(C(C([(0,0)])))))
print(' '.join(''.join(map(str, index)) for index in tmp))

# 23 0012 0004 1101 000001 1200 1002 000100
# 23 0012 0004 1101 000001
# 23 0012 0004
# 23 1002 1101 1200
# 23 1002 1101
# 23


tmp = D(C(D(C([(0,0)]))))
print(' '.join(''.join(map(str, index)) for index in tmp))
# 22 1001


g_vector = list(doit_G(3,5)[1][4])
print(g_vector)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
#  1, 0, 1, 1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

cd_vector = list(numpy.dot(CD_from_G[8], g_vector))
print(cd_vector)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1,
# 1, 1, 1, -1, 0, 1, 0, 1, -1, 0, 0, 0, -1, -1, 0, 1, 0]

terms = [
    (c, ''.join(map(str, ind)))
    for (c, ind) in zip(cd_vector, FIB_WORDS[8])
    if c
]

print(terms)
# [
#     (-1, '121112'),
#     (-1, '121211'),
#     (1, '12122'),
#     (1, '122111'),
#     (1, '12212'),
#     (-1, '12221'),
#     (1, '211112'),
#     (1, '211211'),
#     (-1, '21122'),
#     (-1, '221111'),
#     (-1, '22112'),
#     (1, '22211')
# ]


def expand_word(word):

    value = [(0, 0)]
    for c in reversed(word):

        value = {'1': C, '2': D}[c](value)

    value = ' '.join(''.join(map(str, index)) for index in value)
    return value

for c, word in terms:
    print(c, ' # ', expand_word(word))


# -1  #  24 0013 0005 1102 1003 000002 1201 000101 1300 1102 000200
# -1  #  24 0013 0005 1102 1003 000002
#  1  #  32 0021 0013 0005 1110 1011 000010 1102 1003 000002
#  1  #  24 0013 0005
#  1  #  32 0021 0013 0005 2100 2001 001000 000200
# -1  #  32 0021 0013 0005
#  1  #  24 1003 1102 1201 1300
#  1  #  24 1003 1102
# -1  #  32 1011 1003 1110 1102
# -1  #  24
# -1  #  32 2001 2100
#  1  #  32

# Exploring

# 8 1
# [010000] * [01] = [020000] + [100000]
# [000100] * [01] = [010100] + [000200]
# [000001] * [01] = [010001] + [000101] + [000002]

print('Exploring 8 1, rank 1, 3')

i = INDEXES[7].index(b'\x00\x01\x00\x00\x00\x00')

print(i)
# 6
g_row = [0] * 21
g_row[6] = 1
cd_row = list(numpy.dot(CD_from_G[7], g_row))
print(cd_row)
# [0, 0, 0, 0, 0, 0, 1, -1, 0, -1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

doit_CD(1, 7)[0]


# The following confirms
# [010000] * [01] = [020000] + [100000]
# and gives insight into it rectification (if required).
# Work in Dec 2015 suggest that the above line is correct.

# Find the index of the g-indexes.
i = INDEXES[8].index(b'\x00\x02\x00\x00\x00\x00')
j = INDEXES[8].index(b'\x01\x00\x00\x00\x00\x00')
print(i, j)
# 6 27

# Convert into a CD vector.
g_row = [0] * 34
g_row[6] = g_row[27] = 1


from linhomy.fibonacci import FIBONACCI
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


cd_value = list(numpy.dot(CD_from_G[8], g_row))

# Split into C and D parts.
c_g_part, d_g_part = cd_inverse(8, g_row)

print(c_g_part)
print(d_g_part)
# [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]

# Turn the parts back into g-indexes.
# >>> INDEXES[7][6]
# b'\x00\x01\x00\x00\x00\x00'
# >>> INDEXES[6][6]
# b'\x00\x00\x00\x00\x00\x00'

# Compute what C and D do on the g-indexes.
# >>> from linhomy.rules import C_rule
# >>> C_rule((0, 1, 0, 0, 0, 0))
# <generator object C_rule at 0x7f1f8986fea0>
# >>> list(C_rule((0, 1, 0, 0, 0, 0)))
# [(0, 2, 0, 0, 0, 0)]
# >>> list(D_rule((0, 0, 0, 0, 0, 0)))
# [(1, 0, 0, 0, 0, 0)]
