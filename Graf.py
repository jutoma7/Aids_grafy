import sys
from collections import defaultdict
from collections import deque
import random

def macierz_losowa(n):
    matrix = ['0']*n
    len_list = (n*n - n) // 2
    half = len_list // 2
    if len_list % 2 == 1:
        lista = ['0'] * half + ['1'] * half + ['0']
    else:
        lista = ['0'] * half + ['1'] * half
    random.shuffle(lista)
    a = 0
    for i in range(n):
        matrix[i] = ['0'] * (i+1)
        for j in range(n-i-1):
            matrix[i].append(lista[a])
            a +=1

    return matrix

def macierz_sasiedztwa(n):
    m_sas=[]
    print("podaj kolejne wiersze macierzy sąsiedztwa:")
    for i in range(n):
        m=input().split()
        m_sas.append(m)
    print("macierz sąsiedztwa: ")
    print(end="   ")
    for i in range(n):
        print(f"{i+1}:",end=" ")
    print()
    for i in range(n):
        print(f"{i+1}:",end=" ")
        for j in range(n):
            print(m_sas[i][j],end="  ")
        print()
    return m_sas

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

def lista_sasiadow(n, m_sas):
    l_sas={}
    for i in range(n):
        sasiedzi=[]
        for j in range(n):
            if m_sas[i][j]=='1':
                sasiedzi.append(j+1)
        l_sas[f"{i+1}"]=sasiedzi
    print("lista sąsiadów:")
    for key, value in l_sas.items():
        print(key, ":", value)
    return l_sas

def DFS(visited,tab_kraw,current):
    if current not in visited:
        visited.append(current)
        print(current)
    for line in tab_kraw:
        if line[0]==current and line[1] not in visited:
            DFS(visited,tab_kraw,line[1])
        if line[0] not in visited:
            DFS(visited, tab_kraw, line[0])

def BFS(visited, graph, node, n):
  queue = []
  visited.append(node)
  queue.append(node)
  while queue:
    m = queue.pop(0)
    print (m, end = " ")
    for neighbour in graph[m]:
      if str(neighbour) not in visited:
        visited.append(str(neighbour))
        queue.append(str(neighbour))
  if len(visited) != n:
    for i in range(n):
      if str(i+1) not in visited:
        node = str(i+1)
        break

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

def in_degree_tab_kraw(n, tab_kraw):  # tablica in degree od tablicy krawedzi do kahna
    tab_in = {}

    for i in range(n):
        tab_in[i + 1] = []
    for line in tab_kraw:
        tab_in[line[1]].append(line[0])
    return tab_in

def in_degree_lista_sasiadow(n, l_sas): # tablica in degree od listy sasiadow do kahna
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


sys.setrecursionlimit(10**7)

print('Podaj ilość wierzchołków grafu')
n = int(input())
print('Wybierz 1 jeśli chcesz podać macierz sąsiedztwa lub 0 jesli chcesz ją losowo wygenerować')
if input() == 1:
    m_sas = macierz_sasiedztwa(n)
else:
    m_sas = macierz_losowa(n)
    print(end="   ")
    for i in range(n):
        print(f"{i + 1}:", end=" ")
    print()
    for i in range(n):
        print(f"{i + 1}:", end=" ")
        for j in range(n):
            print(m_sas[i][j], end="  ")
        print()

tab_kraw = tablica_krawedzi(n, m_sas)
l_sas = lista_sasiadow(n, m_sas)

m = -1
while (m!=0):
    print('Proszę wpisać numer znajdujący się przy zadaniu, które chcesz aby wykonał program.')
    print('0 : Zakończenie działania programu')
    print('1 : Przeszukanie grafu wszerz (BFS)')
    print('2 : Przeszukanie grafu w głąb (DFS)')
    print('3 : Sortowanie topologiczne - algorytm Kahna (BFS)')
    print('4 : Sortowanie topologiczne - algorytm Tarjana (DFS)')
    m = int(input())
    if m == 1:
        BFS([], l_sas, '1', n)
        print('')
    elif m == 2:
        v = []
        DFS(v, tab_kraw, tab_kraw[0][0])
        print(end=" ")
    elif m == 3:
        print('Wybierz na jakim rodzaju danych chcesz działać.')
        print('1 : macierz sąsiedztwa')
        print('2 : tablica krawędzi')
        print('3 : lista sąsiadów')
        s = int(input())
        if s == 1:
            print(kahns_topological_sort_lista_sasiadow(in_degree_matrix(m_sas)))
        elif s == 2:
            print(kahns_topological_sort_lista_sasiadow(in_degree_tab_kraw(n, tab_kraw)))
        elif s == 3:
            print(kahns_topological_sort_lista_sasiadow(in_degree_lista_sasiadow(n, l_sas)))
    elif m == 4:
        print('Wybierz na jakim rodzaju danych chcesz działać.')
        print('1 : macierz sąsiedztwa')
        print('2 : tablica krawędzi')
        print('3 : lista sąsiadów')
        s = int(input())
        if s == 1:
            wynik = tarjan_topological_sort_matrix(m_sas)
            for line in wynik:
                print(int(line) + 1)
        elif s == 2:
            wynik = tarjan_topological_sort_edges(tab_kraw)
            for line in wynik:
                print(line)
        elif s == 3:
            wynik = topological_sort_tarjan_l_sas(l_sas)
            for line in wynik:
                print(line)
