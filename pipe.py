import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
    def move(self):
        self.rect.x -= 5
        
    def update(self):
        self.move()