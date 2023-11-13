#Crea un código para pygame
import pygame

# Inicializa el motor de juegos
pygame.init()

# Crea una ventana de 800x600
screen = pygame.display.set_mode((800, 600))


# Crea un reloj para controlar el tiempo
clock = pygame.time.Clock()

# Crea un bucle principal
running = True
while running:
    # Controla los eventos
    for event in pygame.event.get():
        # Si el evento es salir de la ventana, termina el bucle
        if event.type == pygame.QUIT:
            running = False

    # Actualiza la pantalla
    pygame.display.flip()

    # 60 fotogramas por segundo
    clock.tick(60)

# Finaliza el motor de juegos
pygame.quit()