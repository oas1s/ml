import pygame
import random
import numpy as np
from sklearn import svm

clf = svm.SVC(kernel='linear')


class Point():
    def __init__(self, x, y, color=(0, 0, 0), cluster=-1):
        self.x = x
        self.y = y
        self.color = color
        self.cluster = cluster


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


def train(pts):

    clf.fit([(p.x, p.y) for p in pts], [p.cluster for p in pts])
    print('train succeed')


def add_point(pos):
    point = Point(pos[0], pos[1])
    point.cluster = clf.predict([(point.x, point.y)])
    if point.cluster == 1:
        point.color = colour = (255, 0, 0)
    if point.cluster == 2:
        point.color = colour = (0, 0, 255)
    points.append(point)


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
        screen.fill('WHITE')
        for point in points:
            pygame.draw.circle(screen, point.color, (point.x, point.y), r)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    points = []
    r = 4
    pygame_draw()
