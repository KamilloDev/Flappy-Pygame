import pygame

class Flappy(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite = pygame.Rect(50, 50, 50, 50)
        self.rect = self.sprite
        
    