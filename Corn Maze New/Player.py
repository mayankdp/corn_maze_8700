import pygame
from wall import *

screen = pygame.display.set_mode((798, 500))
pumpkin=pygame.image.load("Images/pumpkin.png")
pumpkin=pygame.transform.scale(pumpkin,(30,30))

# Holds the level layout in a list of strings.
level = """
WWWWWWWWWWWWWWWWWWWWWWWWWWW
W                         W               
W   WWWW  WWWWWWWWWW  WW  W    
W   W             W       W       
W   W          WWWWWWWWW  W           
W  WW  WWWW        W   W  W    
W   W     W W      W   W  W       
W   W     W   WWW  W   W  W       
W   WWW WWW   W W  W   W  W       
W     W   W   W W      W  W         
WWW   W   WWWWW W      W  W        
W W      WW       WWWW    W        
W W   WWWW   WWW          W       
W              W  WWWWWWWWW        
WWWWWW  WWWWWWWW          W
W                       E W
WWWWWWWWWWWWWWWWWWWWWWWWWWW                                      
""".splitlines()[1:]
    
level2 = """
WWWWWWWWWWWWWWWWWWWWWWWWWWW
W                         W               
W   WWWWWWWWWWW  WWWWWW   W    
W   W             W       W       
W   W          WWWWWWWWW  W           
W  WWWWWWWW            W  W    
W   W     W   WWWWWWW  W  W       
W   W     W   W        W  W       
W   WWW   W   W W      W  W       
W     W   W   W W      W  W         
WWW   W   W   W W      W  W        
W W      WW       WWWW    W        
W W   WWWWW   WWW         W       
W              W  WWWWWWWWW        
WWWWWWWWWWWWWWWW          W
W                       E W
WWWWWWWWWWWWWWWWWWWWWWWWWWW                                      
""".splitlines()[1:]

level3 = """
WWWWWWWWWWWWWWWWWWWWWWWWWWW
W   WWWWWWWW              W               
W   WWWWWWWWWWW  WWWWWW   W    
W   W             W       W       
W   W          WWWWWWWWW  W           
W  WWWWWWWW            W  W    
W   W     W   WWWWWWW  W  W       
W   W     W   W        W  W       
W   WWW   W   W W      W  W       
W     W   W   W W      W  W         
WWW   W   W   W W      W  W        
W W      WW       WWWW    W        
W W   WWWWW   WWW         W       
W              W  WWWWWWWWW        
WWWWWWWWWWWWWWWW          W
W                       E W
WWWWWWWWWWWWWWWWWWWWWWWWWWW                                      
""".splitlines()[1:]

# Parse the level string above. W = wall, E = exit
x = y = 1
for row in level3:
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