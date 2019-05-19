### DEPENDENCIAS
### ------------------

import sys
import os
import time

from model.training import Training
from model.model_concept import ModelConcept

from game.game import Game
from game.player import Player

import utils.gui as gui
import processing.plotter as plotter
from utils.const import MenuOps, PlayerType, GameMode, GameTokens, GameResults, ModelTypes

### METODO PRINCIPAL
### ----------------

if __name__ == '__main__':

    op = MenuOps.TRAIN
    players = []

    # NOTA: variable global con historial de models. Ver si rinde
    historial_weigths = []

    while op == MenuOps.TRAIN or op == MenuOps.PLAY:

        gui.printMenu(players)
        op = gui.printMenuOption()

        if op == MenuOps.TRAIN:

            modelType = gui.printModelOptions()
            (playerType, playerName) = gui.printPlayerType()

            options = {
                'modelType': modelType,
                'playerType': playerType,
                'iters': gui.printTrainingIterations(),
                'maxRounds': gui.printMaxRounds(),
                'notDraw': gui.printSkipOnDraw(),
            }
            if modelType == ModelTypes.CONCEPT:
                options['learningRate'] = gui.printLearningRate()
                options['weights'] = gui.printInitialWeights()
                options['normalize_weights'] = gui.printNormalizeWeights()
            else:
                options['a'] = ''    
            
            t = Training(GameTokens.PLAYER1, options)

            print()
            print("-> COMIENZO DEL ENTRENAMIENTO")

            tic = time.time()
            (player, results, resultsPlot, errorsPlot) = t.training()
            toc = time.time()

            print("-> FIN DEL ENTRENAMIENTO")
            print()

            playerData = {
                'player': player,
                'type': playerType,
                'name': playerName,
                'time': toc-tic,
                'iterations': options['iters'],
                'maxRounds': options['maxRounds'],
                'results': results
            }
            if modelType == ModelTypes.CONCEPT:
                historial_weigths.append(player.getModel().getWeights())
                playerData['learningRate'] = options['learningRate']
                playerData['initialWeights'] = options['weights']
                playerData['finalWeights'] = player.getModel().getWeights()
            else:
                playerData['a'] = ''

            players.append(playerData)

            gui.printTrainedPlayer(playerData)
            plotter.printResultsPlot(resultsPlot, options['iters'])
            plotter.printErrorPlot(errorsPlot, options['iters'])

            input("-> Oprima enter para volver al menú")

        elif op == MenuOps.PLAY:

            gui.printClear()
            gui.printPlayers(players)

            c = int( input("-> Elija un jugador por el índice: ") )
            print("")

            if c >= 0 and c < len(players) + 1:

                # Representa la partida
                g = None

                # Se eligio un jugador aleatorio sin entrenar
                if c == 0:
                    g = Game(GameMode.PLAYING, Player(GameTokens.PLAYER1, PlayerType.RANDOM))

                # Se eligió un jugador previamente entrenado
                else:
                    g = Game(GameMode.PLAYING, players[c-1]['player'])

                # Se juega la partida y se imprime el mensaje segun el resultado
                res = g.play()
                if res == GameResults.WIN:
                    print("-> Has ganado la partida. Oprime enter para volver al menú")
                else:
                    print("-> Has perdido la partida. Oprime enter para volver al menú")
                input()
            else:
                print("-> El índice ingresado no corresponde a ningún jugador")