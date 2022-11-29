#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 12:39:17 2022

@author: sushmaamara, Mayank, Parita, Mattie
"""

import os
from tkinter import messagebox
import pygame
from pygame import mixer
from tkinter import *
from tkinter import messagebox
import sys
from singleton import Singleton 
from Player import *


global welcomescreen
welcomescreen = False

pygame.init()
background = pygame.image.load('Images/background.png')
pygame.display.set_caption("Corn Maze")
icon = pygame.image.load('Images/icongame.ico')
pygame.display.set_icon(icon)
main_font = pygame.font.SysFont("cambria", 50)
screen.blit(background,(0,0))

t = "Welcome to Corn Maze!"
text = main_font.render(t, True, (255, 156, 0))
textRect = text.get_rect()
textRect.center = (400, 50)
screen.blit(text, textRect)

class Button():
	def __init__(self, image, x_pos, y_pos, text_input):
		self.image = image
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_input = text_input
		self.text = main_font.render(self.text_input, True, (255, 255, 255))
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
			self.text = main_font.render(self.text_input, True, (0, 255, 0))
		else:
			self.text = main_font.render(self.text_input, True, (255, 255, 255))

class GameState():
    def __init__(self):
        self.state = 'main_game'

    def main_game(self):
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
                        pygame.draw.rect(screen, (73,56,112), singleton.player.rect)
                        playerImg = pygame.image.load("Images/marathon.png")
                        playerImg = pygame.transform.scale(playerImg, (38, 38))
                        screen.blit(playerImg, pygame.Rect(32, 32, 20, 20))
                        
                        pygame.draw.rect(screen, (73,56,112), end_rect)
                        houseImg = pygame.image.load("Images/house.png")
                        houseImg = pygame.transform.scale(houseImg, (38, 38))
                        screen.blit(houseImg, end_rect)

                        mixer.init()
                        mixer.music.load(r"Music/background.wav")
                        mixer.music.play(loops=-1)
                        
            
            if event.type == pygame.KEYDOWN:
                # print("Hi")
                if event.key == pygame.K_LEFT:
                    # print("key Left")
                    singleton.player.move(-10, 0)
                if event.key == pygame.K_RIGHT:
                    singleton.player.move(10, 0)
                if event.key == pygame.K_UP:
                    singleton.player.move(0, -10)
                if event.key == pygame.K_DOWN:
                    singleton.player.move(0, 10)
    
            if singleton.player.rect.colliderect(end_rect):
                Tk().wm_withdraw() #to hide the main window
                messagebox.showinfo('Continue','OK')
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        clock.tick(360)

os.environ["SDL_VIDEO_CENTERED"] = "1"
 
clock = pygame.time.Clock()

button_surface = pygame.image.load("Images/button.png")
button_surface = pygame.transform.scale(button_surface, (300, 100))
button = Button(button_surface, 400, 250, "START")
button.update()
button.changeColor(pygame.mouse.get_pos())
welcomescreen = True

# Singleton 
singleton = Singleton.getInstance()
singleton.player = Player()


click = False
running = True
game = GameState()
while running:
    game.main_game()