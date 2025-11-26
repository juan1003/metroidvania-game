import pygame
import sys
from src.entities.player import Player
from src.systems.game_state import GameState
from src.systems.renderer import Renderer
from src.systems.input_handler import InputHandler
from src.systems.background_loader import BackgroundLoader

class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 1024
        self.screen_height = 768
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Metroidvania Game")
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialize game systems
        self.game_state = GameState()
        self.renderer = Renderer(self.screen)
        self.input_handler = InputHandler()
        self.background_loader = BackgroundLoader()
        
        # Try to load background from Unsplash
        print("Loading background from Unsplash...")
        if self.background_loader.get_unsplash_background():
            self.background_loader.set_background("unsplash")
            print("Background loaded successfully!")
        else:
            print("Using fallback background")
        
        # Create player
        self.player = Player(100, 400)
        
        # Colors
        self.bg_color = (20, 20, 30)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
        
        # Handle input
        keys = pygame.key.get_pressed()
        self.input_handler.update(keys)
    
    def update(self, dt):
        # Update player
        self.player.update(dt, self.input_handler, self.game_state)
    
    def render(self):
        # Render background with parallax
        self.background_loader.render(self.screen, self.player.x, self.player.y)
        
        # Render game objects
        self.renderer.render_player(self.player)
        
        # Render UI
        self.renderer.render_ui(self.game_state)
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000.0  # Delta time in seconds
            
            self.handle_events()
            self.update(dt)
            self.render()
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
