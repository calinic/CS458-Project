import pygame, sys, time
from settings import *
from button import *
from level import Level
from level2 import Level2
from level3 import Level3
from level4 import Level4

class Game:
    def __init__(self):
        # general setup
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        self.backgound = pygame.image.load("./graphics/menu/background.jpg")
        pygame.display.set_caption('Sasquatch')
        self.clock = pygame.time.Clock()
        self.level = Level()
        self.level2 = Level2()
        #self.level3 = Level3()

    def level_select(self):
        while True:
            self.screen.blit(self.backgound,(0,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            MENU_TEXT = get_font(75).render("Sasquatch: The Game", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            LEVEL_1 = Button(image=pygame.image.load("./graphics/menu/rect.png"), pos=(640, 250), 
                            text_input="Community Forest", font=get_font(23), base_color="#d7fcd4", hovering_color="White")
            LEVEL_2 = Button(image=pygame.image.load("./graphics/menu/rect.png"), pos=(640, 350), 
                            text_input="Redwood Bowl", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            #LEVEL_3 = Button(image=pygame.image.load("./graphics/menu/rect.png"), pos=(640, 450), 
            #                text_input="Level 3", font=get_font(25), base_color="#d7fcd4", hovering_color="White")
            #LEVEL_4 = Button(image=pygame.image.load("./graphics/menu/rect.png"), pos=(640, 550), 
            #                text_input="Level 4", font=get_font(25), base_color="#d7fcd4", hovering_color="White")

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
                    if LEVEL_3.checkForInput(MENU_MOUSE_POS):
                        game3 = Game()
                        game3.run3()
                    if LEVEL_4.checkForInput(MENU_MOUSE_POS):
                        game = Game()
                        game.run4()

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
                        self.level2.toggle_menu()
 
            self.screen.fill(WATER_COLOR)
            self.level2.run()                 
            pygame.display.update()	
            self.clock.tick(FPS)

    def run3(self):
        while True:
            for event in pygame.event.get():	
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level3.toggle_menu()
 
            self.screen.fill(WATER_COLOR)
            self.level3.run()                 
            pygame.display.update()	
            self.clock.tick(FPS)

    def run4(self):
        while True:
            for event in pygame.event.get():	
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level4.toggle_menu()
 
            self.screen.fill(WATER_COLOR)
            self.level4.run()                 
            pygame.display.update()	
            self.clock.tick(FPS)

def get_font(size):
    return pygame.font.Font(UI_FONT, size)
    
game = Game()
game.level_select()