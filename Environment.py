import pygame
import random
import math

class Environment:
    def __init__(self) -> None:
        # inicialización de variables necesarias
        #pantalla
        self.x_screen = 400
        self.y_screen = 400
        # jugador (bot)
        self.x_player = random.randint(0, self.x_screen)
        self.y_player = random.randint(0, self.y_screen)
        # pelota
        self.x_ball = random.randint(0, self.x_screen)
        self.y_ball = random.randint(0, self.y_screen)
        # portería
        self.x_goal = self.x_screen
        self.y_goal = self.y_screen/2


        print("player: ", self.x_player, self.y_player)
        print("ball: ", self.x_ball, self.y_ball)
        print("goal: ", self.x_goal, self.y_goal)
        # setup de pygame
        pygame.init()

        screen = pygame.display.set_mode((self.x_screen, self.y_screen))
        clock = pygame.time.Clock()
        running = True 

        while running:
            # revisar si se sale
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill("#78e87e")

            # pos_goal = (self.x_goal, self.y_goal, 10, 10)
            # pygame.draw.rect(screen, "black", pos_goal, 5)
            pos_goal = (self.x_goal-10, self.y_goal - 50, 10, 100)
            pygame.draw.rect(screen, "white", pos_goal, 2)
            
            pos_ball = pygame.Vector2(self.x_ball, self.y_ball)
            pygame.draw.circle(screen, "red", pos_ball, 5)

            pos_player = (self.x_player, self.y_player, 15, 15)
            pygame.draw.rect(screen, "black", pos_player, 2)

            pygame.display.flip()

            clock.tick(60)

        pygame.quit()

    def diffuse(self): 
        0

    
    def distace(self):
        0

    def strenght(self):
        0