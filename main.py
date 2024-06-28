import pygame, sys
from flappy import Flappy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 400))
        self.clock = pygame.time.Clock()
        
        self.flappy = pygame.sprite.Group(Flappy())
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.flappy.draw(self.screen)

Game().run()