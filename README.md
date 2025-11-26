# 2D Metroidvania Game

A 2D Metroidvania-style platformer game built with Python and Pygame.

## Features

- **Player Character**: Smooth movement with physics-based controls
- **Metroidvania Elements**: 
  - Ability progression system
  - Exploration-based gameplay
  - Backtracking with new abilities
- **Core Mechanics**:
  - Running and jumping
  - Double jump (unlockable)
  - Wall jump (unlockable)
  - Dash (unlockable)
  - Health and energy systems
  - Checkpoint system
  - Collectibles and upgrades

## Project Structure

```
rpi-project/
├── main.py                 # Main game entry point
├── requirements.txt        # Python dependencies
├── assets/                 # Game assets
│   ├── sprites/           # Character and object sprites
│   ├── tilemaps/          # Level tilemaps
│   └── sounds/            # Audio files
├── src/                   # Source code
│   ├── entities/          # Game entities (player, enemies, etc.)
│   ├── levels/            # Level definitions and loading
│   └── systems/           # Game systems (rendering, input, etc.)
└── README.md              # This file
```

## Installation

1. Install Python 3.8 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Controls

- **Arrow Keys / WASD**: Move left/right
- **Space / Z**: Jump
- **X / C**: Attack
- **Left Shift / C**: Dash (when unlocked)
- **E / Up**: Interact
- **Escape**: Exit game

## Getting Started

Run the game:
```bash
python main.py
```

## Development

### Adding New Abilities

1. Add the ability to `Player` class in `src/entities/player.py`
2. Update `GameState` to track the ability
3. Add input handling in `InputHandler`
4. Create visual feedback in `Renderer`

### Creating Levels

1. Create new level classes in `src/levels/`
2. Use the `Level` class methods to add platforms, hazards, and collectibles
3. Load levels in the main game loop

### Adding Assets

Place your game assets in the appropriate folders:
- Sprites: `assets/sprites/`
- Tilemaps: `assets/tilemaps/`
- Sounds: `assets/sounds/`

## Game Systems

- **Player**: Handles player physics, movement, and abilities
- **GameState**: Manages game progression, collectibles, and player stats
- **Renderer**: Handles all rendering and camera work
- **InputHandler**: Processes input and provides edge detection
- **Level**: Defines level structure and elements

## Future Enhancements

- Enemy AI and combat system
- Save/load system
- More complex level design
- Particle effects and visual polish
- Sound effects and music
- Boss battles
- Equipment system
- Map system

## Dependencies

- **pygame**: Core game engine
- **pymunk**: Physics engine (for advanced physics)
- **pytmx**: Tiled map loader
- **pillow**: Image processing

## License

This project is open source and available under the MIT License.
