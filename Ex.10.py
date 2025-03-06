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

def dfs(grafo, inicio, visitados=None, ordem_visita=None):
    if visitados is None:
        visitados = set()
    if ordem_visita is None:
        ordem_visita = []

    if inicio not in visitados:
        visitados.add(inicio)
        ordem_visita.append(inicio)
        for vizinho in grafo[inicio]:
            dfs(grafo, vizinho, visitados, ordem_visita)

    return ordem_visita

grafo = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [6],
    5: [6],
    6: []
}

resultado_bfs = bfs(grafo, 1)
resultado_dfs = dfs(grafo, 1)

print("Ordem dos vértices visitados pela BFS:", resultado_bfs)
print("Ordem dos vértices visitados pela DFS:", resultado_dfs)
