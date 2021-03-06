### DEPENDENCIAS
### ------------------

from enum import Enum

### CONSTANTES
### ------------------

# Opciones del menú principal
class MenuOps(Enum):
    PCA = 1
    KMEANS = 2

class PCAOps(Enum):
    COVARIANZA = 0
    SVD = 1

class PCAnalysis(Enum):
    NONE = 0
    GENERAL = 1
    ALL_PARTY = 2
    EACH_PARTY = 3

class PCAIntermediates(Enum):
    NONE = 0
    COV_MATRIX = 1    
    EIGEN_VALUES = 2
    VARIANCE_RATIO = 3

class KmeansAnalysis(Enum):
    NONE = 0
    GENERAL = 1
    CANDIDATES = 2
    PARTIES = 3

class KmeansEvaluations(Enum):
    NONE = 0
    SILHOUETTE = 1
    ARI = 2

class CandidateDivision(Enum):
    PARTIES = 0
    SPECTRUM = 1
    NOLAN = 2
    DUAL_SPECTRUM = 3

# Datasets y sus ubicaciones
DATA_ENCUESTAS = 'data/data.csv'
DATA_CANDIDATOS = 'data/candidatos.json'
DATA_CANDIDATOS_ESPECTRO = 'data/candidatosEspectro.json'
DATA_CANDIDATOS_ESPECTRO_DUAL = 'data/candidatosEspectroDual.json'
DATA_CANDIDATOS_NOLAN = 'data/candidatosNolan.json'
DATA_CANDIDATOS_SIN_PARTIDO = 'data/candidatosSinPartido.json'


