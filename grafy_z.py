import random


def macierz_sasiedztwa(n):
    m_sas = []
    print("podaj kolejne wiersze macierzy sąsiedztwa:")
    for i in range(n):
        m = input().split()
        m_sas.append(m)
    print("macierz sąsiedztwa: ")
    print(end="   ")
    for i in range(n):
        print(f"{i + 1}:", end=" ")
    print()
    for i in range(n):
        print(f"{i + 1}:", end=" ")
        for j in range(n):
            print(m_sas[i][j], end="  ")
        print()
    return m_sas


def m_sasiedztwa_los(n):
    m_sas_los = []
    for i in range(n):
        lista = []
        for j in range(i + 1):
            lista.append('0')
        for j in range(n - (i + 1)):
            lista.append(str(random.randint(0, 1)))
        m_sas_los.append(lista)
    return m_sas_los


def lista_sasiadow(n):
    l_sas = {}
    for i in range(n):
        sasiedzi = []
        for j in range(n):
            if m_sas[i][j] == '1':
                sasiedzi.append(j + 1)
        l_sas[f"{i + 1}"] = sasiedzi
    print("lista sąsiadów:")
    for key, value in l_sas.items():
        print(key, ":", value)
    return l_sas


def tablica_krawedzi(n):
    tab_kraw = []
    for i in range(n):
        for j in range(n):
            if m_sas[i][j] == '1':
                tab_kraw.append((i + 1, j + 1))
    print("tablica krawędzi: ")
    print("  out | in ")
    for i in range(len(tab_kraw)):
        print(f"{chr(ord('a') + i)}: {tab_kraw[i][0]}  |  {tab_kraw[i][1]}")
    return tab_kraw


def DFS(visited, tab_kraw, current):
    if current not in visited:
        visited.append(current)
        print(current)
    for line in tab_kraw:
        if line[0] == current and line[1] not in visited:
            DFS(visited, tab_kraw, line[1])
        if line[0] not in visited:
            DFS(visited, tab_kraw, line[0])


def tarjan_topological_sort_matrix(matrix):
    def tarjan(u, graph, visited, stack):
        visited[u] = True
        for v in range(len(graph)):
            if matrix[u][v] == 1 and not visited[v]:
                tarjan(v, graph, visited, stack)
        stack.append(u)

    n = len(matrix)
    visited = [False] * n
    stack = []
    for i in range(n):
        if not visited[i]:
            tarjan(i, matrix, visited, stack)
    return stack


def topological_sort_tarjan_l_sas(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph.keys():
        if node not in visited:
            dfs(node)
    ost = []
    for i in stack:
        if type(i) == str:
            ost.append(i)
    return ost


def tarjan_topological_sort_edges(edge_list):
    graph = {}
    for u, v in edge_list:
        if u not in graph:
            graph[u] = []
        graph[u].append(v)
        if v not in graph:
            graph[v] = []
    sorted(graph)
    print(graph)
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph.keys():
        if node not in visited:
            dfs(node)
    return stack[::-1]


def in_degree_tab_kraw(n):  # tablica in degree od tablicy krawedzi do kahna
    tab_in = {}

    for i in range(n):
        tab_in[i + 1] = []
    for line in tab_kraw:
        tab_in[line[1]].append(line[0])
    return tab_in

def in_degree_lista_sasiadow(l_sas): # tablica in degree od listy sasiadow do kahna
    in_degree = {}
    for i in range(1, n + 1):
        in_degree[i] = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j in l_sas[str(i)]:
                in_degree[j].append(int(i))
    return in_degree

def in_degree_matrix(mat): # tablica in degree od macierzy sasiadow do kahna
    in_degree={}
    for i in range(len(mat)):
        in_degree[i+1]=[]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]=='1':
                in_degree[j + 1].append(i + 1)
    return in_degree

