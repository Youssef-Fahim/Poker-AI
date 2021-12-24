import itertools
from card import Card


class LookUpTable:
    """
    Number of Distinct Hand Values:

    Straight Flush   10
    Four of a Kind   156      [(13 choose 2) * (2 choose 1)]
    Full Houses      156      [(13 choose 2) * (2 choose 1)]
    Flush            1277     [(13 choose 5) - 10 straight flushes]
    Straight         10
    Three of a Kind  858      [(13 choose 3) * (3 choose 1)]
    Two Pair         858      [(13 choose 3) * (3 choose 2)]
    One Pair         2860     [(13 choose 4) * (4 choose 1)]
    High Card      + 1277     [(13 choose 5) - 10 straights]
    -------------------------
    TOTAL            7462

    AKQJT straight flush --> rank = 1    (best hand possible royal straight flush)
    75432 unsuited       --> rank = 7462 (worst hand possible)
    """

    MAX_RANK_STRAIGHT_FLUSH = 10
    MAX_RANK_FOUR = 166
    MAX_RANK_FULL_HOUSE = 322
    MAX_RANK_FLUSH = 1599
    MAX_RANK_STRAIGHT = 1609
    MAX_RANK_THREE = 2467
    MAX_RANK_TWO_PAIRS = 3325
    MAX_RANK_ONE_PAIR = 6185
    MAX_RANK_HIGH = 7462

    def __init__(self):
        self.lookup_table_flush = {}
        self.lookup_table_unique = {}

        self.lookup_table_four = {}
        self.lookup_table_full_house = {}
        self.lookup_table_three = {}
        self.lookup_table_two_pairs = {}
        self.lookup_table_one_pair = {}

        self.straight = []
        self.not_straight = []

        self.feed_flush()
        self.feed_unique()
        self.feed_remainder()

    def feed_flush(self):
        """
        Create the FLUSH lookup table containing the 10 straight flush hands and the other 1277
        flush which sums up to a final table containing 1287 flushes. The key of the table is
        equal to the rank binary representation of the hand. That means that for a special card,
        the rank binary representation uses 16 bits with only 1 out of 13 that can be activated.
        For a special flush hand, the rank binary representation is encoded in 16 bits with
        exactly 5 bits out of 13 activated and for a straight flush the 5 bits are contiguous
        except for the suited (5432A)
        """
        straight_flushes = {
            int("0b0001111100000000", 2): 1,  # (AKQJT)
            int("0b0000111110000000", 2): 2,  # (KQJT9)
            int("0b0000011111000000", 2): 3,  # (QJT98)
            int("0b0000001111100000", 2): 4,  # (JT987)
            int("0b0000000111110000", 2): 5,  # (T9876)
            int("0b0000000011111000", 2): 6,  # (98765)
            int("0b0000000001111100", 2): 7,  # (87654)
            int("0b0000000000111110", 2): 8,  # (76543)
            int("0b0000000000011111", 2): 9,  # (65432)
            int("0b0001000000001111", 2): 10,  # (5432A)
        }

        self.straight = list(straight_flushes.keys())

        flushes = []
        init_gen = self.get_lexographically_next_bit_sequence(
            int("0b0000000000011111", 2)
        )

        for _ in range(
            LookUpTable.MAX_RANK_FULL_HOUSE + 1, LookUpTable.MAX_RANK_FLUSH + 10
        ):
            hand = next(init_gen)
            if hand not in straight_flushes:
                flushes.append(hand)

        flushes.reverse()
        self.not_straight = flushes

        init_rank = LookUpTable.MAX_RANK_FULL_HOUSE + 1

        for ns_flush in self.not_straight:
            prime_product = Card.get_prime_product_from_rankbits(ns_flush)
            self.lookup_table_flush[prime_product] = init_rank
            init_rank += 1

        for s_flush in self.straight:
            prime_product = Card.get_prime_product_from_rankbits(s_flush)
            self.lookup_table_flush[prime_product] = straight_flushes[s_flush]

        # self.lookup_table_flush = {**straight_flushes, **self.lookup_table_flush}

    def feed_unique(self):
        """
        Create the UNIQUE lookup table containing the 10 distinct straight hands which are
        not suited and containing the 1277 high card hands.
        """
        for straight_, rank in zip(
            self.straight,
            list(
                range(LookUpTable.MAX_RANK_FLUSH + 1, LookUpTable.MAX_RANK_STRAIGHT + 1)
            ),
        ):
            prime_product = Card.get_prime_product_from_rankbits(straight_)
            self.lookup_table_unique[prime_product] = rank

        for nstraight_, rank in zip(
            self.not_straight,
            list(
                range(LookUpTable.MAX_RANK_ONE_PAIR + 1, LookUpTable.MAX_RANK_HIGH + 1)
            ),
        ):
            prime_product = Card.get_prime_product_from_rankbits(nstraight_)
            self.lookup_table_unique[prime_product] = rank

    def feed_remainder(self):

        # 1) Four of a kind

        init_rank = LookUpTable.MAX_RANK_STRAIGHT_FLUSH + 1

        for main_four in Card.BACK_INT_RANKS:
            kickers = Card.BACK_INT_RANKS[:]
            kickers.remove(main_four)
            for kicker in kickers:
                prime_product = (
                    Card.PRIME_NUMBERS[main_four] ** 4
                ) * Card.PRIME_NUMBERS[kicker]
                self.lookup_table_four[prime_product] = init_rank
                init_rank += 1

        # 2) Full House

        init_rank = LookUpTable.MAX_RANK_FOUR + 1

        for main_three in Card.BACK_INT_RANKS:
            kickers = Card.BACK_INT_RANKS[:]
            kickers.remove(main_three)
            for kicker in kickers:
                prime_product = (Card.PRIME_NUMBERS[main_three] ** 3) * (
                    Card.PRIME_NUMBERS[kicker] ** 2
                )
                self.lookup_table_full_house[prime_product] = init_rank
                init_rank += 1

        # 3) Three of a kind

        init_rank = LookUpTable.MAX_RANK_STRAIGHT + 1

        for main_three in Card.BACK_INT_RANKS:
            kickers = Card.BACK_INT_RANKS[:]
            kickers.remove(main_three)
            kickers_combinations = itertools.combinations(kickers, 2)
            # kickers_combinations already classified in decreasing lexicographical order from itertools. No need to rearange
            # the kickers combinations
            for kicker1, kicker2 in kickers_combinations:
                prime_product = (
                    (Card.PRIME_NUMBERS[main_three] ** 3)
                    * Card.PRIME_NUMBERS[kicker1]
                    * Card.PRIME_NUMBERS[kicker2]
                )
                self.lookup_table_three[prime_product] = init_rank
                init_rank += 1

        # 4) Two pairs

        init_rank = LookUpTable.MAX_RANK_THREE + 1

        main_twos = Card.BACK_INT_RANKS[:]
        main_twos_combinations = itertools.combinations(main_twos, 2)
        for main_two_1, main_two_2 in main_twos_combinations:
            kickers = Card.BACK_INT_RANKS[:]
            kickers.remove(main_two_1)
            kickers.remove(main_two_2)
            for kicker in kickers:
                prime_product = (
                    (Card.PRIME_NUMBERS[main_two_1] ** 2)
                    * (Card.PRIME_NUMBERS[main_two_2] ** 2)
                    * Card.PRIME_NUMBERS[kicker]
                )
                self.lookup_table_two_pairs[prime_product] = init_rank
                init_rank += 1
                # print(main_two_1, main_two_1, main_two_2, main_two_2, kicker, 'rank = ', init_rank)

        # 5) One pair

        init_rank = LookUpTable.MAX_RANK_TWO_PAIRS + 1

        for main_two in Card.BACK_INT_RANKS:
            kickers = Card.BACK_INT_RANKS[:]
            kickers.remove(main_two)
            kickers_combinations = itertools.combinations(kickers, 3)
            # kickers_combinations already classified in decreasing lexicographical order from itertools. No need to rearange
            # the kickers combinations
            for kicker1, kicker2, kicker3 in kickers_combinations:
                prime_product = (
                    (Card.PRIME_NUMBERS[main_two] ** 2)
                    * Card.PRIME_NUMBERS[kicker1]
                    * Card.PRIME_NUMBERS[kicker2]
                    * Card.PRIME_NUMBERS[kicker3]
                )
                self.lookup_table_one_pair[prime_product] = init_rank
                init_rank += 1
                # print(main_two, main_two, kicker1, kicker2, kicker3, 'rank = ', init_rank)

        self.lookup_table_unique = {
            **self.lookup_table_unique,
            **self.lookup_table_four,
            **self.lookup_table_full_house,
            **self.lookup_table_three,
            **self.lookup_table_two_pairs,
            **self.lookup_table_one_pair,
        }

    def get_lexographically_next_bit_sequence(self, bits):
        """
        Bit hack from here:
        http://www-graphics.stanford.edu/~seander/bithacks.html#NextBitPermutation

        Generator even does this in poker order rank
        so no need to sort when done! Perfect.
        """
        t = (bits | (bits - 1)) + 1
        next = t | ((((t & -t) // (bits & -bits)) >> 1) - 1)
        yield next
        while True:
            t = (next | (next - 1)) + 1
            next = t | ((((t & -t) // (next & -next)) >> 1) - 1)
            yield next
