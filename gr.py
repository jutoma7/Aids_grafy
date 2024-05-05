import sys
from collections import defaultdict
from collections import deque
import random

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

def m_sasiedztwa_los(n):
    m_sas_los=[]
    for i in range(n):
        lista=[]
        for j in range(i+1):
            lista.append('0')
        for j in range(n-(i+1)):
            lista.append(str(random.randint(0,1)))
        m_sas_los.append(lista)
    return m_sas_los

def tablica_krawedzi(n):
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

def lista_sasiadow(n):
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

def BFS(self, s):
    visited = [False] * (len(self) + 1)
    queue = []
    queue.append(s)
    visited[s] = True
    while queue:
        s = queue.pop(0)
        print(s, end=" ")
        for i in self[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

def tablica_in(n): #potrzebna do sortowania topologicznego, odwrócenie listy sąsiadów
    tab_in={}
    for i in range(n):
        tab_in[i+1]=[]
    for line in tab_kraw:
        tab_in[line[1]].append(line[0])
    return tab_in


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
    return stack[::-1]


def Kahn(adj, V):
    indegree = [0] * V
    for i in range(V):
        for vertex in adj[i]:
            indegree[vertex] += 1
    q = deque()
    for i in range(V):
        if indegree[i] == 0:
            q.append(i)
    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for adjacent in adj[node]:
            indegree[adjacent] -= 1
            if indegree[adjacent] == 0:
                q.append(adjacent)
    if len(result) != V:
        print("Graf zawiera cykl!")
        return []
    return result


sys.setrecursionlimit(10**7)

n = int(input())

m_sas=macierz_sasiedztwa(n)
tab_kraw=tablica_krawedzi(n)
l_sas=lista_sasiadow(n)
print(m_sas, tab_kraw, l_sas)
m = -1
while (m!=0):
    print('Proszę wpisać numer znajdujący się przy zadaniu, które chcesz aby wykonał program.')
    print('0 : Zakończenie działania programu')
    print('1 : Przeszukanie grafu wszerz (BFS)')
    print('2 : Przeszukanie grafu w głąb (DFS)')
    print('3 : Sortowanie topologiczne - algorytm Kahna (BFS)')
    print('4 : Sortowanie topologiczne - algorytm Tarjana (DFS)')
    m = int(input())
    if m == 1:          #Sprawdzić czemu nie wypisuje całości, naprawić dla losowego
        BFS(tab_kraw, tab_kraw[0][0])
        print('')
    elif m == 2:
        v = []
        DFS(v, tab_kraw, tab_kraw[0][0])
        print(end=" ")
    elif m == 3:
        adj = [[] for _ in range(n)]
        for i in tab_kraw:
            adj[i[0]-1].append(i[1]-1)
        result = Kahn(adj, n)
        for i in result:
            print(i+1, end=" ")
        print('')
    elif m == 4:
        tab_in = tablica_in(n)
        Tarjan(tab_in)

'''from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	def addEdge(self, u, v):
		self.graph[u].append(v)
	
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			print(s, end=" ")

			# Get all adjacent vertices of the
			# dequeued vertex s.
			# If an adjacent has not been visited,
			# then mark it visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


# Driver code
if __name__ == '__main__':

	# Create a graph given in
	# the above diagram
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Breadth First Traversal"
		" (starting from vertex 2)")
	g.BFS(2)'''

