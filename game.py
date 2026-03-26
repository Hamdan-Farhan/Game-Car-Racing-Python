
from pickle import TRUE
from secrets import choice
import pygame
from ob import Player
from ob import Road
from ob import Tree
from ob import Pr
import random

pygame.init()
SCREEN  = WIDTH , HEIGHT =  500, 800

win = pygame.display.set_mode(SCREEN)

clock = pygame.time.Clock()
FPS = 10

BLUE = (30,144,255)

home_img = pygame.image.load('Assets/home.png')
bg = pygame.image.load('Assets/bg.png')
road = pygame.image.load('Assets/road.png')
road = pygame.transform.scale(road,(WIDTH-60, HEIGHT))


p = Player(100,HEIGHT-120,0)
move_left = False
move_right = False


road = Road()
speed = 5
tree_group = pygame.sprite.Group()

Pr_group = pygame.sprite.Group()

home_page = False
game_page = True
counter = 0

running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            if x < WIDTH // 2:
                move_left = True
            else:
                move_right = True

        if event.type == pygame.MOUSEBUTTONUP:
            move_left = False
            move_right = False

    if home_page:

        win.blit(home_img,(0,0))

    if game_page:

        win.blit(bg, (0,0))
        road.update(speed)
        road.draw(win)

        counter += 1
        if counter %60 == 0 :
            tree = Tree(random.choice([-5, WIDTH-35]), -20)
            tree_group.add(tree)
        tree_group.update(speed)
        tree_group.draw(win)

        if counter %90 == 0 :
            obs = random.choices([1,2,3], weights=[6,2,2], k=1)[0]
            obee = Pr(obs)
            Pr_group.add(obee)
        Pr_group.update(speed)
        Pr_group.draw(win)

    p.draw(win)
    p.update(move_left, move_right)
    pygame.display.update()

pygame.quit()

