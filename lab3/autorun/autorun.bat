﻿:: Call:
:: python automain.py DATASET MODEL EVALUATION ... (Depending on model, detailed below)
:: DATASET = { 1: Iris, 2: Covertype }
:: MODEL = { 1: Arbol, 2: Bosque, 3: Naive Bayes, 4: KNN }
:: EVALUATION = { 1: Normal, 2: Cross }

:: Arboles o Bosques:
:: python automain.py DATASET MODEL EVALUATION CONTINUOUS MEASURE
:: CONTINUOUS = { 1: Fixed, 2: Variable, 3: C4.5 }
:: MEASURE = { 1: Gain, 2: Gain Ratio, 3: Impurity Reduction }
::
:: python automain.py (1|2) (1|2) (1|2) (1|2|3) (1|2|3)
:: EX: automain.py 2 2 1 2 3

:: Bayes:
:: python automain.py DATASET MODEL EVALUATION ONEHOT CONTINUOUS mEST
:: ONEHOT = { 1: Deshacer Onehot Encoding, 2: Conservar Onehot Encoding }
:: CONTINUOUS = { 1: Standarization, 2: Variable }
:: mEST = 0..n
::
:: python automain.py (1|2) 3 (1|2) (1|2) (1|2) (0..n)
:: EX: automain.py 2 3 1 1 1

:: KNN:
:: python automain.py DATASET MODEL EVALUATION ONEHOT K MEASURE NORM WEIGHTED
:: ONEHOT = { 1: Deshacer Onehot Encoding, 2: Conservar Onehot Encoding }
:: K = 1..n (Se prefieren impares)
:: MEASURE = { 1: Distancia 'Manhattan', 2: Distancia Euclidea, 3: Distancia de Chebychev, 4: Distancia de Mahalanobis }
:: NORM = { 1: Norma Euclidea, 2: Norma Min-Max, 3: Norma Z-Score, 4: Ninguna Norma }
:: WEIGHTED = { 1: Weighted, 2: Not Weighted }
::
:: python automain.py (1|2) 4 (1|2) (1|2) (1..n) (1|2|3|4) (1|2|3|4) (1|2)
:: EX: 2 4 1 1 3 2 1 1

:: IRIS - NB
:: -----------------------------------------------------------------------------------

:: Fijo: Iris, NB, Normal, Deshacer Onehot, Normal Dist
python automain.py 1 3 1 1 1 0
python automain.py 1 3 1 1 1 0.01
python automain.py 1 3 1 1 1 0.5
python automain.py 1 3 1 1 1 1
python automain.py 1 3 1 1 1 100

:: Fijo: Iris, NB, Normal, Deshacer Onehot, Variables
python automain.py 1 3 1 1 2 0
python automain.py 1 3 1 1 2 0.01
python automain.py 1 3 1 1 2 0.5
python automain.py 1 3 1 1 2 1
python automain.py 1 3 1 1 2 100

:: Fijo: Iris, NB, Cross, Deshacer Onehot, Normal Dist
python automain.py 1 3 2 1 1 0
python automain.py 1 3 2 1 1 0.01
python automain.py 1 3 2 1 1 0.5
python automain.py 1 3 2 1 1 1
python automain.py 1 3 2 1 1 100

:: Fijo: Iris, NB, Cross, Deshacer Onehot, Variables
python automain.py 1 3 2 1 2 0
python automain.py 1 3 2 1 2 0.01
python automain.py 1 3 2 1 2 0.5
python automain.py 1 3 2 1 2 1
python automain.py 1 3 2 1 2 100

