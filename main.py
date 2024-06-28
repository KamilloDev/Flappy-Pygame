import pygame, sys, random
from flappy import Flappy
from pipe import Pipedown, Pipeup


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 400))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Flappy bird game - Pygame ')
        
        self.background = pygame.image.load('imgs/game_background.png')
        self.bg_rect = self.background.get_rect(topleft = (0,0))
        
        self.flappy = pygame.sprite.GroupSingle(Flappy('white', 50, 50))
        self.pipes = pygame.sprite.Group()

        self.game_active = True
        
        self.start_time = 0
        
        # Fonts
        self.basic_font = pygame.font.Font(None, 30)
        self.game_over = self.basic_font.render('Game Over! Press spacebar', True, 'black')
        self.game_over_rect = self.game_over.get_rect(center = (200, 200))
        
        # Timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1500)
        done = False

    def display_score(self):
        current_time = int(pygame.time.get_ticks() / 1000) - self.start_time
        score_surface = self.basic_font.render(f'Score: {current_time}', True, 'black')
        score_rect = score_surface.get_rect(center = (235, 50))
        self.screen.blit(score_surface, score_rect)
        return current_time
              
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.flappy.sprite.jump()
                
                if self.game_active:
                    # Draw the pipes            
                    if event.type == self.obstacle_timer:
                        done = True
                        number = random.randint(-125,-11)
                        y = number + 550
                        self.pipes.add(Pipeup(y))
                        self.pipes.add(Pipedown(number))
  
            
            
            self.bg_rect.x -= 1
            self.screen.blit(self.background, self.bg_rect)      
            if self.bg_rect.x <= -1800:
                self.bg_rect.x = 0
             
            
            
            if self.flappy.sprite.rect.y >= 400 or self.flappy.sprite.rect.y <= 0:
                self.game_active = False
            
            if pygame.sprite.groupcollide(self.flappy, self.pipes, True, False):
                self.game_active = False
            
            if self.game_active:
                self.pipes.update()
                self.pipes.draw(self.screen)
                
                
                self.flappy.draw(self.screen)
                self.flappy.update()
                
            score = self.display_score()
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()