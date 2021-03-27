import random
import time

import pygame

from jainflapp import window, exit, clock, fps, right, front

pygame.init()

front = pygame.transform.scale(front,(screenwidth,screenheight+280))
front_x = 0
front_y = -70
background = pygame.image.load('background.png')
background = pygame.transform.scale(background,(screenwidth+100,screenheight))
background_x = 0
background_y = 0
bird = pygame.image.load('bird.png')
bird = pygame.transform.scale(bird,(50,50))
bird_x = 100
bird_y = screenheight/2
bird_relative_y = 565
maximum_height =10
pipe = pygame.image.load('pipe.png')
pipe = pygame.transform.scale(pipe,(50,450))
pipe_x = 300
pipe_y = 450
pipe2 = pygame.image.load('pipe.png')
pipe2 = pygame.transform.scale(pipe2,(50,450))
pipe_x2 = 700
pipe_y2 = 250
pipe3 = pygame.image.load('pipe.png')
pipe3 = pygame.transform.scale(pipe3,(50,550))
pipe_x3 = 900
pipe_y3 = 200
pipe4 = pygame.image.load('pipe.png')
pipe4 = pygame.transform.scale(pipe4,(50,820))
pipe_x4 = 525
pipe_y4 = 200
pipe5 = pygame.image.load('pipe.png')
pipe5 = pygame.transform.scale(pipe5,(50,620))
pipe_x5 = 1100
pipe_y5 = 400
pipe_rotate = pygame.transform.rotate(pipe,180)
pipe_rotate = pygame.transform.scale(pipe_rotate,(50,340))
pipe_rotate_x = 300
pipe_rotate_y = -20
pipe_rotate1  = pygame.transform.rotate(pipe2,180)
pipe_rotate1 = pygame.transform.scale(pipe_rotate1,(50,100))
pipe_rotate_x1 = 520
pipe_rotate_y1 = -20
pipe_rotate2 = pygame.transform.rotate(pipe3,180)
pipe_rotate2 = pygame.transform.scale(pipe_rotate2,(50,150))
pipe_rotate_x2 = 700
pipe_rotate_y2 = -20
pipe_rotate3 = pygame.transform.rotate(pipe4,180)
pipe_rotate3 = pygame.transform.scale(pipe_rotate3,(50,120))
pipe_rotate_x3 = 900
pipe_rotate_y3 = -20
pipe_rotate4 = pygame.transform.rotate(pipe5,180)
pipe_rotate4 = pygame.transform.scale(pipe_rotate4,(50,320))
pipe_rotate_x4 = 1100
pipe_rotate_y4 = -20
isjump = False
gravity = 15
scored = 0
def score(scored):
    font = pygame.font.SysFont(None, 40)
    text = font.render("Score:" + str(scored), True, (255,255,255))
    window.blit(text, (10,screenheight/3))

def text_objects(text, font):
    textsurface = font.render(text, True, (255,0,0))
    return textsurface, textsurface.get_rect()
    window.blit(bird, (bird_x, bird_y))

def message_display(text):
    largetext = pygame.font.Font("freesansbold.ttf", 80)
    textsurf, textrect = text_objects(text, largetext)
    textrect.center = ((screenwidth / 2, screenheight / 2))
    window.blit(textsurf, textrect)
    window.blit(bird, (bird_x, bird_y))
    pygame.display.update()
    time.sleep(1)

