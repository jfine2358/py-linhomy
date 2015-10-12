'''Material related to Fibonacci numbers and objects

TODO: What about slices?  Present behaviour is undefined.
>>> FIBONACCI[12]
144

>>> from .tools import str_from_bytes
>>> list(map(str_from_bytes, FIB_WORDS[4]))
['1111', '112', '121', '211', '22']
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import itertools
from .tools import grow_list

@grow_list
def FIBONACCI(self):
    '''A GrowList that contains [0, 1, 1, 2, 3, 5, 8, 13, ...].'''

    if len(self) < 2:
        return [0, 1][len(self)]

    return self[-2] + self[-1]

@grow_list
def FIB_WORDS(self):
    '''A GrowList that contains the Fibonacci words.

    Each word is a one-two sequence of bytes.
    '''
    if len(self) < 2:
        return [(b'',), (b'\x01',)][len(self)]

    return tuple(itertools.chain(
        (b'\x01' + i for i in self[-1]),
        (b'\x02' + i for i in self[-2]),
    ))


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
