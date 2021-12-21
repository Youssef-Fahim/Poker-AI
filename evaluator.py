from lookup import LookUpTable

class Evaluator:

    LOOK_UP_TABLE_FLUSH = {}
    LOOK_UP_TABLE_UNIQUE = {}

    def __init__(self, *hand):
        if len(hand) != 5:
            raise "hand must be of length 5"
        else:
            self.c1, self.c2, self.c3, self.c4, self.c5 = hand
            self.q_check = self.c1 and self.c2 and self.c3 and self.c4 and self.c5 and bin(0xF000)
            self.q = (self.c1 or self.c2 or self.c3 or self.c4 or self.c5) >> 16
            self.q_int = int(self.q, 2)


    def check_flush(self):
        return self.q_check != 0

    def check_unique(self):
        if Evaluator.LOOK_UP_TABLE_UNIQUE[self.q_int] == 0:
            return False
        else:
            return True

    def hand_rank(self):
        if self.check_flush():
            return Evaluator.LOOK_UP_TABLE_FLUSH[self.q_int]
        elif self.check_unique():
            return Evaluator.LOOK_UP_TABLE_UNIQUE[self.q_int]

