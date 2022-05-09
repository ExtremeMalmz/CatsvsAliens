import json, os

def create_json():
    '''
    Creates a JSON file named games.json if it doesn't exist already. 
    '''
    try:
        # Opens the file "gemes.json" in "read" mode
        my_file = open(os.path.join('Assets','games.json'), 'r')
        # Reads and converts the file content (JSON) to Python datatype (list)
        game = json.loads(my_file.read())
        # Closes the file
        my_file.close()
        # Returns the list of every lines in file
        return game

    except FileNotFoundError:
        data = {"Games": [{"Player_Name": "Boy Wonder", "Player_Level" : 0, "Player_Life_amount" : 9}]}

        # Creates a new file called "gemes.json"
        my_file = open(os.path.join('Assets','games.json'), 'w')
        # Writes the basic structure in JSON-format
        my_file.write(json.dumps(data, indent = 4))
        my_file.close()
        # Returns the basic structure as an empty list
        return {}


        # my_file.write(json.dumps(["Boy Wonder"]))

        #data = {"games": [{"Player_name": "Boy Wonder","Level": 1,"Life_left": 9}]}

'''
{
    "games": [
        {
            "Player_name": "Boy Wonder",
            "Level": 1,
            "Life_left": 9
        }
    ]
}
'''


'''
def MyTextValue(name):
    
    #Gets the name which is in the JSON file
    
    #print('player name is', name)
        
    my_file = open(os.path.join('Assets','games.json'), 'w')
    my_file.write(json.dumps([name]))
    my_file.close() 
'''