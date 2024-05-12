import random

def tablica_krawedzi(n, m_sas):
    tab_kraw=[]
    for i in range(n):
        for j in range(n):
            if m_sas[i][j]=='1':
                tab_kraw.append([i+1,j+1])
    print("tablica krawędzi: ")
    print("  out | in ")
    for i in range(len(tab_kraw)):
        print(f"{chr(ord('a')+i)}: {tab_kraw[i][0]}  |  {tab_kraw[i][1]}")
    return tab_kraw

def macierz_nasycona(n, nas):
    matrix = ['0'] * n
    len_list = (n * n - n) // 2
    half = len_list * nas // 100
    other_half = len_list - half
    if len_list % 2 == 1:
        lista = ['0'] * other_half + ['1'] * half + ['0']
    else:
        lista = ['0'] * other_half + ['1'] * half
    random.shuffle(lista)
    a = 0
    for i in range(n):
        matrix[i] = ['0'] * (i + 1)
        for j in range(n - i - 1):
            matrix[i].append(lista[a])
            a += 1
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == '1':
                matrix[j][i] = '1'

    return matrix
    
def matrix_to_adj_list(matrix):
    adj_list = {}
    for i in range(len(matrix)):
        adj_list[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == '1':
                adj_list[i].append(j)
    return adj_list

def DFS_Euler(graph, v, stack):
    for u in graph[v]:
        graph[v].remove(u)
        graph[u].remove(v)
        DFS_Euler(graph, u, stack)
    stack.append(v)

#hamilton 
def is_valid(v, pos, path, graph):
    if v not in graph[path[pos - 1]]: # Sprawdź, czy można dodać wierzchołek v do ścieżki
        return False
    if v in path:   # Sprawdź, czy wierzchołek v nie jest już w ścieżce
        return False
    return True

def hamilton_cycle_util(graph, path, pos):
    if pos == len(graph): # Warunek końca rekurencji: jeśli wszystkie wierzchołki są w ścieżce
        if path[pos - 1] in graph[path[0]]: # Sprawdź, czy istnieje krawędź między ostatnim wierzchołkiem a pierwszym
            return True
        else:
            return False
    for v in graph.keys(): # Testuj dla każdego wierzchołka
        if is_valid(v, pos, path, graph):
            path[pos] = v
            if hamilton_cycle_util(graph, path, pos + 1): # Rekurencyjnie wywołaj się dla następnego wierzchołka
                return True
            path[pos] = -1 # Jeśli dodanie wierzchołka v nie prowadzi do rozwiązania, usuń go z ścieżki
    return False

def hamilton_cycle(graph):
    path = [-1] * len(graph)  # Inicjalizuj ścieżkę jako pustą listę
    path[0] = next(iter(graph.keys())) # Wybierz pierwszy wierzchołek jako startowy
    if not hamilton_cycle_util(graph, path, 1): # Rozpocznij rekurencję od drugiego wierzchołka
        print("Nie istnieje cykl Hamiltona w tym grafie")
        return False
    print("Cykl Hamiltona:", path)
    return True

def has_hamiltonian_cycle(graph):
    n = len(graph)
    for i in range(n):
        if sum(graph[i]) != 2 or graph[i][i] == 1:
            return False
    return True

def find_hamiltonian_cycle(graph):
    n = len(graph)
    visited = [False] * n
    cycle = []

    def dfs(node):
        cycle.append(node)
        visited[node] = True
        for neighbor, connected in enumerate(graph[node]):
            if connected and not visited[neighbor]:
                dfs(neighbor)

    dfs(0)
    return cycle

def convert_to_hamiltonian_cycle(graph):
    if has_hamiltonian_cycle(graph):
        return graph
    else:
        cycle = find_hamiltonian_cycle(graph)
        for i in range(len(cycle) - 1):
            graph[cycle[i]][cycle[i + 1]] = 1
            graph[cycle[i + 1]][cycle[i]] = 1
        graph[cycle[-1]][cycle[0]] = 1
        graph[cycle[0]][cycle[-1]] = 1
        return graph

n = int(input('Poddaj ilość wierzchołków: ')) # ilość wierzchołków
m = int(input('Podaj nasycenie gdzie należy ono do przedziału liczb naturalnych [0;100]: ')) # nasycenie [0;100], N
matrix = macierz_nasycona(n,m)
t_kraw = tablica_krawedzi(n, matrix)
l_sas=matrix_to_adj_list(matrix)


#rzeczy do eulera
ost = []
poczatek = 0
DFS_Euler(l_sas, poczatek, ost)
print("Cykl Eulera:", ost[::-1])


#hamilton
graph = matrix
for i in range(n):
    for j in range(n):
        graph[i][j] = int(graph[i][j])
hamiltonian_graph = convert_to_hamiltonian_cycle(graph)
for i in range(n):
    for j in range(n):
        graph[i][j] = str(graph[i][j])

hamilton_cycle(graph)

matrix_bez_cyklu = graph
for i in range(n):
    matrix_bez_cyklu[0][i] = '0'
    matrix_bez_cyklu[i][0] = '0'
