Algoritmos de Búsqueda en Grafos (BFS, DFS, UCS)

Este proyecto sencillo contiene implementaciones en Python de tres algoritmos
clásicos de búsqueda en grafos:

-   **BFS (Breadth-First Search) → Búsqueda en Anchura**\
-   **DFS (Depth-First Search) → Búsqueda en Profundidad**\
-   **UCS (Uniform Cost Search) → Búsqueda de Costos Uniformes**

Todos ellos permiten recorrer un grafo y encontrar un camino entre un
nodo **inicio** y un nodo **meta**.

------------------------------------------------------------------------

1. Búsqueda en Anchura (BFS)

### Idea principal

-   Recorre el grafo **nivel por nivel**.\
-   Utiliza una **cola (FIFO)**.\
-   Siempre expande primero los nodos más cercanos al inicio.\
-   Garantiza encontrar el **camino más corto en número de pasos** (si
    no hay pesos).

### Código básico

``` python
from collections import deque

def bfs(grafo, inicio, meta):
    visitados = set()
    cola = deque([[inicio]])  # caminos en la cola

    while cola:
        camino = cola.popleft()
        nodo = camino[-1]

        if nodo == meta:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo.get(nodo, []):
                nuevo_camino = list(camino)
                nuevo_camino.append(vecino)
                cola.append(nuevo_camino)
    return None
```

### Ejemplo

``` python
grafo = {
    'A': ['B', 'L'],
    'B': ['C', 'X'],
    'C': ['E'],
    'E': ['Z'],
    'L': ['O', 'Q'],
    'X': ['Y'],
    'Y': ['J'],
    'J': ['N', 'M'],
    'M': ['G'],
}
print("BFS:", bfs(grafo, 'A', 'G'))
```

**Salida esperada**:

    BFS: ['A', 'B', 'X', 'Y', 'J', 'M', 'G']

------------------------------------------------------------------------

2. Búsqueda en Profundidad (DFS)

### Idea principal

-   Recorre el grafo **tan profundo como sea posible** antes de
    retroceder.\
-   Utiliza una **pila (stack)** o recursión.\
-   No garantiza el camino más corto, pero es útil para explorar todos
    los nodos.

### Código básico (recursivo)

``` python
def dfs(grafo, inicio, meta, visitados=None, camino=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []

    visitados.add(inicio)
    camino.append(inicio)

    if inicio == meta:
        return camino

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            resultado = dfs(grafo, vecino, meta, visitados, camino)
            if resultado is not None:
                return resultado

    camino.pop()
    return None
```

### Ejemplo

``` python
print("DFS:", dfs(grafo, 'A', 'G'))
```

**Salida posible** (dependiendo del orden de los vecinos):

    DFS: ['A', 'B', 'X', 'Y', 'J', 'M', 'G']

------------------------------------------------------------------------

3. Búsqueda de Costos Uniformes (UCS)

### Idea principal

-   Recorre el grafo expandiendo siempre el **nodo con menor costo
    acumulado**.\
-   Utiliza una **cola de prioridad (heapq en Python)**.\
-   Garantiza encontrar el **camino de menor costo total** si los pesos
    son positivos.

### Código básico

``` python
import heapq

def ucs(grafo, inicio, meta):
    cola = [(0, inicio)]  # (costo, nodo)
    visitados = set()
    costo_acumulado = {inicio: 0}
    padre = {inicio: None}

    while cola:
        costo, nodo = heapq.heappop(cola)
        if nodo in visitados:
            continue
        visitados.add(nodo)

        if nodo == meta:
            break

        for vecino, costo_arista in grafo.get(nodo, []):
            nuevo_costo = costo + costo_arista
            if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                heapq.heappush(cola, (nuevo_costo, vecino))
                padre[vecino] = nodo

    return reconstruir_camino(padre, meta), costo_acumulado.get(meta, float('inf'))

def reconstruir_camino(padre, meta):
    camino = []
    while meta is not None:
        camino.append(meta)
        meta = padre.get(meta, None)
    return camino[::-1]
```

### Ejemplo

``` python
grafo_costos = {
    'A': [('B', 1), ('L', 1)],
    'B': [('C', 1), ('X', 1)],
    'C': [('E', 1)],
    'E': [('Z', 1)],
    'L': [('O', 1), ('Q', 1)],
    'X': [('Y', 1)],
    'Y': [('J', 1)],
    'J': [('N', 1), ('M', 1)],
    'M': [('G', 1)]
}
camino, costo = ucs(grafo_costos, 'A', 'G')
print("UCS:", camino, "Costo:", costo)
```

**Salida esperada**:

    UCS: ['A', 'B', 'X', 'Y', 'J', 'M', 'G'] Costo: 6

------------------------------------------------------------------------
