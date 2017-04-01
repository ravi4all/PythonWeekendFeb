import pygame

pygame.init()

red = (255,0,0)

speed = [2,2]

width = 900
height = 500

screen = pygame.display.set_mode((width,height))

rect_x = 0
rect_y = 0

move_x = 10
move_y = 10

lead_x = 0
lead_y = 0

game = False

while not game:
    
    for event in pygame.event.get():
        #print(event)

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rect_x += move_x
            if event.key == pygame.K_LEFT:
                rect_x -= move_x
            if event.key == pygame.K_DOWN:
                rect_y += move_y
            if event.key == pygame.K_UP:
                rect_y -= move_y
                

    screen.fill((255,255,255))
    # Screen, Color, x,y,width,height
    pygame.draw.rect(screen, red, [lead_x,lead_y,100,100])

    lead_x += rect_x
    lead_y += rect_y

    pygame.display.update()


pygame.quit()
quit()

