def matrix_to_list(G):
    V = len(G)

    newG = [[] for _ in range(V)]
    for vertex in range(V):
        for neighbour in range(V):
            if G[vertex][neighbour] == 1:
                newG[vertex].append(neighbour)

    return newG

def edges_to_digraph(edges):
    V = 0
    for edge in edges:
        V = max(V, edge[0], edge[1])
    V += 1

    G = [[] for _ in range(V)]

    for edge in edges:
        G[edge[0]].append(edge[1])

    return G

def edges_to_graph(edges):
    V = 0
    for edge in edges:
        V = max(V, edge[0], edge[1])
    V += 1

    G = [[] for _ in range(V)]

    for edge in edges:
        G[edge[0]].append(edge[1])
        G[edge[1]].append(edge[0])

    return G

def edges_to_graph_with_cost(edges):
    V = 0
    for edge in edges:
        V = max(V, edge[0], edge[1])
    V += 1

    G = [[] for _ in range(V)]

    for edge in edges:
        G[edge[0]].append((edge[1], edge[2]))
        G[edge[1]].append((edge[0], edge[2]))

    return G

def list_to_weighted_edges(G):
    V = len(G)
    edges = []

    for vertex in range(V):
        for neighbour, weight in G[vertex]:
            edges.append((vertex, neighbour, weight))

    return edges

def print_way(parent, vertex):
    def rek(vertex):
        nonlocal parent
        if parent[vertex] == None:
            print(f"{vertex}", end="")
            return
        
        rek(parent[vertex])
        print(f" -> {vertex}", end="")
    #end def
    
    rek(vertex)
    print()

def get_number_of_verticies(edges):
    V = 0
    for edge in edges:
        V = max(V, edge[0], edge[1])

    return V + 1

graph1_list = [[1,2],
            [4],
            [3,5],
            [4],
            [5],
            [6],
            [7],
            []]

graph1_list_weights = [[(1, 3), (2, 4)],
                       [(4, 5)],
                       [(3, 1),(5, 3)],
                       [(4, 2)],
                       [(5, 6)],
                       [(6, 1)],
                       [(7, 2)],
                       []]

graph2_list = [[1,2],
        [],
        [],
        [6],
        [],
        [3,4],
        [5]]

graph3_list = [[4],
        [4,6],
        [4,5],
        [5],
        [0,1,2],
        [2,3],
        [1]]

graph4_matrix = [
        #0,1,2,3,4,5,6
        [0,0,0,0,1,0,0], #0
        [0,0,0,0,1,1,1], #1
        [0,0,0,0,1,1,0], #2
        [0,0,0,0,0,1,0], #3
        [1,1,1,0,0,0,0], #4
        [0,1,1,1,0,0,0], #5
        [0,1,0,0,0,0,0]  #6
             ]

graph4_list = [[4],
          [4, 5, 6],
          [4, 5],
          [5],
          [0, 1, 2],
          [1, 2, 3],
          [1]]

graph5_matrix = [[0,1,0],
          [1,0,1],
          [0,1,0]]

graph6_matrix = [
        #0 1 2 3 4 5 6
        [0,1,0,0,1,0,0], #0
        [1,0,0,0,1,1,1], #1
        [0,0,0,0,1,1,0], #2
        [0,0,0,0,0,1,0], #3
        [1,1,1,0,0,0,0], #4
        [0,1,1,1,0,0,0], #5
        [0,1,0,0,0,0,0]  #6
        ]

graph6_list = [[1, 4],
               [0, 4, 5, 6],
               [4, 5],
               [5],
               [0, 1, 2],
               [1, 2, 3],
               [1]]

graph7_matrix = [[0, 1, 1, 0, 1],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1],
          [1, 0, 1, 0, 0]]

graph8_matrix = [
        #0 1 2 3 4 5 6 7 8
        [0,0,0,0,1,0,1,0,0], #0
        [0,0,0,1,0,1,1,0,0], #1
        [0,1,0,0,1,0,1,0,1], #2
        [0,0,0,0,1,1,1,1,0], #3
        [0,1,1,0,0,0,1,0,0], #4
        [0,1,0,1,0,0,1,0,0], #5
        [0,0,0,0,0,0,0,0,0], #6
        [0,0,1,0,0,0,1,0,0], #7
        [0,0,1,0,0,0,1,1,0]  #8
        ]

