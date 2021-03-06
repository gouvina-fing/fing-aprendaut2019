### DEPENDENCIAS
### ------------------

import random

from model.model_concept import ModelConcept
from random import randint

from utils.const import PlayerType, ModelTypes

### CLASE PRINCIPAL
### ------------------

class Player():

    ### METODOS AUXILIARES
    ### -------------------


    ### CONSTRUCTOR
    ### -------------------

    def __init__(self, playerNumber, playerType, model = None):
        
        # Numero de las fichas del jugador en la partida
        self.playerNumber = playerNumber
        
        # Tipo de jugador
        # 1. Entrenado contra un random
        # 2. Entrenado contra si mismo
        # 0. Random
        self.playerType = playerType

        # Modelo del jugador entrenado. Si es un jugador random,
        # es None y no se usa
        self.model = model

        # Último movimiento para no hacer loops
        self.historialFrom = []
        self.historialTo = []

    ### GETTERS y SETTERS
    ### -------------------

    def getModel(self):
        return self.model
    def setModel(self, m):
        self.model = m

    def getPlayerType(self):
        return self.playerType
    
    def setPlayerNumber(self, n):
        self.playerNumber = n

    ### METODOS PRINCIPALES
    ### -------------------

    # Dado un tablero elige el un movimiento
    # -> Si es un jugador random lo elige aleatoriamente
    # -> Si es un jugador entrenado, evalua todas las posibilidades con el modelo
    # y elige la mejor evaluada
    def chooseMove(self, board):
        
        # Obtener las fichas del jugador
        playerTokens = board.getPlayerSlots(self.playerNumber)

        allMovesForward = []
        allMovesBackward = []

        # Se recorre todas las piezas del jugador
        for token in playerTokens:
            
            # Se obtiene la lista de posibles movimientos desde FROM
            (fromVX, fromVY) = token
            (movesForward, movesBackward) = board.getPossibleMoves(self.playerNumber, fromVX, fromVY)

            for movef in movesForward:
                allMovesForward.append((token, movef))
            for moveb in movesBackward:
                allMovesBackward.append((token, moveb))

        # Preferimos movimientos hacia adelante siempre que estos sean posibles
        if allMovesForward:
            moves = allMovesForward
        else:
            moves = allMovesBackward

        if self.playerType == PlayerType.RANDOM:
            # Se elige un movimiento al azar
            move = random.choice(moves)
            ((fromX, fromY), (toX, toY)) = move
            return move

        else:

            bestFrom = None
            bestTo = None
            bestEvaluation = 0

            # Se recorre todos los posibles movimientos, evaluando el tablero tras cada uno
            for (fromVX, fromVY), (toVX, toVY) in moves:
                # No permitimos movimientos inversos a los últimos 3
                if (self.historialFrom) and ((toVX,toVY) in self.historialFrom[-3:]):
                    continue

                board.moveToken(self.playerNumber, fromVX, fromVY, toVX, toVY)
                if self.model.options['modelType'] == ModelTypes.NEURAL:
                    features = board.getFeatures(self.playerNumber, self.model.options['inputLayer'])
                else:
                    features = board.getFeatures(self.playerNumber)
                evaluation = self.model.evaluate(features)

                # Si es el primer movimiento evaluado o tiene la mejor evaluacion conseguida
                # hasta ahora, se guarda como el mejor movimiento
                if bestTo == None or evaluation >= bestEvaluation:
                    if bestTo == None or evaluation > bestEvaluation:
                        best_moves = []
                    bestFrom = (fromVX, fromVY)
                    bestTo = (toVX, toVY)
                    bestEvaluation = evaluation
                    best_moves.append((bestFrom, bestTo))
                # Se deja el tablero en el estado anterior
                board.undoToken(self.playerNumber, fromVX, fromVY, toVX, toVY)

            try:
                move = best_moves[randint(0,len(best_moves)-1)]
            except:
                # HACK: A veces pasa que todos los movimientos posibles son inversos a movimientos ya hechos
                # (por lo general con otra pieza). Entonces elegimos un movimiento aleatorio
                move = moves[randint(0,len(moves)-1)]
            ((fromX, fromY), (toX, toY)) = move
            self.historialFrom.append((fromX,fromY))
            self.historialTo.append((toX, toY))
            return move