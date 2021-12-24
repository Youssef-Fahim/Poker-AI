import itertools
import sys

import scipy

from card import Card
from evaluator import Evaluator
from lookup import LookUpTable

# def get_lexographically_next_bit_sequence(bits):
#     """
#     Bit hack from here:
#     http://www-graphics.stanford.edu/~seander/bithacks.html#NextBitPermutation

#     Generator even does this in poker order rank
#     so no need to sort when done! Perfect.
#     """
#     t = (bits | (bits - 1)) + 1
#     next = t | ((((t & -t) // (bits & -bits)) >> 1) - 1)
#     yield next
#     while True:
#         t = (next | (next - 1)) + 1
#         next = t | ((((t & -t) // (next & -next)) >> 1) - 1)
#         yield next

# straight_flushes = {
#     int('0b0001111100000000', 2) : 1, # (AKQJT)
#     int('0b0000111110000000', 2) : 2, # (KQJT9)
#     int('0b0000011111000000', 2) : 3, # (QJT98)
#     int('0b0000001111100000', 2) : 4, # (JT987)
#     int('0b0000000111110000', 2) : 5, # (T9876)
#     int('0b0000000011111000', 2) : 6, # (98765)
#     int('0b0000000001111100', 2) : 7, # (87654)
#     int('0b0000000000111110', 2) : 8, # (76543)
#     int('0b0000000000011111', 2) : 9, # (65432)
#     int('0b0001000000001111', 2) : 10 # (5432A)

# }

# init_hand = int('0b0000000000011111', 2)
# print(init_hand in straight_flushes)
# gen = get_lexographically_next_bit_sequence(init_hand)

# print(bin(init_hand))

# for i in range(10):
#     f = next(gen)
#     print(bin(f))

# flushes = []
# init_gen = get_lexographically_next_bit_sequence(int('0b0000000000011111', 2))

# for _ in range(LookUpTable.MAX_RANK_FULL_HOUSE + 1, LookUpTable.MAX_RANK_FLUSH + 10):
#     hand = next(init_gen)
#     if hand not in straight_flushes:
#         flushes.append(bin(hand))

# flushes.reverse()
# print(len(flushes))
# print(flushes)

# dic1 = {0:'a', 1:'b'}
# dic2 = {2:'c', 3:'d'}
# print({**dic1, **dic2})

# table_ = LookUpTable()

# print(table_.lookup_table_flush)
# print("***"*10)
# print(table_.lookup_table_unique)


# backward_ranks = list(range(len(Card.INT_RANKS) - 1, -1, -1))
# backward_ranks_ = backward_ranks[:]

# print(backward_ranks)
# print(Card.BACK_INT_RANKS)
# print(backward_ranks is Card.BACK_INT_RANKS)
# print(backward_ranks_ is backward_ranks)
# comb = itertools.combinations([0,1,2,3,4,5], 2)
# for duo in comb:
#     print(duo)

# table_ = LookUpTable()
# tables = [table_.lookup_table_four,
#          table_.lookup_table_full_house,
#           table_.lookup_table_three,
#            table_.lookup_table_two_pairs,
#             table_.lookup_table_one_pair
#             ]
# for table in tables:
#     print(len(table))
# print("*****"*10)
# print(len(table_.lookup_table_unique))
# print("*****"*10)
# print(len(table_.lookup_table_flush))
# print("*****"*10)
# print(len(table_.lookup_table_unique) + len(table_.lookup_table_flush))
# print(table_.lookup_table_unique)

# INT_RANKS = list(range(13)) # [0, 1, 2, ..., 12]
# STR_RANKS = list('23456789TJQKA')

# ZIP_RANKS = zip(STR_RANKS, INT_RANKS)

# print(dict(list(ZIP_RANKS)))

# print(bin(Card().binary_representation_from_str_card('Kd')))
# print(bin(Card().binary_representation_from_str_card('Ah')))

# eval = Evaluator()
# print(eval.evaluate(['Ad', 'Kh'], ['Qd', 'Jd']))

# table_ = LookUpTable()
# print(table_.lookup_table_flush.keys())
# print(min(table_.lookup_table_flush.values()))


print(sys.path)

# import numpy as np
# import pandas as pd
