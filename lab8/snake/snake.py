import pygame, sys, random

pygame.init()

pygame.init()
pygame.mixer.init()

# SOnic
pygame.mixer.music.load("01 Green Hill Zone Act 1.mp3")
pygame.mixer.music.play(-1)


CELL_SIZE = 20
GRID_WIDTH = 30
GRID_HEIGHT = 20
SCREEN = pygame.display.set_mode((GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE))
pygame.display.set_caption("Snake Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255,255,0)
BLUE = (0,0,255)
PINK = (255,192,203)

walls =[]
clock = pygame.time.Clock()
font = pygame.font.SysFont("AniAce.ttf", 20)


snake = [(5, 5), (4, 5), (3, 5)]  
direction = (1, 0)  
score = 0
level = 1
speed = 8

def random_food():
    while True:
        pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        if pos not in snake and pos not in walls:
            return pos

food = random_food()

def draw_grid():
    col = 0-1
    SCREEN.fill(BLACK)
    for x, y in snake:
        color = (
            WHITE,
            GREEN,
            YELLOW
        )
        #drawing
        pygame.draw.rect(SCREEN, color[col+1], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))
        col = (col+1)%2
    for wx, wy in walls:
        pygame.draw.rect(SCREEN, PINK, (wx * CELL_SIZE, wy * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))
    pygame.draw.rect(SCREEN, RED, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1))
    

    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    SCREEN.blit(text, (10, 10))

def game_over():
    msg = font.render("Game Over!", True, RED)
    SCREEN.blit(msg, (GRID_WIDTH * CELL_SIZE // 2 - 60, GRID_HEIGHT * CELL_SIZE // 2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()


while True:
    #progression
    if level == 2:
        
        walls = [
            (x, 0) for x in range(GRID_WIDTH)
        ] + [
            (x, GRID_HEIGHT - 1) for x in range(GRID_WIDTH)
        ] + [
            (0, y) for y in range(GRID_HEIGHT)
        ] + [
            (GRID_WIDTH - 1, y) for y in range(GRID_HEIGHT)
        ]
    if level == 3:
        
        walls = [
            (x, 0) for x in range(GRID_WIDTH)
        ] + [
            (x, GRID_HEIGHT - 1) for x in range(GRID_WIDTH)
        ] + [
            (0, y) for y in range(GRID_HEIGHT)
        ] + [
            (GRID_WIDTH - 1, y) for y in range(GRID_HEIGHT)
        ] + [(GRID_WIDTH/2 , y ) for y in range (int(GRID_HEIGHT/4), GRID_HEIGHT - int(GRID_HEIGHT/4))]

    if level >= 4:
        if random.randint(1, 30) == 1:
            food = random_food()


    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake[0][1]!=(snake[1][1]+1):
                direction = (0, -1)
            elif event.key == pygame.K_DOWN  and snake[0][1]!=(snake[1][1]-1):
                direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake[0][0]!=(snake[1][0]+1):
                direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake[0][0]!=(snake[1][0]-1):
                direction = (1, 0)

    
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    
    if new_head[0] < 0:
        new_head = (GRID_WIDTH, new_head[1])
    if new_head[0] > GRID_WIDTH:
        new_head = (0, new_head[1])
    if new_head[1] < 0:
        new_head = (new_head[0], GRID_HEIGHT)
    if new_head[1] > GRID_HEIGHT:
        new_head = (new_head[0], 0)

    # Check collision
    if new_head in snake:
        game_over()
    if new_head in walls:
        game_over()

    snake.insert(0, new_head)

    
    #food react
    if new_head == food:
        score += 1
        
        if score % 3 == 0:
            level += 1
            if level > 2:
                walls = walls + [random_food()]
            speed += 2
        food = random_food()
    else:
        snake.pop()  

    draw_grid()
    pygame.display.flip()
    clock.tick(speed)
