import pygame
import random
import numpy as np
from operator import itemgetter


class Point():
    def __init__(self, x, y, color=(0, 0, 0), cluster=-1):
        self.x = x
        self.y = y
        self.color = color
        self.cluster = cluster


def dist(a, b):
    return np.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def knn_with_n_train(point, n):
    print(n)
    distances = []
    for point1 in points:
        if point != point1:
            distances.append([dist(point1, point), point1])
    distances = sorted(distances, key=itemgetter(0))
    neighbours = distances[:n]
    clst1 = 0
    clst2 = 0
    for nbr in neighbours:
        if nbr[1].cluster == 1:
            clst1 += 1
        if nbr[1].cluster == 2:
            clst2 += 1
    if clst1 > clst2:
        point.cluster = 1
        point.color = (255, 0, 0)
    else:
        point.cluster = 2
        point.color = (0, 0, 255)
    return point


def add_points(point, color):
    clst = -1
    colour = (0, 0, 0)
    if color == 'red':
        colour = (255, 0, 0)
        clst = 1
    else:
        colour = (0, 0, 255)
        clst = 2
    points.append(Point(point[0], point[1], color=colour, cluster=clst))
    k = random.randint(1, 4)
    for i in range(k):
        d = random.randint(2 * r, 5 * r)
        alpha = random.random() * np.pi
        x_new = point[0] + d * np.sin(alpha)
        y_new = point[1] + d * np.cos(alpha)
        points.append(Point(x_new, y_new, color=colour, cluster=clst))


def compute_n():
    scoring = []
    for i in range(3,13):




def knn_with_n(point, n):
    print(n)
    distances = []
    for point1 in points:
        if point != point1:
            distances.append([dist(point1, point), point1])
    distances = sorted(distances, key=itemgetter(0))
    neighbours = distances[:n]
    clst1 = 0
    clst2 = 0
    for nbr in neighbours:
        if nbr[1].cluster == 1:
            clst1 += 1
        if nbr[1].cluster == 2:
            clst2 += 1
    if clst1 > clst2:
        point.cluster = 1
        point.color = (255, 0, 0)
    else:
        point.cluster = 2
        point.color = (0, 0, 255)
    points.append(point)


def add_point(pos):
    point = Point(pos[0], pos[1])
    unr_points.append(point)


def train(pts):
    pass


def predict(pts):
    for point in unr_points:
        knn_with_n(point, def_n)


def mark_points(param):
    clst = 0
    color = (0, 0, 0)
    if param == 'red':
        clst = 1
        color = (255, 0, 0)
    else:
        clst = 2
        color = (0, 0, 255)

    for point in unr_points:
        if point.cluster == -1:
            point.cluster = clst
            point.color = color


def pygame_draw():
    screen = pygame.display.set_mode((600, 400), pygame.RESIZABLE)
    screen.fill('WHITE')
    pygame.display.update()
    FPS = 30
    clock = pygame.time.Clock()
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    add_points(event.pos, 'red')
                if event.button == 3:
                    add_points(event.pos, 'blue')
                if event.button == 2:
                    add_point(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    train(points)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    predict(points)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    mark_points('red')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    mark_points('blue')
        screen.fill('WHITE')
        for point in points:
            pygame.draw.circle(screen, point.color, (point.x, point.y), r)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    points = []
    unr_points = []
    r = 4
    def_n = 3
    pygame_draw()
