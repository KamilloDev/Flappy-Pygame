import pygame, random

class Pipeup(pygame.sprite.Sprite):
    def __init__(self, width, height, y):
        super().__init__()
        pipeup = pygame.Surface([width, height])
        self.image = pipeup
        self.image.fill('red')
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
    def __init__(self, width, height, number):
        super().__init__()
        pipedown = pygame.Surface([width, height])
        self.gap = 50
        self.y = 0
        self.image = pipedown
        self.image.fill('red')
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
