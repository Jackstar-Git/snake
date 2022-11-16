import pygame
from sys import exit
import random

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

grey = (55, 55, 55)
blue = (42, 4, 194)
light_blue = (60, 126, 255)

x_pos = 40
y_pos = 240
x_velocity = 20
y_velocity = 0

snake_list = []

speed = 7
length = 2
is_boosted = False

my_font = pygame.font.SysFont('Comic Sans MS', 19)


def draw_snake():
    for idx, block in enumerate(snake_list, start=1):
        if idx == len(snake_list):
            pygame.draw.rect(screen, blue, [block[0], block[1], 18, 18])
        else:
            pygame.draw.rect(screen, light_blue, [block[0], block[1], 18, 18])



food_x = 300
food_y = 240

food_rect = pygame.Rect(food_x, food_y, 20, 20)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w and y_velocity != 20:
                y_velocity = -20
                x_velocity = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s and y_velocity != -20:
                y_velocity = 20
                x_velocity = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d and x_velocity != -20:
                y_velocity = 0
                x_velocity = 20
            if event.key == pygame.K_LEFT or event.key == pygame.K_a and x_velocity != 20:
                y_velocity = 0
                x_velocity = -20
            if event.key == pygame.K_b:
                if is_boosted:
                    speed /= 2
                    is_boosted = False
                elif not is_boosted:
                    speed *= 2
                    is_boosted = True



    x_pos += x_velocity
    y_pos += y_velocity
    screen.fill(grey)



    for i in range(0, 500, 20):
        pygame.draw.line(screen, (75, 75, 75), (0,i), (500,i))
    for i in range(0, 500, 20):
        pygame.draw.line(screen, (75, 75, 75), (i, 0), (i, 500))

    pygame.draw.rect(screen, "green", food_rect)

    snake_block = [x_pos, y_pos]
    snake_list.append(snake_block)

    if len(snake_list) > length:
        del snake_list[0]

    draw_snake()
    if x_pos < 0 or x_pos > 480:
        pygame.quit()
    elif y_pos < 0 or y_pos > 480:
        pygame.quit()
    for x in snake_list[:-1]:
        if x == snake_block:
            pygame.quit()

    if x_pos == food_x and y_pos == food_y:
        food_x = round(random.randrange(20, 460) / 20) * 20
        food_y = round(random.randrange(20, 460) / 20) * 20
        food_rect = pygame.Rect(food_x, food_y, 20, 20)

        length += 1

        if is_boosted:
            speed += (0.215 * (length / 3.25))*2
        else:
            speed += 0.215 * (length / 3.25)

    text_surface = my_font.render(f'Score: {length - 2}   Speed: {round(speed, 2)}', True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))



    pygame.display.update()
    clock.tick(speed)
