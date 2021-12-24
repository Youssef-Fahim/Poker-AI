import itertools

from card import Card
from lookup import LookUpTable


class Evaluator:

    LOOK_UP_TABLE_FLUSH = LookUpTable().lookup_table_flush
    LOOK_UP_TABLE_UNIQUE = LookUpTable().lookup_table_unique

    def __init__(self):
        self.hand_size_map = {
            5: self._five,
            6: self._six,
            7: self._seven,
        }

    def evaluate(self, pockets, board):
        all_cards = pockets + board
        return self.hand_size_map[len(all_cards)](all_cards)

    def _five(self, cards):
        """
        cards in form list of str ['Ad', 'Kd', 'Qd', 'Jd', 'Td'] with size 5
        """
        for i in range(len(cards)):
            cards[i] = Card.binary_representation_from_str_card(cards[i])

        if cards[0] & cards[1] & cards[2] & cards[3] & cards[4] & 0xF000:
            rankbits = (cards[0] | cards[1] | cards[2] | cards[3] | cards[4]) >> 16
            prime = Card.get_prime_product_from_rankbits(rankbits)
            return Evaluator.LOOK_UP_TABLE_FLUSH[prime]

        else:
            prime = Card.get_prime_product_from_hand_binary(cards)
            return Evaluator.LOOK_UP_TABLE_UNIQUE[prime]

    def _six(self, cards):
        min_value = LookUpTable.MAX_RANK_HIGH
        hand_combinations = itertools.combinations(
            cards, 5
        )  # len(hand_combinations) = 6

        for hand in hand_combinations:  # hand is a tuple
            value = self._five(list(hand))
            # print(hand)
            # print(value)
            if value < min_value:
                min_value = value

        return min_value

    def _seven(self, cards):
        min_value = LookUpTable.MAX_RANK_HIGH
        hand_combinations = itertools.combinations(
            cards, 5
        )  # len(hand_combinations) = 21

        for hand in hand_combinations:  # hand is a tuple
            value = self._five(list(hand))
            # print(hand)
            # print(value)
            if value < min_value:
                min_value = value

        return min_value
