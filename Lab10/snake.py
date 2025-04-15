import pygame, sys
import psycopg2
import csv
from config import load_config
from pygame.locals import *
import random, time
config = load_config()
null = 0
with psycopg2.connect(**config) as conn:
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Scores (
                name VARCHAR(100) PRIMARY KEY,
                level INT,
                score INT
            )
        """)
        conn.commit()
def load_or_create_player(name, conn):
    with conn.cursor() as cur:
        cur.execute("SELECT level FROM Scores WHERE name = %s", (name,))
        result = cur.fetchone()
        if result:
            return int(result[0])
        else:
            cur.execute("INSERT INTO Scores (name, level) VALUES (%s, %s)", (name, '1'))
            conn.commit()
            return 1
def update_player_level(name, level, conn):
    with conn.cursor() as cur:
        cur.execute("UPDATE Scores SET level = %s WHERE name = %s", (level, name))
        conn.commit()
def null_player_score(name, null, conn):
    with conn.cursor() as cur:
        cur.execute("UPDATE Scores SET score = %s WHERE name = %s", (null, name))
        conn.commit()
def update_player_score(name, score, conn):
    with conn.cursor() as cur:
        cur.execute("UPDATE Scores SET score = %s WHERE name = %s", (score, name))
        conn.commit()
pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()
level_goals = [10, 20, -1]  
level_speeds = [5, 7, 9 ]
level_walls = {
    2: [(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (16, 17), (16, 19), (16, 18), (16, 16), (16, 15), (16, 14)],     
    3: [(13, 3), (13, 4), (13, 5), (13, 6), (8, 3), (8, 4), (8, 5), (8, 6), (13, 15), (12, 15), (11, 15), (10, 15), (9, 15), (8,15)] 
}
BLUE  = (0, 0, 255)
YELLOW = (255, 255, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (211, 211, 211)
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
WIDTH = 600
HEIGHT = 600
CELL = 30
SCORE = 0
LEVEL = 1
PAUSED = False
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
Screen.fill(WHITE)
DISAPPEAR = pygame.USEREVENT + 1
#All we need for title screen:
running = False
font_mid = pygame.font.SysFont("Verdana", 30)
input_box = pygame.Rect(200, 200, 240, 40)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
walls = []

def draw_grid_chess():
    colors = [WHITE, GRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(Screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

class Wall:
    def __init__(self, x, y):
        self.xf = x
        self.yf = y
        self.pos = Point(self.xf, self.yf)
    def draw(self):
        pygame.draw.rect(Screen, BLACK, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

def load_walls(LEVEL):
    walls.clear()
    for pos in level_walls.get(LEVEL, []):
        walls.append(Wall(pos[0], pos[1]))   
    
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1 #shows in which direction we go
        self.dy = 0
    
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x #previous part of body goes on position of next part
            self.body[i].y = self.body[i - 1].y
        
        self.body[0].x += self.dx
        self.body[0].y += self.dy
    
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(Screen, RED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(Screen, YELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        global SCORE, LEVEL, FPS, text
        for i in self.body[1:]:
            if head.x == i.x and head.y == i.y: #game over screen if snake eats itself
                time.sleep(1)
                   
                Screen.fill(RED)
                Screen.blit(game_over, (WIDTH // 4, HEIGHT / 2.5))
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                sys.exit()
            for wall in walls:
                if head.x == wall.pos.x and head.y == wall.pos.y:
                    time.sleep(1)
                    Screen.fill(RED)
                    Screen.blit(game_over, (WIDTH // 4, HEIGHT / 2.5))
                    pygame.display.flip()
                    time.sleep(2)
                    pygame.quit()
                    sys.exit()
        if head.x == food.pos.x and head.y == food.pos.y:
            SCORE += random.randint(1, 3)#random weight
            
            if LEVEL <= 2 and SCORE >= level_goals[LEVEL - 1]:
                time.sleep(2)
                SCORE = 0
                LEVEL += 1
                null_player_score(text, null, conn)
                update_player_level(text, LEVEL, conn)
                load_walls(LEVEL)
                FPS == level_speeds[LEVEL - 1]
                snake.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
                snake.dx = 1 
                snake.dy = 0
                food.generate_random_pos(snake, walls)
                

            print("Got food!")
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self, walls)
        if head.x < 0 or head.x > WIDTH // CELL - 1 or head.y > HEIGHT // CELL - 1 or head.y < 0: #dies from walls
            time.sleep(1)
                   
            Screen.fill(RED)
            Screen.blit(game_over, (WIDTH // 4, HEIGHT / 2.5))
            pygame.display.flip()
            time.sleep(2)
            pygame.quit()
            sys.exit()
        

        

class Food:
    def __init__(self):
        self.xf = 0
        self.yf = 0
        self.pos = Point(self.xf, self.yf)
    def generate_random_pos(self, snake, walls):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)

            on_snake = any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake.body)
            on_wall = any(wall.xf == self.pos.x and wall.yf == self.pos.y for wall in walls)
            if not on_snake and not on_wall:
                break
        if running and not PAUSED:
            pygame.time.set_timer(DISAPPEAR, 5000) #timer for 5 seconds that activates userevent that regenerates position of food
    def draw(self):
        
        pygame.draw.rect(Screen, GREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


food = Food()

snake = Snake()
food.generate_random_pos(snake, walls)

while True:
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == DISAPPEAR:
            if not PAUSED:
                food.generate_random_pos(snake, walls)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1
            elif event.key == pygame.K_p:
                PAUSED = not PAUSED
            elif event.key == pygame.K_s and PAUSED:
                update_player_score(text, SCORE, conn)
                if PAUSED:
                    pygame.time.set_timer(DISAPPEAR, 0)  
                else:
                    pygame.time.set_timer(DISAPPEAR, 5000)
            elif not running and active:
                if event.key == pygame.K_RETURN and text:
                    FPS = 5
                    LEVEL = load_or_create_player(text, conn)
                    running = True

                elif event.key == pygame.K_BACKSPACE and active:
                    text = text[:-1]
                else:
                    if event.key != pygame.K_RETURN:
                        text += event.unicode
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
            color = color_active if active else color_inactive
            
        
    
    if running:
        Screen.fill(BLACK)
        draw_grid_chess()
        if not PAUSED:
            snake.move()
        snake.check_collision(food)
        load_walls(LEVEL)
        for wall in walls:
            wall.draw()
        snake.draw()
        food.draw()
        
        scores = font_small.render(str(SCORE), True, BLACK)
        levels = font_small.render(str(LEVEL), True, BLACK)
        Screen.blit(scores, (10, 10))
        Screen.blit(levels, (10, 30))
    else:
        Screen.fill((30, 30, 30))
        prompt = font_mid.render("Введите имя и нажмите Enter:", True, (255, 255, 255))
        Screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, 100))

        txt_surface = font_mid.render(text, True, color)
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        Screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(Screen, color, input_box, 2)
    pygame.display.flip()
    FramePerSec.tick(FPS)