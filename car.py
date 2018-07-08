import pygame

pygame.init()
display_h = 500
display_w = 720
black = (0,0,0)
white = (255,255,255)
gameD = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Watch Out')
clock = pygame.time.Clock()
carimg = pygame.image.load('1.png')
def car(x,y):
    gameD.blit(carimg,(x,y))

x = (display_w * 0.45)
y = (display_h * 0.7)

crash = False
x_change, y_change = 0, 0
while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                x_change=0
                y_change=0    
    x+=x_change    
    y+=y_change
    gameD.fill(white)
    car(x,y)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
