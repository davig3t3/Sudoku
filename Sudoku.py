import random

# Creamos una lista para almacenar los valores del Sudoku
sudoku = [0] * 81

# Definimos una función para imprimir el Sudoku
def imprimir_sudoku():
    for i in range(9):
        for j in range(9):
            print(sudoku[i*9+j], end=" ")
        print()

# Definimos una función para comprobar si un valor es válido
def es_valido(y, x, n):
    for i in range(9):
        if sudoku[y*9+i] == n:
            return False
    for i in range(9):
        if sudoku[i*9+x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[(y0+i)*9+(x0+j)] == n:
                return False
    return True

# Definimos una función para resolver el Sudoku recursivamente
def resolver():
    for i in range(81):
        if sudoku[i] == 0:
            y = i // 9
            x = i % 9
            for n in random.sample(range(1, 10), 9):
                if es_valido(y, x, n):
                    sudoku[i] = n
                    if resolver():
                        return True
                    sudoku[i] = 0
            return False
    return True

# Resolvemos el Sudoku
resolver()

# Imprimimos el Sudoku resuelto
imprimir_sudoku()