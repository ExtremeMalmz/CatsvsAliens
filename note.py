from typing import Optional
from pygame.locals import *
from pygame_menu.examples import create_example_window
from msilib.schema import Font
import pygame
from pygame import mixer
import pygame_menu
import json


from level1 import level_1_game_loop
from video import intro

pygame.init()

"""
pygame-menu
https://github.com/ppizarror/pygame-menu

EXAMPLE - IMAGE BACKGROUND
Menu using background image + BaseImage object.
"""

__all__ = ['main']


# Constants and global variables
FPS = 60
WINDOW_SIZE = (900, 700)

sound: Optional['pygame_menu.sound.Sound'] = None
surface: Optional['pygame.Surface'] = None
main_menu: Optional['pygame_menu.Menu'] = None
bg_img = pygame.image.load('bg.png')
# Load image
background_image = pygame_menu.BaseImage("bg.png")


def start_the_game():
    '''
    Sends you to the level 1 game loop unless your name is Gustav which if you are just enjoy the ride
    '''
    pygame.mixer.music.stop()

    my_file = open("games.json", "r")
    data = json.load(my_file)
    # print(data)

    for i in data:
        i = i.upper()
        if i == 'GUSTAV':
            print("hello gutsav")
            intro()

    else:
        level_1_game_loop()


def set_difficulty(value, difficulty):
    '''
    Game difficulty. 9 lives on easy. 1 life on hard.
    '''
    pass


def MyTextValue(name):
    '''
    Gets the name which is in the JSON file
    '''
    #print('player name is', name)

    my_file = open("games.json", "w")
    my_file.write(json.dumps([name]))
    my_file.close()


def main_background() -> None:
    """
    Background color of the main menu, on this function user can plot
    images, play sounds, etc.
    """
    background_image.draw(surface)


def main(test: bool = False) -> None:
    """
    Main program.

    :param test: Indicate function is being tested
    """
    global main_menu
    global sound
    global surface

    # Create window
    surface = create_example_window('Cats vs Aliens', WINDOW_SIZE)
    clock = pygame.time.Clock()

    # Create menus: Main menu
    main_menu_theme = pygame_menu.themes.THEME_BLUE.copy()
    main_menu_theme.set_background_color_opacity(0.2)  # 50% opacity
    main_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        # onclose=pygame_menu.events.EXIT,  # User press ESC button
        theme=main_menu_theme,
        title='Menu',
        width=WINDOW_SIZE[0] * 0.8,
    )

    theme_bg_image = main_menu_theme.copy()
    theme_bg_image.background_color = pygame_menu.BaseImage(
        image_path=pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER
    )
    theme_bg_image.title_font_size = 25
    menu_with_bg_image = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        onclose=pygame_menu.events.EXIT,
        theme=theme_bg_image,
        title='Cats vs Aliens Menu',
        width=WINDOW_SIZE[0] * 0.8
    )
    menu_with_bg_image.add.button('Back', pygame_menu.events.BACK)

    widget_menu_theme = pygame_menu.themes.THEME_BLUE.copy()
    widget_menu_theme.widget_margin = (0, 10)
    widget_menu_theme.widget_padding = 0
    widget_menu_theme.widget_selection_effect.margin_xy(10, 5)
    widget_menu_theme.widget_font_size = 20
    widget_menu_theme.set_background_color_opacity(0.2)  # 50% opacity

    widget_menu = pygame_menu.Menu(
        height=WINDOW_SIZE[1] * 0.7,
        theme=widget_menu_theme,
        title='FAQ',
        width=WINDOW_SIZE[0] * 0.8,
    )

    # button_image = pygame_menu.BaseImage(
    #     pygame_menu.baseimage.IMAGE_EXAMPLE_CARBON_FIBER)
    # widget_menu.add.text_input('Opaque color button',
    #                              background_color=(100, 100, 100))
    # widget_menu.add.button('Transparent color button',
    #                          background_color=(50, 50, 50, 200), font_size=40)
    # widget_menu.add.button('Transparent background inflate to selection effect',
    #                          background_color=(50, 50, 50, 200),
    #                          margin=(0, 15)).background_inflate_to_selection_effect()
    # widget_menu.add.button('Background inflate + font background color',
    #                          background_color=(50, 50, 50, 200),
    #                          font_background_color=(200, 200, 200)
    #                          ).background_inflate_to_selection_effect()
    # widget_menu.add.button('This inflates background to match selection effect',
    #                          background_color=button_image,
    #                          font_color=(255, 255, 255), font_size=15
    #                          ).selection_expand_background = True
    # widget_menu.add.button('This is already inflated to match selection effect',
    #                          background_color=button_image,
    #                          font_color=(255, 255, 255), font_size=15
    #                          ).background_inflate_to_selection_effect()

    main_menu.add.text_input('Name : ', onchange=MyTextValue)
    main_menu.add.selector('Difficulty :', [(
        'Catnip', 1), ('Food', 2), ('Veternarian', 3)], onchange=set_difficulty)
    main_menu.add.button('New Game', start_the_game)
    main_menu.add.button('Continue',
                         lambda: print('continue to game...'))
    main_menu.add.button('FAQ', widget_menu)
    main_menu.add.button('Quit', pygame_menu.events.EXIT)
    # Main loop
    while True:

        # Tick
        clock.tick(FPS)

        # Main menu
        main_menu.mainloop(surface, main_background,
                           disable_loop=test, fps_limit=FPS)

        # Flip surface
        pygame.display.flip()

        # At first loop returns
        if test:
            break


if __name__ == '__main__':
    main()