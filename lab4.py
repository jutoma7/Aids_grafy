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

def macierz_nasycona(n, nasyc):
    matrix = ['0'] * n
    len_list = n * n
    rest = (100 - nasyc) * len_list // 100
    nas = nasyc * len_list // 100
    lista = ['0'] * rest + ['1'] * nas 
    random.shuffle(lista)
    lista = lista + ['0'] * 10
    a = 0
    for i in range(n):
        matrix[i] = []
        for j in range(n):
            matrix[i].append(lista[a])
            a += 1
    for i in range(n):
        matrix[i][i] = '0'
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
hamilton_cycle(graph)

