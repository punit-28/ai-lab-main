
import heapq
import time

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def misplaced(state):
    return sum(1 for i in range(9)
               if state[i] != 0 and state[i] != goal[i])


def manhattan(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            goal_pos = tile - 1
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)

    return distance


def solvable(state):
    tiles = [x for x in state if x != 0]
    inversions = 0

    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            if tiles[i] > tiles[j]:
                inversions += 1

    return inversions % 2 == 0


def solve(start, heuristic):
    start_time = time.perf_counter()

    if not solvable(start):
        return None, 0, time.perf_counter() - start_time

    pq = []
    counter = 0

    heapq.heappush(pq, (heuristic(start), counter, 0, start))

    parent = {start: None}
    best_g = {start: 0}
    expanded = 0

    while pq:
        f, _, g, state = heapq.heappop(pq)

        if g != best_g[state]:
            continue

        expanded += 1

        if state == goal:
            path = []
            current = state

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            elapsed = time.perf_counter() - start_time
            return path, expanded, elapsed

        zero = state.index(0)
        row, col = zero // 3, zero % 3

        moves = []

        if row > 0:
            moves.append(zero - 3)
        if row < 2:
            moves.append(zero + 3)
        if col > 0:
            moves.append(zero - 1)
        if col < 2:
            moves.append(zero + 1)

        for pos in moves:
            new_state = list(state)
            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )
            new_state = tuple(new_state)

            new_g = g + 1

            if new_g < best_g.get(new_state, float("inf")):
                best_g[new_state] = new_g
                parent[new_state] = state
                counter += 1

                new_f = new_g + heuristic(new_state)

                heapq.heappush(
                    pq, (new_f, counter, new_g, new_state)
                )

    return None, expanded, time.perf_counter() - start_time


def display(path):
    for step, state in enumerate(path):
        print("Step", step)

        for i in range(0, 9, 3):
            print(state[i:i + 3])

        print()


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

for name, heuristic in [
    ("Misplaced Tile", misplaced),
    ("Manhattan Distance", manhattan)
]:
    path, expanded, elapsed = solve(start, heuristic)

    print("\nHeuristic:", name)

    if path is None:
        print("Puzzle is unsolvable")
    else:
        display(path)
        print("Expanded nodes:", expanded)
        print("Execution time:", round(elapsed, 6), "seconds")
        print("Solution length:", len(path) - 1)
