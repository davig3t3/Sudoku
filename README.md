# Sudoku

# Juego en Python 3.9

Este código de Python es un solucionador de Sudoku que utiliza el algoritmo de backtracking. El código consta de cuatro funciones principales: imprimir_sudoku(), es_valido(), resolver() y main().

## ¿Que es backtracking?

Es una técnica de programación para resolver problemas mediante la exploración sistemática de todas las posibles soluciones. El proceso de backtracking implica buscar todas las soluciones posibles de forma recursiva y retrocediendo en caso de que se llegue a una solución incorrecta o insatisfactoria.

Esta técnica se utiliza especialmente para resolver problemas de optimización, donde se busca la mejor solución posible entre todas las posibles. En lugar de buscar todas las soluciones posibles, el proceso de backtracking busca una solución paso a paso, examinando si cada paso lleva a una solución viable. Si se encuentra un paso que no lleva a una solución viable, se retrocede al paso anterior y se examina una alternativa diferente.

El algoritmo de backtracking se utiliza en muchas aplicaciones, como la resolución de problemas de Sudoku, la planificación de tareas, la optimización de rutas de entrega y la resolución de laberintos. La eficiencia de la técnica de backtracking depende en gran medida de la complejidad del problema y de cómo se diseñe el algoritmo para explorar las posibles soluciones.

## Explicación del código

La función imprimir_sudoku() se encarga de imprimir la matriz de 9x9 de Sudoku en la consola. La matriz se almacena como una lista de 81 elementos, donde cada elemento representa un número en la matriz. La función utiliza dos bucles anidados para recorrer la matriz y mostrar cada número en su respectiva posición.

La función es_valido(y, x, n) se encarga de comprobar si un número n en la posición (y, x) es válido en el Sudoku. La función realiza tres comprobaciones para asegurarse de que el número n no se repita en la misma fila, columna o submatriz de 3x3. Si se encuentra un número repetido, la función devuelve False. Si no se encuentra un número repetido, la función devuelve True.

La función resolver() es la parte principal del solucionador de Sudoku. La función utiliza un enfoque de backtracking para encontrar la solución. La función utiliza un bucle for para iterar a través de cada elemento en la matriz. Si el elemento es cero, lo que significa que está vacío, la función prueba todos los números del 1 al 9 en esa posición hasta encontrar un número válido utilizando la función es_valido(). Si no encuentra un número válido, devuelve False. Si encuentra un número válido, lo agrega a la matriz y llama a la función resolver() de manera recursiva para continuar con el siguiente elemento. Si se encuentra una solución, la función devuelve True.

La función main() es la función principal del código. En esta función, se inicializa la matriz de Sudoku como una lista de 81 elementos, se llama a la función resolver() para encontrar la solución y se llama a la función imprimir_sudoku() para imprimir la matriz resuelta.

## Tiempo de codificación

Usando la tecnica de pomodoro para realizar este ejercicio el tiempo invertido fue de un total de 10 horas debido a su complejidad.

## Conclusión

Este código proporciona una implementación simple de un solucionador de Sudoku en Python utilizando el algoritmo de backtracking. El código utiliza bucles anidados, funciones y listas para resolver el Sudoku.

***

Codigo del [Sudoku](https://github.com/davig3t3/Sudoku/blob/main/Sudoku.py).

***

# Abstract
# Game in Python 3.9

This Python code is a Sudoku solver that uses the backtracking algorithm. The code consists of four main functions: imprimir_sudoku(), es_valido(), resolver(), and main().

## What is backtracking?

It is a programming technique for solving problems by systematically exploring all possible solutions. The process of backtracking involves recursively searching for all possible solutions and backtracking if an incorrect or unsatisfactory solution is reached.

This technique is particularly used for solving optimization problems, where the best possible solution is sought among all possible solutions. Instead of searching for all possible solutions, the backtracking process looks for a solution step by step, examining if each step leads to a viable solution. If a step is found that does not lead to a viable solution, it backtracks to the previous step and examines a different alternative.

The backtracking algorithm is used in many applications, such as solving Sudoku puzzles, task scheduling, optimizing delivery routes, and solving mazes. The efficiency of the backtracking technique largely depends on the complexity of the problem and how the algorithm is designed to explore possible solutions.

## Code Explenation

The function imprimir_sudoku() is responsible for printing the 9x9 Sudoku matrix to the console. The matrix is stored as a list of 81 elements, where each element represents a number in the matrix. The function uses two nested loops to iterate through the matrix and display each number in its respective position.

The function es_valido(y, x, n) checks whether a number n in the position (y, x) is valid in the Sudoku. The function performs three checks to ensure that the number n is not repeated in the same row, column, or 3x3 submatrix. If a repeated number is found, the function returns False. If no repeated number is found, the function returns True.

The function resolver() is the main part of the Sudoku solver. The function uses a backtracking approach to find the solution. The function uses a for loop to iterate through each element in the matrix. If the element is zero, which means it is empty, the function tries all the numbers from 1 to 9 in that position until it finds a valid number using the es_valido() function. If it does not find a valid number, it returns False. If it finds a valid number, it adds it to the matrix and recursively calls the resolver() function to continue with the next element. If a solution is found, the function returns True.

The main() function is the main function of the code. In this function, the Sudoku matrix is initialized as a list of 81 elements, the resolver() function is called to find the solution, and the imprimir_sudoku() function is called to print the solved matrix.

## Coding time

Using the Pomodoro technique to complete this exercise, the total time invested was 10 hours due to its complexity.

## Conclusion

This code provides a simple implementation of a Sudoku solver in Python using the backtracking algorithm. The code uses nested loops, functions, and lists to solve the Sudoku.

***

Code of [Sudoku](https://github.com/davig3t3/Sudoku/blob/main/Sudoku.py).

***
 
