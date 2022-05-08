import pygame
import time

from pyvidplayer import Video


surface = pygame.display.set_mode((900, 700))

vid = Video("EvenFunnierVideo.mp4")
vid.set_size((900,700))
vid.toggle_pause()

def intro():
    '''
    plays the video which is entered as the vid variable
    '''
    pygame.display.set_caption('Gustav >:)')
    vid.toggle_pause()

    vid.set_volume(30)
    start = time.time()
    
    
    while True:
        
        vid.draw(surface,(0,0))
        pygame.display.update()

        duration = time.time() - start
        #print(duration)

        if duration >= 5:
            #print("Terminate program")

            vid.restart()
            exit()
            