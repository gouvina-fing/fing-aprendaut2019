### DEPENDENCIAS
### ------------------

import sys
import os
import time

from model.model import Model
import processing.reader as reader
import processing.parser as parser
from evaluation.evaluate import normalValidation, crossValidation
import utils.gui as gui
from utils.const import MenuOps, ModelOps, ContinuousOps, MeasureOps, EvaluationOps, COVERTYPE_DATASET

### METODO PRINCIPAL
### ----------------

if __name__ == '__main__':

    op = MenuOps.TRAIN
    classifiers = []

    while op == MenuOps.TRAIN or op == MenuOps.CLASSIFY or op == MenuOps.EVALUATE or op == MenuOps.SHOW:

        gui.printMenu(classifiers)
        op = gui.printMenuOption()

        if op == MenuOps.TRAIN:

            # Independientes del modelo
            datasetFile = gui.printDataset()
            (modelType, modelName) = gui.printModelType()
            revertOnehot = gui.printOneHotEncoding(modelType)

            # Especificos al modelo  
            k = gui.printModelK(modelType)
            continuous = gui.printContinuousStrategy(modelType)
            measure = gui.printMeasureType(modelType)
            norm = gui.printNormType(modelType)
            structure = gui.printStructure(modelType)
            mEst = gui.printMEstimator(modelType)

            model = Model(modelType)
            (dataset, attributes, results) = reader.readDataset(datasetFile, datasetFile == COVERTYPE_DATASET, onehot)
            options = {
              'k': k,
              'continuous': continuous,
              'measure': measure,
              'revertOnehot': revertOnehot,
              'mEst': mEst,
              'norm': norm,
              'structure': structure,
            }

            print()
            print("-> COMIENZO DEL ENTRENAMIENTO")

            tic = time.time()
            model.train(dataset, attributes, results, options)
            toc = time.time()

            print("-> FIN DEL ENTRENAMIENTO")
            print()

            classifier = {
                'model': model,
                'attributes': attributes,
                'results': results,
                'type': modelType,
                'name': modelName,
                'time': toc-tic,
                'options': options,
            }
            classifiers.append(classifier)

            gui.printTrainedClassifier(classifier)
            input("-> Oprima enter para volver al menú")

        elif op == MenuOps.CLASSIFY:

            if classifiers == []:
                print()
                print ("-> No hay clasificadores, entrene uno para clasificar")
                input("-> Oprima enter para volver al menú")

            else:
                gui.printClear()
                gui.printClassifiers(classifiers)

                c = int( input("-> Elija un clasificador por el índice: ") )
                c -= 1
                print("")

                if c >= 0 and c < len(classifiers):
                    print("-> Ingrese un ejemplo a clasificar:")
                    print("ATRIBUTOS: " + str(classifiers[c]['model'].getModelAttributesNames()))
                    example = input()
                    example = parser.getFormattedExample(example, classifiers[c]['model'].getModelAttributesNames())
                    (classification, probability) = classifiers[c]['model'].classify(example)
                    print()
                    print("El ejemplo fue clasificado como ", end=" ")
                    print(classification, end=" ")
                    print("con probabilidad", end=" ")
                    print(probability)
                    input("-> Oprima enter para volver al menú")
                else:
                    print("-> El índice ingresado no corresponde a ningún clasificador")
                    input("-> Oprima enter para volver al menú")

        elif op == MenuOps.EVALUATE:

            # Independientes del modelo
            datasetFile = gui.printDataset()
            (modelType, modelName) = gui.printModelType()
            evalMode = gui.printEvaluationMode()
            if evalMode == EvaluationOps.CROSS:
                evalK = gui.printEvaluationK()
            revertOnehot = gui.printOneHotEncoding(modelType)

            # Especificos al modelo            
            k = gui.printModelK(modelType)
            continuous = gui.printContinuousStrategy(modelType)
            measure = gui.printMeasureType(modelType)
            norm = gui.printNormType(modelType)
            structure = gui.printStructure(modelType)
            mEst = gui.printMEstimator(modelType)
            weighted = gui.printWeighted(modelType)

            (dataset, attributes, results) = reader.readDataset(datasetFile, datasetFile == COVERTYPE_DATASET, revertOnehot)
            model = Model(modelType)
            options = {
              'k': k,
              'continuous': continuous,
              'measure': measure,
              'revertOnehot': revertOnehot,
              'mEst': mEst,
              'norm': norm,
              'structure': structure,
              'weighted': weighted,
            }

            classifier = {
                'model': model,
                'attributes': attributes,
                'results': results,
                'type': modelType,
                'name': modelName,
                'options': options,
            }
            classifiers.append(classifier)

            if evalMode == EvaluationOps.NORMAL:
                (trainingTime, accuracy, means, weightedMeans, eval, confusionMatrix) = normalValidation(dataset, classifier)
                gui.printNormalEvaluation(classifier, trainingTime, accuracy, means, weightedMeans, eval, confusionMatrix, len(dataset))

            elif evalMode == EvaluationOps.CROSS:
                (eval, evalMean) = crossValidation(dataset, classifier, evalK)
                gui.printCrossEvaluation(classifier, eval, evalMean, len(dataset))

            input("-> Oprima enter para volver al menú")

        elif op == MenuOps.SHOW:

            if classifiers == []:
                print()
                print("-> No hay clasificadores, entrene uno para mostrar")

            else:
                gui.printClear()
                gui.printClassifiers(classifiers)

                c = int( input("-> Elija un clasificador por el índice: ") )
                c -= 1
                print("")

                if c >= 0 and c < len(classifiers):

                    if classifiers[c]['model'].getModelType() == ModelOps.KNN:
                        print("-> No hay nada que mostrar")
                    
                    else:
                        classifiers[c]['model'].printClassifier()
                    
                else:
                    print("-> El índice ingresado no corresponde a ningún clasificador")

            input("-> Oprima enter para volver al menú")