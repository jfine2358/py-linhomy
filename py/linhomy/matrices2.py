'''New approach based on rank and {i}

Arises from
  C^r{CD_1 ...} + {C^rD_1C ...} = {C^rCD_1 ...}

>>> for chain in iter_chains(4):
...     str(' ').join(map(CD_from_word, chain))
'CDC CCD'

>>> for chain in iter_chains(5):
...     str(' ').join(map(CD_from_word, chain))
'CDCC CCDC CCCD'

>>> for chain in iter_chains(6):
...     str(' ').join(map(CD_from_word, chain))
'CDCCC CCDCC CCCDC CCCCD'
'CDDC CCDD'

>>> for chain in iter_chains(8):
...     str(' ').join(map(CD_from_word, chain))
'CDCCCCC CCDCCCC CCCDCCC CCCCDCC CCCCCDC CCCCCCD'
'CDCCCD CCDCCD CCCDCD'
'CDCCDC CCDCDC'
'CDDCCC CCDDCC CCCDDC CCCCDD'
'CDDDC CCDDD'

Arises from
    C{D_1 ...} + {D_1C ...} = {CD_1 ...}

>>> for chain in iter_pairs(3):
...     str(' ').join(map(CD_from_word, chain))
'DC CD'

>>> for chain in iter_pairs(4):
...     str(' ').join(map(CD_from_word, chain))
'DCC CDC'

>>> for chain in iter_pairs(5):
...     str(' ').join(map(CD_from_word, chain))
'DCCC CDCC'
'DDC CDD'

>>> for chain in iter_pairs(6):
...     str(' ').join(map(CD_from_word, chain))
'DCCCC CDCCC'
'DCCD CDCD'
'DDCC CDDC'


I've made a mistake somewhere.  Should not get negatives.
>>> basic_matrices.print_C_stats(10)
0 [(1, 1)]
1 [(0, 1), (1, 1)]
2 [(0, 3), (1, 3)]
3 [(0, 11), (1, 4)]
4 [(0, 33), (1, 7)]
5 [(0, 92), (1, 12)]
6 [(-1, 1), (0, 253), (1, 19)]
7 [(-1, 2), (0, 680), (1, 32)]
8 [(-1, 5), (0, 1814), (1, 51)]
9 [(-1, 9), (0, 4802), (1, 84)]
10 [(-1, 17), (0, 12664), (1, 135)]

This allow us to find what is going wrong.
>>> for d in range(1, 7):
...     basic_matrices.print_rule(d)
1 C -> C
2 CC -> CC
2 D -> D
3 CCC -> CCC
3 CD -> CD
3 DC -> DC
4 CCCC -> CCCC
4 CCD -> CCD CDC
4 CDC -> CDC
4 DCC -> DCC
4 DD -> DD
5 CCCCC -> CCCCC
5 CCCD -> CCCD CCDC CDCC
5 CCDC -> CCDC CDCC
5 CDCC -> CDCC
5 CDD -> CDD
5 DCCC -> DCCC
5 DCD -> DCD
5 DDC -> DDC
6 CCCCCC -> CCCCCC
6 CCCCD -> CCCCD CCCDC CCDCC CDCCC
6 CCCDC -> CCCDC CCDCC CDCCC
6 CCDCC -> CCDCC CDCCC
6 CCDD -> CCDD CDDC
6 CDCCC -> CDCCC
6 CDCD -> CDCD
6 CDDC -> CDDC
6 DCCCC -> DCCCC
6 DCCD -> DCCD DCDC
6 DCDC -> DCDC
6 DDCC -> DDCC
6 DDD -> DDD
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import itertools
import re

from .fibonacci import FIBONACCI
from .fibonacci import FIB_WORDS
from .matrices import fib_zeros_array
from .matrices import grow_list
from .matrices import invert_grow_list
from .rankmatrices import CD_from_word
from .rankmatrices import word_from_CD
from .rankmatrices import RankMatrices


# TODO: Document or explain this regular expression.
split_re = re.compile(b'(\x01\x02+)(\x01+)((?:\x01|$).*)')
def split_word(word):

    mo = split_re.match(word)
    if mo:
        return mo.groups()
    else:
        return None


def chain_from_split(pre, c_s, post):

    return tuple(
        c_s[:i]
        + pre
        + c_s[i:]
        + post
        for i in range(len(c_s) + 1)
        )


def iter_chains(n):

    for word in FIB_WORDS[n]:
        tmp = split_word(word)
        if tmp:
            yield chain_from_split(*tmp)


pair_split_re = re.compile(b'(\x02+)(\x01)((?!\x02).*)')
def pair_split(word):

    mo = pair_split_re.match(word)
    if mo:
        return mo.groups()
    else:
        return None

def iter_pairs(n):

    for word in FIB_WORDS[n]:
        tmp = pair_split(word)
        if tmp:
            pre, c, post = tmp
            yield pre + c + post, c + pre + post


@grow_list
def identity(self):

    deg = len(self)
    value = fib_zeros_array(deg, deg)

    for j, word in enumerate(FIB_WORDS[deg]):
        i = j
        value[i, j] += 1

    return value

invert_identity = invert_grow_list(identity)


@grow_list
def basic_from_CDR(self):
    '''Diagonal elements, and ensure C and D rules non-negative.
    '''

    d = len(self)
    value = fib_zeros_array(d, d)


    # Step 1.  Add C^d (which always has index 0).
    word = b'\x01' * d
    i = j = FIB_WORDS[d].index(word)
    value[i, j] += 1

    # Step 2.  Everything of the form Dw.
    if d >= 2:
        src = self[d - 2]

        # Iterate over the src array.
        # TODO: Refactor.
        ranges = map(range, src.shape)
        for coord in itertools.product(*ranges):
            coeff = src[coord]
            if coeff:
                i, j = coord
                i_word = FIB_WORDS[d-2][i]
                j_word = FIB_WORDS[d-2][j]

                # Compute and use new words.
                new_i = FIB_WORDS[d].index(b'\x02' + i_word)
                new_j = FIB_WORDS[d].index(b'\x02' + j_word)

                # Increment value.
                value[new_i, new_j] += 1

    # Step 3. Do all the pairs, to give value to CDw.
    for d_word, c_word in iter_pairs(d):
        d_index = FIB_WORDS[d].index(d_word)
        c_index = FIB_WORDS[d].index(c_word)

        # Transfer values from d_col to c_col.
        d_col = value[:, d_index]
        c_col = value[:, c_index]
        # This is wrong, at least as is.
        if 0:
            c_col += d_col

        # Add the diagonal value.
        c_col[c_index] += 1

    # Step 4. Do chains, to give values to C^rD for r>1.
    for chain in iter_chains(d):
        for word_1, word_2 in zip(chain, chain[1:]):
            index_1 = FIB_WORDS[d].index(word_1)
            index_2 = FIB_WORDS[d].index(word_2)

            # Transfer the existing values.
            value[:, index_2] += value[:, index_1]

            # Add the diagonal value.
            value[index_2, index_2] += 1

    return value

CDR_from_basic = invert_grow_list(basic_from_CDR)

basic_matrices = RankMatrices(matrices=basic_from_CDR)


if __name__ == '__main__':

    import doctest
    print(doctest.testmod())
