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


def has_hamiltonian_cycle(graph):
    n = len(graph)
    for i in range(n):
        if sum(graph[i]) % 2 != 0 or graph[i][i] == 1:
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

def Hamiltonian_path(adj, N):
    dp = [[False for i in range(1 << N)]
          for j in range(N)]
    for i in range(N):
        dp[i][1 << i] = True
    for i in range(1 << N):
        for j in range(N):
            if ((i & (1 << j)) != 0):
                for k in range(N):
                    if ((i & (1 << k)) != 0 and
                            adj[k][j] == 1 and
                            j != k and
                            dp[k][i ^ (1 << j)]):
                        dp[j][i] = True
                        break
    for i in range(N):
        if (dp[i][(1 << N) - 1]):
            return True
            
n = int(input('Poddaj ilość wierzchołków: ')) # ilość wierzchołków
m = int(input('Podaj nasycenie gdzie należy ono do przedziału liczb naturalnych [0;100]: ')) # nasycenie [0;100], N
matrix = macierz_nasycona(n,m)
t_kraw = tablica_krawedzi(n, matrix)
l_sas=matrix_to_adj_list(matrix)

graph = matrix
for i in range(n):
    for j in range(n):
        graph[i][j] = int(graph[i][j])
hamiltonian_graph = convert_to_hamiltonian_cycle(graph)
for i in range(n):
    for j in range(n):
        graph[i][j] = str(graph[i][j])

matrix_bez_cyklu = graph
for i in range(n):
    matrix_bez_cyklu[0][i] = '0'
    matrix_bez_cyklu[i][0] = '0'

m = -1
while (m!=0):
    print('Proszę wpisać numer znajdujący się przy zadaniu, które chcesz aby wykonał program.')
    print('0 : Zakończenie działania programu')
    print('1 : Euler')
    print('2 : Hamilton')
    m = int(input())
    if m == 1:
        #rzeczy do eulera
        ost = []
        poczatek = 0
        DFS_Euler(l_sas, poczatek, ost)
        print("Cykl Eulera:", ost[::-1])
    elif m == 2:
        Hamiltonian_path(hamiltonian_graph,n)
        






