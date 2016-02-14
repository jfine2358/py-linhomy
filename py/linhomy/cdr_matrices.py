'''

>>> for i in range(5):
...    cdr_print(basic_rules, i)
0  -> .
1 C -> C.
2 CC -> CC.
2 D -> D.
3 CCC -> CCC.
3 CD -> CD.
3 DC -> DC.
4 CCCC -> CCCC.
4 CCD -> CCD CDC.
4 CDC -> CDC.
4 DCC -> DCC.
4 DD -> DD.

>>> cdr_print(basic_rules, 5)
5 CCCCC -> CCCCC.
5 CCCD -> CCCD CCDC CDCC.
5 CCDC -> CCDC CDCC.
5 CDCC -> CDCC.
5 CDD -> CDD.
5 DCCC -> DCCC.
5 DCD -> DCD.
5 DDC -> DDC.

>>> cdr_print(basic_rules, 6)
6 CCCCCC -> CCCCCC.
6 CCCCD -> CCCCD CCCDC CCDCC CDCCC.
6 CCCDC -> CCCDC CCDCC CDCCC.
6 CCDCC -> CCDCC CDCCC.
6 CCDD -> CCDD CDDC.
6 CDCCC -> CDCCC.
6 CDCD -> CDCD.
6 CDDC -> CDDC.
6 DCCCC -> DCCCC.
6 DCCD -> DCCD DCDC.
6 DCDC -> DCDC.
6 DDCC -> DDCC.
6 DDD -> DDD.

>>> cdr_print(basic_rules, 7)
7 CCCCCCC -> CCCCCCC.
7 CCCCCD -> CCCCCD CCCCDC CCCDCC CCDCCC CDCCCC.
7 CCCCDC -> CCCCDC CCCDCC CCDCCC CDCCCC.
7 CCCDCC -> CCCDCC CCDCCC CDCCCC.
7 CCCDD -> CCCDD CCDDC CDDCC.
7 CCDCCC -> CCDCCC CDCCCC.
7 CCDCD -> CCDCD CDCCD CDCDC.
7 CCDDC -> CCDDC CDDCC.
7 CDCCCC -> CDCCCC.
7 CDCCD -> CDCCD CDCDC.
7 CDCDC -> CDCDC.
7 CDDCC -> CDDCC.
7 CDDD -> CDDD.
7 DCCCCC -> DCCCCC.
7 DCCCD -> DCCCD DCCDC DCDCC.
7 DCCDC -> DCCDC DCDCC.
7 DCDCC -> DCDCC.
7 DCDD -> DCDD.
7 DDCCC -> DDCCC.
7 DDCD -> DDCD.
7 DDDC -> DDDC.

>>> cdr_print(basic_rules, 8)
8 CCCCCCCC -> CCCCCCCC.
8 CCCCCCD -> CCCCCCD CCCCCDC CCCCDCC CCCDCCC CCDCCCC CDCCCCC.
8 CCCCCDC -> CCCCCDC CCCCDCC CCCDCCC CCDCCCC CDCCCCC.
8 CCCCDCC -> CCCCDCC CCCDCCC CCDCCCC CDCCCCC.
8 CCCCDD -> CCCCDD CCCDDC CCDDCC CDDCCC.
8 CCCDCCC -> CCCDCCC CCDCCCC CDCCCCC.
8 CCCDCD -> CCCDCD CCDCCD CCDCDC CDCCCD CDCCDC CDCDCC.
8 CCCDDC -> CCCDDC CCDDCC CDDCCC.
8 CCDCCCC -> CCDCCCC CDCCCCC.
8 CCDCCD -> CCDCCD CCDCDC CDCCCD CDCCDC CDCDCC.
8 CCDCDC -> CCDCDC CDCCDC CDCDCC.
8 CCDDCC -> CCDDCC CDDCCC.
8 CCDDD -> CCDDD CDDDC.
8 CDCCCCC -> CDCCCCC.
8 CDCCCD -> CDCCCD CDCCDC CDCDCC.
8 CDCCDC -> CDCCDC CDCDCC.
8 CDCDCC -> CDCDCC.
8 CDCDD -> CDCDD.
8 CDDCCC -> CDDCCC.
8 CDDCD -> CDDCD.
8 CDDDC -> CDDDC.
8 DCCCCCC -> DCCCCCC.
8 DCCCCD -> DCCCCD DCCCDC DCCDCC DCDCCC.
8 DCCCDC -> DCCCDC DCCDCC DCDCCC.
8 DCCDCC -> DCCDCC DCDCCC.
8 DCCDD -> DCCDD DCDDC.
8 DCDCCC -> DCDCCC.
8 DCDCD -> DCDCD.
8 DCDDC -> DCDDC.
8 DDCCCC -> DDCCCC.
8 DDCCD -> DDCCD DDCDC.
8 DDCDC -> DDCDC.
8 DDDCC -> DDDCC.
8 DDDD -> DDDD.

As expected, all zeros and ones.
>>> basic_matrices.print_C_stats(10)
0 [(1, 1)]
1 [(0, 1), (1, 1)]
2 [(0, 3), (1, 3)]
3 [(0, 11), (1, 4)]
4 [(0, 33), (1, 7)]
5 [(0, 92), (1, 12)]
6 [(0, 254), (1, 19)]
7 [(0, 682), (1, 32)]
8 [(0, 1818), (1, 52)]
9 [(0, 4810), (1, 85)]
10 [(0, 12677), (1, 139)]

As expected, all zeros and ones.
>>> basic_matrices.print_D_stats(10)
0 [(0, 1), (1, 1)]
1 [(0, 2), (1, 1)]
2 [(0, 8), (1, 2)]
3 [(0, 21), (1, 3)]
4 [(0, 60), (1, 5)]
5 [(0, 160), (1, 8)]
6 [(0, 429), (1, 13)]
7 [(0, 1134), (1, 21)]
8 [(0, 2992), (1, 34)]
9 [(0, 7865), (1, 55)]
10 [(0, 20648), (1, 89)]

Some negatives, that must be removed. Good outcome for little input.
>>> basic_matrices.print_product_stats(10)
2 1 [(1, 2)]
3 1 [(0, 3), (1, 3)]
4 1 [(0, 9), (1, 6)]
4 2 [(0, 14), (1, 6)]
5 1 [(0, 31), (1, 9)]
5 2 [(0, 37), (1, 11)]
6 1 [(0, 88), (1, 16)]
6 2 [(0, 112), (1, 18)]
6 3 [(0, 93), (1, 23), (2, 1)]
7 1 [(0, 247), (1, 26)]
7 2 [(0, 305), (1, 31)]
7 3 [(0, 275), (1, 38), (2, 2)]
8 1 [(0, 671), (1, 43)]
8 2 [(0, 831), (1, 53)]
8 3 [(0, 741), (1, 71), (2, 4)]
8 4 [(-2, 1), (-1, 1), (0, 778), (1, 64), (2, 6)]
9 1 [(0, 1799), (1, 71)]
9 2 [(0, 2223), (1, 87)]
9 3 [(0, 2011), (1, 127), (2, 6), (3, 1)]
9 4 [(-2, 2), (-1, 3), (0, 2061), (1, 122), (2, 12)]
10 1 [(0, 4779), (1, 116)]
10 2 [(0, 5905), (1, 147)]
10 3 [(0, 5374), (1, 220), (2, 11), (3, 2)]
10 4 [(-2, 4), (-1, 10), (0, 5519), (1, 228), (2, 22), (3, 2)]
10 5 [(-2, 6), (-1, 7), (0, 5419), (1, 236), (2, 28)]
'''


