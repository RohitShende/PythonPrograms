
import unittest
from cards import Deck

class MyTest(unittest.TestCase):
    
    def setUp(self):
        self.deck = Deck()
        
    def test_52_cards_in_new_deck(self):
        self.assertEqual(len(self.deck), 52)
