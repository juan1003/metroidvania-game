import pygame
import requests
import os
from PIL import Image

class BackgroundLoader:
    def __init__(self, assets_dir="assets"):
        self.assets_dir = assets_dir
        self.background_images = {}
        self.current_background = None
        
    def download_background(self, url, filename="background.jpg"):
        """Download a background image from URL"""
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            filepath = os.path.join(self.assets_dir, filename)
            os.makedirs(self.assets_dir, exist_ok=True)
            
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"Background downloaded to {filepath}")
            return filepath
        except Exception as e:
            print(f"Error downloading background: {e}")
            return None
    
    def load_background(self, filepath, name="default"):
        """Load a background image from file"""
        try:
            image = pygame.image.load(filepath)
            self.background_images[name] = image
            print(f"Background loaded: {name}")
            return True
        except Exception as e:
            print(f"Error loading background: {e}")
            return False
    
    def get_unsplash_background(self, query="game background fantasy landscape"):
        """Get a background from Unsplash (using a test URL)"""
        # Using a different working image URL
        unsplash_url = "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?w=1920&h=1080&fit=crop"
        
        filepath = self.download_background(unsplash_url, "unsplash_bg.jpg")
        if filepath:
            self.load_background(filepath, "unsplash")
            return True
        return False
    
    def set_background(self, name):
        """Set the current background"""
        if name in self.background_images:
            self.current_background = self.background_images[name]
            return True
        return False
    
    def render(self, screen, camera_x=0, camera_y=0):
        """Render the background with parallax effect"""
        if self.current_background:
            # Scale background to screen size
            screen_width = screen.get_width()
            screen_height = screen.get_height()
            
            # Simple parallax effect
            parallax_x = camera_x * 0.3  # Background moves slower than foreground
            parallax_y = camera_y * 0.3
            
            # Create a surface for the background
            bg_surface = pygame.transform.scale(self.current_background, (screen_width, screen_height))
            
            # Apply parallax offset (with wrapping for seamless scrolling)
            x_offset = int(parallax_x % screen_width)
            y_offset = int(parallax_y % screen_height)
            
            # Draw background with wrapping
            screen.blit(bg_surface, (-x_offset, -y_offset))
            screen.blit(bg_surface, (screen_width - x_offset, -y_offset))
            screen.blit(bg_surface, (-x_offset, screen_height - y_offset))
            screen.blit(bg_surface, (screen_width - x_offset, screen_height - y_offset))
        else:
            # Fallback to solid color
            screen.fill((20, 20, 30))
