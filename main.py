from main_menu import the_main

import json

def create_json():
    '''
    Creates a JSON file named games.json if it doesn't exist already. 
    '''
    try:
        # Opens the file "gemes.json" in "read" mode
        my_file = open("games.json", "r")
        # Reads and converts the file content (JSON) to Python datatype (list)
        game = json.loads(my_file.read())
        # Closes the file
        my_file.close()
        # Returns the list of every lines in file
        return game

    except FileNotFoundError:
        # Creates a new file called "gemes.json"
        my_file = open("games.json", "w")
        # Writes the basic structure in JSON-format
        my_file.write(json.dumps([" Boy Wonder"]))
        my_file.close()
        # Returns the basic structure as an empty list
        return []


if __name__ == '__main__':
    '''
    if the name of the file is main.py it will run, otherwise not
    '''
    create_json()
    the_main()
