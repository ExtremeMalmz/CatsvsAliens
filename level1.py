import pygame, sys
from pygame.locals import *

def send_back_to_main():
    '''
    Sends the program back to the main menu file. Python doesnt allow circular imports so I was forced to do it like this
    '''
    import main_menu
    returnToMain = main_menu.the_main()
    returnToMain

def enemy_movement_direction(enemy):
    '''
    Returns the enemy Ai moving direction
    '''
    #print(enemy.x) 32 267
    #xCoordinate = enemy.x
    if enemy.x == 32:
        #print("Move right")
        direction = "right"
        return direction

    if enemy.x == 267:
        #print("Move left")
        direction = "left"
        return direction

def enemy_movement(enemy,direction):
    '''
    Determines which direction the AI should move
    '''
    if direction == "left":
        enemy.x -= 1
    else:
        enemy.x += 1
    

def win_level():
    '''
    sends the program back to the main menu
    '''
    print("Du vann!")
    send_back_to_main()




def player_death(rect):
    '''
    Respawns the player in case of death
    '''
    
    rect.y = 99
    rect.x = 50

    print("DU DOG, men du åkte till himmlen")
    
    
        

def load_map(path):
    '''
    adds a .txt to inputted file which should be a level map
    '''
    f = open(path + '.txt','r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map


def collision_test(rect,tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect,movement,tiles):
    '''
    Handles player movement
    '''
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

def level_1_game_loop():
    '''
    Game loop for main, basically the main for the game
    '''
        
    clock = pygame.time.Clock()
    pygame.display.set_caption('Level Uno')

    WINDOW_SIZE = (900,700)

    screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

    display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled



    pygame.display.set_caption('Level 1')

    game_map = load_map('level1')

    grass_img = pygame.image.load('grass.png')
    dirt_img = pygame.image.load('dirt.png')
    knd_image = pygame.image.load('knd.png')
    flag_image = pygame.image.load('spasskayatower.jpg')
    red_image = pygame.image.load('red.png')

    player_image = pygame.image.load('player.png').convert()
    #original image, needed to make this to make it go back if mirrored
    player_image_original = pygame.image.load('player.png').convert()
    #mirrored for left movement
    player_image_mirror = pygame.image.load('playermirror.png').convert()

    player_image.set_colorkey((255, 255, 255))
    player_image_original.set_colorkey((255, 255, 255))
    player_image_mirror.set_colorkey((255, 255, 255))

    #this puts the player at the location of the coordinates
    player_rect = pygame.Rect(100,100,5,13)

    #spawn an enemy
    enemy_image = pygame.image.load('enemy.png').convert()
    enemy_image.set_colorkey((0, 0, 0))
    enemy_rect = pygame.Rect(267, 131, 5, 13)

    background_objects = [[0.25,[120,10,70,400]],[0.25,[280,30,40,400]],[0.5,[30,40,40,400]],[0.5,[130,90,100,400]],[0.5,[300,80,120,400]]]

    moving_right = False
    moving_left = False
    vertical_momentum = 0
    air_timer = 0

    true_scroll = [0,0]

    while True: # game loop
        
        display.fill((146,244,255)) # clear screen by filling it with blue

        true_scroll[0] += (player_rect.x-true_scroll[0]-152)/20
        true_scroll[1] += (player_rect.y-true_scroll[1]-106)/20
        scroll = true_scroll.copy()
        scroll[0] = int(scroll[0])
        scroll[1] = int(scroll[1])

        pygame.draw.rect(display,(7,80,75),pygame.Rect(0,120,300,80))
        for background_object in background_objects:
            obj_rect = pygame.Rect(background_object[1][0]-scroll[0]*background_object[0],background_object[1][1]-scroll[1]*background_object[0],background_object[1][2],background_object[1][3])
            if background_object[0] == 0.5:
                pygame.draw.rect(display,(14,222,150),obj_rect)
            else:
                pygame.draw.rect(display,(9,91,85),obj_rect)

        tile_rects = []
        y = 0
        for layer in game_map:
            x = 0
            for tile in layer:
                if tile == '1':
                    display.blit(dirt_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '2':
                    display.blit(grass_img,(x*16-scroll[0],y*16-scroll[1]))
                if tile == '3':
                    display.blit(knd_image, (x * 16-scroll[0], y * 16-scroll[1]))
                if tile == '4':
                    display.blit(flag_image, (x * 16-scroll[0], y * 16-scroll[1]))
                #if tile == '5':
                #    display.blit(whitebricks_image, (x * 16-scroll[0], y * 16-scroll[1]))
                if tile == '6':
                    display.blit(red_image, (x * 16-scroll[0], y * 16-scroll[1]))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x*16,y*16,16,16))
                x += 1
            y += 1

        player_movement = [0,0]
        if moving_right == True:
            player_movement[0] += 2
        if moving_left == True:
            player_movement[0] -= 2
        player_movement[1] += vertical_momentum
        vertical_momentum += 0.2
        if vertical_momentum > 3:
            vertical_momentum = 3

        player_rect,collisions = move(player_rect,player_movement,tile_rects)

        if collisions['bottom'] == True:
            air_timer = 0
            vertical_momentum = 0
        else:
            air_timer += 1

        display.blit(player_image,(player_rect.x-scroll[0],player_rect.y-scroll[1]))
    	
        

        for event in pygame.event.get(): # event loop
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = True
                    if player_image == player_image_mirror:
                        player_image = player_image_original
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = True
                    player_image = player_image_mirror
                if event.key == K_UP or event.key == K_w:
                    if air_timer < 6:
                        vertical_momentum = -5
    
            if event.type == KEYUP:
                if event.key == K_RIGHT or event.key == K_d:
                    moving_right = False
                if event.key == K_LEFT or event.key == K_a:
                    moving_left = False
                if event.key == K_SPACE:
                    send_back_to_main()
                    print("Pressed SPACE")

        #kollar om karaktären ska dö
        if player_rect.y >= 300 :
            player_death(player_rect)

        #get x and y here
        #print("X is")
        #print(player_rect.x)

        #print("Y is")
        #print(player_rect.y)


        #the enemy
        display.blit(enemy_image,(enemy_rect.x-scroll[0],enemy_rect.y-scroll[1]))

        if enemy_rect.x == 32 or enemy_rect.x == 267:
            direction = enemy_movement_direction(enemy_rect)
            #print(direction)

        enemy_movement(enemy_rect,direction)
        #print(enemy_rect.x)

        #old collision 
        #if enemy_rect.x == player_rect.x and enemy_rect.y == player_rect.y:
        #    print("collision!")
        
        #new collision handler
        if enemy_rect.colliderect(player_rect):
            print("Collission 2")
            player_death(player_rect)

        if player_rect.x >= 715 and player_rect.y == 19:
            print("Win")
            win_level()
            
        screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
        pygame.display.update()
        clock.tick(60)