graph9_matrix = [
        #0 1 2 3 4 5 6
        [0,1,0,0,1,0,0], #0
        [1,0,0,1,1,1,1], #1
        [0,0,0,0,1,1,0], #2
        [0,0,0,0,0,1,0], #3
        [0,1,1,0,0,0,0], #4
        [0,1,0,1,0,0,0], #5
        [0,0,0,0,0,0,0]  #6
        ]

graph10_list = [[1,2,4],
        [3,5],
        [5,6],
        [6],
        [6,7],
        [8],
        [],
        [],
        [7]]

graph11_list = [[1,5],
        [2],
        [3],
        [4],
        [0],
        [6],
        [7],
        [8],
        [9],
        [10],
        [5]]

graph12_list = [[1,2],
        [3,5,6,4,2,0],
        [0,1,3,4,5,6],
        [4,1,5,2],
        [5,1,2,3],
        [2,3,1,4],
        [1,2]]

graph13_list = [[1,4],
        [0,2,4],
        [1,3],
        [2,4],
        [0,1,3]]

graph14_list = [[1,2,3,4],
           [0,2,3,4],
           [0,1,3,4],
           [0,1,2,4],
           [0,1,2,3]]

graph15_list =  [[1,2,3],
            [0,2],
            [0,1,4,5,6],
            [0,4],
            [2,3,6],
            [2,6],
            [2,4,5]]

graph15_list_weights = [[(1, 2), (2, 6), (3, 7)],
                        [(0, 2), (2, 4)],
                        [(0, 6), (1, 4), (4, 10), (5, 9), (6, 8)],
                        [(0, 7), (4, 5)],
                        [(2, 10), (3, 5), (6, 3)],
                        [(2, 9), (6, 1)],
                        [(2, 8), (4, 3), (5, 1)]]

graph16_list = [[1,4,5],
                [0,2],
                [1,3],
                [2,4],
                [3,0],
                [10,6],
                [5,7],
                [6,8],
                [7,9],
                [8,10],
                [9,5]]

graph17_list = [[1,3,7],
                [2],
                [3,5,8],
                [4,6],
                [5],
                [6,7,8],
                [7],
                [8,9],
                [9],
                [10],
                []]

graph17_list_weights = [[(1, 1),(3, 3),(7, 4)],
                        [(2, 2)],
                        [(3, 7),(5, 5),(8, 2)],
                        [(4, 3),(6, 1)],
                        [(5, 3)],
                        [(6, 6),(7, 5),(8, 4)],
                        [(7, 7)],
                        [(8, 3),(9, 1)],
                        [(9, 2)],
                        [(10, 1)],
                        []]

graph18_list = [[1,2,4],
                [3,5],
                [5,6],
                [6],
                [6,7],
                [8],
                [5,8],
                [],
                [7]]

graph19_list_weights = [[(1, 2), (2, 3), (3, 7), (4, 12)],
                        [(0, 2), (2, 4), (5, 2)],
                        [(0, 3), (1, 4), (4, 2), (5, 9), (6, 5)],
                        [(0, 7), (4, 5)],
                        [(2, 2), (3, 5), (6, 3)],
                        [(2, 9), (6, 1)],
                        [(2, 5), (4, 3), (5, 1)]]

graph19_edges_weights = [(0, 1, 2), (0, 2, 3), (0, 3, 7), (0, 4, 12), (1, 0, 2), (1, 2, 4), (1, 5, 2), (2, 0, 3), 
                         (2, 1, 4), (2, 4, 2), (2, 5, 9), (2, 6, 5), (3, 0, 7), (3, 4, 5), (4, 2, 2), (4, 3, 5), 
                         (4, 6, 3), (5, 2, 9), (5, 6, 1), (6, 2, 5), (6, 4, 3), (6, 5, 1)]

graph19_list_weights_modified = [[(1, 2), (2, 3), (3, 7), (4, 12)],
                                [(0, 2), (2, 4), (5, 2)],
                                [(0, 3), (1, 4), (4, 2), (5, 9), (6, 5)],
                                [(0, 7), (4, 5)],
                                [(2, 2), (3, 5), (6, 4)],
                                [(2, 9), (6, 1)],
                                [(2, 5), (4, 4), (5, 1)]]

