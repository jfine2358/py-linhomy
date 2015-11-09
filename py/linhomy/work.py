'''Assemble what we have and try it out

Sadly we get an error.  But at n=6 so might be easy to fix.  In
winter 2014-15 calculations we got past 6.

>>> doit(2, 3)
array([[[1, 0, 0, 0, 0, 1, 0, 1],
        [0, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1]],
<BLANKLINE>
       [[0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1]]])

>>> doit(3, 3)
array([[[ 1,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  1],
        [ 0,  1,  1,  1,  0,  1,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0]],
<BLANKLINE>
       [[ 0,  1,  1,  1,  0,  1,  0,  0,  0,  0,  0,  0,  0],
        [ 0,  0,  0, -2,  0,  1,  2,  1,  0,  0, -2,  0,  0],
        [ 0,  0,  1,  1,  0,  0,  0,  0,  0,  1,  1,  0,  0]],
<BLANKLINE>
       [[ 0,  0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  1,  0],
        [ 0,  0,  1,  1,  0,  0,  0,  0,  0,  1,  1,  0,  0],
        [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1]]])
'''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

import itertools
import numpy


from .matrices import G_from_FLAG
from .matrices import IC_from_G

from .product import product_formula
from .product import change_product_basis



def doit(n, m):

    return change_product_basis(
        product_formula(n, m),
        IC_from_G[n],
        IC_from_G[m],
        G_from_FLAG[n+m]
    )
