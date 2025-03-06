from collections import deque

def bfs_caminho_curto(grafo, inicio, destino):
    fila = deque([(inicio, [inicio])])
    visitados = set()

    while fila:
        vertice, caminho = fila.popleft()
        
        if vertice == destino:
            return caminho
        
        if vertice not in visitados:
            visitados.add(vertice)
            for vizinho in grafo[vertice]:
                if vizinho not in visitados:
                    fila.append((vizinho, caminho + [vizinho]))

    return None

grafo_cidade = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

caminho_minimo = bfs_caminho_curto(grafo_cidade, 'A', 'F')

print("Caminho mais curto de A para F:", caminho_minimo)
