'''Tools

>>> def roundtrip(s):
...     b = bytes_from_str(s)
...     s2 = str_from_bytes(b)
...     return list(iterbytes(b)), s2
>>> roundtrip('0123')
([0, 1, 2, 3], '0123')


TODO: What about slices?  Present behaviour is undefined.
>>> @grow_list
... def SQUARES(self):
...     return len(self) ** 2
>>> SQUARES[0], SQUARES[1], SQUARES[5]
(0, 1, 25)


>>> import itertools
>>> def grow(key_lists):
...     if not key_lists:
...         return ('',)
...     prev = key_lists[-1]
...     return tuple(
...         head + tail
...         for (head, tail)
...         in itertools.product(('a', 'b'), key_lists[-1])
...     )

>>> wordss = KeyLists(grow, len)
>>> wordss[3]
('aaa', 'aab', 'aba', 'abb', 'baa', 'bab', 'bba', 'bbb')

>>> wordss.degree('abab')
4
>>> wordss.index('abbaa')
(5, 12)
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
#from __future__ import unicode_literals
__metaclass__ = type

from functools import update_wrapper
from .six import iterbytes
from .six import PY2, PY3

def str_from_bytes(b):

    # TODO: Implement base 36 string conversion.
    # The str('') is to avoid result being Unicode in Python2.
    return str('').join(map(str, iterbytes(b)))


if PY3:
    bytes_from_ints = bytes
    def bytes_from_str(s):
        # TODO: Implement base 36 string conversion.
        return bytes(map(int, s))

if PY2:
    def bytes_from_ints(items):

        return str('').join(map(chr, items))

    def bytes_from_str(s):
        # TODO: Implement base 36 string conversion.
        return str('').join(chr(int(c)) for c in s)

def pairs_from_items(items):
    '''Iterate over items, two items at a time.

    Ignores any odd item left over at end.
    '''

    items = iter(items)
    return zip(items, items)


def items_from_pairs(pairs):
    '''Iterate over pairs, one item at a time.

    Roughly equivalent to itertools.chain.from_iterable.
    '''

    for a, b in pairs:
        yield a
        yield b


def grow_list(grow):
    '''Return list where grow supplies missing elements.

    Argument grow(self) returns next item in the list.
    '''

    class GrowList(list):
        '''A list where grow supplies the missing elements.'''

        def __getitem__(self, key):

            # If necessary grow to provide value for the key.
            while len(self) <= key:
                self.append(grow(self))

            # Now use superclass method to get the value.
            return super(GrowList, self).__getitem__(key)

    value = GrowList()
    # NOTE:  The updated=() is required.
    return update_wrapper(value, grow, updated=())


class KeyLists:
    '''Self-growing collection of key lists
    '''

    def __init__(self, grow, degree):

        self.degree = degree
        self._grow = grow
        self._key_lists = []
        self._lookup_dicts =  []


    def __getitem__(self, deg):

        key_lists = self._key_lists
        while len(key_lists) <= deg:
            new_key_list = self._grow(key_lists)
            self._append(new_key_list)

        return key_lists[deg]


    def _append(self, key_list):

        self._key_lists.append(key_list)

        lookup = dict(
            (key, i)
            for (i, key)
            in enumerate(key_list)
        )

        self._lookup_dicts.append(lookup)


    def index(self, key):

        deg = self.degree(key)
        self[deg]               # Grow if need be.
        locn = self._lookup_dicts[deg][key]
        return deg, locn


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
