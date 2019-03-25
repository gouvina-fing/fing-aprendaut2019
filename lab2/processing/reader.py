### DEPENDENCIAS
### ------------------

import operator
import pandas as pd
from scipy.io import arff

from utils.const import AttributeType, ContinuousOps

### METODOS PRINCIPALES
### -------------------

# Lee 'dsFile' y lo devuelve como un diccionario (atributo, valor)
def readDataset(filename):
    ds = arff.loadarff(filename)
    df = pd.DataFrame(ds[0])
    ds = df.to_dict('records')
    return ds

### METODOS PRINCIPALES - ATRIBUTOS
### ---------------------------------

# Devuelve la lista de posibles atributos y su tipo en 'dataset'
def getAttributes(dataset):
    attributes = set()
    example = dataset[0]
    for key in list(example.keys()):
        if key != 'class':
            attribute = str(key)
            attributeType = checkAttributeType(getPossibleDiscreteValues(dataset, attribute))
            attributes.add((attribute, attributeType))
    return list(attributes)

# Devuelve la lista de posibles valores en 'dataset' para 'attribute'
def getPossibleValues(dataset, attribute, continuous):
    (attributeKey, attributeType) = attribute
    values = getPossibleDiscreteValues(dataset, attributeKey)

    if attributeType == AttributeType.DISCRETE:
        return values
    
    elif attributeType == AttributeType.CONTINUOUS and continuous == ContinuousOps.FIXED:
       
        interval1 = len(values) // 3
        interval2 = (len(values) // 3) * 2

        possibleValues = []
        possibleValues.append(values[interval1 - 1])
        possibleValues.append(values[interval2 - 1])
        possibleValues.append("bigger")

        return possibleValues

    elif attributeType == AttributeType.CONTINUOUS and continuous == ContinuousOps.VARIABLE:

        sortedDataset = sorted(dataset, key=operator.itemgetter(attributeKey))
        possibleValues = []
        lastRes = None
        lastExample = None

        # Iterate through sorted training examples, adding a new value to whenever the answer changes
        # adding the median value between the current value and the previous one
        for example in sortedDataset:
            if lastRes != None and example['class'] != lastRes:
                possibleValues.append(((float(example[attributeKey]) - float(lastExample)) / 2) + float(lastExample))
            lastRes = example['class']
            lastExample = example[attributeKey]
        possibleValues.append("bigger")

        return possibleValues

# Devuelve la lista de posibles valores discretos en 'dataset' para 'attribute'
def getPossibleDiscreteValues(dataset, attribute):
    possibleValues = set()
    for x in dataset:
        possibleValues.add(x[attribute])
    return sorted(list(possibleValues))

### METODOS PRINCIPALES - EJEMPLOS
### ---------------------------------

# Devuelve el subconjunto de 'dataset' con valor 'value' en el atributo 'attribute'
def getExamplesForValue(dataset, attribute, values, value):
    (attributeKey, attributeType) = attribute

    if attributeType == AttributeType.DISCRETE:
        return [x for x in dataset if x[attributeKey] == value]
    
    elif attributeType == AttributeType.CONTINUOUS:
        index = values.index(value)

        # If it is the first element, just check if the value is lesser
        if index == 0:
            return [x for x in dataset if x[attributeKey] <= value]

        # If it is an intermediate interval, check if the value is in there
        elif value != "bigger":
            return [x for x in dataset if x[attributeKey] <= value and x[attributeKey] > values[index-1]]

         # If it is the last element, just check if the value is greater
        else:
            return [x for x in dataset if x[attributeKey] > values[index-1]]

### METODOS PRINCIPALES - RESULTADOS
### ---------------------------------

# Devuelve la lista de posibles clasificaciones en 'dataset'
def getResults(dataset):
    results = set()
    for x in dataset:
        results.add(x['class'])
    return list(results)
  
# Devuelve el resultado de 'results' más frecuente en 'dataset'
def getMostLikelyResult(dataset, results):

    mostLikelyResult = results[0]
    mostLikelyProportion = proportionExamplesForResult(dataset, results[0])

    for result in results[1:]:
        proportion = proportionExamplesForResult(dataset, result)
        if proportion >= mostLikelyProportion:
            mostLikelyResult = result
            mostLikelyProportion = proportion

    return (mostLikelyResult, mostLikelyProportion)

# Devuelve la frecuencia de ejemplos en 'dataset' clasificados como 'result'
def proportionExamplesForResult(dataset, result):
    if len(dataset) == 0:
      return 0
    examples = [x for x in dataset if x['class'] == result]
    return len(examples) / len(dataset)

### METODOS PRINCIPALES - CONTINUIDAD
### ---------------------------------

# Devuelve el tipo de atributo basado en sus posibles valores
def checkAttributeType(possibleValues):

    example = possibleValues[0]
    if type(example) != int and type(example) != float:
        return AttributeType.DISCRETE
    else:
        booleanSet = {0, 1}
        valuesSet = set(possibleValues)
        if booleanSet == valuesSet:
          return AttributeType.DISCRETE
        else:
          return AttributeType.CONTINUOUS

