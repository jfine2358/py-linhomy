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
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from functools import update_wrapper
from .six import iterbytes
from .six import PY2, PY3

def str_from_bytes(b):

    # TODO: Implement base 36 string conversion.
    # The str('') is to avoid result being Unicode in Python2.
    return str('').join(map(str, iterbytes(b)))


if PY3:
    def bytes_from_str(s):
        # TODO: Implement base 36 string conversion.
        return bytes(map(int, s))

if PY2:
    def bytes_from_str(s):
        # TODO: Implement base 36 string conversion.
        return str('').join(chr(int(c)) for c in s)


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


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
