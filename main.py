import pygame, sys, random
from flappy import Flappy
from pipe import Pipedown, Pipeup


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 400))
        self.clock = pygame.time.Clock()
        
        self.flappy = pygame.sprite.GroupSingle(Flappy('white', 50, 50))
        self.pipes = pygame.sprite.Group()
  
        # Timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)
        done = False
                   
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.flappy.sprite.jump()
                    
            self.screen.fill((0, 0, 0))        
            
            
            
            # Draw the pipes            
            if event.type == self.obstacle_timer and not done:
                done = True
                number = random.randint(-125,-11)
                y = number + 550
                self.pipes.add(Pipeup(y))
                self.pipes.add(Pipedown(number))
                
            done = False
                
            
            self.pipes.update()
            self.pipes.draw(self.screen)
            
            
            self.flappy.draw(self.screen)
            self.flappy.update()
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()