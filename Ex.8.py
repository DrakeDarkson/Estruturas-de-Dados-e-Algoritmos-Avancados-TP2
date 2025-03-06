def adiciona_transacao(grafo, origem, destino):
    if origem not in grafo:
        grafo[origem] = []
    grafo[origem].append(destino)

def detecta_ciclo(grafo):
    visitados = set()
    pilha_recursao = set()

    def dfs(conta):
        if conta in pilha_recursao:
            return True
        if conta in visitados:
            return False
        
        visitados.add(conta)
        pilha_recursao.add(conta)

        for vizinho in grafo.get(conta, []):
            if dfs(vizinho):
                return True

        pilha_recursao.remove(conta)
        return False

    for conta in grafo:
        if conta not in visitados:
            if dfs(conta):
                return True
    return False

grafo_transacoes = {}
adiciona_transacao(grafo_transacoes, "A", "B")
adiciona_transacao(grafo_transacoes, "B", "C")
adiciona_transacao(grafo_transacoes, "C", "D")
adiciona_transacao(grafo_transacoes, "D", "A")

if detecta_ciclo(grafo_transacoes):
    print("Ciclo suspeito detectado!")
else:
    print("Nenhum ciclo detectado.")
