import numpy as np
import pandas as pd
import random

class Die:
    """
    A class representing a die that can be rolled.

    Attributes:
    ----------
    _df : pd.DataFrame
        A private dataframe with faces as index and weights as a column.
    """

    def __init__(self, faces: np.ndarray):
        """
        Initialize a Die object with faces.

        Parameters
        ----------
        faces : np.ndarray
            A numpy array of distinct faces (strings or numbers).

        Raises
        ------
        TypeError: If input is not a numpy array.
        ValueError: If faces are not unique.
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a numpy array.")
        if len(np.unique(faces)) != len(faces):
            raise ValueError("All faces must be unique.")

        self._df = pd.DataFrame({
            "weight": [1.0] * len(faces)
        }, index = faces)

    def change_weight(self, face, new_weight):
        """
        Change the weight of a given face.

        Parameters
        ----------
        face : str or number
        new_weight : float or int

        Raises
        ------
        IndexError: If face not in the die.
        TypeError: If weight is not numeric.
        """
        if face not in self._df.index:
            raise IndexError("Face not found in die.")
        try:
            new_weight = float(new_weight)
        except ValueError:
            raise TypeError("Weight must be a numeric value.")

        self._df.loc[face, 'weight'] = new_weight

    def roll(self, rolls=1):
        """
        Roll the die one or more times.

        Parameters
        ----------
        rolls : int, optional
            Number of times to roll the die (default is 1)

        Returns
        -------
        list
            List of outcomes.
        """
        return random.choices(
            population = self._df.index.tolist(),
            weights = self._df['weight'].tolist(),
            k = rolls
        )

    def show(self):
        """
        Show current state of the die.

        Returns
        -------
        pd.DataFrame
        """
        return self._df.copy()