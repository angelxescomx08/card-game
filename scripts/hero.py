import pygame
import os

class Hero:
    def __init__(self, screen):
        self.screen = screen
        self.sprite_width, self.sprite_height = 80, 80
        self.x, self.y = 0, 0
        self.position = [0,0]
        self.current_frame = 0
        self.columns = 6  # Número de columnas en la hoja de sprites

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
            self.position, 
            (self.x, self.y, self.sprite_width, self.sprite_height)
        )
        self.move()

    def move(self):
        self.position[0] += 1
        #self.position[1] += y    
