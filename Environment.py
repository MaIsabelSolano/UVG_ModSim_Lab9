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
        self.x_goal = self.x_screen - 10
        self.y_goal = self.y_screen/2 - 50

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
            pos_goal = (self.x_goal, self.y_goal, 10, 100)
            pygame.draw.rect(screen, "white", pos_goal, 2)
            
            pos_ball = pygame.Vector2(self.x_ball, self.y_ball)
            pygame.draw.circle(screen, "red", pos_ball, 5)

            pos_player = (self.x_player, self.y_player, 15, 15)
            pygame.draw.rect(screen, "black", pos_player, 2)

            pygame.display.flip()

            clock.tick(60)
            self.diffuse()
            


        pygame.quit()


    def diffuse(self):
        d = self.distance()

        if d > 5:
            self.Move()
        else:
            # patear la pelota en dirección a la portería
            pass

    
    def distance(self):
        x2, x1 = self.x_ball, self.x_player
        y2, y1 = self.y_ball, self.y_player
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    def Move(self):
        dx = self.x_ball - self.x_player
        dy = self.y_ball - self.y_player

        l = math.sqrt(dx**2 + dy**2)
        if l > 0:
            dx = dx/l
            dy = dy/l

        v = random.randint(3,5)
        self.x_player += v*dx
        self.y_player += v*dy



    def strenght(self):
        0