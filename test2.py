#Imports
import pygame
import numpy as np
import time
import os 


#config
WIN_NAME =  "Mater"
WIN_RES = (1280,960)
WIN_VER = "1.0"
FPS = 30

#Variables


#Init, Title

pygame.init()
pygame.mixer.init()
pygame.display.set_caption(WIN_NAME + " v" + WIN_VER)
screen = pygame.display.set_mode(WIN_RES, pygame.RESIZABLE)
clock = pygame.time.Clock()

# Assets

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


# Class

class Player(pygame.sprite.Sprite):
    # sprite for car
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"red_car2.png")).convert()
        self.image.set_colorkey((255,255,255))
        self.orig_image = self.image
        self.rect = self.image.get_rect()
        self.rect.center = (WIN_RES[0]/2, WIN_RES[1]/2)
        self.speed = 0 
        self.angle = 0
        
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
            

            
    def rotate(self):
        """Rotate the image of the sprite around its center."""
        # `rotozoom` usually looks nicer than `rotate`. Pygame's rotation
        # functions return new images and don't modify the originals.
        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        # Create a new rect with the center of the old rect.
        self.rect = self.image.get_rect(center=self.rect.center)


        
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

    #player.blitRotate(screen, pos, old_pos)
    sprites_all.draw(screen)
    
    #Flip the final
    pygame.display.flip()
        