import pygame

class Flappy(pygame.sprite.Sprite):
    def __init__(self , color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.rect.x = 0
        self.rect.y = 0
        
    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        # Keep the sprite within the screen bounds
        if self.rect.y > 500 - self.rect.height:
            self.rect.y = 400 - self.rect.height
            self.velocity = 0
        elif self.rect.y < 0:
            self.rect.y = 0
            self.velocity = 0
        
    def jump(self):
        self.velocity = self.jump_strength
