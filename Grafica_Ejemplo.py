import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz A
A = np.array([[4, 1], [2, 3]])

# Calcular los valores y vectores propios
eigenvalues, eigenvectors = np.linalg.eig(A)

# Función para aplicar una transformación repetidamente
def apply_power(matrix, vectors, power):
    transformed_vectors = []
    for i in range(1, power + 1):
        # Elevar la matriz a la potencia i
        matrix_power = np.linalg.matrix_power(matrix, i)
        # Transformar los vectores base
        transformed = matrix_power @ vectors
        transformed_vectors.append(transformed)
    return transformed_vectors

# Vectores base (ejes x e y)
base_vectors = np.array([[1, 0], [0, 1]]).T  # Vectores de base [1,0] y [0,1]

# Aplicar la matriz A y su potencia
transformed_vectors = apply_power(A, base_vectors, 5)

# Graficar
plt.figure(figsize=(10, 6))

# Gráfico original: los ejes x e y
plt.quiver([0, 0], [0, 0], base_vectors[0, :], base_vectors[1, :], angles='xy', scale_units='xy', scale=1, color="grey", label="Vectores Base")

# Graficar los vectores propios
plt.quiver([0, 0], [0, 0], eigenvectors[0, :], eigenvectors[1, :], angles='xy', scale_units='xy', scale=1, color="blue", label="Vectores Propios")

# Agregar los vectores transformados a través de potencias
for i, transformed in enumerate(transformed_vectors, start=1):
    plt.quiver([0, 0], [0, 0], transformed[0, :], transformed[1, :], angles='xy', scale_units='xy', scale=1, 
               alpha=0.6, label=f"A^{i} * Vectores Base")

# Ajustar el gráfico
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.axhline(0, color='grey', lw=0.5)
plt.axvline(0, color='grey', lw=0.5)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc="upper left")
plt.title("Transformación de Vectores bajo Potencias de la Matriz A")
plt.show()
