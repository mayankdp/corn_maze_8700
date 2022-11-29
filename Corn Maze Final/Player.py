import pygame
from wall import *
import random
from Pattern import *


screen = pygame.display.set_mode((798, 500))
pumpkin=pygame.image.load("Images/pumpkin.png")
pumpkin=pygame.transform.scale(pumpkin,(30,30))


#generate random level

pattern = random.randint(1,3)
print(pattern)
maze_pattern = CreateMazeWall.rise(pattern)

# Parse the level string above. W = wall, E = exit
x = y = 1
for row in maze_pattern:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 20, 20)
        x += 30
    y += 29
    x = 1

class Player(object): 
    def __init__(self):
        self.rect = pygame.Rect(30, 30, 20, 20)
 
    def move(self, dx, dy):
        if dx != 0:
            # print("inside move")
            # print(dx)
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
            
        screen.fill((73,56,112))
        for wall in walls:
                screen.blit(pumpkin,wall.rect)
                pygame.draw.rect(screen, (73,56,112), Player().rect)
                playerImg = pygame.image.load("Images/marathon.png")
                playerImg = pygame.transform.scale(playerImg, (38, 38))
                screen.blit(playerImg, self.rect)
                
                pygame.draw.rect(screen, (255, 0, 0), end_rect)
 
    def move_single_axis(self, dx, dy):
        # print("inside move single axis")
        self.rect.x += dx
        self.rect.y += dy
        self.collision(dx, dy)
 
    def collision(self, dx, dy):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom