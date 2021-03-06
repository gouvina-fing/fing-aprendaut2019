### DEPENDENCIAS
### ------------------

import math
import copy
import operator

from utils.const import AttributeType, ContinuousOps

### METODOS PRINCIPALES - ATRIBUTOS
### ---------------------------------

# Devuelve la lista de posibles valores en 'dataset' para 'attribute'
def getPossibleValues(dataset, attribute):
    (attributeKey, attributeType) = attribute
    return dataset[attributeKey].unique().tolist()

# A
def getChangingValues(dataset, attribute):
    
    possibleValues = []
    lastResult = None
    lastExample = None
        
    for index in dataset.index:
        currentResult = dataset.at[index,'class']
        currentExample = dataset.at[index,attribute]
        if lastResult != None and currentResult != lastResult and currentExample not in possibleValues:
            possibleValues.append(currentExample)
        lastResult = currentResult

    totalValues = len(possibleValues)
    maxValues = 10
    if totalValues > maxValues:
        possibleValues = [x for x in possibleValues if possibleValues.index(x) % (totalValues // maxValues) == 0]

    return possibleValues

# Devuelve la lista de posibles valores (discretizados) en 'dataset' para 'attribute'
def getDiscretePossibleValues(dataset, attribute, results, continuous, getGain):

    (attributeKey, attributeType) = attribute
    sortedDataset = dataset.sort_values(by=[attributeKey])
    values = getPossibleValues(sortedDataset, attribute)
    if attributeType == AttributeType.DISCRETE:
        return values
    
    elif attributeType == AttributeType.CONTINUOUS and continuous == ContinuousOps.FIXED:

        median = len(values) // 2

        possibleValues = []
        possibleValues.append(values[median])
        possibleValues.append("bigger")
        return possibleValues

    elif attributeType == AttributeType.CONTINUOUS and continuous == ContinuousOps.VARIABLE:

        possibleValues = getChangingValues(sortedDataset, attributeKey)
        possibleValues.append("bigger")
        return possibleValues
        
    elif attributeType == AttributeType.CONTINUOUS and continuous == ContinuousOps.C45:
        
        possibleValues = getChangingValues(sortedDataset, attributeKey)

        bestGain = 0
        bestThreshold = None
        for value in possibleValues:
            valueThreshold = [value, 'bigger']
            gain = getGain(dataset, attribute, valueThreshold, results)
            if gain > bestGain:
                bestGain = gain
                bestThreshold = value
                
        return [bestThreshold, 'bigger']

### METODOS PRINCIPALES - EJEMPLOS
### ---------------------------------

# Devuelve el subconjunto de 'dataset' con valor 'value' en el atributo 'attribute'
def getExamplesForValue(dataset, attribute, values, value):
    (attributeKey, attributeType) = attribute

    if attributeType == AttributeType.CONTINUOUS and value == 'bigger':
        index = values.index(value)
        condition = dataset[attributeKey] > values[index-1]
        return dataset[condition]

    elif attributeType == AttributeType.CONTINUOUS and value != 'bigger':
        condition = dataset[attributeKey] <= value
        return dataset[condition]

    else:
        condition = dataset[attributeKey] == value
        return dataset[condition]

# Devuelve la frecuencia de ejemplos en 'dataset' con 'attribute'='value'
def getProportionExamplesForValue(dataset, attribute, values, value):
    if len(dataset.index) == 0:
      return 0
    examples = getExamplesForValue(dataset, attribute, values, value)
    return len(examples.index) / len(dataset.index)

### METODOS PRINCIPALES - RESULTADOS
### ---------------------------------
  
# Devuelve el resultado de 'results' más frecuente en 'dataset'
def getMostLikelyResult(dataset, results):

    proportions = getAllProportionExamplesForResults(dataset, results)
    
    mostLikelyResult = None
    mostLikelyProportion = 0

    for key, value in proportions.items():
        if value >= mostLikelyProportion:
            mostLikelyResult = key
            mostLikelyProportion = value

    return (mostLikelyResult, mostLikelyProportion)

# Devuelve la frecuencia de ejemplos en 'dataset' clasificados como 'result'
def getProportionExamplesForResult(dataset, result):
    if len(dataset) == 0:
      return 0
    condition = dataset['class'] == result
    examples = dataset[condition]
    return len(examples) / len(dataset)

# Devuelve las frecuencias de ejemplos en 'dataset' para todos los resultados en 'results'
def getAllProportionExamplesForResults(dataset, results):
    resultsHash = {}
    for result in results:
        resultsHash[result] = 0
    for index in dataset.index:
        resultsHash[dataset.at[index,'class']] += 1
    proportions = {}
    for result in results:
        proportions[result] = resultsHash[result] / len(dataset.index)
    return proportions