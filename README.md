# Comparacion-Evaluacion-Polinomios-CPP
# Comparación de Eficiencia en Evaluación de Polinomios: Método Estándar vs. Algoritmo de Horner

Este proyecto implementa y compara experimentalmente la eficiencia computacional del algoritmo estándar de evaluación de polinomios frente al algoritmo de Horner en C++.

## Autor

[Joan Antonio Lazaro Silva]

## Requisitos del Sistema

- Compilador C++ con soporte para C++11 o superior (g++ 5.0+, clang++ 3.4+, o MSVC 19.0+)
- CMake 3.10 o superior (opcional, para facilitar la compilación)
- Python 3.6+ con matplotlib (opcional, para generar gráficas)

## Instrucciones de Compilación y Ejecución

### Compilación Manual

```bash
# Crear directorios necesarios
mkdir -p build data

# Compilar el proyecto
g++ -std=c++11 -O3 -Wall -Wextra src/polynomial.cpp src/main.cpp -o build/polynomial_benchmark

# Ejecutar el benchmark
./build/polynomial_benchmark
```

### Usar CMake (opcional)

```bash
mkdir build && cd build
cmake ..
make
./polynomial_benchmark
```

### Generar Gráfica (requiere Python con matplotlib)

```bash
python scripts/generate_graph.py
```

## Descripción de los Algoritmos

### Método Estándar

El método estándar para evaluar un polinomio P(x) = a_n * x^n + a_{n-1} * x^{n-1} + ... + a_1 * x + a_0 consiste en calcular cada término por separado y sumar los resultados:

1. Calcular a_n * x^n
2. Calcular a_{n-1} * x^{n-1}
...
3. Calcular a_1 * x
4. Sumar todos los términos más a_0

Este método tiene una complejidad temporal de O(n²) debido a que calcular cada potencia de x requiere O(n) operaciones.

### Algoritmo de Horner

El algoritmo de Horner, también conocido como esquema de Horner, reordena los cálculos para minimizar el número de operaciones:

P(x) = (...((a_n * x + a_{n-1}) * x + a_{n-2}) * x + ... + a_1) * x + a_0

Este método tiene una complejidad temporal de O(n), ya que solo requiere n multiplicaciones y n sumas.

## Resultados Experimentales

A continuación se muestra una gráfica comparativa de los tiempos de ejecución promedio de ambos métodos para polinomios de grados entre 10 y 1000:

![Gráfica comparativa de tiempos](docs/graph.png)

## Análisis de Resultados

El análisis experimental confirma la diferencia teórica en complejidad entre los dos algoritmos:

1. **Algoritmo Estándar (O(n²))**: Los tiempos de ejecución crecen cuadráticamente con el grado del polinomio, lo que se evidencia en la curva más pronunciada en la gráfica.

2. **Algoritmo de Horner (O(n))**: Los tiempos de ejecución crecen linealmente con el grado del polinomio, resultando en una pendiente mucho más suave.

La diferencia entre ambos métodos se hace más evidente a medida que aumenta el grado del polinomio. Por ejemplo, para un polinomio de grado 1000, el método estándar es aproximadamente [X] veces más lento que el algoritmo de Horner.

Esta diferencia se debe principalmente a:
- El método estándar requiere calcular potencias de x para cada término (operación costosa)
- El algoritmo de Horner reutiliza cálculos previos, eliminando la necesidad de calcular potencias

## Conclusiones

Los resultados experimentales confirman claramente la ventaja teórica del algoritmo de Horner sobre el método estándar para la evaluación de polinomios:

1. El algoritmo de Horner es significativamente más eficiente, especialmente para polinomios de alto grado.
2. La diferencia de rendimiento aumenta con el grado del polinomio, alineándose con las complejidades teóricas (O(n) vs O(n²)).
3. Para aplicaciones prácticas donde se requiera evaluar polinomios repetidamente, el algoritmo de Horner debería ser la opción preferida.

Este proyecto demuestra cómo una simple reorganización matemática de un algoritmo puede tener un impacto significativo en su rendimiento computacional.
