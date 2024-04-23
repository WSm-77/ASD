from zad5testy import runtests
from queue import PriorityQueue

# dodaje krawędzie pomiędzy osobliwościami
def edges_to_graph(E, V, S):
    graph = [[] for _ in range(V)]

    # graf pierwotny
    for vertex, neighbour, cost in E:
        graph[vertex].append((neighbour, cost))
        graph[neighbour].append((vertex, cost))

    nextToSingularity = [False]*V
    for vertex in S:
        nextToSingularity[vertex] = True

    # graf z uwzględnieniem krawędzi pomiędzy osobliwościami
    for vertex in range(V):
        if nextToSingularity[vertex]:
            for neighbour in S:
                if neighbour == vertex:
                    continue

                graph[vertex].append((neighbour, 0))
            #end for
    #end for

    return graph

def spacetravel( n, E, S, a, b ):
    # tu prosze wpisac wlasna implementacje

    V = n

    G = edges_to_graph(E, V, S)
    # print(*G, sep="\n")
    distances = [float("inf")]*V
    toVisit = PriorityQueue()
    toVisit.put((0, a))
    distances[a] = 0

    while not toVisit.empty():
        distance, vertex = toVisit.get()

        for neighbour, cost in G[vertex]:
            if distance + cost < distances[neighbour]:
                distances[neighbour] = distance + cost
                toVisit.put((distances[neighbour], neighbour))
            #end if
        #end for

    return distances[b] if distances[b] != float("inf") else None
    # return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )