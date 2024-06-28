import pygame, sys
from flappy import Flappy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 400))
        self.clock = pygame.time.Clock()
        
        self.flappy = pygame.sprite.GroupSingle(Flappy('white', 50, 50))
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill((0, 0, 0))        
            
            self.flappy.draw(self.screen)
            self.flappy.update()
            pygame.display.update()

Game().run()