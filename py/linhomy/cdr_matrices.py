# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

from collections import defaultdict
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


def shift_1(word):
    if word.startswith(b1 + b1):
        i = (word + b1).find(b2 + b1)
        if i != -1:
            return word[1:i+1] + b1 + word[i+1:]

def apply_rule(rule, items):

    value = set()
    for src in items:
        for tgt in rule(src):
            value.add(tgt)

    return value


def sort_by_leading_1(words):
    '''Sort word by number of leading C's.'''
    pairs = sorted(
        ((word + b2).index(b2), word)
        for word in words
    )

    return tuple(pair[1] for pair in (pairs))


def rules_factory(rule_11, rule_12, rule_2):

    @grow_list
    def grow_fn(self):
        value = defaultdict(set)
        d = len(self)

        if d == 0:
            value[b_empty].add(b_empty)

        else:
            # If possible, perform rule_2.
            if d - 2 >= 0:
                for keyword, items in self[d-2].items():
                    value[b2 + keyword].update(apply_rule(rule_2, items))

            pre_C = self[d-1]
            pre_C_keys = sort_by_leading_1(pre_C.keys())

            for key in pre_C_keys:
                add = value[b1 + key].update

                # TODO: Not quite right. Iterate over pre_C[key]?
                if key.startswith(b2):
                    add(apply_rule(rule_12, pre_C[key]))
                else:
                    add(apply_rule(rule_11, pre_C[key]))

                    tmp = shift_1(b1 + key)
                    if tmp:
                        # Check value[tmp] already calculated.
                        if not tmp in value:
                            raise ValueError
                        add(value[tmp])

        # Normalise the value.
        tmp = dict()
        for k, v in value.items():
            tmp[k] = tuple(sorted(v))

        return tmp

    return grow_fn


def cdr_print(rules, d):
    format = '{d} {src} -> {val}.'.format
    for k, v in sorted(rules[d].items()):
        val = ' '.join(v)
        s = format(d=d, src=k, val=val)
        print(s)


basic_rules = rules_factory(basic_11, basic_12, basic_2)

for i in range(9):
    cdr_print(basic_rules, i)
