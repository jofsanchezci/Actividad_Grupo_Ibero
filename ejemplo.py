import numpy as np

def diagonalize_and_power(matrix, power):
    """
    Diagonaliza una matriz y calcula su potencia elevada al valor de `power`.
    
    Parámetros:
    matrix (ndarray): La matriz cuadrada a diagonalizar.
    power (int): La potencia a la cual elevar la matriz.
    
    Retorna:
    dict: Un diccionario con 'eigenvalues' (valores propios), 'eigenvectors' (vectores propios),
          'diagonal_matrix' (matriz diagonalizada) y 'matrix_power' (matriz elevada a la potencia dada).
    """
    # Paso 1: Calcular valores y vectores propios
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    
    # Paso 2: Formar la matriz diagonal D y la matriz de vectores propios P
    D = np.diag(eigenvalues)  # Matriz diagonal con los valores propios
    P = eigenvectors  # Matriz de vectores propios
    P_inv = np.linalg.inv(P)  # Inversa de P
    
    # Paso 3: Elevar la matriz diagonal D a la potencia especificada
    D_power = np.linalg.matrix_power(D, power)
    
    # Paso 4: Calcular la matriz original elevada a la potencia usando la diagonalización
    matrix_power = P @ D_power @ P_inv
    
    return {
        "eigenvalues": eigenvalues,
        "eigenvectors": P,
        "diagonal_matrix": D,
        "matrix_power": matrix_power
    }

# Ejemplo de uso
A = np.array([[4, 1], [2, 3]])
result = diagonalize_and_power(A, 5)

# Imprimir resultados
print("Valores Propios:", result["eigenvalues"])
print("Vectores Propios:\n", result["eigenvectors"])
print("Matriz Diagonal:\n", result["diagonal_matrix"])
print("A^5:\n", result["matrix_power"])
