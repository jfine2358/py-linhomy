'''Material related to Fibonacci numbers and objects

TODO: What about slices?  Present behaviour is undefined.
>>> FIBONACCI[12]
144

>>> from .tools import str_from_bytes
>>> list(map(str_from_bytes, FIB_WORDS[0]))
['']
>>> list(map(str_from_bytes, FIB_WORDS[1]))
['1']
>>> list(map(str_from_bytes, FIB_WORDS[4]))
['1111', '112', '121', '211', '22']

>>> for word in FIB_WORDS[6]:
...     index = index_from_word(word)
...     word_2 = word_from_index(index)
...     print(str_from_bytes(word), str_from_bytes(index))
...     if word != word_2: print('roundtripping failure')
111111 06
11112 0300
11121 0201
11211 0102
1122 0110
12111 0003
1212 000000
1221 0011
21111 14
2112 1100
2121 1001
2211 22
222 30

>>> list(map(str_from_bytes, INDEXES[0]))
['00']
>>> list(map(str_from_bytes, INDEXES[1]))
['01']
>>> list(map(str_from_bytes, INDEXES[5]))
['05', '0200', '0101', '0002', '0010', '13', '1000', '21']
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import itertools

from .six import iterbytes
from .tools import grow_list
from .tools import bytes_from_ints
from .tools import items_from_pairs
from .tools import pairs_from_items
from .tools import key_lists_from_fn


# Useful constants.
_empty = b''
_one = b'\x01'
_two = b'\x02'
_one_two = b'\x01\x02'

@grow_list
def FIBONACCI(self):
    '''A GrowList that contains [0, 1, 1, 2, 3, 5, 8, 13, ...].'''

    if len(self) < 2:
        return [0, 1][len(self)]

    return self[-2] + self[-1]


@key_lists_from_fn
def FIB_WORDS():
    '''A KeysList for Fibonacci words.

    Each word is a one-two sequence of bytes.
    '''
    initial = [(b'',), (b'\x01',)]

    def grow(key_lists):

        n = len(key_lists)
        return tuple(itertools.chain(
            (b'\x01' + i for i in key_lists[n-1]),
            (b'\x02' + i for i in key_lists[n-2]),
        ))

    def degree(key):
        return sum(iterbytes(key))

    return locals()


def index_from_word(word):

    pieces =  word.split(_one_two)
    return bytes_from_ints(
        items_from_pairs(
            (p.count(_two), p.count(_one))
            for p in pieces
        ))

def word_from_index(index):

    if len(index) % 2:
        raise ValueError

    return _one_two.join(
        _two * a + _one * b
       for a, b in pairs_from_items(iterbytes(index))
    )

@key_lists_from_fn
def INDEXES():
    '''A KeyList that contains the Fibonacci indexes, by degree.

    Each index is an even-length sequence of bytes.
    '''

    initial = ()

    def grow(key_list):
        words = FIB_WORDS[len(key_list)]
        return tuple(map(index_from_word, words))

    def degree(index):

        deg = 0
        ints = iterbytes(index)
        for d, c in zip(ints, ints):
            deg += 3 + 2 * d + c
        return deg

    return locals()


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
