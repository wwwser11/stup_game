import pygame
from os import path
from text_writer import show_go_screen
from Player_class import Player
from ground import Ground

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
        global ground1
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
        ground_img = pygame.image.load(path.join(img_dir, 'ground.png'))


        running = True
        game_over = True
        while running:  # game cycle
            # clock.tick(fps)  # set cycle speed
            if game_over:
                # show start screen
                show_go_screen(screen, background, background_rect, WIDTH, HEIGHT, FPS, clock, colors)
                game_over = False
                all_sprites = pygame.sprite.Group()
                player = Player(width, height, player_img, colors)
                all_sprites.add(player)
                ground1 = Ground(width, height, ground_img, colors)
                ground2 = Ground(width, height, ground_img, colors)
                all_sprites.add(ground1)


            for event in pygame.event.get():  # now we can close screen
                if event.type == pygame.QUIT:
                    running = False

            all_sprites.update()
            # make infinity ground
            # if ground1.rect.left < (ground1.img_height - ground1.w):
            if ground1.rect.left < (-90):
                all_sprites.add(ground2)

            screen.fill(colors['BLACK'])  # rendering
            screen.blit(background, background_rect)
            all_sprites.draw(screen)
            pygame.display.flip()  # flip screen

        pygame.quit()  # close screen

game(FPS, WIDTH, HEIGHT, colors)