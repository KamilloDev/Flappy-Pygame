import pygame

class Flappy(pygame.sprite.Sprite):
    def __init__(self , color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        bird_1 = pygame.transform.scale_by(pygame.image.load('imgs/00.png').convert_alpha(), 1.8)
        bird_2 = pygame.transform.scale_by(pygame.image.load('imgs/10.png').convert_alpha(), 1.8)
        bird_3 = pygame.transform.scale_by(pygame.image.load('imgs/20.png').convert_alpha(), 1.8)
        bird_4 = pygame.transform.scale_by(pygame.image.load('imgs/30.png').convert_alpha(), 1.8)
        bird_5 = pygame.transform.scale_by(pygame.image.load('imgs/40.png').convert_alpha(), 1.8)
        bird_6 = pygame.transform.scale_by(pygame.image.load('imgs/50.png').convert_alpha(), 1.8)
        bird_7 = pygame.transform.scale_by(pygame.image.load('imgs/60.png').convert_alpha(), 1.8)
        bird_8 = pygame.transform.scale_by(pygame.image.load('imgs/70.png').convert_alpha(), 1.8)
        bird_9 = pygame.transform.scale_by(pygame.image.load('imgs/80.png').convert_alpha(), 1.8)
        
        self.birds = [bird_1, bird_2, bird_3, bird_4, bird_5, bird_6, bird_7, bird_8, bird_9]
        self.bird_index = 0
        self.image = self.birds[self.bird_index]
        self.rect = self.image.get_rect(center = (50,50))
        
        self.rect = self.image.get_rect()
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -10
        self.rect.x = 10
        self.rect.y = 100
        
    def update(self):
        self.change_animation()
        self.velocity += self.gravity
        self.rect.y += self.velocity

    def check_Alive(self):
        if self.rect.y >= 400 or self.rect.y <= 0:
            self.kill()
            return False
        else:
            return True
        
    def jump(self):
        self.velocity = self.jump_strength
        
    def change_animation(self):
        self.bird_index += 0.5
        if self.bird_index >= len(self.birds):
            self.bird_index = 0
            self.jumping = False
        self.image = self.birds[int(self.bird_index)]
