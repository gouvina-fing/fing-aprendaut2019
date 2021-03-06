### DEPENDENCIAS
### ------------------

import time
import operator

from model.training import Training
import processing.plotter as plotter
import processing.archiver as archiver
from utils.const import ModelTypes, InputLayerTypes, HiddenLayersOps, ActivationFunctions, LearningRateOps, GameTokens, CompareOps, HiddenLayersCount, HiddenNeuronsCount
from utils.gui import printTrainedPlayer

### METODOS PRINCIPALES
### -------------------

# Dado un tipo de oponente y una representación del tablero, entrena todas las configuraciones paramétricas posibles
def getAllNeuralNetworks(playerType, inputLayer):

    players = []
    index = 1

    print()
    print("Iniciando búsqueda...")
    print()

    for hiddenLayer in HiddenLayersOps:
        for activFunction in ActivationFunctions:
            for learningRate in LearningRateOps:

                if type(hiddenLayer) == int:
                    hiddenLayerLength = 1
                    hiddenLayerNeurons = hiddenLayer
                else:
                    hiddenLayerLength = len(hiddenLayer)
                    hiddenLayerNeurons = hiddenLayer[0]

                options = {
                    'playerType': playerType,
                    'modelType': ModelTypes.NEURAL,
                    'inputLayer': inputLayer,
                    'hiddenLayer': hiddenLayerLength,
                    'hiddenNeuron': hiddenLayerNeurons,
                    'hiddenLayerSizes': hiddenLayer,
                    'activationFunction': activFunction,
                    'learningRate': learningRate,
                    'iters': 100,
                    'maxRounds': 300,
                    'notDraw': True,
                }

                t = Training(GameTokens.PLAYER1, options)
                
                tic = time.time()
                (player, results, _, _) = t.training()
                toc = time.time()

                playerData = {
                    'playerID': len(players) + 1,
                    'player': player,
                    'type': playerType,
                    'name': 'Red Neuronal',
                    'modelType': ModelTypes.NEURAL,
                    'time': toc-tic,
                    'inputLayer': options['inputLayer'],
                    'hiddenLayer': options['hiddenLayer'],
                    'hiddenNeuron': options['hiddenNeuron'],
                    'activationFunction': options['activationFunction'],
                    'learningRate': options['learningRate'],
                    'iterations': options['iters'],
                    'maxRounds': options['maxRounds'],
                    'notDraw': options['notDraw'],
                    'results': results
                }

                players.append(playerData)
                
                print()
                print("Entrenamiento finalizado")
                printTrainedPlayer(playerData, index)
                index += 1

                playerTypeTxt = playerType.value
                inputLayerTxt = options['inputLayer'].value
                hiddenLayerTxt = options['hiddenLayer']
                hiddenNeuronTxt = options['hiddenNeuron']
                activTxt = options['activationFunction'].value
                learningRateTxt = options['learningRate'][0]
                filename = f'{playerTypeTxt}_{inputLayerTxt}_{hiddenLayerTxt}_{hiddenNeuronTxt}_{activTxt}_{learningRateTxt}'
                archiver.savePlayer(filename, playerData)

    print("Finalizando búsqueda...")
    return players

# Dada una lista de jugadores entrenados, los ordena descendentemente según ratio de partidas ganadas
def getBestNeuralNetworks(players):

    aux = []

    for player in players:
        winRate = getWinRate(player['results'])
        aux.append((winRate, player))

    aux = sorted(aux, key=operator.itemgetter(0), reverse=True)
    return [p for w,p in aux]

### METODOS AUXILIARES
### -------------------

def getRateFromPlayers(players, rateType):
    aux = []
    for player in players:
        if rateType == CompareOps.WIN_RATE:
            rate = getWinRate(player['results'])
        elif rateType == CompareOps.VICTORY_RATE:
            rate = getVictoryRate(player['results'])
        aux.append(rate)
    return aux

def getHiddenLayersRateFromPlayers(players):
    aux = []
    for h in HiddenLayersCount:
        winRateAvg = 0
        pCount = 0
        for p in players:
            if p['hiddenLayer'] == h:
                pCount += 1
                winRateAvg += getWinRate(p['results'])
        winRateAvg /= pCount
        aux.append(winRateAvg)
    return aux

def getHiddenNeuronsRateFromPlayers(players):
    aux = []
    for h in HiddenNeuronsCount:
        winRateAvg = 0
        pCount = 0
        for p in players:
            if p['hiddenNeuron'] == h:
                pCount += 1
                winRateAvg += getWinRate(p['results'])
        winRateAvg /= pCount
        aux.append(winRateAvg)
    return aux

def getActivationRateFromPlayers(players):
    aux = []
    for a in ActivationFunctions:
        winRateAvg = 0
        pCount = 0
        for p in players:
            if p['activationFunction'] == a:
                pCount += 1
                winRateAvg += getWinRate(p['results'])
        winRateAvg /= pCount
        aux.append(winRateAvg)
    return aux

def getLearningRatesRateFromPlayers(players):
    aux = []
    for lr in LearningRateOps:
        winRateAvg = 0
        pCount = 0
        for p in players:
            if p['learningRate'] == lr:
                pCount += 1
                winRateAvg += getWinRate(p['results'])
        winRateAvg /= pCount
        aux.append(winRateAvg)
    return aux

### METODOS INTERNOS
### -------------------

def getWinRate(results):
    return results[0] / sum(results)

def getVictoryRate(results):
    divisor = results[0] + results[1]
    if divisor == 0:
        return 0
    else:
        return results[0] / divisor