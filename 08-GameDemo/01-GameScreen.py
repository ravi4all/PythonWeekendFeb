import pygame

pygame.init()

white = (255,255,255)
color_1 = (100,120,255)

screen = pygame.display.set_mode((600,400))

screen.fill(white)

while True:
    
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()


pygame.quit()
quit()
