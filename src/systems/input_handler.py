import pygame

class InputHandler:
    def __init__(self):
        # Movement keys
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False
        
        # Action keys
        self.jump_pressed = False
        self.jump_held = False
        self.attack_pressed = False
        self.dash_pressed = False
        self.interact_pressed = False
        
        # Previous frame state for edge detection
        self.prev_jump = False
        self.prev_attack = False
        self.prev_dash = False
        self.prev_interact = False
    
    def update(self, keys):
        # Store previous state
        self.prev_jump = self.jump_pressed
        self.prev_attack = self.attack_pressed
        self.prev_dash = self.dash_pressed
        self.prev_interact = self.interact_pressed
        
        # Movement
        self.move_left = keys[pygame.K_LEFT] or keys[pygame.K_a]
        self.move_right = keys[pygame.K_RIGHT] or keys[pygame.K_d]
        self.move_up = keys[pygame.K_UP] or keys[pygame.K_w]
        self.move_down = keys[pygame.K_DOWN] or keys[pygame.K_s]
        
        # Actions
        self.jump_pressed = keys[pygame.K_SPACE] or keys[pygame.K_z]
        self.jump_held = self.jump_pressed
        self.attack_pressed = keys[pygame.K_x] or keys[pygame.K_c]
        self.dash_pressed = keys[pygame.K_LSHIFT] or keys[pygame.K_c]
        self.interact_pressed = keys[pygame.K_e] or keys[pygame.K_UP]
    
    def jump_just_pressed(self):
        """Check if jump was just pressed this frame"""
        return self.jump_pressed and not self.prev_jump
    
    def attack_just_pressed(self):
        """Check if attack was just pressed this frame"""
        return self.attack_pressed and not self.prev_attack
    
    def dash_just_pressed(self):
        """Check if dash was just pressed this frame"""
        return self.dash_pressed and not self.prev_dash
    
    def interact_just_pressed(self):
        """Check if interact was just pressed this frame"""
        return self.interact_pressed and not self.prev_interact
    
    def get_movement_vector(self):
        """Get normalized movement vector"""
        vx = 0
        vy = 0
        
        if self.move_left:
            vx = -1
        elif self.move_right:
            vx = 1
        
        if self.move_up:
            vy = -1
        elif self.move_down:
            vy = 1
        
        # Normalize diagonal movement
        if vx != 0 and vy != 0:
            vx *= 0.707  # 1/sqrt(2)
            vy *= 0.707
        
        return vx, vy
