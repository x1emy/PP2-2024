import pygame
import sys
import copy
import random
import time
import psycopg2
from color_palette import *
print("Enter your name")
name = input()

db = psycopg2.connect(dbname='Lab10', user='postgres', password='1234', host='localhost')
current = db.cursor()

sql="""
    CREATE TABLE IF NOT EXISTS Scores(
        player_name VARCHAR,
        player_score VARCHAR
    );
"""
current.execute(sql)

pygame.init()

WIDTH = 600
HEIGHT = 600

CELL = 30

def draw_grid():
    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]

    for i in range(HEIGHT // 2):
        for j in range(WIDTH // 2):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

screen = pygame.display.set_mode((HEIGHT, WIDTH))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"
#coding snake
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
    #coloring from palette
    def draw(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            print("Got food!")
            self.body.append(Point(head.x, head.y))
#coding food
class Food:
    def __init__(self, snake):
        self.snake = snake
        self.pos = self.generate_position()
        self.timer_start = time.time()  # Start timer for food
        self.timer_duration = random.randint(3, 6)  # Random duration between 3 to 6 seconds
        self.score = random.choice([1, 2, 5])  # Different scores for food items
    #position of food
    def generate_position(self):
        while True:
            x = random.randint(0, WIDTH // CELL - 1)
            y = random.randint(0, HEIGHT // CELL - 1)
            if Point(x, y) not in self.snake.body:
                return Point(x, y)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def is_expired(self):
        return time.time() - self.timer_start > self.timer_duration

FPS = 5
clock = pygame.time.Clock()

snake = Snake()
food = None  

score = 0
level = 1

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -1

    head = snake.body[0]
    if head.x < 0 or head.x >= WIDTH // CELL or head.y < 0 or head.y >= HEIGHT // CELL:
        print("Game Over!")
        done = True

    draw_grid_chess()

    snake.move()
    if food is None or food.is_expired():  #Check if food is expired or not yet generated
        food = Food(snake)

    snake.check_collision(food)

    if snake.body[0].x == food.pos.x and snake.body[0].y == food.pos.y:
        score += food.score  
        food = Food(snake)  #Generate new food
        if score % 3 == 0:
            FPS += 1
            print("Level Up!")

    snake.draw()
    food.draw()

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 100, 0))
    level_text = font.render(f"Level: {level}", True, (255, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    pygame.display.flip()
    clock.tick(FPS)
