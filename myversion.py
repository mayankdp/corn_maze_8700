import math
import random
import os
import pygame
from pygame import mixer
import sys
#import Welcome

class Screen():
    #Initialize python game
    pygame.init()

    #Create Screen
    screen = pygame.display.set_mode((800,800))
    pygame.display.set_caption("Corn Maze")
    icon = pygame.image.load(r'Images/icongame.ico')
    pygame.display.set_icon(icon)
    main_font = pygame.font.SysFont("cambria", 50)

class Player(Screen):

    def player(self,playerX, playerY):
        playerImg = pygame.image.load(r'Images/marathon.png')
        #playerImg = pygame.transform.scale(playerImg, (44,44))
        Screen.screen.blit(playerImg, (playerX, playerY))
       
class Maze(Screen):
 
    #def maze(self):
        #background = pygame.image.load(r'/home/parita/Desktop/CPSC8700/#FinalProject/Images/background.png')
        #walls.append(self)
        #self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        #mazeX = 0
        #mazeY = 0
        #Screen.screen.blit(background, (0,0))

    tiles = [r"Images/empty.png", r"Images/pumpkin.png", r"Images/trophy.png"]
    TileSize = 64
    maze = [ [1,1,1,1,1,1,1,1,1,1],
                [1,0,0,0,0,0,0,0,0,1],
                [1,1,1,0,1,1,1,1,1,1],
                [1,0,0,0,1,1,1,1,0,1],
                [1,0,1,0,0,0,0,0,0,1],
                [1,0,0,1,1,1,1,1,0,1],
                [1,0,0,1,1,2,0,0,0,1],
                [1,1,0,0,0,0,1,1,0,1],
                [1,1,1,1,1,1,1,1,1,1]]
    def draw(self):
        
        #pumpkin=pygame.image.load(r"/home/parita/Desktop/CPSC8700/#FinalProject/Images/pumpkin.png")
        #pumpkin=pygame.transform.scale(pumpkin,(64,64))

        for row in range(len(Maze.maze)):
            for column in range(len(Maze.maze[row])):
                x = column * Maze.TileSize
                y = row * Maze.TileSize
                tile = Maze.tiles[Maze.maze[row][column]]
                tile_i = pygame.image.load(tile)
                #if maze[row][column] == 1: tile_i=pygame.transform.scale(tile_i,(40,40))
                Screen.screen.blit(tile_i, (x, y))
        '''
        for row in range(len(maze)):
            for column in range(len(maze[row])):
                x = column * TileSize
                y = row * TileSize
                tile = tiles[maze[row][column]]
                Screen.screen.blit(pumpkin, (x, y))
        '''
class Game(Player,Maze):
    __instance = None

    def __init__(self):
        if Game.__instance != None:
            raise Exception("This is a Singleton class!")
        else:
            Game.__instance = self

    def run(self):
        running = True
        #Background Sound
        mixer.music.load(r"Music/strangerthings.wav")
        mixer.music.play(-1)
        playerX = 64
        playerY= 64

        while running:
            Screen.screen.fill((0,0,0))
            '''
            for wall in walls:
                Screen.screen.blit(pumpkin,wall.rect)
                Screen.screen.blit(playerImg)
                pygame.draw.rect(screen, (255, 0, 0), end_rect)
            '''
            #current = Maze.tiles[Maze.maze[1][1]]
            Maze.draw(self) 
            Player.player(self,playerX, playerY)    

            for event in pygame.event.get():
                row = int(playerY / Maze.TileSize)
                column = int(playerX / Maze.TileSize)
                
                if event.type == pygame.QUIT:
                    running = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        #print("key Left")
                        column -= 1
                        #Player.player.move(-2, 0)

                    if event.key == pygame.K_RIGHT:
                        #print("key Right")
                        column += 1

                    if event.key == pygame.K_UP:
                        row = row - 1
                        #Player.player.move(0, -2)

                    if event.key == pygame.K_DOWN:
                        row += 1

                current = Maze.tiles[Maze.maze[row][column]]
                if current == r"Images/trophy.png":
                    runnning = False
                    white = (255, 255, 255)

                    newScreen = pygame.display.set_mode((400, 400))
                    newScreen.fill(white)
                    pygame.display.set_caption('Game Over')
                    font = pygame.font.Font('freesansbold.ttf', 32)
                    text = font.render('Game Over: You won...!', True, (0, 255, 0), white)
                    #Screen.screen = False
                    newScreen.blit(text,(400,400))
                    
            if current == r'Images/empty.png':
                playerY = row * 64
                playerX = column*64

            Player.player(self,playerX,playerY)

            pygame.display.flip()
            pygame.display.update()  

        
