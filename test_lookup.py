import unittest
from lookup import LookUpTable

class TestLookUp(unittest.TestCase):

    def setUp(self):
        self.look_up_table = LookUpTable()

    def test_lookup_table_flush(self):
        self.assertEqual(len(self.look_up_table.lookup_table_flush), 1287)
        self.assertEqual(min(self.look_up_table.lookup_table_flush.values()), 1)
        self.assertEqual(max(self.look_up_table.lookup_table_flush.values()), 1599)

    def test_lookup_table_unique(self):
        self.assertEqual(len(self.look_up_table.lookup_table_unique), 6175)
        self.assertEqual(min(self.look_up_table.lookup_table_unique.values()), 11)
        self.assertEqual(max(self.look_up_table.lookup_table_unique.values()), 7462)

        self.assertEqual(len(self.look_up_table.lookup_table_unique) + len(self.look_up_table.lookup_table_flush), 7462)

    def test_lookup_table_four(self):
        self.assertEqual(len(self.look_up_table.lookup_table_four), 156)
        self.assertEqual(min(self.look_up_table.lookup_table_four.values()), 11)
        self.assertEqual(max(self.look_up_table.lookup_table_four.values()), 166)

    def test_lookup_table_full_house(self):
        self.assertEqual(len(self.look_up_table.lookup_table_full_house), 156)
        self.assertEqual(min(self.look_up_table.lookup_table_full_house.values()), 167)
        self.assertEqual(max(self.look_up_table.lookup_table_full_house.values()), 322)

    def test_lookup_table_three(self):
        self.assertEqual(len(self.look_up_table.lookup_table_three), 858)
        self.assertEqual(min(self.look_up_table.lookup_table_three.values()), 1610)
        self.assertEqual(max(self.look_up_table.lookup_table_three.values()), 2467)

    def test_lookup_table_two_pairs(self):
        self.assertEqual(len(self.look_up_table.lookup_table_two_pairs), 858)
        self.assertEqual(min(self.look_up_table.lookup_table_two_pairs.values()), 2468)
        self.assertEqual(max(self.look_up_table.lookup_table_two_pairs.values()), 3325)

    def test_lookup_table_one_pair(self):
        self.assertEqual(len(self.look_up_table.lookup_table_one_pair), 2860)
        self.assertEqual(min(self.look_up_table.lookup_table_one_pair.values()), 3326)
        self.assertEqual(max(self.look_up_table.lookup_table_one_pair.values()), 6185)



if __name__ == '__main__':
    unittest.main()