:: IRIS - KNN
:: -----------------------------------------------------------------------------------

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 1, Distancia Manhattan
python automain.py 1 4 1 1 1 1 1
python automain.py 1 4 1 1 1 1 2
python automain.py 1 4 1 1 1 1 3

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 1, Distancia Euclidea
python automain.py 1 4 1 1 1 2 1
python automain.py 1 4 1 1 1 2 2
python automain.py 1 4 1 1 1 2 3

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 1, Distancia Chebychev
python automain.py 1 4 1 1 1 3 1
python automain.py 1 4 1 1 1 3 2
python automain.py 1 4 1 1 1 3 3

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 1, Distancia Mahalanobis
::python automain.py 1 4 1 1 1 4 4

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 3, Distancia Manhattan
python automain.py 1 4 1 1 3 1 1
python automain.py 1 4 1 1 3 1 2
python automain.py 1 4 1 1 3 1 3

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 3, Distancia Euclidea
python automain.py 1 4 1 1 3 2 1
python automain.py 1 4 1 1 3 2 2
python automain.py 1 4 1 1 3 2 3

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 3, Distancia Chebychev
python automain.py 1 4 1 1 3 3 1
python automain.py 1 4 1 1 3 3 2
python automain.py 1 4 1 1 3 3 3

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 1, Distancia Mahalanobis
::python automain.py 1 4 1 1 3 4 4

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 7, Distancia Manhattan
python automain.py 1 4 1 1 7 1 1
python automain.py 1 4 1 1 7 1 2
python automain.py 1 4 1 1 7 1 3

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 7, Distancia Euclidea
python automain.py 1 4 1 1 7 2 1
python automain.py 1 4 1 1 7 2 2
python automain.py 1 4 1 1 7 2 3

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 7, Distancia Chebychev
python automain.py 1 4 1 1 7 3 1
python automain.py 1 4 1 1 7 3 2
python automain.py 1 4 1 1 7 3 3

:: Fijo: Iris, KNN, Normal, Deshacer Onehot, 7, Distancia Mahalanobis
::python automain.py 1 4 1 1 7 4 4

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 1, Distancia Manhattan
python automain.py 1 4 2 1 1 1 1
python automain.py 1 4 2 1 1 1 2
python automain.py 1 4 2 1 1 1 3

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 1, Distancia Euclidea
python automain.py 1 4 2 1 1 2 1
python automain.py 1 4 2 1 1 2 2
python automain.py 1 4 2 1 1 2 3

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 1, Distancia Chebychev
python automain.py 1 4 2 1 1 3 1
python automain.py 1 4 2 1 1 3 2
python automain.py 1 4 2 1 1 3 3

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 1, Distancia Mahalanobis
::python automain.py 1 4 2 1 1 4 4

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 3, Distancia Manhattan
python automain.py 1 4 2 1 3 1 1
python automain.py 1 4 2 1 3 1 2
python automain.py 1 4 2 1 3 1 3

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 3, Distancia Euclidea
python automain.py 1 4 2 1 3 2 1
python automain.py 1 4 2 1 3 2 2
python automain.py 1 4 2 1 3 2 3

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 3, Distancia Chebychev
python automain.py 1 4 2 1 3 3 1
python automain.py 1 4 2 1 3 3 2
python automain.py 1 4 2 1 3 3 3

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 1, Distancia Mahalanobis
::python automain.py 1 4 2 1 3 4 4

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 7, Distancia Manhattan
python automain.py 1 4 2 1 7 1 1
python automain.py 1 4 2 1 7 1 2
python automain.py 1 4 2 1 7 1 3

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 7, Distancia Euclidea
python automain.py 1 4 2 1 7 2 1
python automain.py 1 4 2 1 7 2 2
python automain.py 1 4 2 1 7 2 3

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 7, Distancia Chebychev
python automain.py 1 4 2 1 7 3 1
python automain.py 1 4 2 1 7 3 2
python automain.py 1 4 2 1 7 3 3

:: Fijo: Iris, KNN, Cross, Deshacer Onehot, 7, Distancia Mahalanobis
::python automain.py 1 4 2 1 7 4 4

:: CoverType - NB
:: -----------------------------------------------------------------------------------

:: Fijo: CoverType, NB, Normal, Deshacer Onehot, Normal Dist
python automain.py 2 3 1 1 1 0
python automain.py 2 3 1 1 1 0.01
python automain.py 2 3 1 1 1 0.5
python automain.py 2 3 1 1 1 1
python automain.py 2 3 1 1 1 100

:: Fijo: CoverType, NB, Normal, Deshacer Onehot, Variables
python automain.py 2 3 1 1 2 0
python automain.py 2 3 1 1 2 0.01
python automain.py 2 3 1 1 2 0.5
python automain.py 2 3 1 1 2 1
python automain.py 2 3 1 1 2 100

:: Fijo: CoverType, NB, Normal, Conservar Onehot, Normal Dist
python automain.py 2 3 1 2 1 0
python automain.py 2 3 1 2 1 0.01
python automain.py 2 3 1 2 1 0.5
python automain.py 2 3 1 2 1 1
python automain.py 2 3 1 2 1 100

