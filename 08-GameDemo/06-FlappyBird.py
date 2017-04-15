import pygame
import random

pygame.init()

width = 400
height = 600

red = (255,0,0)

board = pygame.display.set_mode((width,height))

bird_img = pygame.image.load("assets/0.png")
bg_img = pygame.image.load("assets/background.png")
bg_img_2 = pygame.image.load("assets/background.png")
bg_fix = pygame.image.load("assets/background.png")
top_wall = pygame.image.load("assets/top.png")
bottom_wall = pygame.image.load("assets/bottom.png")

clock = pygame.time.Clock()
FPS = 30

def counter(count):
    font = pygame.font.SysFont("None",30)
    text = font.render("Counter:"+str(count),True, red)
    board.blit(text,(50,10))

def gameLoop():

    bird_x = 50
    bird_y = 10

    bird_rect = [50,10,40,30]

    jump = 0
    gravity = 10
    jumpspeed = 10

    bg_x = 0
    bg_2_x = width

    wall_x = width
    top_wall_y = random.randint(-300,0)
    bottom_wall_y = top_wall_y + height + 20

    count = 0
    
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                jump = 20
                gravity = 10
                jumpspeed = 10
                pygame.mixer.music.load("assets/swoosh.wav")
                pygame.mixer.music.play(1)

        board.blit(bg_fix,(0,0))
        board.blit(bg_img_2, (bg_2_x,0))
        board.blit(bg_img,(bg_x,0))
        board.blit(bird_img, (bird_x,bird_y))
        board.blit(top_wall, (wall_x,top_wall_y))
        board.blit(bottom_wall, (wall_x,bottom_wall_y))

        up_rect = pygame.Rect(wall_x,top_wall_y,top_wall.get_width(), top_wall.get_height())
        bottom_rect = pygame.Rect(wall_x,bottom_wall_y,bottom_wall.get_width(), bottom_wall.get_height())

        bird_rect[1] = bird_y

        if up_rect.colliderect(bird_rect) or bottom_rect.colliderect(bird_rect):
            pygame.mixer.music.load("assets/hit.wav")
            pygame.mixer.music.play(1)
            gameLoop()

        wall_x -= 5
        bg_x -= 6
        bg_2_x -= 6

        if bird_y > height:
            gameLoop()

        if wall_x < 0-80:
            wall_x = width
            top_wall_y = random.randint(-300,0)
            bottom_wall_y = top_wall_y + height + 20
            count += 1

        if jump:
            jumpspeed -= 1
            bird_y -= jumpspeed
            jump -= 1
        else:
            bird_y += gravity
            gravity += 0.2

        if bg_x < -400:
            bg_x = width
            bg_x -= 6

        elif bg_2_x < -400:
            bg_2_x = width
            bg_2_x -= 6

        counter(count)

        pygame.display.update()
        clock.tick(FPS)

gameLoop()
