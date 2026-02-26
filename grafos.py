estados = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", 
    "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", 
    "RO", "RR", "RS", "SC", "SE", "SP", "TO"
]
n = len(estados)

matriz = [[0 for _ in range(n)] for _ in range(n)]

#Funções criadas por você nas imagens
def adicionarFronteira(estado1, estado2):
    i = estados.index(estado1)
    j = estados.index(estado2)
    matriz[i][j] = 1
    matriz[j][i] = 1

def removerFronteira(estado1, estado2):
    i = estados.index(estado1)
    j = estados.index(estado2)
    matriz[i][j] = 0
    matriz[j][i] = 0

# Arestas (fronteiras do Brasil)
arestas = [
    ("AC", "AM"), ("AC", "RO"),
    ("AL", "BA"), ("AL", "PE"), ("AL", "SE"),
    ("AM", "MT"), ("AM", "PA"), ("AM", "RO"), ("AM", "RR"),
    ("AP", "PA"),
    ("BA", "ES"), ("BA", "GO"), ("BA", "MG"), ("BA", "PE"), ("BA", "PI"), ("BA", "SE"), ("BA", "TO"),
    ("CE", "PB"), ("CE", "PE"), ("CE", "PI"), ("CE", "RN"),
    ("DF", "GO"), ("DF", "MG"),
    ("ES", "MG"), ("ES", "RJ"),
    ("GO", "MG"), ("GO", "MS"), ("GO", "MT"), ("GO", "TO"),
    ("MA", "PA"), ("MA", "PI"), ("MA", "TO"),
    ("MG", "MS"), ("MG", "RJ"), ("MG", "SP"),
    ("MS", "MT"), ("MS", "PR"), ("MS", "SP"),
    ("MT", "PA"), ("MT", "RO"), ("MT", "TO"),
    ("PA", "RR"), ("PA", "TO"),
    ("PB", "PE"), ("PB", "RN"),
    ("PE", "PI"),
    ("PI", "TO"),
    ("PR", "SC"), ("PR", "SP"),
    ("RJ", "SP"),
    ("RS", "SC")
]

# 1. MATRIZ DE ADJACÊNCIA (Preenchendo usando a sua função)
for u, v in arestas:
    adicionarFronteira(u, v)

# Imprimindo a matriz de adjacência com a sua formatação
print("MATRIZ DE ADJACÊNCIA\n")
print("    ", end="")
for estado in estados:
    print(f"{estado:>4}", end="")
print()

for i in range(n):
    print(f"{estados[i]:>4}", end="")
    for j in range(n):
        print(f"{matriz[i][j]:>4}", end="")
    print()

print("\n" + "="*60 + "\n")

# 2. MATRIZ DE INCIDÊNCIA
m = len(arestas)
matriz_inc = [[0 for _ in range(m)] for _ in range(n)]

for e in range(m):
    u, v = arestas[e]
    i = estados.index(u)
    j = estados.index(v)
    matriz_inc[i][e] = 1
    matriz_inc[j][e] = 1

# 3. LISTA INDEXADA (Lista de Adjacência)
lista_adj = {uf: [] for uf in estados}
for u, v in arestas:
    lista_adj[u].append(v)
    lista_adj[v].append(u)
    
for uf in estados:
    lista_adj[uf].sort()

# c) Algoritmos de Análise (Graus, Vizinhos e Histograma)

graus = []
vizinhos_dict = {}

# Calculando os graus baseando-se na sua matriz de adjacência
for i in range(n):
    grau = sum(matriz[i]) # A soma da linha dá o grau do vértice
    uf = estados[i]
    graus.append((grau, uf))
    
    # Pegando quem são os vizinhos
    vizinhos = [estados[j] for j in range(n) if matriz[i][j] == 1]
    vizinhos_dict[uf] = vizinhos

# Identificando máximos e mínimos
max_grau = max(g for g, _ in graus)
min_grau = min(g for g, _ in graus)

uf_max = [uf for g, uf in graus if g == max_grau]
uf_min = [uf for g, uf in graus if g == min_grau]

print("ANÁLISE DE VIZINHOS (GRAUS)\n")

print(f"• Maior Grau: {max_grau}")
for uf in uf_max:
    print(f"  {uf} -> Vizinhos: {', '.join(vizinhos_dict[uf])}")
    
print(f"\n• Menor Grau: {min_grau}")
for uf in uf_min:
    print(f"  {uf} -> Vizinhos: {', '.join(vizinhos_dict[uf])}")

# Criando o Histograma de frequências
print("\n• Histograma de Frequência dos Graus:")
freq = {}
for g, _ in graus:
    freq[g] = freq.get(g, 0) + 1
    
for g in sorted(freq.keys()):
    barra = '█' * freq[g]
    print(f"  Grau {g:2d} | {barra} ({freq[g]})")