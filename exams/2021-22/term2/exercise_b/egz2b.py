# Opis algorytmu:
# Dla każdej komnaty wyznaczamy maksymalną liczbę złota z jaką możemy znaleźć się w danej komnacie. Aby to zrobić
# przechodzimy iteracyjnie po każdej komnacie od 0 do n - 1 i korzystając z uprzednio obliczonej wartości złota
# wyznaczamy maksymalną liczbę złota dla 3 kolejnych komnat, do których możemy dostać się z tej, w której obecnie 
# przebywamy (o ile możemy sie do nich przedostać).
# Złożoność: O(n)  

from egz2btesty import runtests


def next_gold(currentGold, goldInChest, travleCost):
    take = min(10, goldInChest)
    goldInChest -= take
    addToChest = travleCost - goldInChest

    # there is already enough gold in chest to go through this door
    if addToChest < 0:
        return currentGold + take
    
    return currentGold + take - addToChest

def can_open(currentGold, goldInChest, travelCost):
    take = min(10, goldInChest)
    goldInChest -= take
    if goldInChest > travelCost:
        return False
    elif goldInChest + take + currentGold >= travelCost:
        return True
    else:
        return False

def magic( C ):
    # tu prosze wpisac wlasna implementacje

    n = len(C)
    maxGold = [-1 for _ in range(n)]
    maxGold[0] = 0

    for i in range(n - 1):
        # if we can't get to i-th chamber from 0-th chamber continue 
        if maxGold[i] == -1:
            continue

        gold = C[i][0]
        currentGold = maxGold[i]
        for doorId in range(1, 4):
            door = C[i][doorId]
            if door[1] > i and can_open(currentGold, gold, door[0]):
                nextGold = next_gold(currentGold, gold, door[0])
                maxGold[door[1]] = max(maxGold[door[1]], nextGold)

    return maxGold[n - 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
