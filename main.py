import pygame, sys
from Snake import Snake
from Food import Food
import time
# Initialize Pygame
pygame.init()

# Setting some values
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)
RANDOM = (100, 100, 100)
# Set the clock(time)
clock = pygame.time.Clock()

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Super snake game")

# Render text at top of screen
text = "Happy hunting the food"
font_style = pygame.font.SysFont(None, 30)

def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [10, 0])

def paint_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, WHITE,[x[0],x[1],10,10]) 

# Main program
def main():
    # Instansiate Snake, food
    snake_1 = Snake(ORANGE, 15, 1)
    snake_list = []
    food = Food()
    # Setting starting coords
    food_cord_x, food_cord_y = food.coord_spawn()
    snake_coord_x, snake_coord_y = WINDOW_WIDTH/2, WINDOW_HEIGHT/2
    snake_coord_x_move, snake_coord_y_move = 0, 0
    text = "Super Snake"

    # Other constants
    points = 0
    game_over = False
    while not game_over:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                # returns coords to where the snake is moving
                snake_coord_x_move, snake_coord_y_move = snake_1.move(event.key)
        snake_coord_x += snake_coord_x_move
        snake_coord_y += snake_coord_y_move

        screen.fill(BLACK)
        pygame.draw.rect(screen, food.color(),[food_cord_x, food_cord_y,10,10]) 

        # Collision with walls
        if(snake_coord_x < 0 or snake_coord_x >= WINDOW_WIDTH or snake_coord_y < 30 or snake_coord_y >= WINDOW_HEIGHT):
            print(snake_coord_x, snake_coord_y)
            text = "GAME OVER: Collision with walls"
            game_over = True

        # Eating food
        if((food_cord_x, food_cord_y) == (snake_coord_x , snake_coord_y)):
            points += 1
            text = "POINTS: {}".format(points)
            food_cord_x, food_cord_y = food.coord_spawn()
            # for fun more speed on snake
            snake_1.speed += 5
            snake_1.length += 1

        snake_list = snake_1.snake_body(snake_coord_x, snake_coord_y)
        if len(snake_list) > snake_1.length:
            del snake_list[0]
        # Collision with self
        if snake_list.count(snake_list[0]) > 1 and snake_1.length > 1:
            text = "GAME OVER: Collision with self"
            game_over = True

        paint_snake(snake_list)
        message(text, WHITE)
        pygame.display.update()
        clock.tick(snake_1.speed)

    message(text, ORANGE)
    time.sleep(4)
    pygame.quit()
    sys.exit()

main()