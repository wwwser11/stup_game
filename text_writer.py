import pygame


# func to draw score
def draw_text(surf, text, size, x, y, colors):
    font = pygame.font.Font('font/a_FuturaRound Bold.ttf', size)
    # 'True' turn on anti-aliased
    text_surface = font.render(text, True, colors['BLACK'])
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def show_go_screen(screen,background, background_rect, width, height, fps, clock, colors):
    screen.blit(background, background_rect)
    draw_text(screen, 'game', 64, width / 2, height / 4, colors)
    draw_text(screen, "gameplay", 22,
              width / 2, height / 2, colors)
    draw_text(screen, "Press a key to begin", 18, width / 2, height * 3 / 4, colors)
    pygame.display.flip()
    waiting = True
    while waiting:
        # clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False