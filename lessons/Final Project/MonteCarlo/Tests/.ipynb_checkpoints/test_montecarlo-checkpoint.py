import unittest
import numpy as np
import pandas as pd
from montecarlo.montecarlo import Die, Game, Analyzer

class TestDie(unittest.TestCase):
    """Unit tests for the Die class."""

    def setUp(self):
        """Set up a Die instance with faces 1, 2, 3."""
        self.faces = np.array([1, 2, 3])
        self.die = Die(self.faces)

    def test_init(self):
        """Test that Die is initialized with correct number of faces."""
        self.assertEqual(len(self.die.show()), 3)

    def test_change_weight(self):
        """Test that changing a face's weight works correctly."""
        self.die.change_weight(1, 5)
        self.assertEqual(self.die.show().loc[1, 'weight'], 5.0)

    def test_roll(self):
        """Test that rolling the die returns the correct number of results."""
        result = self.die.roll(5)
        self.assertEqual(len(result), 5)

    def test_show(self):
        """Test that show() returns a pandas DataFrame."""
        self.assertIsInstance(self.die.show(), pd.DataFrame)
        
    def test_roll_faces(self):
        """Test that roll produces only valid faces."""
        result = self.die.roll(10)
        for face in result:
            self.assertIn(face, self.faces)


class TestGame(unittest.TestCase):
    """Unit tests for the Game class."""
    def setUp(self):
        """Set up a Game instance with two identical dice."""
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        self.game = Game([die1, die2])

    def test_play(self):
        """Test that play() rolls the dice correct number of times."""
        self.game.play(5)
        self.assertEqual(self.game._results.shape[0], 5)

    def test_show_wide(self):
        """Test that show('wide') returns results with one column per die."""
        self.game.play(3)
        df = self.game.show('wide')
        self.assertEqual(df.shape[1], 2)  # 2 dice

    def test_show_narrow(self):
        """Test that show('narrow') returns a DataFrame with correct index names."""
        self.game.play(3)
        df = self.game.show('narrow')
        self.assertEqual(df.index.names, ['Roll Number', None])  # FIXED


class TestAnalyzer(unittest.TestCase):
    """Unit tests for the Analyzer class."""

    def setUp(self):
        """Set up an Analyzer with a Game of two dice."""
        die1 = Die(np.array([1, 2, 3]))
        die2 = Die(np.array([1, 2, 3]))
        game = Game([die1, die2])
        game.play(5)
        self.analyzer = Analyzer(game)

    def test_jackpot(self):
        """Test that jackpot() returns an integer count."""
        result = self.analyzer.jackpot()
        self.assertTrue(isinstance(result, (int, np.integer)))

    def test_face_counts_per_roll(self):
        """Test that face_counts_per_roll() returns a DataFrame."""
        result = self.analyzer.face_counts_per_roll() 
        self.assertTrue(isinstance(result, pd.DataFrame))

    def test_combo_count(self):
        """Test that combo_count() returns a DataFrame."""
        result = self.analyzer.combo_count()
        self.assertIsInstance(result, pd.DataFrame)

    def test_permutation_count(self):
        """Test that permutation_count() returns a DataFrame."""
        result = self.analyzer.permutation_count()
        self.assertIsInstance(result, pd.DataFrame)


if __name__ == '__main__':
    unittest.main()