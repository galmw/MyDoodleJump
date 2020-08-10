import pygame


windowHeight = 1024
windowWidth = 768

class Player:
    live = True
    x = 0
    y = 0
    speed = 20
    points = 0
    addPoints = 0
    moveDirection = ''
    stopMove = False
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def moveLeft(self):
        self.moveDirection = 'left'
    def moveRight(self):
        self.moveDirection = 'right'
    def move(self):
        if self.moveDirection == 'right':
            self.x += 10
        if self.moveDirection == 'left':
            self.x -= 10
        if self.x >= windowWidth:
            self.x = 10
        if self.x <= 0:
            self.x = windowWidth - 10
    def collide(self, xStep, yStep, xStepSize, yStepSize):
        if self.x <= xStep + xStepSize and self.x + 40 >= xStep:
            if self.y + 60 <= yStep + yStepSize and self.y + 60 >= yStep and self.speed < 0:
               return True
        return False
    def hitStep(self):
        self.speed = 25
    def jumping(self):
        if self.y < 90 and self.speed > 0:
            self.y = 91
            self.speed = -5
        self.y -= self.speed
        if self.speed > -25:
            self.speed -= 1
        if self.y > windowHeight + 50:
            return True
            
    
