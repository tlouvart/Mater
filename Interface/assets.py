import os
import pygame

# Assets

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

#config
WIN_NAME =  "Mater"
WIN_RES = (1280,720)
WIN_VER = "1.0"
FPS = 20

# Sprite group

sprites_all = pygame.sprite.Group()
cars_all = pygame.sprite.Group()
blocks_all = pygame.sprite.Group()




class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()

    def createBlock(self, position):
        print(position[0], position[1])
        self.rect.x =  position[0]
        self.rect.y = position[1]
    