# For Python2 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
__metaclass__ = type

from collections import defaultdict
from itertools import chain
from .fibonacci import FIB_WORDS
from .matrices import fib_zeros_array
from .matrices import grow_list
from .rankmatrices import word_from_CD
from .rankmatrices import CD_from_word
from .rankmatrices import RankMatrices

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


def rule_matrices_from_rules(rules):

    @grow_list
    def grow(self):
        d = len(self)

        src = rules[d]
        tgt = fib_zeros_array(d, d)
        for k, v in src.items():
            word_k = word_from_CD(k)
            j = FIB_WORDS[d].index(word_k)
            for i_w in v:
                word_i = word_from_CD(i_w)
                i = FIB_WORDS[d].index(word_i)
                tgt[i, j] += 1

        return tgt

    return grow


def cdr_print(rules, d):
    format = '{d} {src} -> {val}.'.format
    for k, v in sorted(rules[d].items()):
        val = ' '.join(v)
        s = format(d=d, src=k, val=val)
        print(s)


basic_rules = rules_factory(basic_11, basic_12, basic_2)
basic_rule_matrices = rule_matrices_from_rules(basic_rules)
basic_matrices = RankMatrices(matrices=basic_rule_matrices)

if __name__ == '__main__':

    import doctest
    print(doctest.testmod())
