import os
from main_menu import the_main
from main_json import create_json


if __name__ == '__main__':
    '''
    if the name of the file is main.py it will run, otherwise not
    '''
    create_json()
    the_main()
