import pandas as pd

class Game:
    """
    A class representing a game of rolling one or more dice multiple times.

    Attributes
    ----------
    _dice : list
        A list of Die objects.
    _results : pd.DataFrame
        DataFrame storing results of the most recent play.
    """

    def __init__(self, dice):
        """
        Initialize the Game object.

        Parameters
        ----------
        dice : list
            A list of Die objects.
        """
        self._dice = dice
        self._results = pd.DataFrame()

    def play(self, num_rolls):
        """
        Roll all dice a number of times.

        Parameters
        ----------
        num_rolls : int
            Number of times to roll each die.
        """
        records = {}
        for i, die in enumerate(self._dice):
            records[i] = die.roll(num_rolls)
        self._results = pd.DataFrame(records)
        self._results.index.name = 'Roll Number'

    def show(self, form = 'wide'):
        """
        Show results from the most recent play.

        Parameters
        ----------
        form : str
            'wide' or 'narrow'

        Returns
        -------
        pd.DataFrame

        Raises
        ------
        ValueError: If form is not 'wide' or 'narrow'
        """
        if form == 'wide':
            return self._results.copy()
        elif form == 'narrow':
            return self._results.stack().to_frame("Outcome").rename_axis(['Roll Number', 'Die Number'])
        else:
            raise ValueError("Form must be 'wide' or 'narrow'")