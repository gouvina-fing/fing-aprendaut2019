### DEPENDENCIAS
### ------------------

import csv
import copy
import matplotlib.pyplot as plt
import numpy as np

from .model_concept import ModelConcept
from .model_neural import ModelNeural

from game.game import Game
from game.player import Player

from utils.const import PlayerType, GameMode, GameTokens, GameResults, ModelTypes


### CLASE PRINCIPAL
### ------------------

class TrainingDuel():

    ### CONSTRUCTOR
    ### -------------------

    def __init__(self, player1, player2, options):

        # Tipo de jugador a entrenar (basado en su oponente)
        self.playerType = options['playerType']

        # Cantidad de iteraciones en el entrenamiento
        self.iters = options['iters']

        # Cantidad de turnos antes de declarar empate
        self.maxRounds = options['maxRounds']

        self.notDraw = options['notDraw']

        # Ratio de aprendizaje en el entrenamiento
        self.learningRate = options['learningRate']

        self.spectate = options['spectate']

        self.player1 = player1

        self.player2 = player2

    # Entrenamiento de los modelos
    def training(self):
        results = [0,0,0]
        results_x_axis = []
        results_y_axis = []
        variable = self.learningRate == 'var'

        if variable:
            self.learningRate = 1
            count = 100

        i = 0
        while i < self.iters:
            if variable:
                if self.iters <= 100:
                    if count != 100 and count % 10 == 0:
                        self.learningRate -= 0.1
                elif self.iters == 500:
                    if count != self.iters and count % 50 == 0:
                        self.learningRate -= 0.1
                elif self.iters == 1000:
                    if count != self.iters and count % 100 == 0:
                        self.learningRate -= 0.1
            
            # Se genera un juego nuevo para cada iteración
            g = Game(GameMode.TRAINING, (self.player1, self.player2), self.maxRounds)
            res = g.play(self.spectate)

            # Obtener tableros del juego
            historial = g.getBoards()

            # Se arma la lista de pares [tablero, evaluación de sucesor]
            for board, nextBoard in zip(historial, historial[1:]):
                if self.player1.getPlayerType() != PlayerType.TRAINED_RANDOM:
                    # Entrenamiento del player 1
                    trainingExamplesPlayer1 = []
                    featuresPlayer1 = board.getFeatures(self.player1.playerNumber, self.player1.model.options['modelType'])
                    nextFeaturesPlayer1 = nextBoard.getFeatures(self.player1.playerNumber, self.player1.model.options['modelType'])
                    trainingExamplesPlayer1.append([featuresPlayer1, self.player1.model.evaluate(nextFeaturesPlayer1)])

                # Entrenamiento del player 2
                if self.player2.getPlayerType() != PlayerType.TRAINED_RANDOM:
                    # Entrenamiento del player 1
                    trainingExamplesPlayer2 = []
                    featuresPlayer2 = board.getFeatures(self.player2.playerNumber, self.player2.model.options['modelType'])
                    nextFeaturesPlayer2 = nextBoard.getFeatures(self.player2.playerNumber, self.player2.model.options['modelType'])
                    trainingExamplesPlayer2.append([featuresPlayer2, self.player2.model.evaluate(nextFeaturesPlayer2)])

            # Se checkea el resultado del juego para setear la evaluación del último tablero
            if res == GameResults.WIN:
                print("-> Ha ganado el jugador 1!")
                lastEvaluation = 1
                results[0] = results[0] + 1
            elif res == GameResults.LOSE:
                print("-> Ha ganado el jugador 2!")
                lastEvaluation = -1
                results[1] = results[1] + 1
            else:
                print("-> Ha habido un empate!")
                results[2] = results[2] + 1
                if not self.notDraw:
                    print("Resultado omitido a causa de empate")
                    i += 1
                    if variable:
                        count -= 1
                    continue
                lastEvaluation = 0

            results_x_axis.append(i)
            results_y_axis.append(lastEvaluation)
            
            lastBoard = historial[-1]

            # Se actualizan los pesos del modelo utilizando los datos de la última partida

            # Player 1
            if self.player1.getPlayerType() != PlayerType.TRAINED_RANDOM:
                trainingExamplesPlayer1.append([lastBoard.getFeatures(self.player1.playerNumber, self.player1.model.options['modelType']), lastEvaluation])
                for t in trainingExamplesPlayer1:
                    self.player1.model.update(t[0], t[1], self.learningRate)

            # Player2
            if self.player2.getPlayerType() != PlayerType.TRAINED_RANDOM:
                trainingExamplesPlayer2.append([lastBoard.getFeatures(self.player2.playerNumber, self.player2.model.options['modelType']), (-1)*lastEvaluation])
                for t in trainingExamplesPlayer2:
                    self.player2.model.update(t[0], t[1], self.learningRate)

            i += 1
            if variable:
                count -= 1

        return (self.player1, self.player2, results, (results_x_axis, results_y_axis))