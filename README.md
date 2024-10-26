
# Diagonalización y Potencia de una Matriz

Este documento describe los conceptos de **diagonalización** de matrices y cómo utilizar este proceso para calcular potencias de matrices de forma eficiente. También incluye ejemplos en Python para entender y visualizar estos conceptos.

---

## Conceptos Clave

### 1. Diagonalización de una Matriz
La diagonalización de una matriz cuadrada consiste en expresar una matriz \( A \) en la forma:
\[ A = PDP^{-1} \]
donde:
- \( P \) es la matriz de **vectores propios** de \( A \).
- \( D \) es la matriz **diagonal** que contiene los **valores propios** de \( A \).
- \( P^{-1} \) es la inversa de la matriz de vectores propios.

La diagonalización es posible si podemos encontrar una base completa de vectores propios para la matriz \( A \).

### 2. Potencia de una Matriz Diagonalizable
Si una matriz es diagonalizable, calcular una potencia elevada de \( A \) se simplifica mediante la fórmula:
\[ A^n = P D^n P^{-1} \]
donde \( D^n \) se obtiene simplemente elevando cada valor propio en \( D \) a la potencia deseada.

---

## Ejemplo en Python

### Diagonalización y Cálculo de Potencia
El siguiente código en Python calcula los valores y vectores propios, forma la matriz diagonal y luego calcula \( A^5 \) para una matriz de ejemplo.

```python
import numpy as np

def diagonalize_and_power(matrix, power):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    D = np.diag(eigenvalues)
    P = eigenvectors
    P_inv = np.linalg.inv(P)
    D_power = np.linalg.matrix_power(D, power)
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
print("Valores Propios:", result["eigenvalues"])
print("Vectores Propios:
", result["eigenvectors"])
print("Matriz Diagonal:
", result["diagonal_matrix"])
print("A^5:
", result["matrix_power"])
```

### Visualización de la Transformación

El siguiente código permite visualizar la transformación de los vectores base al aplicar la matriz \( A \) y sus potencias. Este enfoque es útil para comprender la influencia de los valores propios y vectores propios en el espacio.

```python
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
        matrix_power = np.linalg.matrix_power(matrix, i)
        transformed = matrix_power @ vectors
        transformed_vectors.append(transformed)
    return transformed_vectors

# Vectores base (ejes x e y)
base_vectors = np.array([[1, 0], [0, 1]]).T

# Aplicar la matriz A y su potencia
transformed_vectors = apply_power(A, base_vectors, 5)

# Graficar
plt.figure(figsize=(10, 6))
plt.quiver([0, 0], [0, 0], base_vectors[0, :], base_vectors[1, :], angles='xy', scale_units='xy', scale=1, color="grey", label="Vectores Base")
plt.quiver([0, 0], [0, 0], eigenvectors[0, :], eigenvectors[1, :], angles='xy', scale_units='xy', scale=1, color="blue", label="Vectores Propios")
for i, transformed in enumerate(transformed_vectors, start=1):
    plt.quiver([0, 0], [0, 0], transformed[0, :], transformed[1, :], angles='xy', scale_units='xy', scale=1, alpha=0.6, label=f"A^{i} * Vectores Base")

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
```

---

## Explicación de los Resultados

- **Vectores Base**: Representados en gris, muestran los ejes iniciales (1,0) y (0,1).
- **Vectores Propios**: En azul, muestran los vectores que no cambian en dirección bajo la transformación de \( A \).
- **Vectores Transformados**: Varias potencias de \( A \) aplicadas sobre los vectores base muestran cómo la matriz amplifica o rota el espacio en cada paso.

Este ejemplo permite visualizar cómo la diagonalización y los valores propios afectan las transformaciones de matrices en el espacio.

