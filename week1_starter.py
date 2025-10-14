# importing modules
import math
import os
import random
import pygame

# constants
WALL_THICKNESS = 32
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
NUM_ENEMIES = 5
NUM_COLLECTIBLES = 3
FRAMES_PER_SECOND = 60

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scavenger Haunt")
clock = pygame.time.Clock()
running = True
dt = 0

# TODO create a 2D vector for the player position at the center of the screen
# TODO create an empty list for enemies (list of tuples (enemy_pos, enemy_direction))
# TODO create an empty list for collectibles

# TODO load wall image, convert it to a surface, and scale it by 2
# TODO load floor image, convert it to a surface
# TODO load gift image, convert it to a surface with an alpha channel
# TODO load battery image, convert it to a surface with an alpha channel and scale it by 4
# TODO load player image, convert it to a surface with an alpha channel
# TODO load enemy image, convert it to a surface with an alpha channel


def draw_bg():
    # TODO: clear the screen and draw floor image covering the whole screen
    pass


def draw_walls():
    # TODO draw four walls around the edges of the screen using the wall image
    pass


def spawn_enemies():
    # TODO spawn enemies at random positions with random directions
    pass


def spawn_collectibles():
    # TODO spawn collectibles at random positions
    pass


def draw_enemies():
    # TODO draw all enemies in the enemies list
    pass


def draw_collectibles():
    # TODO draw all collectibles in the collectibles list
    pass


def draw_player():
    # TODO draw the player at the player position
    pass


# TODO call spawn_enemies
# TODO call spawn_collectibles

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # TODO call draw_bg
    # TODO call draw_walls
    # TODO call draw_player
    # TODO call draw_enemies
    # TODO call draw_collectibles

    pygame.display.flip()  # display your drawing to the screen
    dt = clock.tick(FRAMES_PER_SECOND) / 1000  # limits FPS to 60

pygame.quit()
