'''Material related to Fibonacci numbers and objects

TODO: What about slices?  Present behaviour is undefined.
>>> FIBONACCI[12]
144
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from .tools import grow_list

@grow_list
def FIBONACCI(self):
    '''A GrowList that contains [0, 1, 1, 2, 3, 5, 8, 13, ...].'''

    if len(self) < 2:
        return [0, 1][len(self)]

    return self[-2] + self[-1]


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
