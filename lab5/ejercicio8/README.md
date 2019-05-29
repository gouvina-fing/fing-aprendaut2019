Para ejecutar el programa del ejercicio 8, debe situarse en el mismo directorio que main.py y correr en python 3:
python main.py
Luego se le va a desplegar el siguiente menú, del cual puede elegir que acción realizar:

#####################################################
#                                                   #
#        MENÚ - Laboratorio 5 (Damas Chinas)        #
#                                                   #
#####################################################

Jugadores actuales:
-> 0 - Jugador: Random sin entrenar

General:
1. Entrenar modelo
2. Cargar modelo
3. Guardar modelo

Evaluación:
4. Buscar mejor modelo
5. Comparar modelos

Simulación:
6. Simular partida contra modelo
7. Simular partida entre modelos
8. Simular torneo

0. Salir

-> Elija una opción:

--------------------------------------------------------------------------------------------------------

Dentro de las opciones, cada una cubre lo siguiente:
# General
- Entrenar modelo: Permite entrenar un jugador de damas chinas
    - Puede ser un entrenamiento desde cero (Eligiendo VS Random o VS Si Mismo), o un entrenamiento incremental entre dos jugadores guarados en memoria (VS otra IA).
- Cargar modelo: Permite cargar jugadores guardados (mediante la biblioteca pickle).
    - Permite cargar un jugador partir de un filename.
    - Permite cargar muchos jugadores.
        - Todos los jugadores entrenados
        - A partir de keywords relacionadas al nombre del archivo y detalladas en la consola.
- Guardar modelo: Permite guardar un jugador en memoria al filesystem (mediante la biblioteca pickle)

# Evaluación
- Buscar mejor modelo: Automatiza el entrenamiento de todos los jugadores que fueron entrenados, imprimendo cual fue el de mayor Win Rate.
- Comparar modelos: Permite generar gráficas de los jugadores que fueron entrenados y están guardados en la carpeta player. (Estas graficas se incluyen en el notebook)

# Simulación
- Simular partida contra modelo: Permite al usuario jugar una partida contra un jugador cargado en memoria.
- Simular partida entre modelos: Permite espectar una partida entre dos jugadores cargados en memoria.
- Simular torneo: Permite simular un torneo (con el comportamiento definido en el informe) entre 8 jugadores.

- Salir: Termina la ejecución del programa.
