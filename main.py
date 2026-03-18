import pygame
import sys
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FPS, 
                     FIREBOY_SPRITE_PATH, WATERGIRL_SPRITE_PATH,
                     RED_GEM_COLOR, BLUE_GEM_COLOR)
from player import Player
from level import Level

def main():
    """
    Main entry point for the Fireboy and Watergirl clone.
    Initializes Pygame, handles the game loop, and coordinates updates.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fireboy and Watergirl Prototype")
    clock = pygame.time.Clock()

    # Define Control Schemes
    # Fireboy usually uses Arrow Keys
    fireboy_controls = {
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT,
        'jump': pygame.K_UP
    }
    
    # Watergirl usually uses WASD
    watergirl_controls = {
        'left': pygame.K_a,
        'right': pygame.K_d,
        'jump': pygame.K_w
    }

    # Setup Level
    level = Level()
    level.create_basic_level()

    # Create Players
    fireboy = Player(50, 500, FIREBOY_SPRITE_PATH, fireboy_controls)
    watergirl = Player(150, 500, WATERGIRL_SPRITE_PATH, watergirl_controls)

    # Sprite Groups for Rendering
    all_sprites = pygame.sprite.Group()
    all_sprites.add(level.all_sprites)
    all_sprites.add(fireboy)
    all_sprites.add(watergirl)
    
    # We maintain a separate group for players if we need specific updates later
    players = pygame.sprite.Group()
    players.add(fireboy)
    players.add(watergirl)

    # Game Loop
    running = True
    while running:
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # 2. Input Polling
        keys = pygame.key.get_pressed()
        
        # 3. Update State
        # We update each player relative to platforms in the level
        fireboy.update(keys, level.platforms)
        watergirl.update(keys, level.platforms)
        
        # 4. Collection Logic (Gems)
        # Check collisions between each player and the gems in the level.
        # Fireboy only collects Red gems, Watergirl only collects Blue gems.
        for player, gem_color, name in [(fireboy, RED_GEM_COLOR, "Fireboy"), 
                                        (watergirl, BLUE_GEM_COLOR, "Watergirl")]:
            collected = pygame.sprite.spritecollide(player, level.gems, False)
            for gem in collected:
                if gem.color == gem_color:
                    gem.kill() # Remove from all groups (gems and all_sprites)
                    player.score += 1
                    print(f"{name} collected a gem! Total Score: {player.score}")

        # 5. Rendering
        screen.fill(BLACK) # Clear screen
        
        # Draw all sprites (platforms, characters, gems)
        all_sprites.draw(screen)
        
        # Refreshes the display
        pygame.display.flip()
        
        # Caps frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
