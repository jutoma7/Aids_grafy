import random

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]
        self.edges = []

    def add_edge(self, u, v):
        if not self.adj_matrix[u][v]:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
            self.edges.append((u, v))

    def remove_edge(self, u, v):
        if self.adj_matrix[u][v]:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
            self.edges.remove((u, v))

    def degree(self, node):
        return sum(self.adj_matrix[node])

    def neighbors(self, node):
        return [i for i in range(self.num_nodes) if self.adj_matrix[node][i]]

def create_hamiltonian_cycle(graph):
    nodes = list(range(graph.num_nodes))
    random.shuffle(nodes)

    for i in range(len(nodes)):
        graph.add_edge(nodes[i], nodes[(i + 1) % len(nodes)])

    return nodes

def add_edges_to_saturate(graph, saturation):
    num_edges_to_add = int(saturation * graph.num_nodes)

    while num_edges_to_add > 0:
        u, v = random.sample(range(graph.num_nodes), 2)
        if not graph.adj_matrix[u][v]:
            graph.add_edge(u, v)
            num_edges_to_add -= 1

def make_degrees_even(graph):
    odd_degree_nodes = [node for node in range(graph.num_nodes) if graph.degree(node) % 2 != 0]

    while odd_degree_nodes:
        u = odd_degree_nodes.pop()
        v = odd_degree_nodes.pop()

        if not graph.adj_matrix[u][v]:
            graph.add_edge(u, v)
        else:
            neighbors_u = set(graph.neighbors(u))
            neighbors_v = set(graph.neighbors(v))
            common_neighbors = neighbors_u & neighbors_v

            if common_neighbors:
                w = random.choice(list(common_neighbors))
                graph.remove_edge(u, w)
                graph.remove_edge(v, w)
                graph.add_edge(u, v)
                graph.add_edge(u, w)
                graph.add_edge(v, w)
            else:
                graph.add_edge(u, v)

def print_adj_matrix(graph):
    matrix = []
    for row in graph.adj_matrix:
        matrix.append(list(row))
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

def DFS_Euler(graph, v, stack):
    for u in graph[v]:
        graph[v].remove(u)
        graph[u].remove(v)
        DFS_Euler(graph, u, stack)
    stack.append(v)

def matrix_to_adj_list(matrix):
    adj_list = {}
    for i in range(len(matrix)):
        adj_list[i] = []
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                adj_list[i].append(j)
    return adj_list

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

def main():
    num_nodes = int(input("Podaj liczbę wierzchołków: "))
    saturation = float(input("Podaj współczynnik nasycenia (0-1): "))

    graph = Graph(num_nodes)

    create_hamiltonian_cycle(graph)
    add_edges_to_saturate(graph, saturation)
    make_degrees_even(graph)

    matrix = print_adj_matrix(graph)
    for i in matrix:
        print(i)
    l_sas = matrix_to_adj_list(matrix)
    print(l_sas)

    matrix_bez_cyklu = matrix
    for i in range(num_nodes):
        matrix_bez_cyklu[0][i] = 0
        matrix_bez_cyklu[i][0] = 0

    m = -1
    while (m != 0):
        print('Proszę wpisać numer znajdujący się przy zadaniu, które chcesz aby wykonał program.')
        print('0 : Zakończenie działania programu')
        print('1 : Euler')
        print('2 : Hamilton')
        print('3 : Wybierz inne wejście.')
        m = int(input())
        if m == 1:
            # rzeczy do eulera
            ost = []
            poczatek = 0
            DFS_Euler(l_sas, poczatek, ost)
            print("Cykl Eulera:", ost[::-1])
        elif m == 2:
            if Hamiltonian_path(matrix, num_nodes):
                print('Graf posiada Hamiltona')
            else:
                print('Graf nie posiada Hamiltona')
        elif m == 3:
            l = int(input('1 - wpisanie z klawiatury, 2 - wygenerowanie nowego grafu, 3 - macierz z/bez cyklu, 4 - zostań przy obecnym grafie ; '))
            if l == 1:
                num_nodes = int(input('Podaj ilość wierzchołków: '))
                matrix = macierz_sasiedztwa(num_nodes)
                l_sas = matrix_to_adj_list(matrix)
                matrix_bez_cyklu = matrix
                for i in range(num_nodes):
                    matrix_bez_cyklu[0][i] = 0
                    matrix_bez_cyklu[i][0] = 0
            elif l == 2:
                main()
            elif l == 3:
                a = matrix
                matrix = matrix_bez_cyklu
                matrix_bez_cyklu = a




if __name__ == "__main__":
    main()
