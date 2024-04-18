def matrix_to_list(G):
    V = len(G)

    newG = [[] for _ in range(V)]
    for vertex in range(V):
        for neighbour in range(V):
            if G[vertex][neighbour] == 1:
                newG[vertex].append(neighbour)

    return newG

graph1_list = [[1,2],
            [4],
            [3,5],
            [4],
            [5],
            [6],
            [7],
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