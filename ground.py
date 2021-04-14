import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, w, h, ground_img, colors):
        self.w = w
        self.h = h
        self.img = ground_img
        self.colors = colors
        self.img_height = 850
        self.image = pygame.transform.scale(ground_img, (750, 32))
        self.image.set_colorkey(colors['WHITE'])
        self.rect = self.image.get_rect()
        self.colors = colors
        self.rect.x = 650
        self.rect.y = 460
        self.speedx = -1
        pygame.sprite.Sprite.__init__(self)

    def update(self):
        self.rect.x += self.speedx
        if self.rect.right < -10:
            self.rect.left = 650