def kahns_topological_sort_lista_sasiadow(in_degree): #ogólna funkcja do sortowania Kahna
    kontrolna=[]
    if not in_degree:
        return
    for item in list(in_degree.keys()):
        if in_degree[item] == []:
            print(item)
            kontrolna.append(item)
            del in_degree[item]
            for key, value in in_degree.items():
                if item in value:
                    value.remove(item)
    kahns_topological_sort_lista_sasiadow(in_degree)




n = int(input("podaj liczbę wierzchołków grafu: "))
print("0 - macierz sąsiedztwa")
print("1 - losowa macierz sąsiedztwa")
print("2 - lista sąsiadów")
print("3 - tablica krawędzi")
print("4 - przeszukiwanie w głąb")
print("5 - sortwanie topologiczne metodą Tarjana - macierz sąsiedztwa")
print("6 - sortowanie topologiczne metodą Tarjana - lista sąsiadów")
print("7 - sortwanie topologiczne metodą Tarjana - tablica krawędzi")
print("8 - sortowanie topologiczne metodą Kahna - tablica krawędzi")
print("-1 - koniec")
m = int(input("podaj, które z powyższych działań chcesz wykonać:"))

while m >= 0:
    
    if m == 0:
        m_sas = macierz_sasiedztwa(n)
        print(m_sas)
        
    if m == 1:
        m_sas_los = m_sasiedztwa_los(n)
        print("losowa macierz sasiedztwa:")
        print(end="  ")
        for i in range(n):
            print(f"{i + 1}:", end=" ")
        print()
        for i in range(n):
            print(f"{i + 1}:", end=" ")
            for j in range(n):
                print(m_sas_los[i][j], end="  ")
            print()
            
    if m == 2:
        l_sas = {}
        l_sas = lista_sasiadow(n)
        
    if m == 3:
        tab_kraw = tablica_krawedzi(n)
        print(tab_kraw)
        
    if m == 4:
        visited = []
        print("wyszukiwanie w głąb:")
        DFS(visited, tab_kraw, tab_kraw[0][0])
        
    if m == 5:  # matrix
        
        h = int(input("0 - sortowanie macierzy podanej, 1 - sortowanie macierzy losowej"))
        
        if h == 0:
            matrix = []
            print("podaj kolejne wiersze macierzy sąsiedztwa")
            for i in range(n):
                m = input().split()
                matrix.append(m)
            wynik = tarjan_topological_sort_matrix(matrix)
            print("sortoanie topologiczne Tarjan:")
            for line in wynik:
                print(int(line) + 1)
                
        if h == 1:
            matrix = m_sasiedztwa_los(n)
            wynik = tarjan_topological_sort_matrix(matrix)
            print("sortoanie topologiczne Tarjan:")
            for line in wynik:
                print(int(line) + 1)
                
    if m == 6:
        try:
            wynik = topological_sort_tarjan_l_sas(l_sas)
            print("sortowanie topologiczne Tarjan:")
            for line in wynik:
                print(line)
                
        except NameError:
            l_sas = {}
            print("podaj listę sąsiadów:")
            for i in range(n):
                m = int(input("podaj wierzchołek: "))
                s = []
                print("podaj sąsiadów wierzchołka: ")
                s = input().split()
                l_sas[m] = s
            wynik = topological_sort_tarjan_l_sas(l_sas)
            print("sortowanie topologiczne Tarjan:")
            for line in wynik:
                print(line)

    if m == 7:
        wynik = tarjan_topological_sort_edges(tab_kraw)
        print("sortowanie topologiczne metodą Tarjana:")
        for line in wynik:
                print(line)

    if m == 8:
        print("sortowanie topologiczne Kahn:")
        print(kahns_topological_sort_lista_sasiadow(in_degree_tab_kraw(n)))
        
    if m == 9:
            '''if len(kontrolna) != len(graph):
                return None
            else:
                return kontrolna'''

        print(kahns_topological_sort_lista_sasiadow(in_degree_lista_sasiadow(l_sas)))

    if m == 10:
        print(kahns_topological_sort_lista_sasiadow(in_degree_matrix(m_sas)))

            
    m = int(input('podaj dalsze działanie:'))

