import pygame, sys, random, psycopg2, json

softlock = True
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",    
    password="new_password",  
    host="localhost",
    port="5432"
)
cur = conn.cursor()


cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    level INTEGER DEFAULT 1
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    username TEXT PRIMARY KEY,
    score INTEGER,
    snake TEXT,
    direction TEXT,
    extra INTEGER,
    food TEXT,
    speed INTEGER,
    FOREIGN KEY (username) REFERENCES users(username)
)
""")
conn.commit()

# -------------------- USER LOGIN --------------------
username = input("Enter your username: ").strip()

cur.execute("SELECT level FROM users WHERE username=%s", (username,))
row = cur.fetchone()
if row:
    level = row[0]
    print(f"Welcome back {username}, current level: {level}")
    
    cur.execute("SELECT * FROM user_score WHERE username=%s", (username,))
    saved = cur.fetchone()
    if saved:
        score = saved[1]
        snake = json.loads(saved[2])
        direction = tuple(json.loads(saved[3]))
        extra = saved[4]
        food = tuple(json.loads(saved[5]))
        speed = saved[6]
        
    else:
        snake = [(5,5), (4,5), (3,5)]
        direction = (1,0)
        score = 0
        extra = 0
        speed = 8
        food = (random.randint(1,28), random.randint(1,18))
else:
    level = 1
    snake = [(5,5), (4,5), (3,5)]
    direction = (1,0)
    score = 0
    extra = 0
    speed = 8
    cur.execute("INSERT INTO users(username) VALUES(%s)", (username,))
    conn.commit()
    food = (random.randint(1,28), random.randint(1,18))
# -------------------- PYGAME SETUP 
pygame.init()
pygame.mixer.init()
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
PURPLE = (128, 0 ,128)

walls =[]
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
WEIGHT = 0

# -------------------- HELPER FUNCTIONS --------------------
def random_food():
    while True:
        pos = (random.randint(1, GRID_WIDTH - 2), random.randint(1, GRID_HEIGHT - 2))
        if pos not in snake and pos not in walls:
            return pos

def draw_grid():
    SCREEN.fill(BLACK)
    col = 0
    for x, y in snake:
        color = [WHITE, GREEN, YELLOW]
        pygame.draw.rect(SCREEN, color[col % 3], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1))
        col += 1
    for wx, wy in walls:
        pygame.draw.rect(SCREEN, PINK, (wx * CELL_SIZE, wy * CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1))
    pygame.draw.rect(SCREEN, [RED, PURPLE][WEIGHT], (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE-1, CELL_SIZE-1))
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    SCREEN.blit(text, (10,10))

def game_over():
    msg = font.render("Game Over!", True, RED)
    SCREEN.blit(msg, (GRID_WIDTH*CELL_SIZE//2 - 60, GRID_HEIGHT*CELL_SIZE//2))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

def save_game():
    cur.execute("""
    INSERT INTO user_score(username, score, snake, direction, extra, food, speed)
    VALUES(%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (username) DO UPDATE SET
        score = EXCLUDED.score,
        snake = EXCLUDED.snake,
        direction = EXCLUDED.direction,
        extra = EXCLUDED.extra,
        food = EXCLUDED.food,
        speed = EXCLUDED.speed
    """, (username, score, json.dumps(snake), json.dumps(direction), extra, json.dumps(food), speed))
    conn.commit()


# -------------------- GAME LOOP --------------------
while True:

    walls = []
    if level >= 2 and softlock == False:
        walls = [(x,0) for x in range(GRID_WIDTH)] + [(x,GRID_HEIGHT-1) for x in range(GRID_WIDTH)] + \
                [(0,y) for y in range(GRID_HEIGHT)] + [(GRID_WIDTH-1,y) for y in range(GRID_HEIGHT)]
    if level >= 3 and softlock == False:
        walls += [(GRID_WIDTH//2, y) for y in range(GRID_HEIGHT//4, GRID_HEIGHT - GRID_HEIGHT//4)]
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake[0][1] != snake[1][1]+1:
                direction = (0,-1)
            elif event.key == pygame.K_DOWN and snake[0][1] != snake[1][1]-1:
                direction = (0,1)
            elif event.key == pygame.K_LEFT and snake[0][0] != snake[1][0]+1:
                direction = (-1,0)
            elif event.key == pygame.K_RIGHT and snake[0][0] != snake[1][0]-1:
                direction = (1,0)
            elif event.key == pygame.K_p:  # Pause + Save
                save_game()
                paused = True
                while paused:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif e.type == pygame.KEYDOWN and e.key == pygame.K_p:
                            paused = False

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    
    # Wrap around
    if new_head[0] < 0: new_head = (GRID_WIDTH-1, new_head[1])
    if new_head[0] >= GRID_WIDTH: new_head = (0, new_head[1])
    if new_head[1] < 0: new_head = (new_head[0], GRID_HEIGHT-1)
    if new_head[1] >= GRID_HEIGHT: new_head = (new_head[0], 0)
    
    # Collisions
    if new_head in snake or new_head in walls:
        save_game()
        game_over()
    
    snake.insert(0, new_head)

    # Food
    if new_head == food:
        softlock = False
        extra += WEIGHT + 1
        score += 1 + WEIGHT
        if score % 3 == 0:
            level = score/3
            speed += 2
            cur.execute("UPDATE users SET level=%s WHERE username=%s", (level, username)) 
            conn.commit()
        WEIGHT = random.randint(0,1)
        food = random_food()
    if extra == 0:
        snake.pop()
    else:
        extra -= 1

    draw_grid()
    pygame.display.flip()
    clock.tick(speed)
