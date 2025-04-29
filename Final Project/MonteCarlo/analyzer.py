import pandas as pd
from collections import Counter

class Analyzer:
    """
    A class to analyze the results of a Game.

    Attributes
    ----------
    game : Game
        Game object containing the play results.
    """

    def __init__(self, game):
        """
        Initialize the Analyzer object.

        Parameters
        ----------
        game : Game
            A Game object.

        Raises
        ------
        ValueError: If input is not a Game object.
        """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object.")
        self.game = game
        self._results = game.show('wide')

    def jackpot(self):
        """
        Count how many rolls resulted in all dice showing the same face.

        Returns
        -------
        int
        """
        return sum(self._results.nunique(axis=1) == 1)

    def face_counts_per_roll(self):
        """
        Count how many times each face appeared per roll.

        Returns
        -------
        pd.DataFrame
        """
        return self._results.apply(lambda row: pd.Series(Counter(row)), axis=1).fillna(0).astype(int)

    def combo_counts(self):
        """
        Count occurrences of each unique combination of rolled faces.

        Returns
        -------
        pd.DataFrame
        """
        combos = self._results.apply(lambda row: tuple(sorted(row)), axis=1)
        return combos.value_counts().to_frame("Count")

    def permutation_counts(self):
        """
        Count occurrences of each unique permutation of rolled faces.

        Returns
        -------
        pd.DataFrame
        """
        perms = self._results.apply(lambda row: tuple(row), axis = 1)
        return perms.value_counts().to_frame("Count")