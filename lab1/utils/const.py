### DEPENDENCIAS
### ------------------

from enum import Enum

### CONSTANTES
### ------------------

# Opciones del menú principal
class MenuOps(Enum):
    TRAIN = 1
    PLAY = 2

# Tipos de jugadores para la opción JUGAR
class PlayerType(Enum):
    RANDOM = 1
    SELF = 2
    HUMAN = 3

# Tipos de juego para la clase Game
class GameMode(Enum):
    TRAINING = 1
    PLAYING = 2
