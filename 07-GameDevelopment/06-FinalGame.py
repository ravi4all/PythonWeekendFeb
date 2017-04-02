import pygame
import time
import random

pygame.init()

white = (255,255,255)   # Color is given in rgb
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Title
pygame.display.set_caption('AddingIcon')

icon = pygame.image.load('image2.png')
pygame.display.set_icon(icon)

# Adding image
img = pygame.image.load("image1.png")
img2 = pygame.image.load("image2.png")

clock = pygame.time.Clock() 

block_size = 20
FruitThickness = 30
FPS = 13

direction = "right"

smallfont = pygame.font.SysFont("Comicsansms", 25)
medfont = pygame.font.SysFont("Comicsansms", 50)
largefont = pygame.font.SysFont("Comicsansms", 80)

def pause():
    paused = True
    message("Paused", black, -100, size = "large")
    message("Press C to continue or Q to quit", black, 25,)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        clock.tick(5)

def score(score):
    text = smallfont.render("Score: "+str(score), True, red)
    gameDisplay.blit(text, [0,0])

def randFruitGen():
    randFruitX = round(random.randrange(0, display_width - FruitThickness))#/10.0)*10.0
    randFruitY = round(random.randrange(0, display_height - FruitThickness))#/10.0)*10.0

    return randFruitX, randFruitY
                

# Start Screen
def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    intro = False
        
        gameDisplay.fill(white)
        message("Welcome to Snake game", green, -100, "medium")
        message("Make the snake eat apple", black, 0, "small")
        message("The more apple you eat, the longer snake will get", black, 40, "small")
        message("Press S to start game, P to pause", black, 150, "small")
        pygame.display.update()
        clock.tick(8)


def snake(block_size, snakeList):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)    # Rotating image

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = img

    if direction == "down":
        head = pygame.transform.rotate(img, 180)

    gameDisplay.blit(head, (snakeList[-1][0],snakeList[-1][1]))
    
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, black, [XnY[0],XnY[1],block_size,block_size])

def text_obj(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()  # it will return the surface data and also the rectangle of data

def message(msg, color, y_displace, size = "small"):
    textSurface, textRect = text_obj(msg, color, size)
    textRect.center = (display_width / 2), (display_height / 2) + y_displace # it will center the text
    gameDisplay.blit(textSurface, textRect)

    

def gameLoop():
    # These variable could be change in future so put them under gameLoop()
    global direction

    # Now snake head will always be in right direction by default
    direction ='right'
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randFruitX, randFruitY = randFruitGen()
    
    while not gameExit:

        if gameOver == True:
            message("Game over", red, y_displace = -50, size = "large")
            message("Press C to play again or Q to quit", black, 50, size="medium")
            pygame.display.update()

        while gameOver == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_p:
                    pause()

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)  
        
        gameDisplay.blit(img2, (randFruitX, randFruitY))        

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snakeList[:-1]

        snake(block_size, snakeList)

        score(snakeLength-1)
        
        pygame.display.update()

        if lead_x > randFruitX and lead_x < randFruitX + FruitThickness or lead_x + block_size > randFruitX and lead_x + block_size < randFruitX + FruitThickness:
            if lead_y > randFruitY and lead_y < randFruitY + FruitThickness:

                randFruitX, randFruitY = randFruitGen()
                
                snakeLength += 1

            elif lead_y + block_size > randFruitY and lead_y + block_size < randFruitY + FruitThickness:

                randFruitX, randFruitY = randFruitGen()
                
                snakeLength += 1
        

        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
