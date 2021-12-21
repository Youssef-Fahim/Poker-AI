class Card:
    PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    INT_RANKS = list(range(13)) # [0, 1, 2, ..., 12]
    BACK_INT_RANKS = list(range(len(INT_RANKS) - 1, -1, -1)) # [12, 11, 10, ..., 0]

    @staticmethod
    def get_prime_product_from_hand(card_ints):
        pass

    @staticmethod
    def get_prime_product_from_rankbits(rankbits):
        prod = 1
        for i in Card.INT_RANKS:
            if rankbits & (1 << i):
                prod *= Card.PRIME_NUMBERS[i]
        return prod