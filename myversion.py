import math
import random
import os
import pygame
from pygame import mixer
import sys

class Screen():
    #Initialize python game
    pygame.init()

    #Create Screen
    screen = pygame.display.set_mode((800,500))


class Player(Screen):

    def player(self,playerX, playerY):
        playerImg = pygame.image.load(r'/home/parita/Desktop/CPSC8700/#FinalProject/Images/marathon.png')
        playerImg = pygame.transform.scale(playerImg, (40,40))
        Screen.screen.blit(playerImg, (playerX, playerY))
       
class Maze(Screen):
 
    #def maze(self):
        #background = pygame.image.load(r'/home/parita/Desktop/CPSC8700/#FinalProject/Images/background.png')
        #walls.append(self)
        #self.rect = pygame.Rect(pos[0], pos[1], 16, 16)
        #mazeX = 0
        #mazeY = 0
        #Screen.screen.blit(background, (0,0))

    def draw(self):
        maze = [ 1,1,1,1,1,1,1,1,1,1,
                1,0,0,0,0,0,0,0,0,1,
                1,1,1,0,1,1,1,1,1,1,
                1,0,0,0,1,1,1,1,0,1,
                1,0,1,0,0,0,0,0,0,1,
                1,0,0,1,1,1,1,1,0,1,
                1,0,0,1,1,5,0,0,0,1,
                1,1,0,0,0,0,1,1,0,1,
                1,1,1,1,1,1,1,1,1,1,]
        bx = 0
        by = 0
        M = 10
        N = 9
        pumpkin=pygame.image.load(r"/home/parita/Desktop/CPSC8700/#FinalProject/Images/pumpkin.png")
        pumpkin=pygame.transform.scale(pumpkin,(44,44))
        for i in range(0,M*N):
            if maze[ bx + (by*M) ] == 1:
                Screen.screen.blit(pumpkin,( bx * 44 , by * 44))

            elif maze[ bx + (by*M) ] == 5:
                end_rect = pygame.Rect(bx * 44 , by * 44, 40, 40)
                pygame.draw.rect(Screen.screen, (255, 0, 0), end_rect)
            bx = bx + 1
            if bx > M-1:
                bx = 0 
                by = by + 1

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
        mixer.music.load(r"/home/parita/Desktop/CPSC8700/#FinalProject/Music/strangerthings.wav")
        mixer.music.play(-1)
        playerX = 40
        playerY= 40
        playerX_change = 0
        playerY_change = 0
        while running:
            Screen.screen.fill((73,56,112))
            '''
            for wall in walls:
                Screen.screen.blit(pumpkin,wall.rect)
                Screen.screen.blit(playerImg)
                pygame.draw.rect(screen, (255, 0, 0), end_rect)
            '''
            Maze.draw(self) 
            Player.player(self,playerX, playerY)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        #print("key Left")
                        playerX_change = -0.1
                        playerY_change = 0
                        #Player.player.move(-2, 0)
                    if event.key == pygame.K_RIGHT:
                        #print("key Right")
                        playerX_change = 0.1
                        playerY_change = 0
                    if event.key == pygame.K_UP:
                        playerY_change = -0.1
                        playerX_change = 0
                        #Player.player.move(0, -2)
                    if event.key == pygame.K_DOWN:
                        playerY_change = 0.1
                        playerX_change = 0
                    #Player.player.move(0, 2)
                    #print("key Down")
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN: 
                        playerX_change = 0
                        playerY_change = 0
            playerX += playerX_change
            playerY += playerY_change
            Player.player(self,playerX,playerY)
            pygame.display.flip()
            pygame.display.update()  

        
