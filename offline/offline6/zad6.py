# Wiktor Sędzimir
# 
# Opis algorytmu:
# Dla każdego wierzchołka rozważamy minimalny dystans, który należy przebyć, aby znaleźć się w danym wierzchołku,
# przy uwzględnieniu, czy do wirzchołka wchodzimy wykorzystując dwumilowe buty czy też nie (rozróżniamy to w tablicy
# distances). Do kolejki priorytetowej dodajemy dodatkowe informacje o poprzednim koszcie podróży, dystansie poprzedniego
# wierzchołka oraz czy do dotarcia do poprzedniego wierzchołka skorzystano z butów, po to aby móc rozważać kiedy warto
# użyć dwumilowych butów. Algorytm ma złożoność O(V^2 log V), ponieważ korzysta z algorymu dijkstry dla macierzy, który
# wykorzystuje kolejkę priorytetową

from zad6testy import runtests
from queue import PriorityQueue

# definicja stałej globalnej
INF = float("inf")

def find_not_visited_min_distance(distances, visited, V):
    minDistance = INF
    minVertex = None
    bootsUsage = 0

    for vertex in range(V):
        if not visited[vertex][0] and distances[vertex][0] < minDistance:
            minDistance = distances[vertex][0]
            minVertex = vertex
            bootsUsage = 0

        if not visited[vertex][1] and distances[vertex][1] < minDistance:
            minDistance = distances[vertex][1]
            minVertex = vertex
            bootsUsage = 1
    
    return minDistance, minVertex, bootsUsage

def jumper( G, s, w ):
    # tu prosze wpisac wlasna implementacje

    V = len(G)

    # distances[i][0] - dystans przebyty do i-tego wierzchołka bez używania dwumilowych butów w poprzednim skoku
    # distances[i][1] - dystans przebyty do i-tego wierzchołka z użyciem dwumilowych butów w poprzednim skoku
    distances = [[INF, INF] for _ in range(V)]
    distances[s][1] = 0
    toCheck = PriorityQueue()
    toCheck.put((0, s, 0, INF, INF, 1))

    while not toCheck.empty():
        currentDistance, minVertex, bootsUsage, prevDistance, prevCost, prevBootsUsage = toCheck.get()

        if currentDistance < distances[minVertex][bootsUsage]:
            distances[minVertex][bootsUsage] = currentDistance

        for neighbour in range(V):
            travelCost = G[minVertex][neighbour]
            if travelCost > 0:
                newDistance = currentDistance + travelCost
                if newDistance < distances[neighbour][0]:
                    toCheck.put((newDistance, neighbour, 0, currentDistance, travelCost, bootsUsage))
            
                if not bootsUsage and not prevBootsUsage:
                    bootsTravelCost = max(travelCost, prevCost)
                    bootsNewDistance = prevDistance + bootsTravelCost
                    if bootsNewDistance < distances[neighbour][1]:
                        toCheck.put((bootsNewDistance, neighbour, 1, INF, INF, 0))


    return min(distances[w][0], distances[w][1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )