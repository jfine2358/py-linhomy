'''Run self-test on all modules

Run this as a module and it will perform the self-test.
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


if __name__ == '__main__':

    import doctest

    import linhomy
    import linhomy.classtools
    import linhomy.data
    import linhomy.fibonacci
    import linhomy.matrices
    import linhomy.product
    import linhomy.rank
    import linhomy.rankmatrices
    import linhomy.rules
    import linhomy.tools
    import linhomy.work

    modules = [
        linhomy,
        linhomy.classtools,
        linhomy.data,
        linhomy.fibonacci,
        linhomy.matrices,
        linhomy.product,
        linhomy.rankmatrices,
        linhomy.rules,
        linhomy.tools,
        linhomy.work,
    ]

    # TODO: Pick up 'verbose' from the command line?
    for mod in modules:

        prefix = mod.__name__.ljust(20)
        print(prefix, doctest.testmod(mod))
