### DEPENDENCIAS
### ------------------

import sys
import os
import time
import pickle

from model.training import Training
from model.training_duel import TrainingDuel
from model.model_concept import ModelConcept

from game.game import Game
from game.player import Player

import utils.gui as gui
import processing.plotter as plotter
from utils.const import MenuOps, PlayerType, GameMode, GameTokens, GameResults, ModelTypes, PlayerType

### METODO PRINCIPAL
### ----------------

if __name__ == '__main__':

    op = MenuOps.TRAIN
    players = []

    # NOTA: variable global con historial de models. Ver si rinde
    historial_weigths = []

    while op == MenuOps.TRAIN or op == MenuOps.PLAY_VS_IA or op == MenuOps.LOAD or op == MenuOps.WATCH_IA_VS_IA or op == MenuOps.SAVE:

        gui.printMenu(players)
        op = gui.printMenuOption()

        if op == MenuOps.TRAIN:
            (playerType, playerName) = gui.printPlayerType()

            if playerType == PlayerType.TRAINED_SHOWDOWN:
                player1Index = gui.pickPlayer(players, "-> Elija al jugador 1 por su índice: ")
                player2Index = gui.pickPlayer(players, "-> Elija al jugador 2 por su índice: ")
                
                player1 = players[player1Index-1]['player']
                player1.playerNumber = GameTokens.PLAYER1

                player2 = players[player2Index-1]['player']
                player1.playerNumber = GameTokens.PLAYER2

                spectate = gui.printSpectateOptions()

                options = {
                    'playerType': playerType,
                    'iters': gui.printTrainingIterations(),
                    'maxRounds': gui.printMaxRounds(),
                    'notDraw': gui.printSkipOnDraw(),
                    'learningRate': gui.printLearningRate(),
                    'spectate': spectate
                }

                t = TrainingDuel(player1, player2, options)

                (player1, player2, results, resultsPlot) = t.training()

                # Updateamos los modelos
                players[player1Index-1]['player'] = player1

                # HACK: Guardamos a player1 como un player1 para que no se rompa play vs AI.
                player2.playerNumber = GameTokens.PLAYER1
                players[player2Index-1]['player'] = player2

                plotter.printResultsPlot(resultsPlot, options['iters'])
                
            # Normal training
            else:
                modelType = gui.printModelOptions()
                options = {
                    'modelType': modelType,
                    'playerType': playerType,
                    'iters': gui.printTrainingIterations(),
                    'maxRounds': gui.printMaxRounds(),
                    'notDraw': gui.printSkipOnDraw(),
                    'learningRate': gui.printLearningRate()
                }
                if modelType == ModelTypes.CONCEPT:
                    options['weights'] = gui.printInitialWeights()
                    options['normalize_weights'] = gui.printNormalizeWeights()
                
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
                    'modelType': modelType,
                    'name': playerName,
                    'time': toc-tic,
                    'iterations': options['iters'],
                    'maxRounds': options['maxRounds'],
                    'results': results,
                    'learningRate': options['learningRate']
                }
                if modelType == ModelTypes.CONCEPT:
                    historial_weigths.append(player.getModel().getWeights())
                    playerData['initialWeights'] = options['weights']
                    playerData['finalWeights'] = player.getModel().getWeights()

                players.append(playerData)

                gui.printTrainedPlayer(playerData)
                plotter.printResultsPlot(resultsPlot, options['iters'])
                plotter.printErrorPlot(errorsPlot, options['iters'])

                filename = gui.printSavePlayer()
                if filename.strip():
                    pickle_out = open(filename,"wb")
                    pickle.dump(playerData, pickle_out)
                    pickle_out.close()

            input("-> Oprima enter para volver al menú")

        elif op == MenuOps.PLAY_VS_IA:

            player = gui.pickPlayer(players)

            # Representa la partida
            g = None

            # Se eligio un jugador aleatorio sin entrenar
            if player == 0:
                g = Game(GameMode.PLAYING, Player(GameTokens.PLAYER1, PlayerType.RANDOM))

            # Se eligió un jugador previamente entrenado
            else:
                g = Game(GameMode.PLAYING, players[player-1]['player'])

            # Se juega la partida y se imprime el mensaje segun el resultado
            res = g.play()
            if res == GameResults.WIN:
                print("-> Has ganado la partida. Oprime enter para volver al menú")
            else:
                print("-> Has perdido la partida. Oprime enter para volver al menú")
            input()

        elif op == MenuOps.WATCH_IA_VS_IA:
            player1Index = gui.pickPlayer(players, "-> Elija al jugador 1 por su índice: ")
            player2Index = gui.pickPlayer(players, "-> Elija al jugador 2 por su índice: ")

            # Representa la partida
            g = None

            # Se eligio un jugador aleatorio sin entrenar
            if player1Index == 0:
                player1 = Player(GameTokens.PLAYER1, PlayerType.RANDOM)
            else:
                player1 = players[player1Index-1]['player']
                player1.playerNumber = GameTokens.PLAYER1
            
            if player2Index == 0:
                player2 = Player(GameTokens.PLAYER2, PlayerType.RANDOM)
            else:
                player2 = players[player2Index-1]['player']
                player2.playerNumber = GameTokens.PLAYER2

            g = Game(GameMode.SPECTATING, (player1, player2))

            # Se juega la partida y se imprime el mensaje segun el resultado
            res = g.play(True)
            if res == GameResults.WIN:
                print("-> Ha ganado el jugador 1! Oprime enter para volver al menú")
            elif res == GameResults.LOSE:
                print("-> Ha ganado el jugador 2! Oprime enter para volver al menú")
            else:
                print("-> Ha habido un empate! Oprime enter para volver al menú")
            input()

        elif op == MenuOps.LOAD:
            filename = gui.printLoadPlayer()
            if filename.strip():
                try:
                    pickle_in = open(filename,"rb")
                    player = pickle.load(pickle_in)
                    players.append(player)
                except:
                    print("Error! Archivo erroneo, por favor intente nuevamente.")

        elif op == MenuOps.SAVE:
            playerIndex = gui.pickPlayer(players)
            player = players[playerIndex-1]
            filename = gui.printSavePlayer()
            if filename.strip():
                pickle_out = open(filename,"wb")
                pickle.dump(player, pickle_out)
                pickle_out.close()