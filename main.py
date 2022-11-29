import pygame, sys, time
from settings import *
from level import Level, Level2
from button import *

class Game:
    def __init__(self):
        # general setup
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        self.backgound = pygame.image.load("./graphics/menu/background.jpg")
        pygame.display.set_caption('Sasquatch')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.level2 = Level2()
    
    def level_select(self):
        while True:
            self.screen.blit(self.backgound,(0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            MENU_TEXT = get_font(75).render("Sasquatch: The Game", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            LEVEL_1 = Button(image=pygame.image.load("./graphics/menu/rect.png"), pos=(640, 250), 
                            text_input="Level 1", font=get_font(35), base_color="#d7fcd4", hovering_color="White")
            LEVEL_2 = Button(image=pygame.image.load("./graphics/menu/rect.png"), pos=(640, 400), 
                            text_input="Level 2", font=get_font(35), base_color="#d7fcd4", hovering_color="White")

            self.screen.blit(MENU_TEXT,MENU_RECT)

            for button in [LEVEL_1,LEVEL_2]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if LEVEL_1.checkForInput(MENU_MOUSE_POS):
                        game = Game()
                        game.run()
                    if LEVEL_2.checkForInput(MENU_MOUSE_POS):
                        game = Game()
                        game.run2()

            pygame.display.update()

    def run(self):
        while True:
            for event in pygame.event.get():	# event loop checking if user closing game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
 
            self.screen.fill(WATER_COLOR)			# fill corners of screen with color 
            self.level.run()                    # calling run method from Level.py 
            pygame.display.update()				# updating the screen 
            self.clock.tick(FPS)				# controlling framerate 

    def run2(self):
        while True:
            for event in pygame.event.get():	
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
 
            self.screen.fill(WATER_COLOR)
            self.level2.run()                 
            pygame.display.update()	
            self.clock.tick(FPS)

def get_font(size):
    return pygame.font.Font(UI_FONT, size)
	
game = Game()
game.level_select()