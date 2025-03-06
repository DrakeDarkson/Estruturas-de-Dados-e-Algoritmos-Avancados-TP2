class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_bairro(self, bairro):
        if bairro not in self.adjacencia:
            self.adjacencia[bairro] = []

    def adicionar_rua(self, bairro1, bairro2):
        self.adjacencia[bairro1].append(bairro2)
        self.adjacencia[bairro2].append(bairro1)

    def mostrar_grafo(self):
        for bairro, vizinhos in self.adjacencia.items():
            print(f"{bairro}: {', '.join(vizinhos)}")

cidade = Grafo()

bairros = ["A", "B", "C", "D", "E", "F"]
for bairro in bairros:
    cidade.adicionar_bairro(bairro)

ruas = [("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"), ("C", "E"), ("D", "F"), ("E", "F")]
for rua in ruas:
    cidade.adicionar_rua(*rua)

cidade.mostrar_grafo()
