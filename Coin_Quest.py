#Made byMichael Burgin, 2022
#This is a simple 2d side-scrolling platformer game

print("Loading")
#Imports
import pygame
import time
from pygame.locals import *
import sys
import os
import keyboard
import random
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
teal = (0, 255, 255)
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
Special_button = "space"
Start_button = "enter"
Pause_buton = "escape"


#Classes
#General purpose tools that will help us place graphical elements on screen
class GraphicalTools:
    #This puts up text in a select place in a typewriter fasion.
    #Input is a string in which we want to place on screen, speed is time (in seconds) between each character placement
    #Startplacex/y is the x and y of where we will start placeing text. Length is the amount of characters to print before newlining.
    def Typewriter(Input, speed, startplacex, startplacey, length):
        for letter in Input:
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


class GameFramework:
    #Code to run every 20 frames
    #checktype = what to do
    #type 0 = title/menu checking, type 1 = normal gameplay, type 2 = cutscenes (if applicable), type 3 = bossfights
    def FrameCheck(checktype):
        if checktype == 0:
            return
        elif checktype == 1:
            return
        elif checktype == 2:
            return
        elif checktype == 3:
            return
        else:
            print("Error at GameFramework.Framecheck - Invalid checktype - Please contact developer at michael@burgin.us")
            #shut down systems. Destroy the pygame layer and the backend execution
            pygame.quit()
            sys.exit(-1)


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


#main player sprite
#to be honest I copied this from the internet, not because I'm lazy but because I'm still learning. https://www.geeksforgeeks.org/pygame-creating-sprites/
class player(pygame.sprite.Sprite):
    def __init__(self, color, surface_color, height, width):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill = surface_color()
        self.image.set_colorkey(color)
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

        self.rect = self.image.get_rect()


class Levels:
    def TitleSceenMainMenu():
        levelnumber = 0
        #The fadeout sequence
        isSequenceFinished = 0
        FadeRed = 255
        FadeGreen = 255
        FadeBlue = 255
        while red > 0:
            canvas.fill((FadeRed, FadeBlue, FadeGreen))
            FadeRed -= 5
            FadeBlue -=5
            FadeGreen -=5
            pygame.display.flip()
        pygame.display.flip()
        time.sleep(1)
        #Main menu
        canvas.fill((97, 49, 14))
        return


    #main titlescreen loop
    def TitleScreen():
        levelnumber = 0
        sprites_list = pygame.sprite.Group()
        slowtimer = 0
        totaltimer = 0
        moveon = 0
        keyboard.add_hotkey(Start_button, lambda: TitleScreenMainMenu())

        #setup sprite
        #player_ = Player(red, teal, 50, 25)
        #player_.rect.x = 500
        #player_.rect.y = 325
        #sprites_list.add(player_)

        while a == 0:
            canvas.fill(white)
            canvas.blit(TitleScreenImage, dest = origin)
            canvas.blit(PlayerSprite1, (245, 580))
            #To display a number on the top right
            #This is diognositic tools for the developer version! Will remove in release. =====================================
            str_position = str(pygame.mouse.get_pos())
            str_slowtimer = str(slowtimer)
            str_totaltimer = str(totaltimer)
            GraphicalTools.TextBoxMaker('freesansbold.ttf', 100, 50, str_position, 32, black, teal)
            GraphicalTools.TextBoxMaker('freesansbold.ttf', 900, 50, str_slowtimer, 32, black, teal)
            GraphicalTools.TextBoxMaker('freesansbold.ttf', 800, 50, str_totaltimer, 32, black, teal)
            #==================================================================================================================

            if slowtimer < 20:
                slowtimer += 1
            else:
                slowtimer = 0
                totaltimer += 1

            if moveon == 1:
                TitleScreenMainMenu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
            pygame.display.flip()
            #locks game to 60fps, can be increased if requried however
            time.sleep(0.017)







#Create the canvas on which we put the game on
canvas = pygame.display.set_mode((1000, 650))
#Title of window
pygame.display.set_caption("Platformer game by Michael Burgin")
TitleScreenImage = pygame.image.load("Homescreen1000x650.png")
PlayerSprite1 = pygame.image.load("Player1.png")

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