def crash():
    message_display("COLLIDE")
    window.blit(bird, (bird_x, bird_y))

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
               right = True
               isjump = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                isjump = False

    if right == True:
     if bird_relative_y+1 > bird_y > maximum_height:
        if isjump == True:
            window.blit(bird, (bird_x, bird_y))
            bird_y -= 15

     else:
        isjump = False

     if bird_y < bird_relative_y:
        if isjump == False:
                bird_y += gravity
    window.blit(background, (background_x, background_y))
    if right == True:
       if background_x < -1060:
            background_x = 0
       if pipe_x < -960:
           pipe_x = 0
       if pipe_x2 < -960:
           pipe_x2 = 0
       if pipe_x3 < -960:
           pipe_x3 = 0
       if pipe_x4 < -960:
           pipe_x4 = 0
       if pipe_x5 < -960:
           pipe_x5 = 0
       if pipe_rotate_x < -960:
           pipe_rotate_x = 0
       if pipe_rotate_x1 < -960:
           pipe_rotate_x1 = 0
       if pipe_rotate_x2 < -960:
           pipe_rotate_x2 = 0
       if pipe_rotate_x3 < -960:
           pipe_rotate_x3 = 0
       if pipe_rotate_x4 < -960:
           pipe_rotate_x4 = 0
       window.blit(background, (background_x + 1060, background_y))
       window.blit(pipe, (pipe_x + 960, pipe_y))
       window.blit(pipe2, (pipe_x2 + 960, pipe_y2))
       window.blit(pipe3, (pipe_x3 + 960, pipe_y3))
       window.blit(pipe4, (pipe_x4 + 960, pipe_y4))
       window.blit(pipe5, (pipe_x5 + 960, pipe_y5))
       window.blit(pipe_rotate, (pipe_rotate_x + 960, pipe_rotate_y))
       window.blit(pipe_rotate1, (pipe_rotate_x1 + 960, pipe_rotate_y1))
       window.blit(pipe_rotate2, (pipe_rotate_x2 + 960, pipe_rotate_y2))
       window.blit(pipe_rotate3, (pipe_rotate_x3 + 960, pipe_rotate_y3))
       window.blit(pipe_rotate4, (pipe_rotate_x4 + 960, pipe_rotate_y4))
       pipe_x -= 10
       pipe_x2 -= 10
       pipe_x3 -= 10
       pipe_x4 -= 10
       pipe_x5 -= 10
       pipe_rotate_x -= 10
       pipe_rotate_x1 -= 10
       pipe_rotate_x2 -= 10
       pipe_rotate_x3 -= 10
       pipe_rotate_x4 -= 10
       background_x -= 10
       score(scored)
       window.blit(bird, (bird_x, bird_y))
    elif right == False:
        window.blit(front, (front_x, front_y))
        time.sleep(1)
    if pipe_x+960 < bird_x+ 50 < pipe_x+960+50 and pipe_y < bird_y+50 < pipe_y+450:
       crash()
       exit = True
    elif pipe_x2+960 < bird_x+50 < pipe_x2+960+50 and pipe_y2 < bird_y+50 <pipe_y2+450:
        crash()
        exit = True
    elif pipe_x3+960 < bird_x+50 < pipe_x3+960+50 and pipe_y3 < bird_y+50 <pipe_y3+550:
        crash()
        exit = True
    elif pipe_x4+960 < bird_x+50 < pipe_x4+960+50 and pipe_y4 < bird_y+50 <pipe_y4+820:
        crash()
        exit = True
    elif pipe_x5+960 < bird_x+50 < pipe_x5+960+50 and pipe_y5 < bird_y+50 <pipe_y5+620:
        crash()
        exit = True
    elif pipe_rotate_x+960 < bird_x+50 <pipe_rotate_x+960+50 and pipe_rotate_y < bird_y+50 < pipe_rotate_y+340 :
        crash()
        exit = True
    elif pipe_rotate_x1+960 < bird_x+50 <pipe_rotate_x1+960+50 and pipe_rotate_y1 < bird_y+50 < pipe_rotate_y1+100 :
        crash()
        exit = True
    elif pipe_rotate_x2+960 < bird_x+50 <pipe_rotate_x2+960+50 and pipe_rotate_y2 < bird_y+50 < pipe_rotate_y2+150 :
        crash()
        exit = True
    elif pipe_rotate_x3+960 < bird_x+50 <pipe_rotate_x3+960+50 and pipe_rotate_y3 < bird_y+50 < pipe_rotate_y3+120 :
        crash()
        exit = True
    elif pipe_rotate_x4+960 < bird_x+50 <pipe_rotate_x4+960+50 and pipe_rotate_y4 < bird_y+50 < pipe_rotate_y4+320 :
        crash()
        exit = True
    elif bird_y+50 < 65:
        crash()
        exit = True
    elif bird_y+50 > 623:
        crash()
        exit = True
    if pipe_y > bird_y+50 > pipe_rotate_y + 340 and   pipe_x+960+50 > bird_x+50 > pipe_x+960+30:
        scored += 1
    elif pipe_y2 > bird_y+50 > pipe_rotate_y1 + 100 and   pipe_x2+960+50 > bird_x+50 > pipe_x2+960+30 :
        scored += 1
    elif pipe_y3 > bird_y+50 > pipe_rotate_y2 + 150 and  pipe_x3+960+50 > bird_x+50 > pipe_x3+960+35:
        scored += 1
    elif pipe_y4 > bird_y+50 > pipe_rotate_y3 + 120 and   pipe_x4+960+50 > bird_x+50 > pipe_x4+960+35:
        scored += 1
    elif pipe_y5 > bird_y+50 > pipe_rotate_y4 + 320 and  pipe_x5+960+50 > bird_x+50 > pipe_x5+960+30:
        scored += 1
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()