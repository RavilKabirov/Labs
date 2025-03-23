import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

FPS = 5
FramePerSec = pygame.time.Clock()

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
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
Screen.fill(WHITE)

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(Screen, GRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [WHITE, GRAY]

    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(Screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x}, {self.y}"

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
    
    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
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
        global SCORE, LEVEL, FPS
        for i in self.body[1:]:
            if head.x == i.x and head.y == i.y:
                time.sleep(1)
                   
                Screen.fill(RED)
                Screen.blit(game_over, (WIDTH // 4, HEIGHT / 2.5))
                pygame.display.flip()
                time.sleep(2)
                pygame.quit()
                sys.exit()
        if head.x == food.pos.x and head.y == food.pos.y:
            SCORE += 1
            if SCORE % 3 == 0:
                LEVEL += 1
                FPS += 1
            print("Got food!")
            self.body.append(Point(head.x, head.y))
            food.generate_random_pos(self)
        if head.x < 0 or head.x > WIDTH // CELL - 1 or head.y > HEIGHT // CELL - 1 or head.y < 0:
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
    def generate_random_pos(self, snake):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)

            if not any(segment.x == self.pos.x and segment.y == self.pos.y for segment in snake.body):
                break   

    def draw(self):
        
        pygame.draw.rect(Screen, GREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


food = Food()

snake = Snake()
food.generate_random_pos(snake)

while True:
    
    #Цикл всех событий
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
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
       
    Screen.fill(BLACK)
    draw_grid_chess()
    snake.move()
    snake.check_collision(food)

    snake.draw()
    food.draw()
    
    scores = font_small.render(str(SCORE), True, BLACK)
    levels = font_small.render(str(LEVEL), True, BLACK)
    Screen.blit(scores, (30,30))
    Screen.blit(levels, (90,30))
    pygame.display.flip()
    FramePerSec.tick(FPS)