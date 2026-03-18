# Fireboy and Watergirl Clone (Python/Pygame)

This repository contains a prototype implementation of the popular Fireboy and Watergirl game, developed as part of an assignment for 15113 (HW7). The focus is on clarity, documentation, and building a solid baseline for future developers.

## Current Progress & Documentation

The project currently implements the fundamental physics and movement mechanics for two players (Fireboy and Watergirl). The code is organized into manageable modules for easy extensibility:

1. [main.py](main.py): Entry point and game loop management.
2. [player.py](player.py): Core mechanics for character movement, jumping, and collision resolution.
3. [level.py](level.py): Basic system to manage levels and platform layout.
4. [constants.py](constants.py): Centralized configuration for physics, screen settings, and colors.

### Controls:

- **Fireboy**: Use Arrow Keys to move and jump.
- **Watergirl**: Use WASD keys (W to jump).

## Project TODO List (Future Implementation)

- [ ] **Hazard Tiles**: Implement Fire, Water, and Mud tiles which interact differently with characters (Fireboy burns in water, Watergirl burns in fire, both die in mud).
- [ ] **Interactive Mechanisms**: Levers, buttons, and elevators that require coordination between both players.
- [ ] **Exit Doors**: Implementation of level completion when both players reach their respective colored doors.
- [ ] **Level Design**: A complete multi-level map with increasing difficulty.
- [ ] **UI/Menu system**: Start screen, level selection, and win/lose screens.

## Design Philosophy

The project prioritizes clarity over cleverness. Design decisions, such as using a basic velocity-based physics system and modularizing character controls, are clearly labeled with comments to ensure any developer can easily pick up where I left off.

---

fireboy_sprite credit: https://official-fireboy-watergirl.fandom.com/wiki/Fireboy

watergirl_sprite credit: https://official-fireboy-watergirl.fandom.com/wiki/Watergirl
