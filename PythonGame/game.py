import os
import pygame


class Game:
    def __init__(self):
        #Settings the screen
        self.width = 1000
        self.height = 700
        self.win = pygame.display.set_mode((self.width, self.height))
        self.enemys = []
        self.towers = []
        self.lives = 10
        self.money = 100
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))


    def run(self):

        # Main Game Loop
        run = True
        clock = pygame.time.Clock()

        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

        pygame.quit()

    def draw(self):
        self.win.blit(self.bg, (0, 0))
        pygame.display.update()
