#!/bin/bash

# Colores para salida en terminal
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Iniciando compilación del proyecto de evaluación de polinomios...${NC}"

# Verificar que tenemos el compilador adecuado
if ! command -v g++ &> /dev/null; then
    echo -e "${RED}Error: g++ no está instalado${NC}"
    exit 1
fi

# Comprobar versión de C++
echo "Verificando soporte para C++17..."
if ! g++ -std=c++17 -c -x c++ /dev/null -o /dev/null &> /dev/null; then
    echo -e "${RED}Error: Tu compilador no soporta C++17${NC}"
    echo "Se requiere C++17 para std::filesystem"
    exit 1
fi

# Crear directorios si no existen
mkdir -p data
mkdir -p docs

# Compilar el programa
echo "Compilando polynomial_evaluation.cpp..."
g++ -std=c++17 -Wall -Wextra -O2 src/polynomial_evaluation.cpp -o polynomial_evaluation

# Verificar éxito
if [ $? -eq 0 ]; then
    echo -e "${GREEN}Compilación exitosa${NC}"
    chmod +x polynomial_evaluation
    echo -e "Para ejecutar el programa: ${YELLOW}./polynomial_evaluation${NC}"
    echo -e "Para generar gráficas después de ejecutar: ${YELLOW}python src/plot_results.py${NC}"
else
    echo -e "${RED}Error de compilación${NC}"
    exit 1
fi
