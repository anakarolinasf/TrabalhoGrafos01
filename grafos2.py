# VÉRTICES (ESTADOS)
estados = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA",
    "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN",
    "RO", "RR", "RS", "SC", "SE", "SP", "TO"
]

n = len(estados)

# ARESTAS (FRONTEIRAS)
arestas = [
    ("AC","AM"),("AC","RO"),
    ("AL","BA"),("AL","PE"),("AL","SE"),
    ("AM","MT"),("AM","PA"),("AM","RO"),("AM","RR"),
    ("AP","PA"),
    ("BA","ES"),("BA","GO"),("BA","MG"),("BA","PE"),
    ("BA","PI"),("BA","SE"),("BA","TO"),
    ("CE","PB"),("CE","PE"),("CE","PI"),("CE","RN"),
    ("DF","GO"),("DF","MG"),
    ("ES","MG"),("ES","RJ"),
    ("GO","MG"),("GO","MS"),("GO","MT"),("GO","TO"),
    ("MA","PA"),("MA","PI"),("MA","TO"),
    ("MG","MS"),("MG","RJ"),("MG","SP"),
    ("MS","MT"),("MS","PR"),("MS","SP"),
    ("MT","PA"),("MT","RO"),("MT","TO"),
    ("PA","RR"),("PA","TO"),
    ("PB","PE"),("PB","RN"),
    ("PE","PI"),
    ("PI","TO"),
    ("PR","SC"),("PR","SP"),
    ("RJ","SP"),
    ("RS","SC")
]

# 3) MATRIZ DE ADJACÊNCIA

matriz = [[0 for _ in range(n)] for _ in range(n)]

def adicionarFronteira(estado1, estado2):
    i = estados.index(estado1)
    j = estados.index(estado2)
    matriz[i][j] = 1
    matriz[j][i] = 1

for u, v in arestas:
    adicionarFronteira(u, v)

print("\n" + "="*70)
print("3) MATRIZ DE ADJACÊNCIA")
print("="*70)

print("     ", end="")
for estado in estados:
    print(f"{estado:>4}", end="")
print()

for i in range(n):
    print(f"{estados[i]:>4} |", end="")
    for j in range(n):
        print(f"{matriz[i][j]:>4}", end="")
    print()

# 4) MATRIZ DE INCIDÊNCIA

m = len(arestas)
matriz_inc = [[0 for _ in range(m)] for _ in range(n)]

for e in range(m):
    u, v = arestas[e]
    i = estados.index(u)
    j = estados.index(v)
    matriz_inc[i][e] = 1
    matriz_inc[j][e] = 1

print("\n" + "="*70)
print("4) MATRIZ DE INCIDÊNCIA")
print("="*70)

print("\nArestas numeradas:")
for i, (u, v) in enumerate(arestas):
    print(f"E{i:02d} = ({u}, {v})")

print("\nTabela da Matriz de Incidência:\n")

print("      ", end="")
for e in range(m):
    print(f"{e:>3}", end="")
print()

for i in range(n):
    print(f"{estados[i]:>4} |", end="")
    for e in range(m):
        print(f"{matriz_inc[i][e]:>3}", end="")
    print()

#  LISTA INDEXADA (REPRESENTAÇÃO α e β)

lista_temp = {uf: [] for uf in estados}

for u, v in arestas:
    lista_temp[u].append(v)
    lista_temp[v].append(u)

for uf in estados:
    lista_temp[uf].sort()

alpha = [0] * (n + 1)
beta = []

pos = 0
for i in range(n):
    alpha[i] = pos
    beta.extend(lista_temp[estados[i]])
    pos += len(lista_temp[estados[i]])

alpha[n] = pos

print("\n" + "="*70)
print("5) LISTA INDEXADA (α e β)")
print("="*70)

print("\nVetor α (início dos vizinhos):")
for i in range(n):
    print(f"{estados[i]} começa em β[{alpha[i]}]")

print("\nVetor β (vizinhos sequenciais):")
for i in range(len(beta)):
    print(f"β[{i:02d}] = {beta[i]}")

# ANÁLISE DOS GRAUS

def analisar_grafo(nome, calcular_grau, obter_vizinhos):

    print("\n" + "="*70)
    print(f"ANÁLISE - {nome}")
    print("="*70)

    graus = []
    vizinhos_dict = {}

    for i in range(n):
        uf = estados[i]
        grau = calcular_grau(i)
        graus.append((grau, uf))
        vizinhos_dict[uf] = obter_vizinhos(i)

    max_grau = max(g for g, _ in graus)
    min_grau = min(g for g, _ in graus)

    print(f"\nMaior Grau: {max_grau}")
    for g, uf in graus:
        if g == max_grau:
            print(f"{uf} -> {', '.join(vizinhos_dict[uf])}")

    print(f"\nMenor Grau: {min_grau}")
    for g, uf in graus:
        if g == min_grau:
            print(f"{uf} -> {', '.join(vizinhos_dict[uf])}")

    print("\nHistograma:")
    freq = {}
    for g, _ in graus:
        freq[g] = freq.get(g, 0) + 1

    for g in sorted(freq.keys()):
        print(f"Grau {g:2d} | {'|' * freq[g]} ({freq[g]})")


#  Análise final 

def grau_matriz_adj(i):
    return sum(matriz[i])

def vizinhos_matriz_adj(i):
    return [estados[j] for j in range(n) if matriz[i][j] == 1]

analisar_grafo("GRAFO DOS ESTADOS DO BRASIL", grau_matriz_adj, vizinhos_matriz_adj)