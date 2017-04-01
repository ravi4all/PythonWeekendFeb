import pygame

pygame.init()


screen = pygame.display.set_mode((900,500))

game = False

while not game:
    
    for event in pygame.event.get():
        #print(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255,255,255))

    pygame.display.update()


pygame.quit()
quit()

