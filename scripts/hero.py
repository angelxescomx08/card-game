import pygame
import os

class Hero:
    def __init__(self, screen):
        self.screen = screen
        # Definir las coordenadas y dimensiones de la primera sub imagen
        self.sprite_width, self.sprite_height = 64, 64
        self.x, self.y = 0, 0

        # Inicializar variables
        self.current_frame = 0
        self.columns = 6  # Número de columnas en la hoja de sprites
        # Cargar la hoja de sprites
        # Obtener la ruta absoluta del directorio actual
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construir la ruta completa al archivo
        sprite_sheet_path = os.path.join(current_dir, '../assets/hero/neuro_idle_sheet.png')
        if not os.path.exists(sprite_sheet_path):
            raise FileNotFoundError(f"No se encontró el archivo: {sprite_sheet_path}")
        self.sprite_sheet = pygame.image.load(sprite_sheet_path).convert()

    def animate(self):
        self.current_frame = (self.current_frame + 1) % self.columns
        self.x = self.current_frame * self.sprite_width
        self.screen.blit(
            self.sprite_sheet, 
            (0, 0), 
            (self.x, self.y, self.sprite_width, self.sprite_height)
        )