:: Fijo: CoverType, NB, Normal, Conservar Onehot, Variables
python automain.py 2 3 1 2 2 0
python automain.py 2 3 1 2 2 0.01
python automain.py 2 3 1 2 2 0.5
python automain.py 2 3 1 2 2 1
python automain.py 2 3 1 2 2 100

:: Fijo: CoverType, NB, Cross, Deshacer Onehot, Normal Dist
python automain.py 2 3 2 1 1 0
python automain.py 2 3 2 1 1 0.01
python automain.py 2 3 2 1 1 0.5
python automain.py 2 3 2 1 1 1
python automain.py 2 3 2 1 1 100

:: Fijo: CoverType, NB, Cross, Deshacer Onehot, Variables
python automain.py 2 3 2 1 2 0
python automain.py 2 3 2 1 2 0.01
python automain.py 2 3 2 1 2 0.5
python automain.py 2 3 2 1 2 1
python automain.py 2 3 2 1 2 100

:: Fijo: CoverType, NB, Cross, Conservar Onehot, Normal Dist
python automain.py 2 3 2 2 1 0
python automain.py 2 3 2 2 1 0.01
python automain.py 2 3 2 2 1 0.5
python automain.py 2 3 2 2 1 1
python automain.py 2 3 2 2 1 100

:: Fijo: CoverType, NB, Cross, Conservar Onehot, Variables
python automain.py 2 3 2 2 2 0
python automain.py 2 3 2 2 2 0.01
python automain.py 2 3 2 2 2 0.5
python automain.py 2 3 2 2 2 1
python automain.py 2 3 2 2 2 100

:: COVERTYPE - KNN
:: -----------------------------------------------------------------------------------

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 1, Distancia Manhattan
python automain.py 2 4 1 1 1 1 1
python automain.py 2 4 1 1 1 1 2
python automain.py 2 4 1 1 1 1 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 1, Distancia Euclidea
python automain.py 2 4 1 1 1 2 1
python automain.py 2 4 1 1 1 2 2
python automain.py 2 4 1 1 1 2 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 1, Distancia Chebychev
python automain.py 2 4 1 1 1 3 1
python automain.py 2 4 1 1 1 3 2
python automain.py 2 4 1 1 1 3 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 3, Distancia Manhattan
python automain.py 2 4 1 1 3 1 1
python automain.py 2 4 1 1 3 1 2
python automain.py 2 4 1 1 3 1 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 3, Distancia Euclidea
python automain.py 2 4 1 1 3 2 1
python automain.py 2 4 1 1 3 2 2
python automain.py 2 4 1 1 3 2 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 3, Distancia Chebychev
python automain.py 2 4 1 1 3 3 1
python automain.py 2 4 1 1 3 3 2
python automain.py 2 4 1 1 3 3 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 7, Distancia Manhattan
python automain.py 2 4 1 1 7 1 1
python automain.py 2 4 1 1 7 1 2
python automain.py 2 4 1 1 7 1 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 7, Distancia Euclidea
python automain.py 2 4 1 1 7 2 1
python automain.py 2 4 1 1 7 2 2
python automain.py 2 4 1 1 7 2 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 7, Distancia Chebychev
python automain.py 2 4 1 1 7 3 1
python automain.py 2 4 1 1 7 3 2
python automain.py 2 4 1 1 7 3 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 1, Distancia Manhattan
python automain.py 2 4 2 1 1 1 1
python automain.py 2 4 2 1 1 1 2
python automain.py 2 4 2 1 1 1 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 1, Distancia Euclidea
python automain.py 2 4 2 1 1 2 1
python automain.py 2 4 2 1 1 2 2
python automain.py 2 4 2 1 1 2 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 1, Distancia Chebychev
python automain.py 2 4 2 1 1 3 1
python automain.py 2 4 2 1 1 3 2
python automain.py 2 4 2 1 1 3 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 3, Distancia Manhattan
python automain.py 2 4 2 1 3 1 1
python automain.py 2 4 2 1 3 1 2
python automain.py 2 4 2 1 3 1 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 3, Distancia Euclidea
python automain.py 2 4 2 1 3 2 1
python automain.py 2 4 2 1 3 2 2
python automain.py 2 4 2 1 3 2 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 3, Distancia Chebychev
python automain.py 2 4 2 1 3 3 1
python automain.py 2 4 2 1 3 3 2
python automain.py 2 4 2 1 3 3 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 7, Distancia Manhattan
python automain.py 2 4 2 1 7 1 1
python automain.py 2 4 2 1 7 1 2
python automain.py 2 4 2 1 7 1 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 7, Distancia Euclidea
python automain.py 2 4 2 1 7 2 1
python automain.py 2 4 2 1 7 2 2
python automain.py 2 4 2 1 7 2 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 7, Distancia Chebychev
python automain.py 2 4 2 1 7 3 1
python automain.py 2 4 2 1 7 3 2
python automain.py 2 4 2 1 7 3 3

