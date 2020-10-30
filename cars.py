#Imports
import pygame
import numpy as np
import time
import os 
from assets import *


# Class

class Cars(pygame.sprite.Sprite):
    # sprite for car
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"green_car2.png")).convert()
        self.image.set_colorkey((255,255,255))   
        self.orig_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (WIN_RES[0]/2, WIN_RES[1]/2)
        self.speed = 0 
        self.angle = 0
        self.compteur = 0
    
    def brain(self):
        self.compteur += 1
        val = np.random.randint(25,45)      
        if self.compteur <= 5 :           
            val = -val
            if self.rect.right >= WIN_RES[0]:
                self.angle += val
                self.rotate() 
            if self.rect.left <= 0:
                self.angle += val
                self.rotate()
            if self.rect.top == 0:
                self.angle += val
                self.rotate()
            if self.rect.bottom >= WIN_RES[1]:
                self.angle += val
                self.rotate()
            return 3
        self.compteur = 0 
        return 3    
        
    def update(self):
        self.speed = 0        
        action = self.brain()
                    
        if action == 3:
            self.speed = 10
            angle_inc = self.angle % 360
            # print(angle_inc) 
            if (angle_inc >= 0):
                self.rect.x     = self.rect.x  - self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  - self.speed*np.cos(angle_inc*np.pi/180)
            if (angle_inc < 0):
                self.rect.x     = self.rect.x  + self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  + self.speed*np.cos(angle_inc*np.pi/180)
        if action == 4:
            self.speed = 10
            angle_inc = self.angle % 360
            #print(angle_inc) 
            if (angle_inc >= 0):
                self.rect.x     = self.rect.x  +  self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  + self.speed*np.cos(angle_inc*np.pi/180)
            if (angle_inc < 0):
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
