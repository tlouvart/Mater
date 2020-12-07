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

# writings

font = pygame.font.SysFont(None, 26)

# Adding a player in the interface
       
player = Player()
sprites_all.add(player)

# car_one = Cars()
# cars_all.add(car_one)
# car_two = Cars()
# cars_all.add(car_two)
# car_four = Cars()
# cars_all.add(car_four)
# car_three = Cars()
# cars_all.add(car_three)

#Génération des vehicules
for i in range(9):
    
    pos1 = np.random.randint(0,WIN_RES[0])
    pos2 = np.random.randint(0,WIN_RES[1])
    c = Cars(path_img = "green_car2.png", pos=(pos1,pos2),  idCar = i)
    cars_all.add(c)


#### DETECTION SYSTEM

def detection(ent, color):
    for entite in ent:
         hits = entite.collision(screen, sprites_all, font)
         player.collision(screen, ent, font)
         if hits:
             entite.brain_v1(hits[0])
        

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
        if event.type == pygame.KEYDOWN:                  
            if event.key == pygame.K_e:
                FPS -= 5
            if event.key == pygame.K_r:
                FPS = 30
            if event.key == pygame.K_p:
                FPS = 1

    
    #Update
    sprites_all.update()
    cars_all.update()
    blocks_all.update()
    
    #check collisions
    for b in blocks_all:   
        #destroy
        pygame.sprite.spritecollide(b, cars_all, False)
        pygame.sprite.spritecollide(b, sprites_all, False)

    
    
    #Draw Render
    screen.fill((0,0,255))

    #player.blitRotate(screen, pos, old_pos)
    sprites_all.draw(screen)
    cars_all.draw(screen)
    blocks_all.draw(screen)
    
    #detection(sprites_all, (255,0,0)) et collision
    detection(cars_all, (0,255,0))
    #detection(sprites_all, (0,255,0))
    
    #Flip the final
    pygame.display.flip()
        