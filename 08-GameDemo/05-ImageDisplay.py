import pygame

pygame.init()

white = (255,255,255)
color_1 = (100,120,255)

width = 800
height = 500

screen = pygame.display.set_mode((width,height))

rect_x = 0
move_x = 10

rect_y = 0
move_y = 10

clock = pygame.time.Clock()
FPS = 40

ball_img = pygame.image.load("assets/ball.png")

while True:
    
    for event in pygame.event.get():
        #print(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect_x = +10
            elif event.key == pygame.K_LEFT:
                rect_x = -10
            elif event.key == pygame.K_DOWN:
                rect_y = +10
            elif event.key == pygame.K_UP:
                rect_y = -10

    screen.fill(white)
    # Rectangle Parameters - GameSurface, Color, x,y,width,height
    #pygame.draw.rect(screen, color_1, [move_x,move_y,100,100])

    # Blit is used to insert images and fonts etc..
    screen.blit(ball_img, (move_x,move_y))

    move_x += rect_x
    move_y += rect_y

    if move_x > width-100:
        move_x -= rect_x
        rect_x = -10
    elif move_x < 0:
        move_x += rect_x
        rect_x = +10
    elif move_y > height-100:
        move_y -= rect_y
        rect_y = -10
    elif move_y < 0:
        move_y += rect_y
        rect_y = +10

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
quit()
