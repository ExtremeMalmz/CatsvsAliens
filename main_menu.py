import pygame
from pygame import mixer
import pygame_menu
import json
import os

from Levels.level1 import level_1_game_loop
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

    my_file = open(os.path.join('Assets','games.json'), 'r')
    data = json.load(my_file)
    #print(data)

    

    for i in data:
        i = i.upper()
        if i == 'GUSTAV':
            print("hello gutsav")
            #intro()

    else:
        level_1_game_loop()
        
        


'''
    rad 48: öpnna filen, skriv in namn, stäng filen
'''

def MyTextValue(name):
      data = {"Games": [{"Player_Name": name, "Player_Level" : 0, "Player_Life_amount" : 9}]}
      jsonString = json.dumps(data, indent = 4)
      jsonFile = open(os.path.join('Assets','games.json'), "w")
      jsonFile.write(jsonString)
      jsonFile.close()

"""
def MyTextValue(name):

    y = {"Player_Name": name}

    add_json(y)



def add_json(new_data, filename=(os.path.join('Assets','games.json'))):
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_data with file_data inside emp_details
            file_data["games"].append(new_data)
            # Sets file's current position at offset.
            file.seek(0)
            # convert back to json.
            json.dump(file_data, file, indent = 4)
"""

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

    
    with open(os.path.join('Assets','games.json'), 'r') as f:
        data = json.loads(f.read())

        for i in data['Games']:
            name = i['Player_Name']
            



    menu.add.text_input('Name : ', default= name, onchange= MyTextValue)
    menu.add.selector('Difficulty :', [('Catnip', 1), ('Food', 2), ('Veternarian', 3)], onchange=set_difficulty)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(surface)

