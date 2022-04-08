import pygame
import pygame_menu

def new_game_main():
    surface = pygame.display.set_mode((600, 400))

    def set_difficulty(value, difficulty):
        # Do the job here !
        pass

    def start_the_game():
        new_game_main()
        pass

    menu = pygame_menu.Menu('Cats vs Aliens', 400, 300,
                        theme=pygame_menu.themes.THEME_BLUE)

    menu.add.text_input('The boys', default='are back')
    menu.add.button('THE BOYS ARE BACK', pygame_menu.events.EXIT)

    menu.mainloop(surface)
