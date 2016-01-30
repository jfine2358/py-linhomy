'''New approach based on rank and {i}

Arises from
  C^r{CD_1 ... } + {C^rD_1C ...} = {C^rCD_1 ...}

>>> for chain in iter_chains(6):
...     str(' ').join(map(CD_from_word, chain))
'CDCCC CCDCC CCCDC'

>>> for chain in iter_chains(8):
...     str(' ').join(map(CD_from_word, chain))
'CDCCCCC CCDCCCC CCCDCCC CCCCDCC CCCCCDC'
'CDCCCD CCDCCD CCCDCD'
'CDCCDC CCDCDC'
'CDDCCC CCDDCC CCCDDC'

'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import re
from .fibonacci import FIB_WORDS
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


if __name__ == '__main__':

    import doctest
    print(doctest.testmod())
