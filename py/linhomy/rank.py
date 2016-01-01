'''Tools for dealing with words by rank

'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import itertools
import re

from .fibonacci import FIB_WORDS
from .six import PY3

def get_rank(fibword):
    '''Return number of CD's in fibword.

    >>> get_rank(b'\x01\x02')
    1
    >>> list(map(get_rank, FIB_WORDS[6]))
    [0, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 0, 0]
    '''
    return fibword.count(b'\x01\x02')


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    items = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(items, r)
        for r
        in range(len(items)+1)
    )


def cut(seq, indices):
    '''Cut at successive indexes to yield subsequences.
    '''
    start = None
    for stop in indices:
        yield seq[start:stop]
        start = stop
    yield seq[start:None]


find_rank_mos = re.compile(b'\x01(?=\x02)').finditer

def get_rank_indices(word):
    '''Return indices that split word into rank zero pieces.

    >>> list(get_rank_indices(b'\x01\x02\x02\x01\x02'))
    [1, 4]
    '''
    for mo in find_rank_mos(word):
        yield mo.end()


if PY3:
    def str_from_word(word):
        return ''.join(map(str, word))
else:
    def str_from_word(word):
        return  str('').join(str(ord(c)) for c in word)


def rank_reduce(word):
    '''Remove rank indices to yield words of possibly lower rank.

    >>> for val in rank_reduce(b'\x01\x02\x02' * 3):
    ...     str_from_word(val)
    '222222111'
    '122222211'
    '221122221'
    '222211122'
    '122122221'
    '122221122'
    '221122122'
    '122122122'
    '''
    indices = get_rank_indices(word)

    for cut_indices in powerset(indices):

        yield b''.join(
            b'\x02' * piece.count(b'\x02')
            + b'\x01' * piece.count(b'\x01')
            for piece in cut(word, cut_indices)
        )
