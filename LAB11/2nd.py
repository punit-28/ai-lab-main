
import random

def fitness(board):
    n = len(board)
    score = 0

    for i in range(n):
        for j in range(i + 1, n):
            if abs(board[i] - board[j]) != j - i:
                score += 1

    return score


def tournament(population, k=3):
    candidates = random.sample(population, min(k, len(population)))
    return max(candidates, key=fitness)


def crossover(p1, p2):
    point = random.randint(1, len(p1) - 1)
    return p1[:point] + p2[point:]


def mutation(board, rate):
    board = board[:]

    for i in range(len(board)):
        if random.random() < rate:
            board[i] = random.randint(0, len(board) - 1)

    return board


def genetic_algorithm(n, population_size, mutation_rate,
                      max_generations):
    if n < 4:
        print("No solution for N =", n)
        return None, 0

    population = [
        [random.randint(0, n - 1) for _ in range(n)]
        for _ in range(population_size)
    ]

    max_fitness = n * (n - 1) // 2

    for generation in range(max_generations + 1):
        best = max(population, key=fitness)

        if fitness(best) == max_fitness:
            print("Solution found in generation:", generation)
            return best, generation

        if generation == max_generations:
            break

        new_population = [best[:]]  # Elitism

        while len(new_population) < population_size:
            p1 = tournament(population)
            p2 = tournament(population)

            child = crossover(p1, p2)
            child = mutation(child, mutation_rate)

            new_population.append(child)

        population = new_population

    print("Generation limit reached.")
    return None, max_generations


def display_board(board):
    if board is None:
        return

    n = len(board)

    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)


# Configurable parameters
N = 8
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
MAX_GENERATIONS = 1000

solution, generations = genetic_algorithm(
    N, POPULATION_SIZE, MUTATION_RATE, MAX_GENERATIONS
)

print("Generations:", generations)
display_board(solution)