graph19_edges_weights_modified = [(0, 1, 2), (0, 2, 3), (0, 3, 7), (0, 4, 12), (1, 0, 2), (1, 2, 4), (1, 5, 2), 
                                  (2, 0, 3), (2, 1, 4), (2, 4, 2), (2, 5, 9), (2, 6, 5), (3, 0, 7), (3, 4, 5), 
                                  (4, 2, 2), (4, 3, 5), (4, 6, 4), (5, 2, 9), (5, 6, 1), (6, 2, 5), (6, 4, 4), 
                                  (6, 5, 1)]

graph19_list_weights_modified2 = [[(1, 2), (3, 7), (4, 12)],
                                  [(5, 2)],
                                  [(1, 4), (5, 9), (6, -7)],
                                  [(4, 5)],
                                  [(2, 2)],
                                  [(6, 1)],
                                  [(4, 3)]]

graph20_list_weights = [[(1, 1), (2, 2)],
                        [(0, 1), (3, 3), (4, 2)],
                        [(0, 2), (3, 1), (6, 7)],
                        [(1, 3), (2, 1), (5, 2), (7, 3)],
                        [(7, 5)],
                        [(3, 3), (6, 1), (8, 8)],
                        [(2, 7), (5, 1), (8, 4)],
                        [(3, 2), (4, 5), (8, 1)],
                        [(5, 8), (6, 4), (7, 1)]]

graph20_edges_weights = [(0, 1, 1), (0, 2, 2), (1, 0, 1), (1, 3, 3), (1, 4, 2), (2, 0, 2), (2, 3, 1), (2, 6, 7), (3, 1, 3), 
                        (3, 2, 1), (3, 5, 2), (3, 7, 3), (4, 7, 5), (5, 3, 3), (5, 6, 1), (5, 8, 8), (6, 2, 7), (6, 5, 1), 
                        (6, 8, 4), (7, 3, 2), (7, 4, 5), (7, 8, 1), (8, 5, 8), (8, 6, 4), (8, 7, 1)]

graph21_edges = [(0, 3), (0, 1), (1, 2), (1, 10), (2, 3), (3, 4), (4, 2), (4, 5), (5, 2), (6, 5), (6, 9), (7, 6), (8, 7),
                (9, 8), (10, 9), (10, 0)]

graph21_list = [[3, 1],
                [2, 10],
                [3],
                [4],
                [2, 5],
                [2],
                [5, 9],
                [6],
                [7],
                [8],
                [9, 0]]

graph21_list_modified = [[7],
                        [5, 9],
                        [3],
                        [4],
                        [2, 5],
                        [2],
                        [2, 10],
                        [1],
                        [3, 6],
                        [0],
                        [9, 8]]

graph22_edges = [(0, 1), (1, 2), (3, 2), (2, 4), (4, 1), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 6)]

graph22_list = [[1],
                [2],
                [4],
                [2],
                [1, 5],
                [6],
                [7],
                [8],
                [9],
                [6]]

graph22_list_modified = [[1, 3],
                        [2],
                        [4],
                        [2],
                        [1, 5],
                        [6],
                        [7],
                        [8],
                        [9],
                        [6]]

graph23_edges_weights = [(0, 1, 5), (1, 2, 3), (0, 2, 7), (2, 3, 4), (3, 4, 6)]

graph23_list = [[(1, 5), (2, 7)],
                [(0, 5), (2, 3)],
                [(1, 3), (0, 7), (3, 4)],
                [(2, 4), (4, 6)],
                [(3, 6)]]

graph23_verticies_costs = [8.0, 5.0, 3.0, 2.0, 1.0]

graph24_edges_weights = [(0, 1, 4), (0, 7, 5), (0, 6, 8), (6, 7, 3), (1, 6, 6), (7, 8, 20), (8, 4, 9),
                        (5, 6, 12), (5, 4, 7), (1, 2, 15), (5, 2, 17), (2, 4, 10), (2, 3, 5), (4, 3, 18)]

graph24_list = [[(1, 4), (7, 5), (6, 8)],
                [(0, 4), (6, 6), (2, 15)],
                [(1, 15), (5, 17), (4, 10), (3, 5)],
                [(2, 5), (4, 18)],
                [(8, 9), (5, 7), (2, 10), (3, 18)],
                [(6, 12), (4, 7), (2, 17)],
                [(0, 8), (7, 3), (1, 6), (5, 12)],
                [(0, 5), (6, 3), (8, 20)],
                [(7, 20), (4, 9)]]

graph24_verticies_costs = [5, 7, 3, 5, 2, 1, 8, 10, 6]