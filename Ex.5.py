from collections import deque

class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_centro(self, centro):
        if centro not in self.adjacencia:
            self.adjacencia[centro] = []

    def adicionar_rota(self, centro1, centro2, peso):
        self.adjacencia[centro1].append((centro2, peso))
        self.adjacencia[centro2].append((centro1, peso))

    def vizinhos(self, centro):
        return self.adjacencia.get(centro, [])

    def mostrar_grafo(self):
        for centro, vizinhos in self.adjacencia.items():
            conexoes = ', '.join([f"{v}({p} min)" for v, p in vizinhos])
            print(f"{centro}: {conexoes}")

    def bfs_rota_mais_curta(self, inicio, destino):
        fila = deque([(inicio, [inicio])])
        visitados = set()

        while fila:
            atual, caminho = fila.popleft()
            if atual == destino:
                return caminho

            if atual not in visitados:
                visitados.add(atual)
                for vizinho, _ in self.adjacencia.get(atual, []):
                    if vizinho not in visitados:
                        fila.append((vizinho, caminho + [vizinho]))

        return None

empresa = Grafo()
centros = ["A", "B", "C", "D", "E"]
for centro in centros:
    empresa.adicionar_centro(centro)

rotas = [("A", "B", 10), ("A", "C", 15), ("B", "D", 12), ("C", "E", 20), ("D", "E", 5)]
for rota in rotas:
    empresa.adicionar_rota(*rota)

empresa.mostrar_grafo()

# 2 Exibir vizinhos de cada centro
for centro in centros:
    print(f"Vizinhos de {centro}: {', '.join([v for v, _ in empresa.vizinhos(centro)])}")

# 4 Encontrar a rota mais curta usando BFS
origem, destino = "A", "E"
rota = empresa.bfs_rota_mais_curta(origem, destino)
print(f"Rota mais curta entre {origem} e {destino}: {' -> '.join(rota)}")
