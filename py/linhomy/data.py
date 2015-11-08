'''Interface for reading data stored in files

>>> for line in IC_flag[3]:
...     print(str(line))
CCC 1 4 6
CIC 1 5 8
ICC 1 6 9
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import os

_DATAPATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '_data'
    )
)


class _Reader:

    def __init__(self, template):

        self._template = template

    def __getitem__(self, deg):
        '''Iterate over lines in degree deg file.

        Trailing white space is removed.
        '''
        short_name = self._template.format(deg)
        full_name = os.path.join(_DATAPATH, short_name)
        with open(full_name, 'r') as f:
            for line in f:
                yield line.rstrip()


IC_flag = _Reader('IC-{0}-flag.txt')
J_flag = _Reader('J-{0}-flag.txt')
P_flag = _Reader('P-{0}-flag.txt')
