import time
import random

num_vertices = 1000
edges = [(random.randint(0, num_vertices - 1), random.randint(0, num_vertices - 1)) for _ in range(10)]

lista_adj = {i: [] for i in range(num_vertices)}
for u, v in edges:
    lista_adj[u].append(v)
    lista_adj[v].append(u)

matriz_adj = [[0] * num_vertices for _ in range(num_vertices)]
for u, v in edges:
    matriz_adj[u][v] = 1
    matriz_adj[v][u] = 1

def medir_tempo(funcao, *args, repeticoes=10000):
    inicio = time.perf_counter()
    for _ in range(repeticoes):
        funcao(*args)
    return (time.perf_counter() - inicio) / repeticoes

def buscar_vizinhos_lista(vertice):
    return lista_adj[vertice]

def buscar_vizinhos_matriz(vertice):
    return [i for i in range(num_vertices) if matriz_adj[vertice][i] == 1]

def verificar_aresta_lista(u, v):
    return v in lista_adj[u]

def verificar_aresta_matriz(u, v):
    return matriz_adj[u][v] == 1

vertice_teste = random.randint(0, num_vertices - 1)
u_teste, v_teste = random.choice(edges)

tempo_lista_vizinhos = medir_tempo(buscar_vizinhos_lista, vertice_teste)
tempo_matriz_vizinhos = medir_tempo(buscar_vizinhos_matriz, vertice_teste)
tempo_lista_aresta = medir_tempo(verificar_aresta_lista, u_teste, v_teste)
tempo_matriz_aresta = medir_tempo(verificar_aresta_matriz, u_teste, v_teste)

print(f"Tempo médio para buscar vizinhos (Lista de Adjacência): {tempo_lista_vizinhos:.10f} segundos")
print(f"Tempo médio para buscar vizinhos (Matriz de Adjacência): {tempo_matriz_vizinhos:.10f} segundos")
print(f"Tempo médio para verificar aresta (Lista de Adjacência): {tempo_lista_aresta:.10f} segundos")
print(f"Tempo médio para verificar aresta (Matriz de Adjacência): {tempo_matriz_aresta:.10f} segundos")
