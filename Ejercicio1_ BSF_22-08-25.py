# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 09:00:31 2025
@author: camic
"""

from collections import deque  # Importa deque para usar una cola eficiente

# -------- BFS: Encuentra el camino más corto --------
def bfs_shortest_path(graph, start, goal):
    visited = set()              # Conjunto para marcar nodos visitados
    queue = deque([[start]])     # Cola con listas de caminos
    
    if start == goal:            # Caso trivial: inicio = fin
        return [start]

    while queue:                 # Mientras haya caminos en la cola
        path = queue.popleft()   # Saca el primer camino
        node = path[-1]          # Último nodo del camino actual

        if node not in visited:  # Solo procesar nodos no visitados
            neighbors = graph.get(node, [])  # Obtener vecinos
            
            for neighbor in neighbors:       # Recorrer vecinos
                new_path = list(path)        # Copiar camino actual
                new_path.append(neighbor)    # Agregar vecino al camino
                queue.append(new_path)       # Encolar nuevo camino
                
                if neighbor == goal:         # Si llegamos al objetivo
                    return new_path

            visited.add(node)  # Marcar como visitado

    return None  # Si no hay camino

# -------- DFS: Encuentra todos los caminos --------
def dfs_all_paths(graph, start, goal, path=None):
    if path is None:       
        path = []          # Inicializar camino vacío
    
    path = path + [start]  # Agregar nodo actual al camino

    if start == goal:      
        return [path]      # Si llegamos, devolver camino completo

    if start not in graph: 
        return []          # Si no hay vecinos, devolver vacío

    paths = []  
    for neighbor in graph[start]:           # Recorrer vecinos
        if neighbor not in path:            # Evitar ciclos
            new_paths = dfs_all_paths(graph, neighbor, goal, path)
            for p in new_paths:
                paths.append(p)             # Agregar todos los caminos encontrados

    return paths

# -------- Grafo de la imagen --------
graph = {
    'A': ['B', 'L'],
    'B': ['C', 'X'],
    'C': ['E'],
    'E': ['Z'],
    'L': ['O','Q'],
    'X': ['Y'],
    'Y': ['J'],
    'J': ['N', 'M'],
    'M': ['G']
}

# Nodos inicial y final
start_node = 'A'
end_node = 'G'

# Obtener caminos
shortest = bfs_shortest_path(graph, start_node, end_node)  # Camino más corto (BFS)

print("Camino más corto:", shortest)
print("Todos los caminos:", all_paths)

