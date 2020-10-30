#Imports
import pygame
import numpy as np
import time
import os 
from assets  import *
from player import *
from cars import *


#Init, Title

pygame.init()
pygame.mixer.init()
pygame.display.set_caption(WIN_NAME + " v" + WIN_VER)
screen = pygame.display.set_mode(WIN_RES, pygame.RESIZABLE)
clock = pygame.time.Clock()

       
# Sprite group

sprites_all = pygame.sprite.Group()
cars_all = pygame.sprite.Group()
blocks_all = pygame.sprite.Group()
player = Player()
sprites_all.add(player)
car_one = Cars()
cars_all.add(car_one)
car_two = Cars()
cars_all.add(car_two)
car_four = Cars()
cars_all.add(car_four)
car_three = Cars()
cars_all.add(car_three)


def detection(ent, color):
    for entite in ent:
        pygame.draw.rect(screen, color, ((entite.rect.topleft[0]-10, entite.rect.topleft[1]-10), (entite.image.get_size()[0]+20,entite.image.get_size()[1]+20)),2)    
 
class Block(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,100))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()

    def createBlock(self, position):
        print(position[0], position[1])
        self.rect.x =  position[0]
        self.rect.y = position[1]
    
#Loop
launched = True
angle = 0
while launched:
    #FPS
    clock.tick(FPS)
    #Tous les inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
            pygame.quit() 
        if event.type == pygame.MOUSEBUTTONUP:
            b = Block()
            blocks_all.add(b)
            b.createBlock(pygame.mouse.get_pos())    
    
    #Update
    sprites_all.update()
    cars_all.update()
    blocks_all.update()
    
    #check collisions
    for b in blocks_all:   
        #destroy
        pygame.sprite.spritecollide(b, cars_all, True)
        pygame.sprite.spritecollide(b, sprites_all, True)
    
    #Draw Render
    screen.fill((0,0,255))

    #player.blitRotate(screen, pos, old_pos)
    sprites_all.draw(screen)
    cars_all.draw(screen)
    blocks_all.draw(screen)
    
    detection(sprites_all, (255,0,0))
    detection(cars_all, (0,255,0))
    
    #Flip the final
    pygame.display.flip()
        