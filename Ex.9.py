from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    ordem_visita = []

    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            visitados.add(vertice)
            ordem_visita.append(vertice)
            fila.extend(grafo[vertice]) 

    return ordem_visita

grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

resultado = bfs(grafo, 'A')
print("Ordem dos vértices visitados pela BFS:", resultado)
