import pygame
import time
import random
 
# Initialize pygame
pygame.init()
 
# Set the width and height of the screen (width, height).
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Set the font for score
font_style = pygame.font.SysFont(None, 50)
 
# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
# Set snake block size
snake_block = 10
snake_speed = 30
 
# Set initial snake position
snake_x = 300
snake_y = 300

# set initial food position
foodx = 0
foody = 0

# set initial snake length
snake_List = []
snake_length = 1

# set initial direction
direction = "right"
 
# Create food for snake
def create_food():
    global foodx, foody
    foodx = round(random.randrange(0, size[0] - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, size[1] - snake_block) / 10.0) * 10.0

create_food()
 
# Main loop of the game
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
        # Change snake direction based on key press
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
            elif event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
 
    # Move snake in the direction
    if direction == "right":
        snake_x += snake_block
    elif direction == "left":
        snake_x -= snake_block
    elif direction == "up":
        snake_y -= snake_block
    elif direction == "down":
        snake_y += snake_block
    
    # check if the snake hit the wall
    if snake_x >= size[0] or snake_x < 0 or snake_y >= size[1] or snake_y < 0:
        done = True
    
    # check if the snake hit its own tail
    for block in snake_List[:-1]:
        if snake_x == block[0] and snake_y == block[1]:
            done = True

    # check if the snake ate the food
    if snake_x == foodx and snake_y == foody:
        create_food()
        snake_length += 1
    
    # update snake position
    snake_Head = []
    snake_Head.append(snake_x)
    snake_Head.append(snake_y)
    snake_List.append(snake_Head)
    if len(snake_List) > snake_length:
        del snake_List[0]
 
    # Clear screen
    screen.fill(black)
 
    # Draw snake
    for x, y in snake_List:
        pygame.draw.rect(screen, white, [x, y, snake_block, snake_block])
 
    # Draw food
    pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
    
    # Draw score
    score = font_style.render("Score: " + str(snake_length-1), True, white)
    screen.blit(score, [0,0])
 
    # Update the screen
    pygame.display.flip()
 
    # Wait
    clock.tick(snake_speed)

# End of game
pygame.quit()

