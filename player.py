#Imports
import pygame
import numpy as np
import time
import os 
from assets import *


# Class

class Player(pygame.sprite.Sprite):
    # sprite for car
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"red_car2.png")).convert()
        self.image.set_colorkey((255,255,255))   
        self.orig_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (WIN_RES[0], WIN_RES[1]/2)
        self.speed = 0 
        self.angle = 0
        
        #Sensors
        self.sensor_0 = pygame.Rect(self.rect.center[0], self.rect.center[1],3,10)
        
        # self.sensor_1
        # self.sensor_2
        # self.sensor_3
        # self.sensor_4
        # self.sensor_5
        
    def collision(self,screen,ent,font):
        color = (0,255,0)
        #pygame.draw.circle(screen,(0,255,0), self.rect.center, 70, 4)
        pygame.draw.rect(screen, color, self.rect, 2)

        for entite in pygame.sprite.spritecollide(self, ent, False):
            clip = self.rect.clip(entite.rect)
            pygame.draw.rect(screen, pygame.Color('red'), clip)
            hits = [edge for edge in ['bottom', 'top', 'left', 'right'] if getattr(clip, edge) == getattr(self.rect, edge)]
            # text = font.render(f'Collision at {", ".join(hits)}', True, pygame.Color('white'))
            # screen.blit(text, (20, 70))
            
      
        
    def update(self):
        self.speed = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.angle += +5
            self.rotate()

        if keystate[pygame.K_RIGHT]:
            self.angle += -5
            self.rotate()              

        if keystate[pygame.K_UP]:
            self.speed = 10
            angle_inc = self.angle % 360
            
            if keystate[pygame.K_g]:
                    self.speed += 20
            # print(angle_inc) 
            if (angle_inc >= 0):
                # print(" A gauche")
                self.rect.x     = self.rect.x  - self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  - self.speed*np.cos(angle_inc*np.pi/180)
            if (angle_inc < 0):
                # print(" A droite")
                self.rect.x     = self.rect.x  + self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  + self.speed*np.cos(angle_inc*np.pi/180)
                                    
        if keystate[pygame.K_DOWN]:
            self.speed = 10
            angle_inc = self.angle % 360
            # print(angle_inc) 
            if (angle_inc >= 0):
                # print(" A gauche")
                self.rect.x     = self.rect.x  +  self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  + self.speed*np.cos(angle_inc*np.pi/180)
            if (angle_inc < 0):
                # print(" A droite")
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
            
                   
    def rotate(self):
        """Rotate the image of the sprite around its center."""
        # `rotozoom` usually looks nicer than `rotate`. Pygame's rotation
        # functions return new images and don't modify the originals.
        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        self.image.set_colorkey((0,0,0))       
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)
 
