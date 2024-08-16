import pygame
import random
from settings import *

#initial config

pygame.init()
pygame.display.set_caption("SnakeGame")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


#snake parameters

square_size = 20
game_speed = 10

def food_generate ():
    food_x = round(random.randrange(0, WIDTH - square_size) /square_size) * square_size       #float??
    food_y = round(random.randrange(0, HEIGHT - square_size) /square_size) * square_size      #float??

    return food_x, food_y

def draw_food (size, food_x, food_y):
    pygame.draw.rect(screen, green, [food_x, food_y, size, size])

def draw_snake (size, pixels):
    for pixel in pixels:
        pygame.draw.rect(screen, white, [pixel[0], pixel[1], size, size])

def points (score):
    font = pygame.font.SysFont("Arial", 25)
    text = font.render(f"Pontos: {score}", True, red)
    screen.blit(text, [10, 1])

def which_speed(key, current_speed_x, current_speed_y):

    if key == pygame.K_DOWN and current_speed_y == 0:
        return 0, square_size
    elif key == pygame.K_UP and current_speed_y == 0:
        return 0, -square_size
    elif key == pygame.K_RIGHT and current_speed_x == 0:
        return square_size, 0
    elif key == pygame.K_LEFT and current_speed_x == 0:
        return -square_size, 0
    
    return current_speed_x, current_speed_y

def draw_button (text, x, y, width, height, color, hover_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse [0] > x and y + height > mouse [1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, width, height))
        if click[0] == 1 and action is not None: 
            action()
    else:
        pygame.draw.rect(screen, color, (x, y, width, height))

    font = pygame.font.SysFont("Arial", 30)
    text_surf = font.render(text, True, white)
    text_rect = text_surf.get_rect(center=((x + (width/2)), (y + (height/2))))
    screen.blit(text_surf, text_rect)


def game_over_screen(score):

    end_screen = True
    while end_screen:
        screen.fill(black)
        font = pygame.font.SysFont("Arial", 50)
        text = font.render(f"Game Over! Pontos: {score}", True, red)
        screen.blit(text, [WIDTH // 6, HEIGHT // 3])

        draw_button("Restart", WIDTH // 2 - 75, HEIGHT // 2, 150, 50, green, bright_green, run_game)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_screen = False

        pygame.display.update()
        clock.tick(game_speed)





def run_game ():

    end_game = False

    x = WIDTH/2
    y = HEIGHT/2

    speed_x = square_size
    speed_y = 0

    snake_size = 1
    pixels = []

    food_x, food_y = food_generate ()

    while not end_game:
        
        #back screen

        screen.fill(black)

        #close game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = which_speed(event.key, speed_x, speed_y)

        #food generation

        draw_food(square_size, food_x, food_y)

        x += speed_x
        y += speed_y

        #snake mov

        pixels.append([x, y])
        if len(pixels) > snake_size:
            del pixels [0]

        #rules

        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                end_game = True

        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            end_game = True

        draw_snake(square_size, pixels)
        points (snake_size - 1)
        

        #screen update
        pygame.display.update()

        #new food
        if x == food_x and y == food_y:
            snake_size += 1
            food_x, food_x = food_generate ()


        clock.tick(game_speed)

        if end_game:
            game_over_screen(snake_size - 1)
            break

       
run_game()
