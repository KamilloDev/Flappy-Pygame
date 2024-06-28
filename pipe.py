import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, width, height, y):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill('blue')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = y
        
    def move(self):
        self.rect.x -= 5
        
    def update(self):
        self.move()
        
class Pipes(Pipe):
    def __init__(self, loc_y):
        super().__init__(50, 150, loc_y)
        pass