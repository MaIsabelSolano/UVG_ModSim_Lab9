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

        self.up = False
        self.left = False


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
        d = self.distace()
        if d > 5:
            print("distance1: ", self.distace())
            self.moveX()
            self.left = True if self.distace() > d else False
            print("distance2: ", self.distace(), "left: ", self.left)
            d = self.distace()
            self.moveY()
            self.up = True if self.distace() > d else False
            print("distance3: ", self.distace(), "up: ", self.up)
        else:
            # patear la pelota en dirección a la portería
            0
        

    def moveX(self):
        if self.left:
            if self.x_player > 0:
                self.x_player -= random.randint(3,5)
            else:
                self.left = False
        else:
            if self.x_player < self.x_screen:
                self.x_player += random.randint(3,5)
            else:
                self.left = True


    def moveY(self):
        if self.up:
            if self.y_player > 0:
                self.y_player -= random.randint(3,5)
            else:
                self.up = False
        else:
            if self.y_player < self.y_screen:
                self.y_player += random.randint(3,5)
            else:
                self.up = True

    
    def distace(self):
        x2, x1 = self.x_ball, self.x_player
        y2, y1 = self.y_ball, self.y_player
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)

    def strenght(self):
        0