def dfs(grafo, inicio, meta, visitados=None, camino=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []

    visitados.add(inicio)
    camino.append(inicio)

    if inicio == meta:
        return camino  # Camino encontrado

    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            resultado = dfs(grafo, vecino, meta, visitados, camino)
            if resultado is not None:
                return resultado

    camino.pop()  # retrocede si no encuentra meta en este camino
    return None


# Grafo (sin costos, solo vecinos)
grafo = {
    'A': ['B', 'L'],
    'B': ['C', 'X'],
    'C': ['E'],
    'E': ['Z'],
    'L': ['O', 'Q'],
    'O': [],
    'Q': [],
    'X': ['Y'],
    'Y': ['J'],
    'J': ['N', 'M'],
    'M': ['G'],
    'N': [],
    'Z': [],
    'G': []
}

# Ejecutamos DFS desde A hasta G
camino = dfs(grafo, 'A', 'G')
print("DFS - Camino:", camino)
