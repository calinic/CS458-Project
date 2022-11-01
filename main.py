import pygame, sys, time
from settings import *
from level import Level


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Sasquatch')
        self.clock = pygame.time.Clock()
        
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():	# event loop checking if user closing game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
 
            self.screen.fill('black')			# filling screen with color 
            self.level.run()                    # calling run method from Level.py 
            pygame.display.update()				# updating the screen 
            self.clock.tick(FPS)				# controlling framerate 

if __name__ == '__main__':	# check if this is the main file 
    game = Game()			# create an instance of game class
    game.run()				# calling the run method 
