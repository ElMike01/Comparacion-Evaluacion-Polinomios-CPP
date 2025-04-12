# Comparación de Eficiencia: Evaluación de Polinomios

Este repositorio contiene una implementación en C++ para comparar la eficiencia computacional del algoritmo estándar de evaluación de polinomios versus el algoritmo de Horner.

## Autor
[Joan Antonio Lazaro Silva]

## Requisitos del Sistema
- Compilador C++ compatible con C++11 o superior (g++ recomendado)
- Python 3.x con las bibliotecas matplotlib y pandas (para generar gráficas)

## Instrucciones de Compilación y Ejecución

### Compilación del Código C++
```bash
# Crear directorio para datos si no existe
mkdir -p data

# Compilar el programa
g++ -std=c++11 -O2 src/polynomial_evaluation.cpp -o polynomial_evaluation
```

### Ejecución del Experimento
```bash
# Ejecutar el programa de evaluación
./polynomial_evaluation
```

### Generación de Gráficas
```bash
# Ejecutar el script de Python para generar gráficas
python plot_results.py
```

## Descripción de los Algoritmos

### Método Estándar
El método estándar para evaluar un polinomio P(x) = a_n * x^n + a_{n-1} * x^{n-1} + ... + a_1 * x + a_0 consiste en calcular directamente cada término elevando x a la potencia correspondiente y multiplicando por el coeficiente, para luego sumar todos los términos:

```
P(x) = a_n * x^n + a_{n-1} * x^{n-1} + ... + a_1 * x + a_0
```

Este método tiene una complejidad computacional de O(n²) debido a que el cálculo de potencias como x^n requiere n-1 multiplicaciones.

### Método de Horner
El método de Horner reorganiza el polinomio mediante factorización para minimizar las operaciones:

```
P(x) = (...((a_n * x + a_{n-1}) * x + a_{n-2}) * x + ... + a_1) * x + a_0
```

Este algoritmo tiene una complejidad computacional de O(n), ya que requiere exactamente n multiplicaciones y n sumas para evaluar un polinomio de grado n.

## Resultados Experimentales

### Gráfica Comparativa
![Comparación de Eficiencia](docs/comparison_plot.png)

### Relación de Tiempos
![Relación de Tiempos](docs/ratio_plot.png)

## Análisis de Resultados

Los experimentos confirman la ventaja teórica del algoritmo de Horner en términos de eficiencia computacional:

1. **Comparación de Tiempos:** El método de Horner es consistentemente más rápido que el método estándar. La diferencia de rendimiento se vuelve más pronunciada conforme aumenta el grado del polinomio.

2. **Escalabilidad:** El tiempo de ejecución del método estándar crece cuadráticamente con el grado del polinomio (O(n²)), mientras que el método de Horner crece linealmente (O(n)).

3. **Proporción de Tiempos:** Para polinomios de alto grado, el método estándar puede ser hasta n veces más lento que el método de Horner, lo que corrobora la diferencia teórica en complejidad algorítmica.

4. **Precisión Numérica:** Ambos métodos producen resultados numéricamente equivalentes (dentro del margen de error de punto flotante), por lo que la elección entre ellos no afecta la precisión del resultado.

## Conclusiones

1. El algoritmo de Horner representa una mejora significativa sobre el método estándar para la evaluación de polinomios, especialmente para polinomios de grado elevado.

2. La optimización matemática que realiza el método de Horner mediante factorización se traduce en una ventaja computacional clara y medible.

3. Para aplicaciones donde la eficiencia es crítica, como procesamiento de señales o gráficos por computadora, el método de Horner debería ser la elección preferida para la evaluación de polinomios.

4. Los resultados experimentales confirman plenamente la ventaja teórica de complejidad O(n) del método de Horner frente a la complejidad O(n²) del método estándar.
