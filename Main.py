
import pygame
from pygame import *
from Step import *
from Player import *
import random
import inputbox

pygame.mixer.init()
pygame.init()

windowHeight = 1024
windowWidth = 768
screen = pygame.display.set_mode((windowWidth,windowHeight))
screen.fill([255,255,255])

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
blue = (0, 0, 255)
colors = [white, black ,red, blue]

## Pictures:
doodlePicture = pygame.image.load("doodleNinjaPicture.png")
background = pygame.image.load("Picture.jpg")
background.convert()
background2 = pygame.image.load("ws_Outer_Space_Pleiades_768x1024.jpg")
background2.convert()
backgroundRect = background.get_rect()
size = 768, 1024
screen = pygame.display.set_mode()
screen.blit(background, backgroundRect)

## Music and sound:
pygame.mixer.music.load("Music.mp3")
pygame.mixer.music.play(-1)
effect = pygame.mixer.Sound('SoundEffect.mp3')


doodle = Player(384,512)
myStep = Step(512, 0)
stepList = []
lastY = random.randint(50, 100)

## Text:
score = 0
font = pygame.font.Font(None, 36)
text = font.render("Score: " + str(score), 2, (255, 255, 255))
textpos = text.get_rect()
textpos.centerx = screen.get_rect().centerx - 20
textpos.centery = 35

font = pygame.font.Font(None, 72)
textGO = font.render("GAME OVER", 2, (255, 0, 0))
textposGO = text.get_rect()
textposGO.centerx = screen.get_rect().centerx - 100
textposGO.centery = screen.get_rect().centery - 100

pygame.display.update()
sadek = True
minY = 0
jump = False
stepMove = 0
i = 1

answer = inputbox.ask(screen, "Name:")
answer = answer[0].upper() + answer[1:]

## Initial steps

myStep = Step(512, lastY)
stepList.append(myStep)

while(len(stepList) < 7):
    myStep = Step(random.randint(30, 500), lastY)
    stepList.append(myStep)
    lastY += random.randint(150, 250)
    pygame.draw.rect(screen, (0,0,0), (myStep.x,myStep.y,myStep.sizeX,myStep.sizeY), 0)


while sadek:
    
##    if jump:
##        doodle.hitStep()

##    time.delay(5)
    for event in pygame.event.get():
        if event.type == QUIT:
            sadek = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sadek = False
            if event.key == K_LEFT:
                doodle.moveLeft()
            if event.key == K_RIGHT:
                doodle.moveRight()
            if event.key == K_DOWN:
                stepMove = True
            if event.key == K_UP:
                jump = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or pygame.K_LEFT:
                doodle.moveDirection = False
                stepMove = False
                jump = False

                
    doodle.move()
    ## Game over code
    if doodle.jumping():
        pygame.draw.circle(screen, (0, 0, 0), (windowWidth/2,windowHeight/2), 250,0)
        screen.blit(textGO, textposGO)
        screen.blit(font.render(answer + "'s Highscore: ", 2, (255, 0, 0)), (screen.get_rect().centerx - 150, screen.get_rect().centery ))
        screen.blit(font.render(str(score), 2, (255, 0, 0)), (screen.get_rect().centerx, screen.get_rect().centery + 100))
        pygame.display.update()
        time.delay(1000)
        pygame.quit()
    screen.fill([255,255,255])


    ## Loop in charge of moving everything
    for currentStep in stepList:
        if doodle.collide(currentStep.x, currentStep.y, currentStep.sizeX, currentStep.sizeY):
            doodle.hitStep()
            effect.play()
            stepMove = 20
            minY += 150


    ## Step mover!!
    for currentStep in stepList:
        currentStep.y += stepMove
    if doodle.y < 200:
        stepMove = 10
        minY += 150
    ## Score count
    score += stepMove 

    screen.blit(background, backgroundRect)
    
    # Blit everything to the screen
    screen.blit(background, (0, 0))


    ## Out of boundry step remover
    for currentStep in stepList:
        if currentStep.y > windowHeight:
            stepList.remove(currentStep)
        if len(stepList) < 7 and minY > random.randint(100,200):
            currentStep = Step(random.randint(30, 500), 70)
            stepList.append(currentStep)
            minY = 0
        pygame.draw.rect(screen, (colors[3]), (currentStep.x,currentStep.y,currentStep.sizeX,currentStep.sizeY), 0)
##        screen.blit(stepPicture, (currentStep.x,currentStep.y))
        
    # Display some text
    font = pygame.font.Font(None, 48)
    text = font.render("Score: " + str(score), 2, (255, 255, 255))
    screen.blit(text, textpos)

    if stepMove > 0:
        stepMove -= 1

    pygame.draw.rect(screen, (colors[0]), (0, 70, 768, 10), 0)
##    pygame.draw.rect(screen, (0, 191, 255), (doodle.x,doodle.y, 80, 80), 0)
    screen.blit(doodlePicture, (doodle.x, doodle.y))
    pygame.display.update()
    sadek += 1
    
    
