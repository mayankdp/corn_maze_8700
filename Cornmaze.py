#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 12:39:17 2022

@author: sushmaamara
"""

import math
import random
import os
import pygame
from pygame import mixer
import sys

global welcomescreen
welcomescreen = False

pygame.init()
screen = pygame.display.set_mode((798, 500))
background = pygame.image.load('background.png')
pygame.display.set_caption("Corn Maze")
icon = pygame.image.load('icongame.ico')
pygame.display.set_icon(icon)
main_font = pygame.font.SysFont("cambria", 50)
screen.blit(background,(0,0))

class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, "white")
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self):
		screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom) and welcomescreen == True :
			print("Button Press!")
			return True		

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = main_font.render(self.text_input, True, "green")
		else:
			self.text = main_font.render(self.text_input, True, "white")


        
	
class Player(object):
 
    def __init__(self):
        self.rect = pygame.Rect(30, 30, 20, 20)
 
    def move(self, dx, dy):
        if dx != 0:
            print("inside move")
            print(dx)
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
            
        screen.fill((73,56,112))
        for wall in walls:
                screen.blit(pumpkin,wall.rect)
                pygame.draw.rect(screen, (73,56,112), player.rect)
                playerImg = pygame.image.load("marathon.png")
                playerImg = pygame.transform.scale(playerImg, (38, 38))
                screen.blit(playerImg, self.rect)
                
                pygame.draw.rect(screen, (255, 0, 0), end_rect)
 
    def move_single_axis(self, dx, dy):
        print("inside move single axis")
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
 
class Wall(object):
 
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

os.environ["SDL_VIDEO_CENTERED"] = "1"
 
clock = pygame.time.Clock()
walls = []




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
 
# Parse the level string above. W = wall, E = exit
x = y = 1
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 20, 20)
        x += 30
    y += 29
    x = 1


button_surface = pygame.image.load("button.png")
button_surface = pygame.transform.scale(button_surface, (300, 100))
button = Button(button_surface, 400, 250, "START")
button.update()
button.changeColor(pygame.mouse.get_pos())
welcomescreen = True

pumpkin=pygame.image.load("pumpkin.png")
pumpkin=pygame.transform.scale(pumpkin,(30,30))

player = Player()


click = False
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            output=button.checkForInput(pygame.mouse.get_pos())
            if output == True:
                welcomescreen = False
                newscreen = pygame.display.set_mode((800, 500))
                screen.fill((73,56,112))
                for wall in walls:
                     screen.blit(pumpkin,wall.rect)
                     #pygame.draw.rect(screen, (255, 200, 125), player.rect)
                     pygame.draw.rect(screen, (73,56,112), player.rect)
                     playerImg = pygame.image.load("marathon.png")
                     playerImg = pygame.transform.scale(playerImg, (38, 38))
                     screen.blit(playerImg, pygame.Rect(32, 32, 20, 20))
                     pygame.draw.rect(screen, (255, 0, 0), end_rect)
                     mixer.init()
                     mixer.music.load(r"background.wav")
                     mixer.music.play()
                     
        
        if event.type == pygame.KEYDOWN:
            print("Hi")
            if event.key == pygame.K_LEFT:
                print("key Left")
                player.move(-4, 0)
            if event.key == pygame.K_RIGHT:
                player.move(4, 0)
            if event.key == pygame.K_UP:
                player.move(0, -4)
            if event.key == pygame.K_DOWN:
                player.move(0, 4)
 
        if player.rect.colliderect(end_rect):
            pygame.quit()
            sys.exit()
            
        
        

        
        pygame.display.flip()
        clock.tick(360)
                
        
        
    pygame.display.update()
