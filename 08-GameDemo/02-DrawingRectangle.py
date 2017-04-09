import pygame

pygame.init()

white = (255,255,255)
color_1 = (100,120,255)

screen = pygame.display.set_mode((600,400))

rect_x = 0
move_x = 10

clock = pygame.time.Clock()
FPS = 20

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

    screen.fill(white)
    # Rectangle Parameters - GameSurface, Color, x,y,width,height
    pygame.draw.rect(screen, color_1, [move_x,10,100,100])

    move_x += rect_x

    pygame.display.update()
    clock.tick(FPS)


pygame.quit()
quit()
