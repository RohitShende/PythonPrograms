import unittest

from cards import Hand, Card

class TestHand(unittest.TestCase):
    
    def test_simple(self):
        hand = Hand([Card(rank='5', suit='spade')])
        self.assertEqual(hand.score(), 5)
        
    def test_soft_17(self):
        hand = Hand([
            Card(rank='A', suit='spade'),
            Card(rank='6', suit='spade'),
        ])
        self.assertEqual(hand.score(), 17)
            
    def test_hard_17(self):
        hand = Hand([
            Card(rank='A', suit='spade'),
            Card(rank='K', suit='spade'),
            Card(rank='6', suit='spade'),
        ])
        self.assertEqual(hand.score(), 17)
        
    def test_really_hard_14(self):
        hand = Hand([
            Card(rank='A', suit='spade'),
            Card(rank='A', suit='club'),
            Card(rank='A', suit='heart'),
            Card(rank='A', suit='diamond'),
            Card(rank='K', suit='spade')
        ])
        self.assertEqual(hand.score(), 14)
        
