import pygame
import time 
import random

pygame.init()
display_h = 500
display_w = 740
black = (0,0,0)
white = (255,255,255)
car_width = 77
gameD = pygame.display.set_mode((display_w,display_h))
pygame.display.set_caption('Watch Out')
clock = pygame.time.Clock()
carimg = pygame.image.load('1.png')
carimg1 = pygame.image.load('2.png')
carimg2 = pygame.image.load('3.png')
carimg3 = pygame.image.load('4.png')
carimg4 = pygame.image.load('6.png')
carimg5 = pygame.image.load('7.png')
carimg6 = pygame.image.load('5.png')

foo = [carimg1,carimg2,carimg3,carimg4,carimg5,carimg6]
    
def things_dodged(count):
    font=pygame.font.SysFont(None, 25)
    text=font.render("Dodged: "+ str(count), True, black)
    gameD.blit(text, (0,0))

def things(img, thingx, thingy):
    gameD.blit(img, (thingx, thingy))

def car(x,y):
    gameD.blit(carimg,(x,y))

def text_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 115)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center  = ((display_w/2), (display_h/2))
    gameD.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(2)
    gameloop()

def crash():
    message_display("You Crashed!")


def gameloop():
    x = (display_w * 0.45)
    y = (display_h * 0.7)

    gameexit = False
    
    x_change, y_change = 0, 0
    
    thing_startx = random.randrange(0, display_w)
    thing_starty = -600
    thing_speed = 7
    thing_width = 65
    thing_height = 130
    dodged=0
    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
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
        if thing_starty<-100:
            img=random.choice(foo)    

        things(img, thing_startx, thing_starty)
        thing_starty += thing_speed
        
        car(x,y)
        things_dodged(dodged)
        if x > display_w - car_width or x < 0:
            crash()
        
        if thing_starty > display_h:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_w)
            img=random.choice(foo)    
            dodged += 1


        if y < thing_starty + thing_height and y+155>thing_starty:    
            if x>=thing_startx and x<=thing_startx +thing_width or x+car_width>=thing_startx and x+car_width<=thing_startx+thing_width:
                crash()
        pygame.display.update()
        clock.tick(60)

gameloop()
pygame.quit()
quit()
