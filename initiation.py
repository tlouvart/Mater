#Imports
import pygame as pyg
import numpy as np
import time

#Init
pyg.init()


#config
WIN_NAME =  "Mater"
WIN_RES = (1280,960)
WIN_VER = "1.0"


blue_color = (80, 120, 255)
red_color = (255,0,0)

def creation_rect(window_s, actual_pos, color, list_obj):
    pos_2 = list((actual_pos[0]+30, actual_pos[1]))
    coords = (actual_pos, pos_2)
    obj = (color, coords[0], coords[1], 30)
    list_obj.append(obj)
    
    pyg.display.flip()
    return list_obj


class Car():
    def __init__(self, idCAR):
        self.id = idCAR
        self.car_sprite = pyg.image.load("car_yellow.png")
        self.w_car = car_sprite.get_width()
        self.h_car = car_sprite.get_height()
               
    def onClick(self,mouse_pos):
        self.old_pos = list(mouse_pos)        
        collide_box = pyg.Rect((self.old_pos),(self.w_car,self.h_car))       
        window_s.surface.blit(self.car_sprite,self.old_pos)
        pyg.draw.rect(window_s.surface, red_color, collide_box, 2)
        pyg.display.flip()

    def gravite(self, list_obj):
        while self.old_pos[1] <= 600:    
            time.sleep(.0011)
            print(self.old_pos[1])
            self.old_pos[1] += 1
            window_s = Background()
            collide_box = pyg.Rect((self.old_pos),(self.w_car,self.h_car))       
            window_s.surface.blit(self.car_sprite,self.old_pos)
            pyg.draw.rect(window_s.surface, red_color, collide_box, 2)
            pyg.display.flip() 
            
class Background():
    def __init__(self, list_obj):
        #init surface
        self.surface = pyg.display.set_mode(WIN_RES, pyg.RESIZABLE)
        self.surface.fill(blue_color)
        pyg.draw.rect(self.surface, red_color, pyg.Rect(50,700,300,25))

        for o in list_obj:
            print("test")
            pyg.draw.line(self.surface, o[0], o[1], o[2], o[3])

class Block():
    
            

#Variables
launched = True
pos = [0,0]
nb_car = 0
list_obj = []                
            
#Title
pyg.display.set_caption(WIN_NAME + " v" + WIN_VER)

window_s = background(list_obj)


#Sprites
car_sprite = pyg.image.load("car_yellow.png") #retourne une surface
# car_sprite.convert()




while launched:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            launched = False
            pyg.quit()
        v1 = np.random.randint(0,255)
        v2 = np.random.randint(0,255)
        v3 = np.random.randint(0,255)
        color = (v1,v2,v3)
        if event.type == pyg.MOUSEBUTTONUP:
            nb_car += 1
            car = Car(nb_car)
            print(car)
            print(nb_car)
            car.onClick(pyg.mouse.get_pos())
            car.gravite()
            
        if event.type == pyg.KEYDOWN:    
            if event.key == pyg.K_RIGHT:
                pos[0] += 10
                print(pos)
                creation_rect(window_s, pos, color)
            if event.key == pyg.K_LEFT:
                pos[0] -= 10
                print(pos)
                creation_rect(window_s, pos, color) 
            if event.key == pyg.K_UP:
                pos[1] += 10
                print(pos)
                creation_rect(window_s, pos, color)
            if event.key == pyg.K_DOWN:
                pos[1] -= 10
                print(pos)
                creation_rect(window_s, pos, color)                
            
    #corps du programme
    pyg.display.flip()
        