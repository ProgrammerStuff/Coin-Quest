
#Made byMichael Burgin, 2022
#This is a simple 2d side-scrolling platformer game

print("Loading")
#Imports
import pygame
import time
from pygame.locals import *
import sys
import keyboard
import os
import pynput
#import keyboard


#Global variables
#D O  N O T  D E L E T E  "a = 0" I T  W I L L  B R E A K  E V E R Y T H I N G
a = 0
origin = (0, 0)
levelnumber = 0
#Resets every 20 frames, used to update more intensive elements
slowtimer = 0

white = (255, 255, 255)
red = (255, 0, 0)
orange = (225, 100, 0)
yelow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indago = (192, 107, 255)
purple = (150, 0, 150)
black = (0, 0, 0)

#Keybinds, if you want to change them.
A_button = "K"
B_button = "L"
Up_button = "W"
Down_button = "S"
Left_button = "A"
Right_button = "D"
Special_button = "Key.space"
Pause_buton = "Key.escape"


#Classes
#General purpose tools that will help us place graphical elements on screen
class GraphicalTools:
    #This puts up text in a select place in a typewriter fasion.
    #Input is a string in which we want to place on screen, speed is time (in seconds) between each character placement
    #Startplacex/y is the x and y of where we will start placeing text. Length is the amount of characters to print before newlining.
    def Typewriter(input, speed, startplacex, startplacey, length):
        for letter in input:
            pass


    def ClickyButton(style, startx, starty, endx, endy, color):
        pass


    #recommended font: 'freesandsbold.ttf', reccomended size: 32
    def TextBoxMaker(font, locationx, locationy, text, textsize, color1, color2):
        str_text = str(text)
        textboxfont = pygame.font.Font(font, textsize)
        Content = textboxfont.render(str_text.encode(), True, color1, color2)
        textrect = Content.get_rect()
        textrect.center = (locationx, locationy)
        canvas.blit(Content, textrect)
        return

#File management tools to read and write game progress and savestates.
class FileIO:
    def WriteToFile(Input, savefile):
        pass


    def ReadFromFile(savefile):
        pass


    def DeleteFile(savefile):
        pass


    def MakeFile(name):
        pass


class Levels:
    def TitleScreen():
        while a == 0:
            canvas.fill(white)
            canvas.blit(TitleScreenImage, dest = origin)
            #To display a number on the top right
            str_position = str(pygame.mouse.get_pos())
            GraphicalTools.TextBoxMaker('freesansbold.ttf', 100, 50, str_position, 32, black, white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            pygame.display.flip()
            time.sleep(0.017)

        #main titlescreen loop



#Create the canvas on which we put the game on
canvas = pygame.display.set_mode((1000, 650))
#Title of window
pygame.display.set_caption("Platformer game by Michael Burgin")
TitleScreenImage = pygame.image.load("Homescreen1000x650.png")

def main():
    pygame.init()
    Gamertime = True
    #main game loop
    while Gamertime == True:
        #Switch to appropiate level
        if levelnumber == 0:
            Levels.TitleScreen()


        #Check if user closed window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        #update the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()


#str_position = str(pygame.mouse.get_pos())
#text = font.render(str_position.encode(), True, black, white)
#textrect = text.get_rect()
#textrect.center = (100, 50)