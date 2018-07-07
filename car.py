import pygame

pygame.init()
gameD = pygame.display.set_mode((900,900))
pygame.display.set_caption('Watch Out')
clock = pygame.time.Clock()

crash = False

while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crash = True
        
        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
