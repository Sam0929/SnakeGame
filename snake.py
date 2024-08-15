import pygame
import random
from settings import *

#initial config

pygame.init()
pygame.display.set_caption("SnakeGame")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


#snake parameters

square_size = 10
snake_speed = 15

def food_generate ():

    food_x = random.randrange(0, WIDTH - square_size)
    food_y = random.randrange(0, WIDTH - square_size)

    return food_x, food_y


def run_game ():

    end_game = False

    x = WIDTH/2
    y = HEIGHT/2

    speed_x = 0
    speed_y = 0

    snake_size = 1
    pixels = []

    food_x, food_y = food_generate ()

    while not end_game:
        
        screen.fill(black)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True

       
run_game()
