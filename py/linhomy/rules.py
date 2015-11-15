'''Rules for the C and D subset operators

Throughout this module, the index is assumed to be a tuple, being
alternately the exponents of D and C in the index.

The C rule has two cases. If the first exponent of D is zero, just add
one to the first exponent of C.
>>> list(C_rule((0, 0)))
[(0, 1)]
>>> list(C_rule((0, 1)))
[(0, 2)]
>>> list(C_rule((0, 1, 3, 4)))
[(0, 2, 3, 4)]

If the first exponent of D is not zero, yield as before and in
addition give a series of (0, 0)-prefixed higher rank indexes.
>>> list(C_rule((1, 0)))
[(1, 1), (0, 0, 0, 0)]
>>> list(C_rule((2, 0)))
[(2, 1), (0, 0, 1, 0), (0, 0, 0, 2)]
>>> list(C_rule((3, 0)))
[(3, 1), (0, 0, 2, 0), (0, 0, 1, 2), (0, 0, 0, 4)]

The first exponent of C is carried through.
>>> list(C_rule((1, 5)))
[(1, 6), (0, 0, 0, 5)]
>>> list(C_rule((2, 5)))
[(2, 6), (0, 0, 1, 5), (0, 0, 0, 7)]
>>> list(C_rule((3, 5)))
[(3, 6), (0, 0, 2, 5), (0, 0, 1, 7), (0, 0, 0, 9)]

The D rule three cases.  If rank is zero, just add one to first
exponent of D.
>>> list(D_rule((0, 0)))
[(1, 0)]
>>> list(D_rule((0, 1)))
[(1, 1)]
>>> list(D_rule((1, 0)))
[(2, 0)]

Do the same if the first exponent of D is not zero.
>>> list(D_rule((1, 0, 0, 0)))
[(2, 0, 0, 0)]

The remaining case.  If rank >= 1 and first exponent of D is zero we
get an extra term, which increments the first two exponents of C.
>>> list(D_rule((0, 0, 0, 0)))
[(1, 0, 0, 0)]

Everything else is just carried througn.
>>> list(D_rule((0, 1, 0, 0)))
[(1, 1, 0, 0)]
>>> list(D_rule((0, 0, 1, 0)))
[(1, 0, 1, 0)]
>>> list(D_rule((0, 0, 0, 1)))
[(1, 0, 0, 1)]

>>> _test_product((0, 0), (0, 0))
'00'
>>> _test_product((0, 1), (0, 2))
'03'
>>> _test_product((1, 0), (2, 0))
'30'
>>> _test_product((1, 3), (2, 4))
'37'
'''

# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


def str_from_items(items):

    # NOTE: The str is to prevent u'00' in Python2 tests.
    return str(' ').join(
        str('').join(map(str, item))
        for item in items
    )

def _test_product(ind1, ind2):
    return str_from_items(product_rule(ind1, ind2))


def C_rule(index):
    '''Yields indexes obtained by applying the C rule to an index.

    Assumes index is a tuple.  Yields tuples.
    '''

    (a, b), body = index[:2], index[2:]

    # Increment the first exponent of C.
    yield (a, b + 1) + body

    bool_index = tuple(map(bool, index))

    # Now look further into the body.
    # Using length at least 4 slightly improves 9-3, 10-3 and 10-4.
    if len(index) >= 4:
        if index[0] and index[1] == index[3] == 0:
            tmp = list(index)
            tmp[3] += 1
            yield tuple(tmp)

    # Looking into at least 6 further improves 9-3, 10-3 and 10-4
    if len(index) >= 6:
        if (
            index[0]
            and index[1] == index[3] == index[5] == 0
        ):
            tmp = list(index)
            tmp[5] += 1
            yield tuple(tmp)

    # This makes 7-1 non-negative, and improves further.
    if 0 and index == (1, 1, 0, 0):
        yield (1, 0, 0, 2)

    # Refactored to give general pattern - much better.
    # Use >= instead of == to give slight improvment.
    if 1 and bool_index[:4] == (1, 1, 0, 0):
            tmp = list(index)
            tmp[1] -= 1
            tmp[3] += 2
            yield tuple(tmp)

    # Looking into at least 6 gives further improvements.
    if 1 and bool_index[:6] == (1, 1, 0, 0, 0, 0):
            tmp = list(index)
            tmp[1] -= 1
            tmp[5] += 2
            yield tuple(tmp)

    # This makes 7-3 non-negative, and improves further.
    if 0 and index == (1, 0, 0, 1):
        yield (1, 0, 0, 2)

    # Refactored to give general pattern - much better.
    # Use >= instead of == to give slight improvment.
    if 1 and bool_index[:4] == (1, 0, 0, 1):
            tmp = list(index)
            tmp[3] += 1
            yield tuple(tmp)

    # Looking into at least 6 gives further improvements.
    if 1 and bool_index[:6] == (1, 0, 0, 0, 0, 1):
            tmp = list(index)
            tmp[5] += 1
            yield tuple(tmp)

    # Now yield (0, 0)-prefixed indexes, if possible.
    if a >= 0:
        a_seq = reversed(range(a)) #  a - 1, a - 2, ..., 0.
        b_seq = range(b, b + 2*a, 2) # b, b + 2, ..., b + 2*(a-1).

        for a_1, b_1 in zip(a_seq, b_seq):
            yield (0, 0, a_1, b_1) + body


def D_rule(index):
    '''Yields indexes obtained by applying the D rule to an index.

    Assumes index is a tuple.  Yields tuples.
    '''

    (a, b), body = index[:2], index[2:]

    # Increment the first exponent of D.
    yield (a + 1, b) + body

    # Suppress this rule to improve zeros, especially d=6.
    if 0 and a == 0 and body:
        (a_1, b_1), rest = body[:2], body[2:]

        # Increment the first two exponents of C.
        yield (a, b + 1, a_1, b_1 + 1) + rest


def product_rule(ind1, ind2):

    # Convert to lists, remove leading D's.
    ind1, ind2 = list(ind1), list(ind2)
    d_count = ind1[0] + ind2[0]
    ind1[0] = ind2[0] = 0

    # Delegate, without leading D's.
    for item in _product_rule_1(ind1, ind2):

        value = list(item)      # Ensure no side-effests.
        value[0] += d_count
        yield list(value)


def _product_rule_1(ind1, ind2):

    (d1, c1), b1 = ind1[:2], ind1[2:]
    (d2, c2), b2 = ind2[:2], ind2[2:]

    yield [d1 + d2, c1 + c2]



if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
