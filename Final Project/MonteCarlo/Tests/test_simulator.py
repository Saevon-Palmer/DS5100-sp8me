import unittest
import numpy as np
from die import Die
from game import Game
from analyzer import Analyzer

class TestMonteCarloSimulator(unittest.TestCase):
    
    def test_die_roll(self):
        die = Die(np.array([1, 2, 3]))
        result = die.roll(5)
        self.assertEqual(len(result), 5)
        
    def test_die_change_weight(self):
        die = Die(np.array([1, 2, 3]))
        die.change_weight(2, 5.0)
        self.assertEqual(die.show().loc[2, "weight"], 5.0)
        
    def test_game_play(self):
        die = Die(np.array([1, 2, 3]))
        game = Game([die, die])
        game.play(5)
        self.assertEqual(game.show().shape, (5, 2))
        
    def test_analyzer_jackpot(self):
        die = Die(np.array([1]))
        game = Game([die, die])
        game.play(3)
        analyzer = Analyzer(game)
        self.assertEqual(analyzer.jackpot(), 3)
        
if __name__ == "__main__":
    unittest.main()