import unittest
from card import Card

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card = Card()
        self.string1 = 'Ah'
        self.string2 = 'Kd'
        self.string3 = 'Qs'
        self.string4 = 'Jc'
        self.string5 = 'Td'
        self.string6 = '9h'
        self.string7 = '8c'
        self.string8 = '7d'
        self.string9 = '6h'
        self.string10 = '5s'
        self.string11 = '4s'
        self.string12 = '3c'
        self.string13 = '2h'


    def test_binary_representation_from_str_card(self):
        self.assertEqual(self.card.binary_representation_from_str_card(self.string1),  0b00010000000000000010110000101001)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string2),  0b00001000000000000100101100100101)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string3),  0b00000100000000000001101000011111)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string4),  0b00000010000000001000100100011101)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string5),  0b00000001000000000100100000010111)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string6),  0b00000000100000000010011100010011)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string7),  0b00000000010000001000011000010001)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string8),  0b00000000001000000100010100001101)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string9),  0b00000000000100000010010000001011)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string10), 0b00000000000010000001001100000111)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string11), 0b00000000000001000001001000000101)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string12), 0b00000000000000101000000100000011)
        self.assertEqual(self.card.binary_representation_from_str_card(self.string13), 0b00000000000000010010000000000010)

    def test_get_prime_product_from_(self):
        self.assertEqual(self.card.get_prime_product_from_rankbits(0b0001111100000000), 41*37*31*29*23)
        self.assertEqual(self.card.get_prime_product_from_rankbits(0b0001111000000001), 41*37*31*29*2)
        self.assertEqual(self.card.get_prime_product_from_hand_string(['Ad', 'Kh', 'Ah', '7c', '2s']), 41*37*41*13*2)
        


if __name__ == '__main__':
    unittest.main()