import pygame, random

class Pipeup(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        pipeup = pygame.transform.scale_by(pygame.image.load('imgs/pipeup.png').convert_alpha(), 2)
        self.image = pipeup
        # I guess it sets the positions too
        self.rect = self.image.get_rect(center = (450, y))

    def destroy(self):
        if self.rect.x <= -100:
           self.kill() 
           
    def move(self):
        self.rect.x -= 2
    
    def update(self):
       self.move()
       self.destroy()

class Pipedown(pygame.sprite.Sprite):
    def __init__(self, number):
        super().__init__()
        pipedown = pygame.transform.scale_by(pygame.image.load('imgs/pipedown.png').convert_alpha(), 2)
        self.gap = 50
        self.y = 0
        self.image = pipedown
        # Also sets the pos?
        self.rect = self.image.get_rect(center = (450, number))

    def destroy(self):
        if self.rect.x <= -100:
           self.kill() 

    def move(self):
        self.rect.x -= 2
    
    def update(self):
       self.move()
       self.destroy()      
