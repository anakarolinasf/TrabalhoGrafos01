# Lista das Unidades da Federação (vértices)
estados = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", 
    "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN", 
    "RO", "RR", "RS", "SC", "SE", "SP", "TO"
]

n = len(estados)

# 1. MATRIZ DE ADJACÊNCIA

# Matriz n x n inicializada com 0
matriz = [[0 for _ in range(n)] for _ in range(n)]

def adicionarFronteira(estado1, estado2):
    """Adiciona aresta não direcionada entre dois estados."""
    i = estados.index(estado1)
    j = estados.index(estado2)
    matriz[i][j] = 1
    matriz[j][i] = 1

def removerFronteira(estado1, estado2):
    """Remove aresta entre dois estados."""
    i = estados.index(estado1)
    j = estados.index(estado2)
    matriz[i][j] = 0
    matriz[j][i] = 0

# Arestas do grafo (fronteiras entre estados)
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

# Preenchendo matriz de adjacência
for u, v in arestas:
    adicionarFronteira(u, v)

# Impressão da matriz
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

# Matriz n x m
matriz_inc = [[0 for _ in range(m)] for _ in range(n)]

for e in range(m):
    u, v = arestas[e]
    i = estados.index(u)
    j = estados.index(v)
    matriz_inc[i][e] = 1
    matriz_inc[j][e] = 1


# 3. LISTA INDEXADA (α e β)

# Lista auxiliar de adjacência
lista_temp = {uf: [] for uf in estados}

for u, v in arestas:
    lista_temp[u].append(v)
    lista_temp[v].append(u)

for uf in estados:
    lista_temp[uf].sort()

# Vetores α e β
alpha = [0] * (n + 1)
beta = []

pos = 0
for i in range(n):
    alpha[i] = pos
    beta.extend(lista_temp[estados[i]])
    pos += len(lista_temp[estados[i]])

alpha[n] = pos

# Impressão da lista indexada
print("LISTA INDEXADA (α e β)\n")

print("α (início dos vizinhos):")
for i in range(n):
    print(f"{estados[i]} -> β[{alpha[i]}]")

print("\nβ (vizinhos sequenciais):")
for i in range(len(beta)):
    print(f"β[{i}] = {beta[i]}")

# FUNÇÃO GERAL DE ANÁLISE

def analisar_grafo(nome, calcular_grau, obter_vizinhos):
    print(f"\n{'='*60}")
    print(f"ANÁLISE USANDO {nome}")
    print(f"{'='*60}\n")

    graus = []
    vizinhos_dict = {}

    for i in range(n):
        uf = estados[i]
        grau = calcular_grau(i)
        graus.append((grau, uf))
        vizinhos_dict[uf] = obter_vizinhos(i)

    max_grau = max(g for g, _ in graus)
    min_grau = min(g for g, _ in graus)

    uf_max = [uf for g, uf in graus if g == max_grau]
    uf_min = [uf for g, uf in graus if g == min_grau]

    print(f"• Maior Grau: {max_grau}")
    for uf in uf_max:
        print(f"  {uf} -> {', '.join(vizinhos_dict[uf])}")

    print(f"\n• Menor Grau: {min_grau}")
    for uf in uf_min:
        print(f"  {uf} -> {', '.join(vizinhos_dict[uf])}")

    # Histograma de frequência
    print("\n- Histograma:")
    freq = {}
    for g, _ in graus:
        freq[g] = freq.get(g, 0) + 1

    for g in sorted(freq.keys()):
        print(f"  Grau {g:2d} | {'|' * freq[g]} ({freq[g]})")

# ANÁLISES

# Matriz de Adjacência
def grau_matriz_adj(i):
    return sum(matriz[i])

def vizinhos_matriz_adj(i):
    return [estados[j] for j in range(n) if matriz[i][j] == 1]

analisar_grafo("MATRIZ DE ADJACÊNCIA", grau_matriz_adj, vizinhos_matriz_adj)

# Matriz de Incidência
def grau_matriz_inc(i):
    return sum(matriz_inc[i])

def vizinhos_matriz_inc(i):
    vizinhos = []
    for e in range(m):
        if matriz_inc[i][e] == 1:
            u, v = arestas[e]
            vizinhos.append(v if estados[i] == u else u)
    return sorted(vizinhos)

analisar_grafo("MATRIZ DE INCIDÊNCIA", grau_matriz_inc, vizinhos_matriz_inc)

# Lista Indexada
def grau_lista_indexada(i):
    return alpha[i+1] - alpha[i]

def vizinhos_lista_indexada(i):
    return beta[alpha[i]:alpha[i+1]]

analisar_grafo("LISTA INDEXADA (α e β)", grau_lista_indexada, vizinhos_lista_indexada)