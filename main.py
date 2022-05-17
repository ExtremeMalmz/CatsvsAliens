from GameFiles.main_menu import the_main
from GameFiles.main_json import create_json

from Levels.level4 import level_4_game_loop

if __name__ == '__main__':
    '''
    if the name of the file is main.py it will run, otherwise not
    '''
    create_json()
    the_main()