'''New approach based on rank and {i}

Arises from
  C^r{CD_1 ...} + {C^rD_1C ...} = {C^rCD_1 ...}

>>> for chain in iter_chains(6):
...     str(' ').join(map(CD_from_word, chain))
'CDCCC CCDCC CCCDC'

>>> for chain in iter_chains(8):
...     str(' ').join(map(CD_from_word, chain))
'CDCCCCC CCDCCCC CCCDCCC CCCCDCC CCCCCDC'
'CDCCCD CCDCCD CCCDCD'
'CDCCDC CCDCDC'
'CDDCCC CCDDCC CCCDDC'


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


split_re = re.compile(b'(\x01\x02+\x01)(\x01+)(.*)')
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

    return value

# CDR_from_basic = invert_grow_list(basic_from_CDR)


if __name__ == '__main__':

    import doctest
    print(doctest.testmod())
