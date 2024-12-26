from .settings import *
import pygame
import random

class drop :
    
    slow = False
    up = False

    def __init__(self) :
        self.color = get_raincolor()
        self.x = random.randint(0, width) 
        self.y = random.randint(-200, height//3)
        self.yspeed = random.random() 
        self.length = random.randint(10, 20)
    
    def fall(self) :

        if (drop.slow == True) and (drop.up == False):
            self.yspeed = random.random() 
        elif (drop.up == True) and (drop.slow == True):
            self.yspeed = (random.random() * (-1)) 
        elif (drop.slow == False) :
            self.yspeed = random.random() + 1
        self.y += self.yspeed
        
        if self.yspeed > 0 :
            if self.y > height  :
                self.y = random.randint(-200, 0)
                self.x = random.randint(0, width)
                if (drop.slow == False) :
                    self.yspeed = random.random() + 1
                if (drop.slow == True) :
                    self.yspeed = random.random() 

        elif self.yspeed < 0 :
            if self.y < 0 :
                self.y = random.randint(height, height + 200)
                self.x = random.randint(0, width)


    def show(self, window) :
        #print(get_colors())
        pygame.draw.line(window, get_raincolor(), (self.x, self.y), (self.x, self.y + self.length), 3)
    
    @classmethod
    def up_status(cls) :
        return cls.up

    @classmethod
    def slow_status(cls) :
        return cls.slow
    
    @classmethod
    def drop_slow(cls) :
        cls.slow = True
    
    @classmethod
    def drop_fast(cls) :
        cls.slow = False
        
    @classmethod
    def drop_down(cls) :
        cls.up = False
    
    @classmethod
    def drop_up(cls) :
        cls.up = True
    
    def __str__(self) :
        return f"{self.x} {self.y} {self.yspeed}"