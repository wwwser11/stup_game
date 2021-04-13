import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, w, h, player_img, colors):
        self.w = w
        self.h = h
        self.image = player_img
        self.colors = colors
        self.image = pygame.transform.scale(player_img, (170, 88))
        self.image.set_colorkey(colors['WHITE'])
        self.rect = self.image.get_rect()
        self.colors = colors
        self.speedx = 0
        self.speedy = 0
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.speedy = -1
        if keystate[pygame.K_DOWN]:
            self.speedy = 1
        self.rect.y += self.speedy
        if self.rect.bottom > self.h:
            self.rect.bottom = self.h
        if self.rect.top < 0:
            self.rect.top = 0
        if keystate[pygame.K_LEFT]:
            self.speedx = -1
        if keystate[pygame.K_RIGHT]:
            self.speedx = 1
        self.rect.x += self.speedx
        if self.rect.right > self.w:
            self.rect.right = self.w
        if self.rect.left < 0:
            self.rect.left = 0
