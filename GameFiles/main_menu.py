import pygame
from pygame import mixer
import pygame_menu
import json


from level1 import level_1_game_loop
#from video import intro

pygame.init()



surface = pygame.display.set_mode((900, 700))

def set_difficulty(value, difficulty):
    '''
    Game difficulty. 9 lives on easy. 1 life on hard.
    '''
    pass

def start_the_game():
    '''
    Sends you to the level 1 game loop unless your name is Gustav which if you are just enjoy the ride
    '''
    pygame.mixer.music.stop()

    my_file = open("games.json", "r")
    data = json.load(my_file)
    #print(data)

    

    for i in data:
        i = i.upper()
        if i == 'GUSTAV':
            print("hello gutsav")
            #intro()

    else:
        level_1_game_loop()

def MyTextValue(name):
    '''
    Gets the name which is in the JSON file
    '''
    #print('player name is', name)
        
    my_file = open("games.json", "w")
    my_file.write(json.dumps([name]))
    my_file.close()   


def the_main():
    '''
    Main menu screen along with buttons 
    '''
    pygame.display.set_caption('Menu')
    
    #NO MUSIC THIS TIME
    #mixer.music.load('background.wav')
    #set to -1 for infinite music peoples
    #mixer.music.play(-1)


    
    

    menu = pygame_menu.Menu('Cats vs Aliens', 400, 300,
                        theme=pygame_menu.themes.THEME_BLUE)

    

    my_file = open("games.json", "r")
    
    data = json.load(my_file)
    #print(data)
    
    for i in data:
        name = data[0]
    my_file.close()

    menu.add.text_input('Name : ', default= name, onchange= MyTextValue)
    menu.add.selector('Difficulty :', [('Catnip', 1), ('Food', 2), ('Veternarian', 3)], onchange=set_difficulty)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)

