# Sudoku

# Juego en Python 3.9

Este código fue escrito en el lenguaje de programación Python y la versión utilizada es Python 3.9. El propósito de este código es simular un juego donde el jugador debe encontrar las letras "O" y "A" en una matriz cuadrada de tamaño `tam`. La matriz se genera aleatoriamente cada vez que se reinicia el juego. El jugador obtiene un punto por cada "O" encontrado, pero el juego termina cuando se encuentra un "A". El jugador puede elegir reiniciar el juego después de encontrar un "A" o terminar el juego.

## Explicación del código

El primer paso en este código es crear una matriz de tamaño `tam` x `tam` utilizando un bucle anidado. El valor de `tam` se toma como entrada del usuario. La matriz se llena con "." o "O" o "A" utilizando la función `random.choice`.

Luego, comienza el bucle del juego que se ejecutará hasta que el jugador decida dejar de jugar. En cada iteración del bucle, se busca en la matriz por "O" y "A". Si se encuentra "O", el jugador obtiene un punto. Si se encuentra "A", el juego termina y se le pregunta al jugador si desea reiniciar el juego. Si el jugador elige reiniciar, la matriz se vuelve a generar y los puntos se reinician a 0. Si el jugador elige terminar el juego, el bucle se interrumpe y el juego termina.

Finalmente, se imprime un mensaje agradeciendo al jugador por jugar.

## Conclusión

Este código proporciona una implementación simple de un juego en Python 3.9. Demuestra el uso de entrada/salida, bucles, listas y estructuras de control básicas en Python.

***

# Abstract
# Game in Python 3.9

This code was written in Python programming language and the version used is Python 3.9. The purpose of this code is to simulate a game where the player has to find letters "O" and "A" in a square matrix of size `tam`. The matrix is randomly generated each time the game is restarted. The player gets a point for each "O" found, but the game ends when an "A" is found. The player can choose to restart the game after an "A" is found or to end the game. 

## Code Explenation

The first step in this code is to create a matrix of size `tam` x `tam` using a nested loop. The value of `tam` is taken as input from the user. The matrix is filled with either "." or "O" or "A" using the `random.choice` function.

Then, the game loop starts which will run until the player decides to stop playing. In each iteration of the loop, the matrix is searched for "O" and "A". If "O" is found, the player gets a point. If "A" is found, the game ends and the player is asked if they want to restart the game. If the player chooses to restart, the matrix is re-generated and the points are reset to 0. If the player chooses to end the game, the loop breaks and the game ends.

Finally, a message thanking the player for playing is printed.

## Conclusion

This code provides a simple implementation of a game in Python 3.9. It demonstrates the use of input/output, loops, lists, and basic control structures in Python.

***
 
