import pygame
import random

windowHeight = 1024
windowWidth = 768

class Step:
    x = 0
    y = 0
    sizeX = 0
    sizeY = 0
    
    def __init__(self, xGrid, yGrid):                              
        self.x = xGrid
        self.y = yGrid
        self.sizeX = random.randint(100, 200)
        self.sizeY = 30
    def ascend(self):
        ##    for currentStep in stepList:
        self.y += 1
        print self.y
        if self.y > windowHeight:
            return False

##    def collide(self, player):
##        i = self.x
##        j = self.y
####        if player.speed <= 0:
##        while i < i + self.sizeX:
##            while j < j + self.sizeY:
##                if self.x == player.x and self.y == player.y:
##                    return True
##                j += 1
##            i += 1
##        return False
