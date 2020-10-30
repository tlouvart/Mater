#Imports
import pygame
import numpy as np
import time
import os 
from assets.py import *
from player.py import *

#config
WIN_NAME =  "Mater"
WIN_RES = (1280,960)
WIN_VER = "1.0"
FPS = 30




#Init, Title

pygame.init()
pygame.mixer.init()
pygame.display.set_caption(WIN_NAME + " v" + WIN_VER)
screen = pygame.display.set_mode(WIN_RES, pygame.RESIZABLE)
clock = pygame.time.Clock()




# Class

class Player(pygame.sprite.Sprite):
    # sprite for car
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"red_car2.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (WIN_RES[0]/2, WIN_RES[1]/2)
        self.speed = 0 
        self.angle = 0
        
    def update(self):
        self.speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.angle += +5
        if keystate[pygame.K_RIGHT]:
            self.angle += -5                  
        if keystate[pygame.K_UP]:
            self.speed = 10
            angle_inc = self.angle % 360
            print(angle_inc) 
            if (angle_inc >= 0):
                print(" A gauche")
                self.rect.x     = self.rect.x  - self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  - self.speed*np.cos(angle_inc*np.pi/180)
            if (angle_inc < 0):
                print(" A droite")
                self.rect.x     = self.rect.x  + self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  + self.speed*np.cos(angle_inc*np.pi/180)
                                    
        if keystate[pygame.K_DOWN]:
            self.speed = 10
            angle_inc = self.angle % 360
            print(angle_inc) 
            if (angle_inc >= 0):
                print(" A gauche")
                self.rect.x     = self.rect.x  +  self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  + self.speed*np.cos(angle_inc*np.pi/180)
            if (angle_inc < 0):
                print(" A droite")
                self.rect.x     = self.rect.x  - self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  - self.speed*np.cos(angle_inc*np.pi/180)
            
        if self.rect.right > WIN_RES[0]:
            self.rect.right = WIN_RES[0]
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIN_RES[1]:
            self.rect.bottom = WIN_RES[1]
            
def blitRotate(surf, image, pos, originPos, angle, dx, dy):
    # calcaulate the axis aligned bounding box of the rotated image
    pos = list(pos)   
    pos[0] =  pos[0] + dx
    pos[1] =  pos[1] + dy        
    
    
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot 
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    return rotated_image, origin

        
# Sprite group

sprites_all = pygame.sprite.Group()
player = Player()
sprites_all.add(player)

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
    
    
    
    #Update
    sprites_all.update()
    
    #Draw Render
    screen.fill((0,0,255))
    player_image_new, origin_player_new = blitRotate(screen, player.image, (WIN_RES[0]/2, WIN_RES[1]/2), (player.image.get_size()[0]//2, player.image.get_size()[1]//2), player.angle, player.rect.x, player.rect.y)
    # rotate and blit the image
    screen.blit(player_image_new, origin_player_new)

    # draw rectangle around the image
    pygame.draw.rect (screen, (255, 0, 0), (*origin_player_new, *player_image_new.get_size()),2)    
    sprites_all.draw(screen)
    
    #Flip the final
    pygame.display.flip()
        