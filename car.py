import pygame
import time 
import random

pygame.init()
display_h = 680
display_w = 1350
black = (0,0,0)
grey=(192,192,192)
green=(0,200,0)
red=(200,0,0)
bright_green=(0,255,0)
yellow=(200,200,0)
bright_red=(255,0,0)
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

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameD, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameD, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameD.blit(textSurf, textRect)

def quitgame():
    pygame.quit()

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameD.fill(yellow)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Watch Out!", largeText)
        TextRect.center = ((display_w/2),(display_h/2))
        gameD.blit(TextSurf, TextRect)

        button("GO!",350,450,100,50,green,bright_green,gameloop)
        button("Quit",900,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)


def things_dodged(count):
    font=pygame.font.SysFont(None, 25)
    text=font.render("SCORE: "+ str(count), True, black)
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
        gameD.fill(grey)
        if thing_starty<-500:
            img=random.choice(foo)    

        things(img, thing_startx, thing_starty)
        thing_starty += thing_speed
        
        car(x,y)
        things_dodged(dodged)
        if x > display_w - car_width or x < 0 or y<0 or y>display_h:
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

game_intro()
gameloop()
pygame.quit()
quit()
