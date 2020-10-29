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
            

            
    def blitRotate(self, surf, pos, originPos):
        # calcaulate the axis aligned bounding box of the rotated image
        pos = list(pos)
        pos[0] =  pos[0] + self.rect.x
        pos[1] =  pos[1] + self.rect.y  
        
        w, h       = self.image.get_size()
        box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(self.angle) for p in box]
        min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    
        # calculate the translation of the pivot 
        pivot        = pygame.math.Vector2(originPos[0]/2, -originPos[1]/2)
        pivot_rotate = pivot.rotate(self.angle)
        pivot_move   = pivot_rotate - pivot
    
        # calculate the upper left origin of the rotated image
        origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    
        # get a rotated image
        rotated_image = pygame.transform.rotate(self.image, self.angle)
    
        # rotate and blit the image
        screen.blit(rotated_image, origin)
        
        # draw rectangle around the image
        pygame.draw.rect (screen, (255, 0, 0), (*origin, *rotated_image.get_size()),2)


        
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
    pos = (WIN_RES[0]/2, WIN_RES[1]/2)
    old_pos = (player.image.get_size()[0]//2, player.image.get_size()[1]//2)
    player.blitRotate(screen, pos, old_pos)
    sprites_all.draw(screen)
    
    #Flip the final
    pygame.display.flip()
        