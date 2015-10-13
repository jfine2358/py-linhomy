'''

'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


# Exclude all keys provided by the empty class.
excluded_classdict_keys = set(
    type(str('name'), (object,), {}).__dict__.keys()
)


# The standard library has both copy_sign and copysign (decimal and
# math modules).  The author prefers the former.
def copy_classdict(classdict):

    '''Return copy of classdict, omitting items not in class body.

    The following are always keys in cls.__dict__.  The corresponding
    items are excluded (except for the docstring, if it is not None).

    >>> sorted(list(excluded_classdict_keys))
    ['__dict__', '__doc__', '__module__', '__weakref__']

    >>> copy_classdict(dict(__doc__=None, __module__='something'))
    {}

    >>> copy_classdict(dict(__doc__=str('docstring')))
    {'__doc__': 'docstring'}

    '''

    # Copy, omitting items to be excluded.
    copy_of_classdict = dict(
        (key, value)
        for (key, value) in classdict.items()
        if key not in excluded_classdict_keys
        )

    # If not None, add the docstring.
    docstring = classdict[str('__doc__')]
    if docstring is not None:
        copy_of_classdict[str('__doc__')] = docstring

    return copy_of_classdict


def unclass(cls):
    '''Return class tuple (classname, bases, classdict)

    >>> @unclass
    ... class mytuple(object):
    ...         a = 1
    ...         b = 2

    >>> mytuple == ('mytuple', (object,), {'a': 1, 'b': 2})
    True

    If the class body supplies a docstring it is picked up.
    >>> @unclass
    ... class mytuple(object):
    ...         'docstring'

    >>> mytuple == ('mytuple', (object,), {'__doc__': 'docstring'})
    True

    From the class tuple we can create a class
    >>> myclass = type(*mytuple)
    >>> myclass
    <class 'linhomy.classtools.mytuple'>

    '''

    classname = cls.__name__
    bases = cls.__bases__
    classdict = copy_classdict(cls.__dict__)

    return classname, bases, classdict


if __name__ == '__main__':

    import doctest
    import linhomy.classtools as this_module
    reload(this_module)
    print(doctest.testmod(this_module))
