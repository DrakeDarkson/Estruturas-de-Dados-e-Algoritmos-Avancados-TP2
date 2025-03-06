grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

def buscar_vizinhos(cidade):
    return grafo.get(cidade, [])

for cidade in grafo:
    print(f"{cidade}: {buscar_vizinhos(cidade)}")
