#Imports
import pygame
import numpy as np
import time
import os 
from assets import *
import math

# Class
        
        
class Cars(pygame.sprite.Sprite, object):
    # sprite for car
    def __init__(self, path_img, pos, idCar):
        pygame.sprite.Sprite.__init__(self)
        self.ID = idCar
        self.image = pygame.image.load(os.path.join(img_folder,path_img)).convert()
        self.image.set_colorkey((255,255,255))   
        self.orig_image = self.image.copy()
        self.rect = self.image.get_rect()
        # self.rect.center = (WIN_RES[0]/2, WIN_RES[1]/2)
        self.rect.center = pos
        
        self.compteur = 0
        self.speed = 0
        self.angle = 0
        
        self.radars = []
        
    def check_radar(self, degree, screen):
        len = 0
        x = int(self.rect.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * len)
        y = int(self.rect.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * len)

        while not screen.get_at((x, y)) == (35,200,200, 255) and len < 100:
            len = len + 1
            x = int(self.rect.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * len)
            y = int(self.rect.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * len)

        dist = int(math.sqrt(math.pow(x - self.rect.center[0], 2) + math.pow(y - self.rect.center[1], 2)))
        self.radars.append([(x, y), dist])     
    
    def draw_radar(self, screen):
        for r in self.radars:
            pos, dist = r
            pygame.draw.line(screen, (0, 255, 0), self.rect.center, pos, 1)
            pygame.draw.circle(screen, (0, 255, 0), pos, 5)
    
    def collision(self,screen,ent,font):
        color = (0,255,0)
        #pygame.draw.circle(screen,(0,255,0), self.rect.center, 70, 4)
        pygame.draw.rect(screen, color, self.rect, 2)
        
        for entite in pygame.sprite.spritecollide(self, ent, False):
            clip = self.rect.clip(entite.rect)
            pygame.draw.rect(screen, pygame.Color('red'), clip)
            hits = [edge for edge in ['bottom', 'top', 'left', 'right'] if getattr(clip, edge) == getattr(self.rect, edge)]
            text = font.render(f'Collision at {", ".join(hits)}', True, pygame.Color('white'))
            text2 = font.render(f'Car n° : {self.ID}', True, pygame.Color('white'))
            screen.blit(text, (20, 30 + self.ID*20))
            screen.blit(text2, (20, self.ID*20 + 10))
            return hits
    
        
    def brain_v1(self, test):
        val = np.random.randint(-50,50)
        if (test == 'bottom'):
            self.angle += val
            self.rotate()            
        if (test == 'top'):
            self.angle += val
            self.rotate()            
        if (test == 'left'):
            self.angle += val
            self.rotate()
        if (test == 'right'):
            self.angle += val
            self.rotate()
        return 3
    
            
    def update(self,screen):
        self.speed = 0
        test = self.limitV2(self.rect)        
        action = self.brain_v1(test)
                    
        if action == 3:
            self.speed = 12
            angle_inc = self.angle % 360
            # print(angle_inc) 
            if (angle_inc >= 0):
                self.rect.x     = self.rect.x  - self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  - self.speed*np.cos(angle_inc*np.pi/180)                
            if (angle_inc < 0):
                self.rect.x     = self.rect.x  + self.speed*np.sin(angle_inc*np.pi/180)
                self.rect.y     = self.rect.y  + self.speed*np.cos(angle_inc*np.pi/180)
        
        #self.radars.clear()
        for d in range(-90, 120, 45):
            self.check_radar(d, screen)
            
       
    def draw(self, screen):
        self.draw_radar(screen)

                       
    def limitV2(self,ent):
        if ent.right > WIN_RES[0]:
            ent.right = WIN_RES[0]
            return "right"
        if ent.left < 0:
            ent.left = 0 
            return "left"            
        if ent.top < 0:
            ent.top = 0
            return "top"
        if ent.bottom > WIN_RES[1]:
            ent.bottom = WIN_RES[1]
            return "bottom"
        
        
    def rotate(self):
        """Rotate the image of the sprite around its center."""
        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        self.image.set_colorkey((0,0,0))       

        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)
