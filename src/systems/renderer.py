import pygame

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.camera_x = 0
        self.camera_y = 0
        
        # Colors
        self.bg_color = (20, 20, 30)
        self.platform_color = (100, 100, 100)
        self.hazard_color = (200, 50, 50)
        
    def set_camera(self, x, y):
        """Set camera position"""
        self.camera_x = x
        self.camera_y = y
    
    def world_to_screen(self, x, y):
        """Convert world coordinates to screen coordinates"""
        screen_x = x - self.camera_x
        screen_y = y - self.camera_y
        return screen_x, screen_y
    
    def render_player(self, player):
        """Render the player"""
        screen_x, screen_y = self.world_to_screen(player.x, player.y)
        player_rect = pygame.Rect(screen_x, screen_y, player.width, player.height)
        pygame.draw.rect(self.screen, player.color, player_rect)
        
        # Draw facing indicator
        eye_y = screen_y + 10
        if player.facing_right:
            pygame.draw.circle(self.screen, (255, 255, 255), 
                             (int(screen_x + player.width - 8), int(eye_y)), 3)
        else:
            pygame.draw.circle(self.screen, (255, 255, 255), 
                             (int(screen_x + 8), int(eye_y)), 3)
    
    def render_platform(self, platform):
        """Render a platform"""
        screen_x, screen_y = self.world_to_screen(platform['x'], platform['y'])
        platform_rect = pygame.Rect(screen_x, screen_y, 
                                   platform['width'], platform['height'])
        pygame.draw.rect(self.screen, self.platform_color, platform_rect)
    
    def render_hazard(self, hazard):
        """Render a hazard (spikes, lava, etc.)"""
        screen_x, screen_y = self.world_to_screen(hazard['x'], hazard['y'])
        hazard_rect = pygame.Rect(screen_x, screen_y, 
                                 hazard['width'], hazard['height'])
        pygame.draw.rect(self.screen, self.hazard_color, hazard_rect)
    
    def render_collectible(self, collectible):
        """Render a collectible item"""
        screen_x, screen_y = self.world_to_screen(collectible['x'], collectible['y'])
        
        # Draw as a glowing circle
        color = collectible.get('color', (255, 215, 0))  # Gold color by default
        pygame.draw.circle(self.screen, color, 
                         (int(screen_x + 16), int(screen_y + 16)), 12)
        pygame.draw.circle(self.screen, (255, 255, 255), 
                         (int(screen_x + 16), int(screen_y + 16)), 8)
    
    def render_background(self):
        """Render background elements"""
        # Simple gradient background
        self.screen.fill(self.bg_color)
        
        # Add some background elements (stars, etc.)
        import random
        random.seed(42)  # Fixed seed for consistent star positions
        for _ in range(50):
            star_x = random.randint(0, self.screen.get_width())
            star_y = random.randint(0, self.screen.get_height())
            pygame.draw.circle(self.screen, (100, 100, 100), (star_x, star_y), 1)
    
    def render_ui(self, game_state):
        """Render UI elements"""
        font = pygame.font.Font(None, 36)
        
        # Health bar
        health_text = font.render(f"Health: {game_state.current_health}/{game_state.max_health}", 
                                 True, (255, 255, 255))
        self.screen.blit(health_text, (10, 10))
        
        # Energy bar
        energy_text = font.render(f"Energy: {game_state.current_energy}/{game_state.max_energy}", 
                                 True, (255, 255, 255))
        self.screen.blit(energy_text, (10, 50))
        
        # Abilities
        y_offset = 90
        abilities_font = pygame.font.Font(None, 24)
        for ability in game_state.unlocked_abilities:
            ability_text = abilities_font.render(f"✓ {ability}", True, (100, 255, 100))
            self.screen.blit(ability_text, (10, y_offset))
            y_offset += 25
