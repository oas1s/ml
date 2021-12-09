# 23x - 13y +7z = 5
import random
from operator import itemgetter

N = 10
min_c = 100000
best = []
population = []


def count_diff(x, y, z):
    left = 23 * x - 13 * y + 7 * z
    return 5 - left


def mutation(pop):
    for i in range(N):
        pop[random.randint(0, 9)][random.randint(0, 2)] = random.randint(1, 50)


def selection(pop):
    global min_c
    global best
    ranking = []
    for i in range(N):
        if abs(count_diff(pop[i][0], pop[i][1], pop[i][2]))<min_c:
            min_c = abs(count_diff(pop[i][0], pop[i][1], pop[i][2]))
            best = pop[i]
        ranking.append([abs(count_diff(pop[i][0], pop[i][1], pop[i][2])), i])
    ranking = sorted(ranking, key=itemgetter(0))

    items_to_remove = []
    for i in range(int(N/2),N):
        index = ranking[i][1]
        item = pop[index]
        items_to_remove.append(item)

    for i in range(int(N/2)):
        pop.remove(items_to_remove.pop())


def form_new_pop(pop):
    for i in range(int(N/2)):
        parent1 = pop[random.randint(0,4)]
        while True:
            parent2 = pop[random.randint(0, 4)]
            if parent1 != parent2:
                break
        new_child = [parent1[0],parent2[1],parent1[2]]
        pop.append(new_child)


if __name__ == '__main__':
    # generate population
    for i in range(N):
        member = [random.randint(1, 50), random.randint(1, 50), random.randint(1, 50)]
        population.append(member)
    print(population)

    for i in range(1000):
        mutation(population)
        selection(population)
        form_new_pop(population)
        print(population)
        if min_c == 0:
            break

    print(min_c,best)
