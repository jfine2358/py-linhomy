# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

from itertools import chain
from .matrices import grow_list

b_empty = b''
b1 = b'\x01'
b2 = b'\x02'

b_empty = ''
b1 = 'C'
b2 = 'D'

def basic_11(word):
    yield b1 + word

def basic_12(word):
    yield b1 + word

def basic_2(word):
    yield  b2 + word


def apply_rule(rule, items):

    value = set()
    for src in items:
        for tgt in rule(src):
            value.add(tgt)

    return tuple(sorted(value))


def sort_by_leading_1(words):
    '''Sort word by number of leading C's.'''
    pairs = sorted(
        ((word + b2).index(b2), word)
        for word in words
    )

    return tuple(pair[1] for pair in (pairs))


def factory(rule_11, rule_12, rule_2):

    @grow_list
    def grow_fn(self):
        value = dict()
        d = len(self)

        if d == 0:
            value[b_empty] = (b_empty,)

        else:
            # If possible, perform rule_2.
            if d - 2 >= 0:
                for keyword, items in self[d-2].items():
                    value[b2 + keyword] = apply_rule(rule_2, items)

            # Prepare for rule_11 and rule_12.
            pre_C = self[d-1]
            pre_C_keys = tuple(sorted(pre_C.keys()))

            # Perform rule_12
            rule_12_keys = tuple(
                key for key in pre_C_keys
                if key.startswith(b2)
            )

            for keyword in rule_12_keys:
                value[b1 + keyword] = tuple(sorted(rule_12(keyword)))

            # Perform rule_11.
            rule_11_keys = tuple(
                key for key in pre_C_keys
                if key[:1] in {b_empty, b1}
            )
            for keyword in rule_11_keys:
                items = pre_C[keyword]
                value[b1 + keyword] = apply_rule(rule_11, items)

        return value

    return grow_fn

x = factory(basic_11, basic_12, basic_2)

for i in range(7):
    print(len(x[i]), x[i])
    print(' '.join(sorted(x[i].keys())))
