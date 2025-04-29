import numpy as np
import pandas as pd

class Die:
    """
    A die has N faces and associated weights. Faces can be rolled randomly.
    Faces may be numeric or strings.
    """

    def __init__(self, faces: np.ndarray):
        """
        Initializes the Die object.

        Arguments:
            faces (np.ndarray): Array of faces (strings or numbers).

        Raises:
            TypeError: If faces is not a numpy array.
            ValueError: If faces are not unique.
        """
        if isinstance(faces, list):
            faces = np.array(faces)
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a NumPy array.")
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Faces must be unique.")

        self._df = pd.DataFrame({'face': faces, 'weight': np.ones(len(faces))})
        self._df.set_index('face', inplace=True)

    def change_weight(self, face, new_weight):
        """
        Changes the weight of a given face.

        Arguments:
            face: The face to change.
            new_weight: The new weight (must be numeric).

        Raises:
            IndexError: If face is not found.
            TypeError: If new_weight is not numeric.
        """
        if face not in self._df.index:
            raise IndexError("Face not found.")
        try:
            new_weight = float(new_weight)
        except ValueError:
            raise TypeError("New weight must be numeric.")

        self._df.at[face, 'weight'] = new_weight

    def roll(self, n_rolls=1):
        """
        Rolls the die n times.

        Arguments:
            n_rolls (int): Number of rolls.

        Returns:
            list: Outcomes of rolls.
        """
        return list(
            self._df.sample(n=n_rolls, weights=self._df['weight'], replace=True).index
        )

    def show(self):
        """
        Shows the die's faces and current weights.

        Returns:
            pd.DataFrame: Faces and weights.
        """
        return self._df.copy()


class Game:
    """
    A game consists of rolling one or more similar dice one or more times.
    """

    def __init__(self, dice: list):
        """
        Initializes the Game object.

        Arguments:
            dice (list): List of Die objects.
        """
        self._dice = dice
        self._results = None

    def play(self, n_rolls):
        """
        Plays the game: roll all dice n times.

        Arguments:
            n_rolls (int): Number of times to roll all dice.
        """
        rolls = {}
        for i, die in enumerate(self._dice):
            rolls[i] = die.roll(n_rolls)

        self._results = pd.DataFrame(rolls)
        self._results.index.name = 'Roll Number'

    def show(self, form='wide'):
        """
        Shows the results of the most recent play.

        Arguments:
            form (str): 'wide' or 'narrow' format.

        Returns:
            pd.DataFrame: Results in requested format.

        Raises:
            ValueError: If form is not 'wide' or 'narrow'.
        """
        if form == 'wide':
            return self._results.copy()
        elif form == 'narrow':
            return self._results.stack().to_frame('Outcome')
        else:
            raise ValueError("Form must be 'wide' or 'narrow'.")


class Analyzer:
    """
    Analyzes the results of a Game.
    """

    def __init__(self, game: Game):
        """
        Initializes the Analyzer.

        Arguments:
            game (Game): A Game object.

        Raises:
            ValueError: If input is not a Game object.
        """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object.")
        self._game = game

    def jackpot(self):
        """
        Counts the number of jackpots (all faces the same).

        Returns:
            int: Number of jackpots.
        """
        return (self._game._results.nunique(axis=1) == 1).sum()

    def face_counts_per_roll(self):
        """
        Counts the number of each face per roll.

        Returns:
            pd.DataFrame: Counts of each face per roll.
        """
        return self._game._results.apply(pd.Series.value_counts, axis=1).fillna(0)

    def combo_count(self):
        """
        Counts distinct combinations of faces rolled.

        Returns:
            pd.DataFrame: Combination counts (order-independent).
        """
        combos = self._game._results.apply(lambda x: tuple(sorted(x)), axis=1)
        combo_counts = combos.value_counts().to_frame('Count')
        combo_counts.index.name = 'Combination'
        return combo_counts

    def permutation_count(self):
        """
        Counts distinct permutations of faces rolled.

        Returns:
            pd.DataFrame: Permutation counts (order-dependent).
        """
        perms = self._game._results.apply(lambda x: tuple(x), axis=1)
        perm_counts = perms.value_counts().to_frame('Count')
        perm_counts.index.name = 'Permutation'
        return perm_counts