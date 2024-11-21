import unittest
from PokerNew import *
class PokerUnittest(unittest.TestCase):
    def setUp(self):
        # Gemeinsame Test-Daten
        self.suits_ascii = ["\u2663", "\u2660", "\u2666", "\u2665"]
        self.numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'B', 'D', 'K', 'A']
        self.suits_len = len(self.suits_ascii)
        self.numbers_len = len(self.numbers)
        self.deck = [i for i in range(self.suits_len * self.numbers_len)]

    def test_get_suit(self):
        self.assertEqual(get_suit(0, self.numbers_len), 0)  # Card 0 belongs to suit 0
        self.assertEqual(get_suit(13, self.numbers_len), 1)  # Card 13 belongs to suit 1
        self.assertEqual(get_suit(51, self.numbers_len), 3)  # Card 51 belongs to suit 3

    def test_get_number(self):
        self.assertEqual(get_number(0, self.numbers_len), 0)  # Card 0 is number 0
        self.assertEqual(get_number(13, self.numbers_len), 0)  # Card 13 is number 0 (next suit)
        self.assertEqual(get_number(51, self.numbers_len), 12)  # Card 51 is number 12 (Ace)

    def test_shuffle_cards(self):
        deck_copy = self.deck[:]
        shuffle_cards(deck_copy)
        self.assertNotEqual(deck_copy, self.deck)  # Ensure deck is shuffled
        self.assertEqual(sorted(deck_copy), self.deck)  # Ensure no cards are lost

    def test_draw_cards(self):
        shuffled_deck = self.deck[:]
        shuffle_cards(shuffled_deck)
        drawn_cards = draw_cards(5, shuffled_deck)
        self.assertEqual(len(drawn_cards), 5)  # Ensure the correct number of cards is drawn

        with self.assertRaises(ValueError):
            draw_cards(53, self.deck)  # Attempt to draw more cards than available

    def test_sort_cards(self):
        cards = [25, 13, 10, 36, 12]  # Beispielkarten (IDs)
        numbers_len = 13
        expected_sorted = [13, 10, 36, 25, 12]  # Erwartete sortierte IDs
        result = sort_cards(cards, numbers_len)
        self.assertEqual(result, expected_sorted, "Cards are not sorted correctly!")

    def test_has_straight(self):
        straight_hand = [0, 1, 2, 3, 4]  # 2, 3, 4, 5, 6 (numbers)
        self.assertTrue(has_straight(straight_hand, self.numbers_len))

        non_straight_hand = [0, 1, 2, 3, 12]  # straight
        self.assertTrue(has_straight(non_straight_hand, self.numbers_len))

        non_straight_hand = [0, 1, 5, 3, 12]  # straight
        self.assertFalse(has_straight(non_straight_hand, self.numbers_len))

    def test_has_flush(self):
        flush_hand = [0, 1, 2, 3, 4]  # All same suit (Clubs)
        self.assertTrue(has_flush(flush_hand, self.numbers_len))

        non_flush_hand = [0, 13, 26, 39, 4]  # Different suits
        self.assertFalse(has_flush(non_flush_hand, self.numbers_len))

    def test_has_pair(self):
        pair_hand = [0, 13, 1, 14, 27]  # Two cards of rank 2
        self.assertEqual(has_pair(pair_hand, 2, self.numbers_len), 1)  # One pair

        three_of_a_kind_hand = [0, 13, 26, 1, 14]  # Three cards of rank 2
        self.assertEqual(has_pair(three_of_a_kind_hand, 3, self.numbers_len), 1)  # One triple

        no_pair_hand = [0, 1, 2, 3, 4]  # No pairs
        self.assertEqual(has_pair(no_pair_hand, 2, self.numbers_len), 0)  # No pairs

if __name__ == '__main__':
    unittest.main()
