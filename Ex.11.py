def dfs(grafo, vertice, visitados=None, ordem_visita=None):
    if visitados is None:
        visitados = set()
    if ordem_visita is None:
        ordem_visita = []

    if vertice not in visitados:
        visitados.add(vertice)
        ordem_visita.append(vertice)
        for vizinho in grafo[vertice]:
            dfs(grafo, vizinho, visitados, ordem_visita)

    return ordem_visita

grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

resultado_dfs = dfs(grafo, 'A')

print("Ordem dos vértices visitados pela DFS:", resultado_dfs)
