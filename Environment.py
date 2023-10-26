import pygame
import random
import math
import matplotlib.pyplot as plt
import numpy as np

class Environment:
    def __init__(self) -> None:
        # Configuración de Matplotlib para las funciones de pertenencia
        plt.ion()

        # Gráficos para la distancia
        self.fig_distance, self.ax_distance = plt.subplots()
        self.ax_distance.set_title('Función de Pertenencia para Distancia')
        self.ax_distance.set_xlabel('Distancia')
        self.ax_distance.set_ylabel('Pertenencia')
        self.line_distance, = self.ax_distance.plot([], [], label='Pertenencia')
        self.ax_distance.legend()

        # Gráficos para la fuerza
        self.fig_strength, self.ax_strength = plt.subplots()
        self.ax_strength.set_title('Función de Pertenencia para Fuerza')
        self.ax_strength.set_xlabel('Fuerza')
        self.ax_strength.set_ylabel('Pertenencia')
        self.bar_strength = self.ax_strength.bar([], [], label='Pertenencia', color='orange')
        self.ax_strength.legend()

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

        # Configuración de Matplotlib para las funciones de pertenencia
        plt.ion()  # Habilitar modo interactivo para actualizar gráficos en tiempo real

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
            self.update_membership_functions()

        pygame.quit()
        plt.show(block="False")


    def diffuse(self):
        d = self.distance()

        if d > 5 and not self.kicked:
            self.Move()
        else:
            # patear la pelota en dirección a la portería
            self.kick(self.s)
            # Actualizar gráficos de funciones de pertenencia
            
            pass

    
    def distance(self):
        x2, x1 = self.x_ball, self.x_player
        y2, y1 = self.y_ball, self.y_player
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    def defuzzify_distance(self, distance):
        
        if distance > 100:
            return "lejano"
        elif 30 < distance <= 100:
            return "medio"
        else:
            return "cercano"
        
    def Move(self):
        dx = self.x_ball - self.x_player
        dy = self.y_ball - self.y_player

        l = math.sqrt(dx**2 + dy**2)
        if l > 0:
            dx = dx/l
            dy = dy/l
        
        # utilizar el valor en la funcion de defuzzificacion
        v = self.defuzzify_distance(l)

        print("distancia", l)
        print("velocidad: ", v)


        if v == "lejano":
            v = random.randint(5,7)
        
        if v == "medio":
            v = random.randint(2,4)
        
        if v == "cercano":
            v = random.randint(1,2)
        
        
        self.x_player += v*dx
        self.y_player += v*dy

        return v


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

    def update_membership_functions(self):
        # Obtener datos para graficar
        dx, dy, distance = self.ballDistance()
        print("distance: ", distance)

        # Actualizar gráfico de distancia
        x_vals = np.linspace(0, 300, 100)
        y_vals = [self.defuzzify_distance(d) for d in x_vals]
        self.line_distance.set_xdata(x_vals)
        self.line_distance.set_ydata(y_vals)
        self.ax_distance.relim()
        self.ax_distance.autoscale_view()

        # Actualizar gráfico de fuerza
        # labels = ['lejano', 'medio', 'cercano']
        # y_vals_strength = [9, 6, 3]
        # for bar, val in zip(self.bar_strength, y_vals_strength):
        #     bar.set_height(val)
        # self.ax_strength.relim()
        # self.ax_strength.autoscale_view()

        # Actualizar gráficos
        self.fig_distance.canvas.draw_idle()
        self.fig_strength.canvas.draw_idle()