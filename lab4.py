
def tablica_krawedzi(n):
    tab_kraw = []
    for i in range(n):
        for j in range(n):
            if m_sas[i][j] == '1':
                tab_kraw.append((i + 1, j + 1))
    return tab_kraw
