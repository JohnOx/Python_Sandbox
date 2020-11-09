import pygame
import random

pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# creating window
scr_width = 900
scr_height = 600
gameWindow = pygame.display.set_mode((scr_width, scr_height))

# Game Title
pygame.display.set_caption("Home")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def txt_scr(text, color, x, y):
    scr_text = font.render(text, True, color)
    gameWindow.blit(scr_text, [x, y])


def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])


# Game Loop

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, scr_width - 20)
    food_y = random.randint(60, scr_height - 20)
    score = 0
    init_velocity = 4
    snake_size = 30
    fps = 60  # framerate

    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            txt_scr("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.type == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.type == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.type == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 1
                food_x = random.randint(20, scr_width - 30)
                food_y = random.randint(60, scr_height - 30)
                snk_length += 5

            gameWindow.fill(white)
            txt_scr("Score: " + str(score * 10), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
            pygame.draw.line(gameWindow, red, (0, 40), (900, 40), 5)

            head = [snake_x, snake_y]
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True

            if snake_x < 0 or snake_x > scr_width - 20 or snake_y < 50 or snake_y > scr_height - 20:
                game_over = True

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()

    gameloop()
