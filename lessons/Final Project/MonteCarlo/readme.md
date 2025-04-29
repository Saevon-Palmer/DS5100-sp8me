# Monte Carlo Simulator

## Author
Sae'von Palmer

## Synopsis
```python
from die import Die
from game import Game
from analyzer import Analyzer
import numpy as np

die = Die(np.array(['A', 'B', 'C']))
game = Game([die, die])
game.play(5)
analyzer = Analyzer(game)
print(analyzer.jackpot())

#API

Die
__init__(faces: np.ndarray)

change_weight(face, new_weight)

roll(rolls = 1)

show()

Game
__init__(dice: list)


play(num_rolls: int)


show(form = 'wide')

Analyzer
__init__(game: Game)

jackpot()

face_counts_per_roll()

combo_counts()

permutation_counts()