:: Fijo: CoverType, KNN, Normal, Conservar Onehot, 1, Distancia Manhattan
python automain.py 2 4 1 2 1 1 1
python automain.py 2 4 1 2 1 1 2
python automain.py 2 4 1 2 1 1 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 1, Distancia Euclidea
python automain.py 2 4 1 2 1 2 1
python automain.py 2 4 1 2 1 2 2
python automain.py 2 4 1 2 1 2 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 1, Distancia Chebychev
python automain.py 2 4 1 2 1 3 1
python automain.py 2 4 1 2 1 3 2
python automain.py 2 4 1 2 1 3 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 3, Distancia Manhattan
python automain.py 2 4 1 2 3 1 1
python automain.py 2 4 1 2 3 1 2
python automain.py 2 4 1 2 3 1 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 3, Distancia Euclidea
python automain.py 2 4 1 2 3 2 1
python automain.py 2 4 1 2 3 2 2
python automain.py 2 4 1 2 3 2 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 3, Distancia Chebychev
python automain.py 2 4 1 2 3 3 1
python automain.py 2 4 1 2 3 3 2
python automain.py 2 4 1 2 3 3 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 7, Distancia Manhattan
python automain.py 2 4 1 2 7 1 1
python automain.py 2 4 1 2 7 1 2
python automain.py 2 4 1 2 7 1 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 7, Distancia Euclidea
python automain.py 2 4 1 2 7 2 1
python automain.py 2 4 1 2 7 2 2
python automain.py 2 4 1 2 7 2 3

:: Fijo: CoverType, KNN, Normal, Deshacer Onehot, 7, Distancia Chebychev
python automain.py 2 4 1 2 7 3 1
python automain.py 2 4 1 2 7 3 2
python automain.py 2 4 1 2 7 3 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 1, Distancia Manhattan
python automain.py 2 4 2 2 1 1 1
python automain.py 2 4 2 2 1 1 2
python automain.py 2 4 2 2 1 1 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 1, Distancia Euclidea
python automain.py 2 4 2 2 1 2 1
python automain.py 2 4 2 2 1 2 2
python automain.py 2 4 2 2 1 2 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 1, Distancia Chebychev
python automain.py 2 4 2 2 1 3 1
python automain.py 2 4 2 2 1 3 2
python automain.py 2 4 2 2 1 3 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 3, Distancia Manhattan
python automain.py 2 4 2 2 3 1 1
python automain.py 2 4 2 2 3 1 2
python automain.py 2 4 2 2 3 1 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 3, Distancia Euclidea
python automain.py 2 4 2 2 3 2 1
python automain.py 2 4 2 2 3 2 2
python automain.py 2 4 2 2 3 2 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 3, Distancia Chebychev
python automain.py 2 4 2 2 3 3 1
python automain.py 2 4 2 2 3 3 2
python automain.py 2 4 2 2 3 3 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 7, Distancia Manhattan
python automain.py 2 4 2 2 7 1 1
python automain.py 2 4 2 2 7 1 2
python automain.py 2 4 2 2 7 1 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 7, Distancia Euclidea
python automain.py 2 4 2 2 7 2 1
python automain.py 2 4 2 2 7 2 2
python automain.py 2 4 2 2 7 2 3

:: Fijo: CoverType, KNN, Cross, Deshacer Onehot, 7, Distancia Chebychev
python automain.py 2 4 2 2 7 3 1
python automain.py 2 4 2 2 7 3 2
python automain.py 2 4 2 2 7 3 3

pause