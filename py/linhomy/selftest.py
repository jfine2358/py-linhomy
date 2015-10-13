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
    import linhomy.fibonacci
    import linhomy.rules
    import linhomy.tools

    modules = [
        linhomy,
        linhomy.classtools,
        linhomy.fibonacci,
        linhomy.rules,
        linhomy.tools,
    ]

    # TODO: Pick up 'verbose' from the command line?
    for mod in modules:

        prefix = mod.__name__.ljust(20)
        print(prefix, doctest.testmod(mod))
