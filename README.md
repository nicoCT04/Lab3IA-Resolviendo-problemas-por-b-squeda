# Lab 3 IA: Resolviendo problemas por búsqueda

## Descripción del Proyecto

Este laboratorio implementa y compara 5 algoritmos de búsqueda clásicos en Inteligencia Artificial aplicados al problema de diseñar una rutina de ejercicios óptima en un gimnasio. El objetivo es encontrar el camino desde las actividades de calentamiento hasta los estiramientos, minimizando el tiempo total de recuperación.

## Problema a Resolver

**Contexto**: Diseñar una rutina de ejercicios que:
- Comience en "Warm-up activities" (Calentamiento)
- Termine en "Stretching" (Estiramientos)
- Involucre todo el cuerpo
- Minimice el tiempo total de recuperación

**Inputs**:
- `funcion_de_costo.csv`: Grafo de actividades con costos de transición entre ejercicios
- `heuristica.csv`: Tiempo de recuperación estimado después de quemar 300 calorías por actividad

## Algoritmos Implementados

### 1. Búsqueda No Informada

#### BFS (Breadth-First Search)
- **Estrategia**: Explora por niveles, expandiendo todos los nodos a una profundidad antes de pasar al siguiente nivel
- **Estructura**: Cola FIFO (First In, First Out)
- **Características**: Garantiza encontrar la solución más corta en número de pasos, pero no necesariamente la de menor costo

#### DFS (Depth-First Search)
- **Estrategia**: Explora en profundidad, siguiendo un camino hasta el final antes de retroceder
- **Estructura**: Cola LIFO (Last In, First Out) / Pila
- **Características**: Puede encontrar soluciones rápidamente, pero no garantiza optimalidad

#### UCS (Uniform Cost Search)
- **Estrategia**: Expande el nodo con menor costo acumulado g(n)
- **Estructura**: Cola de prioridad ordenada por path_cost
- **Características**: Garantiza encontrar la solución de menor costo

### 2. Búsqueda Informada

#### Greedy Best-First Search
- **Estrategia**: Expande el nodo que parece estar más cerca de la meta según la heurística h(n)
- **Estructura**: Cola de prioridad ordenada por heurística
- **Características**: Rápido pero no garantiza optimalidad

#### A* (A-Star)
- **Estrategia**: Expande el nodo con menor f(n) = g(n) + h(n)
- **Estructura**: Cola de prioridad ordenada por f(n)
- **Características**: Óptimo y completo si la heurística es admisible

## Estructura del Código

### Clases Implementadas

#### `TreeNode`
Representa un nodo en el árbol de búsqueda:
```python
- state: Estado/actividad actual
- path_cost: Costo acumulado desde el inicio (g)
- heuristic: Valor heurístico (h)
- parent: Referencia al nodo padre
- children: Lista de nodos hijos
- f(): Retorna g(n) + h(n) para A*
```

#### Estructuras de Datos

**`FIFOQueue`** (para BFS)
- `EMPTY()`: Verifica si la cola está vacía
- `TOP()`: Retorna el primer elemento sin removerlo
- `POP()`: Retorna y remueve el primer elemento
- `ADD(item)`: Agrega elemento al final de la cola

**`LIFOQueue`** (para DFS)
- Mismos métodos que FIFO
- `POP()`: Retorna y remueve el último elemento (comportamiento de pila)

**`PriorityQueue`** (para UCS y A*)
- Mismos métodos base
- `ADD(item)`: Inserta y ordena por path_cost o f(n)
- Constructor acepta `use_heuristic` para elegir entre UCS y A*

**`GreedyQueue`** (para Greedy)
- Hereda de PriorityQueue
- `ADD(item)`: Ordena solo por heurística h(n)

### Función Principal

```python
algoritmo_busqueda(inicio, meta, grafo, heuristicas, tipo_cola, usar_h)
```
- Implementa el algoritmo de búsqueda general
- Retorna: ruta, costo total, nodos expandidos
- Evita ciclos usando conjunto de visitados

## Uso

### 1. Cargar los datos
```python
grafo, heuristicas = cargar_datos()
```

### 2. Definir inicio y meta
```python
inicio = "Warm-up activities"
meta = "Stretching"
```

### 3. Ejecutar los 5 algoritmos
```python
# BFS
ruta_bfs, costo_bfs, exp_bfs = algoritmo_busqueda(
    inicio, meta, grafo, heuristicas, FIFOQueue()
)

# DFS
ruta_dfs, costo_dfs, exp_dfs = algoritmo_busqueda(
    inicio, meta, grafo, heuristicas, LIFOQueue()
)

# UCS
ruta_ucs, costo_ucs, exp_ucs = algoritmo_busqueda(
    inicio, meta, grafo, heuristicas, PriorityQueue(use_heuristic=False)
)

# Greedy
ruta_greedy, costo_greedy, exp_greedy = algoritmo_busqueda(
    inicio, meta, grafo, heuristicas, GreedyQueue()
)

# A*
ruta_astar, costo_astar, exp_astar = algoritmo_busqueda(
    inicio, meta, grafo, heuristicas, PriorityQueue(use_heuristic=True)
)
```

### 4. Visualizar resultados
Los resultados muestran para cada algoritmo:
- Costo total de la ruta
- Número de nodos expandidos (eficiencia)
- Ruta completa de ejercicios

## Resultados Esperados

Los algoritmos se comparan en:
1. **Optimalidad**: ¿Encuentra la mejor solución?
   - UCS y A*: Sí (óptimos)
   - BFS: Óptimo en número de pasos, no en costo
   - DFS y Greedy: No garantizan optimalidad

2. **Eficiencia**: ¿Cuántos nodos explora?
   - A*: Generalmente el más eficiente con buena heurística
   - Greedy: Rápido pero puede no ser óptimo
   - UCS: Óptimo pero puede expandir muchos nodos
   - BFS/DFS: Depende de la estructura del grafo

3. **Completitud**: ¿Siempre encuentra solución si existe?
   - Todos los implementados son completos en grafos finitos

## Archivos del Proyecto

```
├── Lab3IA.ipynb              # Notebook principal con implementación
├── funcion_de_costo.csv      # Grafo con costos entre actividades
├── heuristica.csv            # Valores heurísticos por actividad
└── README.md                 # Este archivo
```

## Requisitos

- Python 3.x
- Jupyter Notebook
- Bibliotecas estándar: `csv`

## Ejecución

1. Asegúrate de tener los archivos CSV en el mismo directorio
2. Abre `Lab3IA.ipynb` en Jupyter Notebook
3. Ejecuta todas las celdas en orden
4. Observa la comparación de resultados al final

## Trabajo Realizado

### Parte Manual ✓
- Resolución del problema con 2 algoritmos (1 no informado, 1 informado)
- Documentación de iteraciones y soluciones

### Parte en Código ✓
- ✅ Implementación de estructura `TreeNode`
- ✅ Implementación de colas FIFO, LIFO y PRIORITY
- ✅ Implementación de los 5 algoritmos de búsqueda
- ✅ Integración con funciones de costo y heurística
- ✅ Comparación de resultados

## Conclusiones

Este laboratorio demuestra:
- La importancia de elegir el algoritmo correcto según el problema
- El balance entre optimalidad y eficiencia computacional
- El impacto de las heurísticas en algoritmos informados
- La estructura general de algoritmos de búsqueda en IA

## Autor

Nicolás Concua  
Universidad del Valle de Guatemala  
Inteligencia Artificial - 7mo Semestre

## Referencias

- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.)
- Materiales del curso de Inteligencia Artificial, UVG
