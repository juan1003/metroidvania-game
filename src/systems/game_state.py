class GameState:
    def __init__(self):
        # Game progression
        self.current_level = 0
        self.checkpoints = []
        self.unlocked_abilities = set()
        
        # Player stats
        self.max_health = 100
        self.current_health = 100
        self.max_energy = 100
        self.current_energy = 100
        
        # Collectibles
        self.items_collected = set()
        self.upgrades_obtained = set()
        
        # World state
        self.enemies_defeated = set()
        self.doors_opened = set()
        self.switches_activated = set()
    
    def unlock_ability(self, ability):
        """Unlock a new ability for the player"""
        self.unlocked_abilities.add(ability)
    
    def has_ability(self, ability):
        """Check if player has a specific ability"""
        return ability in self.unlocked_abilities
    
    def add_checkpoint(self, x, y, level_name):
        """Add a checkpoint at the specified position"""
        checkpoint = {
            'x': x,
            'y': y,
            'level': level_name,
            'health': self.current_health,
            'energy': self.current_energy
        }
        self.checkpoints.append(checkpoint)
    
    def get_last_checkpoint(self):
        """Get the most recent checkpoint"""
        if self.checkpoints:
            return self.checkpoints[-1]
        return None
    
    def collect_item(self, item_id):
        """Mark an item as collected"""
        self.items_collected.add(item_id)
    
    def has_item(self, item_id):
        """Check if an item has been collected"""
        return item_id in self.items_collected
    
    def heal(self, amount):
        """Heal the player"""
        self.current_health = min(self.current_health + amount, self.max_health)
    
    def restore_energy(self, amount):
        """Restore player energy"""
        self.current_energy = min(self.current_energy + amount, self.max_energy)
    
    def take_damage(self, amount):
        """Apply damage to player"""
        self.current_health = max(0, self.current_health - amount)
    
    def use_energy(self, amount):
        """Consume energy for abilities"""
        if self.current_energy >= amount:
            self.current_energy -= amount
            return True
        return False
