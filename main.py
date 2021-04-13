import pygame
from os import path
from text_writer import show_go_screen

# size
WIDTH = 600
HEIGHT = 480
FPS = 30

# colors (R, G, B)
colors = dict(
    BLACK=(0, 0, 0),
    WHITE=(255, 255, 255),
    RED=(255, 0, 0),
    GREEN=(0, 255, 0),
    BLUE=(0, 0, 255)
)

def game(fps, width, height, colors, ):

        # turn pygame on
        pygame.init()
        # here must be music

        # make game screen
        screen = pygame.display.set_mode((width, height))
        # get game name
        pygame.display.set_caption('stupid_game')
        # start track time
        clock = pygame.time.Clock
        # give image, music and etc dirs
        img_dir = path.join(path.dirname(__file__), 'img')

        # make pics
        player_img = pygame.image.load(path.join(img_dir, 'flying.gif')).convert()
        background = pygame.image.load(path.join(img_dir, 'bg001.png')).convert()
        background_rect = background.get_rect()


        running = True
        game_over = True
        while running:  # game cycle
            # clock.tick(fps)  # set cycle speed
            if game_over:
                # show start screen
                show_go_screen(screen, background, background_rect, WIDTH, HEIGHT, FPS, clock, colors)
                game_over = False
                pass

            for event in pygame.event.get():  # now we can close screen
                if event.type == pygame.QUIT:
                    running = False

                # rendering

           # pygame.display.flip()  # flip screen

        pygame.quit()  # close screen

game(FPS, WIDTH, HEIGHT, colors)