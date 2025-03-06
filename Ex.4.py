class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_bairro(self, bairro):
        if bairro not in self.adjacencia:
            self.adjacencia[bairro] = []

    def adicionar_rua(self, bairro1, bairro2):
        self.adjacencia[bairro1].append(bairro2)
        self.adjacencia[bairro2].append(bairro1)

    def vizinhos(self, bairro):
        return self.adjacencia.get(bairro, [])

    def mostrar_grafo(self):
        for bairro, vizinhos in self.adjacencia.items():
            print(f"{bairro}: {', '.join(vizinhos)}")

cidade = Grafo()

bairros = ["Centro", "Bairro A", "Bairro B", "Bairro C", "Bairro D"]
for bairro in bairros:
    cidade.adicionar_bairro(bairro)

ruas = [("Centro", "Bairro A"), ("Centro", "Bairro B"), ("Bairro A", "Bairro C"), ("Bairro B", "Bairro C"), ("Bairro C", "Bairro D")]
for rua in ruas:
    cidade.adicionar_rua(*rua)

cidade.mostrar_grafo()

bairro_consultado = "Bairro C"
print(f"Vizinhos de {bairro_consultado}: {', '.join(cidade.vizinhos(bairro_consultado))}")
