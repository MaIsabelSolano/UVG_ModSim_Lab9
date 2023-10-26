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
        self.x_ball = random.randint(0, self.x_screen - 100)
        #self.x_ball = 350
        self.y_ball = random.randint(0, self.y_screen)
        # portería
        self.x_goal = self.x_screen - 10
        self.y_goal = self.y_screen/2 - 50

        self.s = self.strength()
        self.kicked = False

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
            dx, dy, l = self.ballDistance()
            if l > 5:

                pos_goal = (self.x_goal, self.y_goal, 10, 100)
                pygame.draw.rect(screen, "white", pos_goal, 2)
                
                pos_ball = pygame.Vector2(self.x_ball, self.y_ball)
                pygame.draw.circle(screen, "red", pos_ball, 5)

                pos_player = (self.x_player, self.y_player, 15, 15)
                pygame.draw.rect(screen, "black", pos_player, 2)

                pygame.display.flip()

                clock.tick(60)
                self.diffuse()

            else:
                running = False



            


        pygame.quit()


    def diffuse(self):
        d = self.distance()

        if d > 5 and not self.kicked:
            self.Move()
        else:
            # patear la pelota en dirección a la portería
            self.kick(self.s)
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

        v = random.randint(2,4)
        self.x_player += v*dx
        self.y_player += v*dy


    # Desencadena el movimiento de la pelota
    def kick(self, strength):
        # calcular la fuerza del disparo - Debe ser por default al menos tan rápido como el máximo del jugador o más, sino el jugador alcanza la pelota y la patea repetidamente a cada rato
        s = strength
        print(' - ', s)
        self.kicked = True
        # calcular la dirección del disparo - esto puede ser fijo, pues sabemos siempre dónde está la portería
        dx, dy, l = self.ballDistance()

        if l > 0:
            dx = dx/l
            dy = dy/l

        self.x_ball += s*dx
        self.y_ball += s*dy
        # imponer las coordenas finales del disparo
        pass

    # Lógica para calcular la fuerza del disparo de la pelota en relación a la distancia entre el jugador y la portería
    def strength(self):
        dx, dy, l = self.ballDistance()

        # hard kick
        if l > 200:
            return 9
        # medium kick
        elif l > 100:
            return 6
        # soft kick
        else:
            return 3
        
    def ballDistance(self):
        dx = self.x_goal - self.x_ball
        dy = (self.y_goal + 50) - self.y_ball

        l = math.sqrt(dx**2 + dy**2)
        return dx, dy, l
