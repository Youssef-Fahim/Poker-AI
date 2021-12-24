import unittest

from evaluator import Evaluator


class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.eval_hand = Evaluator()

    def test_five(self):
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Td"], ["Kd", "Qd", "Jd"]), 1
        )  # quite flush royale
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ah"], ["As", "Ac", "Kd"]), 11
        )  # quad
        self.assertEqual(
            self.eval_hand.evaluate(["Kd", "Kh"], ["Ks", "Ac", "Ad"]), 179
        )  # full house
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Kd"], ["Qd", "Jd", "9d"]), 323
        )  # flush
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ks"], ["Qd", "Jd", "Td"]), 1600
        )  # straight
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "As"], ["Ah", "Kd", "Qd"]), 1610
        )  # three of a kind
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ah"], ["Kd", "Ks", "Qd"]), 2468
        )  # two pairs
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ah"], ["Kd", "Js", "Qd"]), 3326
        )  # one pair
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Kh"], ["Jc", "9s", "Qd"]), 6186
        )  # high card

    def test_six(self):
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Td"], ["Kd", "Qd", "Jd", "6h"]), 1
        )  # quinte flush royale
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ah"], ["As", "Ac", "Kd", "6c"]), 11
        )  # quad
        self.assertEqual(
            self.eval_hand.evaluate(["Kd", "Kh"], ["Ks", "Ac", "Ad", "6c"]), 179
        )  # full house
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Kd"], ["Qd", "Jd", "9d", "6c"]), 323
        )  # flush
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ks"], ["Qd", "Jd", "Td", "6c"]), 1600
        )  # straight
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "As"], ["Ah", "Kd", "Qd", "6c"]), 1610
        )  # three of a kind
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ah"], ["Kd", "Ks", "Qd", "6c"]), 2468
        )  # two pairs
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ah"], ["Kd", "Js", "Qd", "6c"]), 3326
        )  # one pair
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Kh"], ["Jc", "9s", "Qd", "6c"]), 6186
        )  # high card

    def test_seven(self):
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Td"], ["Kd", "Qd", "Jd", "6h", "3s"]), 1
        )  # quinte flush royale
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ah"], ["As", "Ac", "Kd", "6c", "2s"]), 11
        )  # quad
        self.assertEqual(
            self.eval_hand.evaluate(["Kd", "Kh"], ["Ks", "Ac", "Ad", "6c", "2s"]), 179
        )  # full house
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Kd"], ["Qd", "Jd", "9d", "6c", "2s"]), 323
        )  # flush
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ks"], ["Qd", "Jd", "Td", "6c", "2s"]), 1600
        )  # straight
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "2s"], ["Ah", "Kd", "Qd", "6c", "As"]), 1610
        )  # three of a kind
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ah"], ["Kd", "Ks", "Qd", "6c", "2s"]), 2468
        )  # two pairs
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Ah"], ["Kd", "Js", "Qd", "6c", "2s"]), 3326
        )  # one pair
        self.assertEqual(
            self.eval_hand.evaluate(["Ad", "Kh"], ["Jc", "9s", "Qd", "6c", "2s"]), 6186
        )  # high card


if __name__ == "__main__":
    unittest.main()
