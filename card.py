class Card:
    PRIME_NUMBERS = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    INT_RANKS = list(range(13)) # [0, 1, 2, ..., 12]
    STR_RANKS = list('23456789TJQKA')
    BACK_INT_RANKS = list(range(len(INT_RANKS) - 1, -1, -1)) # [12, 11, 10, ..., 0]

    STR_RANK_TO_INT_RANK =  {
                                '2' : 0,
                                '3' : 1,
                                '4' : 2,
                                '5' : 3,
                                '6' : 4,
                                '7' : 5,
                                '8' : 6,
                                '9' : 7,
                                'T' : 8,
                                'J' : 9,
                                'Q' : 10,
                                'K' : 11,
                                'A' : 12
                            } # = dict(list(zip(STR_RANKS, INT_RANKS)))

    STR_SUIT_TO_INT_SUIT = {
                                's' : 1,
                                'h' : 2,
                                'd' : 4,
                                'c' : 8
                            }

    @staticmethod
    def binary_representation_from_str_card(string):
        """
        The string card representation is composed of a string of 2 chars with char_rank representing the STR_RANK and char_suit
        representing the STR_SUIT. For instance, the King of Diamonds is represented by 'Kd'
        """
        char_rank = string[0]
        char_suit = string[1]

        int_rank = Card.STR_RANK_TO_INT_RANK[char_rank]
        int_suit = Card.STR_SUIT_TO_INT_SUIT[char_suit]

        bitrank = 1 << int_rank << 16
        suit = int_suit << 12
        rank = int_rank << 8
        prime = Card.PRIME_NUMBERS[int_rank]

        final_binary_repr = bitrank | suit | rank | prime 

        return final_binary_repr


    @staticmethod
    def get_prime_product_from_hand_binary(card_binary):
        prod = 1
        for c in card_binary:
            prod *= (c & 0xFF) 
        return prod

    @staticmethod
    def get_prime_product_from_hand_string(card_strs):
        # card_strs in the form ['Ad','Kd', 'Qd', 'Jd', 'Td']
        prod = 1
        for c in card_strs:
            c = Card.binary_representation_from_str_card(c)
            prod *= (c & 0xFF) 
        return prod


    @staticmethod
    def get_prime_product_from_rankbits(rankbits):
        """
        Assumes that the input is in form (set bits):

                    rankbits     
                +--------+--------+
                |xxxbbbbb|bbbbbbbb|
                +--------+--------+

        For instance, if we have a King straight, the rankbits of the hand is represented by:

                    rankbits     
                +--------+--------+
                |xxx01111|10000000|
                +--------+--------+

        If we have a hand composed of the worst unsuited cards (7, 5, 4, 3, 2):

                    rankbits     
                +--------+--------+
                |xxx00000|00101111|
                +--------+--------+

        We use this method when calculating the prime product of flushes (straight flushes and not straight flushes) and 
        of straight and high card hands. In these special cases, we have 5 distinct ranks for each hand and therefore, the
        rankbits resulting in OR operation of each bitrank contains exactly 5 ones. For other types of hands, we have to
        use the other get_prime method because we would have at most 4 ones in the rankbits OR result
        """
        prod = 1
        for i in Card.INT_RANKS:
            if rankbits & (1 << i):
                prod *= Card.PRIME_NUMBERS[i]
        return prod