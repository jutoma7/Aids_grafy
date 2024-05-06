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
    if len_list % 2 == 1:
        lista = ['0'] * rest + ['1'] * nas + ['0']
    else:
        lista = ['0'] * rest + ['1'] * nas
    random.shuffle(lista)
    a = 0
    for i in range(n):
        matrix[i] = []
        for j in range(n):
            matrix[i].append(lista[a])
            a += 1

    return matrix

n = int(input())
m = int(input())
matrix = macierz_nasycona(n,m)
for i in range(n):
    print(matrix[i])

t_kraw = tablica_krawedzi(n, matrix)

