import heapq

def ucs(grafo, inicio, meta):
    cola = [(0, inicio)]   # (costo, nodo)
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
    return camino[::-1]  # invertir para obtener de inicio a meta


# Grafo con costo = 1 en cada arista
grafo_costo = {
    'A': [('B', 1), ('L', 1)],
    'B': [('C', 1), ('X', 1)],
    'C': [('E', 1)],
    'E': [('Z', 1)],
    'L': [('O', 1), ('Q', 1)],
    'O': [],
    'Q': [],
    'X': [('Y', 1)],
    'Y': [('J', 1)],
    'J': [('N', 1), ('M', 1)],
    'M': [('G', 1)],
    'N': [],
    'Z': [],
    'G': []
}

# Ejecutamos UCS desde A hasta G
camino, costo = ucs(grafo_costo, 'A', 'G')
print("UCS - Camino:", camino, "Costo:", costo)
