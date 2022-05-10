import pygame
import pygame, sys
from pygame.locals import *
import random

def loading_screen_main():    
    pygame.init()

    clock = pygame.time.Clock()
    pygame.display.set_caption('LOADING THE GAME')

    WINDOW_SIZE = (900,700)

    screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

    display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled
    
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    
    #drawings
    font = pygame.font.Font('freesansbold.ttf', 32)

    #put messages here to load
    loadingMessage = font.render("Loading the game", True, (25, 255, 255))
    star = font.render("***", True, (25, 255, 255))

    timer = 0
        
    einz,zwei,drei = random.randint(0,1000),random.randint(1000,2000),random.randint(2000,3000)
    print(einz,zwei,drei)
    while True:
        

        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(loadingMessage, (300, 300))

        timer += 1
        #print(timer)
 
        if einz <= timer:
            screen.blit(star, (300, 450))
            if zwei <= timer:
                screen.blit(star, (400,450))
                if drei <= timer:
                    screen.blit(star, (500, 450))


        pygame.display.update()
 