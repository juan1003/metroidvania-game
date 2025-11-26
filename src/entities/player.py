import pygame
import math

class Player:
    def __init__(self, x, y):
        # Position and physics
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.width = 32
        self.height = 48
        
        # Movement parameters
        self.move_speed = 200  # pixels per second
        self.jump_power = 400
        self.gravity = 800
        self.max_fall_speed = 600
        
        # State
        self.on_ground = False
        self.facing_right = True
        self.can_jump = True
        
        # Abilities (Metroidvania elements)
        self.has_double_jump = False
        self.has_wall_jump = False
        self.has_dash = False
        self.double_jump_used = False
        
        # Visual
        self.color = (100, 200, 255)
        self.rect = pygame.Rect(x, y, self.width, self.height)
    
    def update(self, dt, input_handler, game_state):
        # Handle input
        self.handle_movement(input_handler, dt)
        
        # Apply physics
        self.apply_physics(dt)
        
        # Update collision rectangle
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Check ground collision (simple platform check)
        self.check_ground_collision(game_state)
        
        # Reset double jump when on ground
        if self.on_ground:
            self.double_jump_used = False
    
    def handle_movement(self, input_handler, dt):
        # Horizontal movement
        if input_handler.move_left:
            self.vx = -self.move_speed
            self.facing_right = False
        elif input_handler.move_right:
            self.vx = self.move_speed
            self.facing_right = True
        else:
            self.vx = 0
        
        # Jumping
        if input_handler.jump_pressed:
            if self.on_ground:
                self.vy = -self.jump_power
                self.can_jump = False
            elif self.has_double_jump and not self.double_jump_used:
                self.vy = -self.jump_power * 0.8
                self.double_jump_used = True
        
        # Dashing (when ability is unlocked)
        if input_handler.dash_pressed and self.has_dash:
            dash_speed = 500
            self.vx = dash_speed if self.facing_right else -dash_speed
            # Add cooldown logic here
    
    def apply_physics(self, dt):
        # Apply gravity
        if not self.on_ground:
            self.vy += self.gravity * dt
            if self.vy > self.max_fall_speed:
                self.vy = self.max_fall_speed
        
        # Update position
        self.x += self.vx * dt
        self.y += self.vy * dt
    
    def check_ground_collision(self, game_state):
        # Simple ground collision (will be replaced with proper tilemap collision)
        ground_level = 600
        if self.y + self.height >= ground_level:
            self.y = ground_level - self.height
            self.vy = 0
            self.on_ground = True
        else:
            self.on_ground = False
        
        # Keep player in bounds
        if self.x < 0:
            self.x = 0
        elif self.x + self.width > 1024:  # Screen width
            self.x = 1024 - self.width
    
    def draw(self, screen):
        # Draw player as a rectangle for now
        pygame.draw.rect(screen, self.color, self.rect)
        
        # Draw facing indicator
        eye_y = self.y + 10
        if self.facing_right:
            pygame.draw.circle(screen, (255, 255, 255), (int(self.x + self.width - 8), int(eye_y)), 3)
        else:
            pygame.draw.circle(screen, (255, 255, 255), (int(self.x + 8), int(eye_y)), 3)
