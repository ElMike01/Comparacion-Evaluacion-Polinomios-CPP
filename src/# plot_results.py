# plot_results.py
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

def ensure_dir(directory):
    """Crear directorio si no existe"""
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directorio creado: {directory}")

def plot_results():
    # Asegurar que los directorios existan
    ensure_dir('docs')
    
    # Cargar los datos del experimento
    try:
        data = pd.read_csv('data/results.csv')
    except Exception as e:
        print(f"Error al cargar los datos: {e}")
        return
    
    # Verificar que los datos contienen las columnas esperadas
    required_columns = ['grado', 'tiempo_promedio_estandar', 'tiempo_promedio_horner']
    if not all(col in data.columns for col in required_columns):
        print("Error: El archivo CSV no contiene las columnas esperadas")
        print(f"Columnas esperadas: {required_columns}")
        print(f"Columnas encontradas: {data.columns.tolist()}")
        return
    
    # 1. Crear la figura para la comparación de tiempos
    plt.figure(figsize=(12, 8))
    
    # Determinar si se necesita escala logarítmica
    use_log_scale = data['tiempo_promedio_estandar'].max() > 10 * data['tiempo_promedio_horner'].max()
    
    # Graficar los tiempos para ambos métodos
    plt.plot(data['grado'], data['tiempo_promedio_estandar'], 'ro-', linewidth=2, markersize=5, label='Método Estándar')
    plt.plot(data['grado'], data['tiempo_promedio_horner'], 'bo-', linewidth=2, markersize=5, label='Método de Horner')
    
    # Añadir títulos y etiquetas
    plt.title('Comparación de Eficiencia: Evaluación de Polinomios', fontsize=18)
    plt.xlabel('Grado del Polinomio (n)', fontsize=14)
    
    # Ajustar la escala si es necesario
    if use_log_scale:
        plt.yscale('log')
        plt.ylabel('Tiempo Promedio de Ejecución (μs) - Escala Logarítmica', fontsize=14)
    else:
        plt.ylabel('Tiempo Promedio de Ejecución (μs)', fontsize=14)
    
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    
    # Guardar la figura
    plt.tight_layout()
    plt.savefig('docs/comparison_plot.png', dpi=300)
    print("Gráfica guardada como 'docs/comparison_plot.png'")
    
    # 2. Crear una segunda gráfica para la relación de tiempos
    plt.figure(figsize=(12, 6))
    ratio = data['tiempo_promedio_estandar'] / data['tiempo_promedio_horner']
    
    # Graficar la relación de tiempos vs. grado
    plt.plot(data['grado'], ratio, 'go-', linewidth=2, markersize=5)
    
    # Añadir una línea teórica O(n) para comparar
    x = data['grado']
    y_theoretical = x / x.iloc[0] * ratio.iloc[0]  # Normalizar al primer punto
    plt.plot(x, y_theoretical, 'k--', alpha=0.7, linewidth=1.5, label='Tendencia O(n)')
    
    # Añadir títulos y etiquetas
    plt.title('Relación de Tiempos: Estándar/Horner', fontsize=18)
    plt.xlabel('Grado del Polinomio (n)', fontsize=14)
    plt.ylabel('Proporción de Tiempo (Estándar/Horner)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)
    
    # Guardar la figura
    plt.tight_layout()
    plt.savefig('docs/ratio_plot.png', dpi=300)
    print("Gráfica de proporción guardada como 'docs/ratio_plot.png'")
    
    # 3. Añadir una tercera gráfica que muestra el tiempo absoluto vs grado con ajustes teóricos
    plt.figure(figsize=(12, 6))
    
    # Modelo teórico: ajuste polinómico para el método estándar (debería seguir O(n²))
    z = np.polyfit(data['grado'], data['tiempo_promedio_estandar'], 2)
    p = np.poly1d(z)
    
    # Crear puntos para la curva teórica
    xp = np.linspace(data['grado'].min(), data['grado'].max(), 100)
    
    # Graficar datos reales y curva teórica
    plt.scatter(data['grado'], data['tiempo_promedio_estandar'], color='red', s=30, alpha=0.6, label='Método Estándar (datos)')
    plt.plot(xp, p(xp), 'r-', linewidth=2, label=f'Ajuste O(n²): {z[0]:.6f}n² + {z[1]:.4f}n + {z[2]:.4f}')
    
    # Modelo teórico: ajuste lineal para Horner (debería seguir O(n))
    z_horner = np.polyfit(data['grado'], data['tiempo_promedio_horner'], 1)
    p_horner = np.poly1d(z_horner)
    
    plt.scatter(data['grado'], data['tiempo_promedio_horner'], color='blue', s=30, alpha=0.6, label='Método de Horner (datos)')
    plt.plot(xp, p_horner(xp), 'b-', linewidth=2, label=f'Ajuste O(n): {z_horner[0]:.6f}n + {z_horner[1]:.4f}')
    
    # Añadir títulos y etiquetas
    plt.title('Análisis de Complejidad: Ajustes Teóricos', fontsize=18)
    plt.xlabel('Grado del Polinomio (n)', fontsize=14)
    plt.ylabel('Tiempo de Ejecución (μs)', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    
    # Guardar la figura
    plt.tight_layout()
    plt.savefig('docs/complexity_analysis.png', dpi=300)
    print("Gráfica de análisis de complejidad guardada como 'docs/complexity_analysis.png'")

if __name__ == "__main__":
    plot_results()