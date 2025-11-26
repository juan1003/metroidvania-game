class Level:
    def __init__(self, name):
        self.name = name
        self.width = 3200  # Level width in pixels
        self.height = 1200  # Level height in pixels
        
        # Level elements
        self.platforms = []
        self.hazards = []
        self.collectibles = []
        self.enemies = []
        self.checkpoints = []
        self.exits = []
        
        # Background and visual elements
        self.background_elements = []
        self.foreground_elements = []
        
        # Starting position for player
        self.spawn_x = 100
        self.spawn_y = 400
    
    def add_platform(self, x, y, width, height, platform_type="normal"):
        """Add a platform to the level"""
        platform = {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'type': platform_type
        }
        self.platforms.append(platform)
    
    def add_hazard(self, x, y, width, height, hazard_type="spikes"):
        """Add a hazard to the level"""
        hazard = {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'type': hazard_type
        }
        self.hazards.append(hazard)
    
    def add_collectible(self, x, y, item_type="health", color=(255, 215, 0)):
        """Add a collectible item to the level"""
        collectible = {
            'x': x,
            'y': y,
            'type': item_type,
            'color': color,
            'collected': False
        }
        self.collectibles.append(collectible)
    
    def add_checkpoint(self, x, y):
        """Add a checkpoint to the level"""
        checkpoint = {
            'x': x,
            'y': y,
            'activated': False
        }
        self.checkpoints.append(checkpoint)
    
    def add_exit(self, x, y, width, height, destination_level, spawn_x, spawn_y):
        """Add an exit to another level"""
        exit_door = {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'destination': destination_level,
            'spawn_x': spawn_x,
            'spawn_y': spawn_y
        }
        self.exits.append(exit_door)
    
    def create_test_level(self):
        """Create a simple test level"""
        # Ground
        self.add_platform(0, 600, 3200, 600, "normal")
        
        # Platforms
        self.add_platform(200, 500, 200, 20, "normal")
        self.add_platform(500, 400, 150, 20, "normal")
        self.add_platform(750, 350, 200, 20, "normal")
        self.add_platform(1050, 450, 150, 20, "normal")
        self.add_platform(1300, 300, 200, 20, "normal")
        
        # Walls
        self.add_platform(0, 0, 20, 1200, "normal")  # Left wall
        self.add_platform(3180, 0, 20, 1200, "normal")  # Right wall
        
        # Hazards
        self.add_hazard(400, 580, 100, 20, "spikes")
        self.add_hazard(900, 580, 150, 20, "spikes")
        
        # Collectibles
        self.add_collectible(250, 450, "health", (255, 100, 100))
        self.add_collectible(550, 350, "energy", (100, 100, 255))
        self.add_collectible(850, 300, "upgrade", (255, 215, 0))
        self.add_collectible(1100, 400, "health", (255, 100, 100))
        self.add_collectible(1400, 250, "ability", (200, 100, 255))
        
        # Checkpoints
        self.add_checkpoint(800, 550)
        self.add_checkpoint(1500, 550)
        
        # Exit
        self.add_exit(3000, 500, 80, 100, "level2", 100, 400)
