import pygame
import sys
from constants import (SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, FPS, 
                     FIREBOY_SPRITE_PATH, WATERGIRL_SPRITE_PATH,
                     RED_GEM_COLOR, BLUE_GEM_COLOR)
from player import Player
from level import Level

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fireboy and Watergirl Prototype")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 64, bold=True)

    # Controls
    fireboy_controls = {'left': pygame.K_LEFT, 'right': pygame.K_RIGHT, 'jump': pygame.K_UP}
    watergirl_controls = {'left': pygame.K_a, 'right': pygame.K_d, 'jump': pygame.K_w}

    # Level Setup
    current_level_num = 1
    level = Level()
    level.load_level(current_level_num) 

    # Players
    fireboy = Player(50, 500, FIREBOY_SPRITE_PATH, fireboy_controls)
    watergirl = Player(150, 500, WATERGIRL_SPRITE_PATH, watergirl_controls)

    all_sprites = pygame.sprite.Group()
    
    def refresh_sprite_groups():
        all_sprites.empty()
        all_sprites.add(level.all_sprites)
        all_sprites.add(fireboy)
        all_sprites.add(watergirl)

    refresh_sprite_groups()

    # Exit Area (Matches Level 1 top platform at y=250)
    exit_rect = pygame.Rect(270, 170, 60, 80) 

    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over and event.type == pygame.KEYDOWN:
                running = False # Press any key to close after game over

        if not game_over:
            keys = pygame.key.get_pressed()
            fireboy.update(keys, level.platforms)
            watergirl.update(keys, level.platforms)
            
            # Gem Collection
            for player, gem_color in [(fireboy, RED_GEM_COLOR), (watergirl, BLUE_GEM_COLOR)]:
                collected = pygame.sprite.spritecollide(player, level.gems, False)
                for gem in collected:
                    if gem.color == gem_color:
                        gem.kill()
                        player.score += 1

            # Level Transition Logic
            if fireboy.rect.colliderect(exit_rect) and watergirl.rect.colliderect(exit_rect):
                current_level_num += 1
                
                if current_level_num > 2:
                    game_over = True
                else:
                    level.load_level(current_level_num)
                    # Reposition exit for Level 2 (Matches top platform at y=250)
                    if current_level_num == 2:
                        exit_rect.topleft = (370, 170) 
                    
                    # Reset Positions
                    fireboy.rect.topleft = (50, 500)
                    watergirl.rect.topleft = (150, 500)
                    fireboy.vel_y = 0
                    watergirl.vel_y = 0
                    refresh_sprite_groups()

        # --- DRAWING ---
        screen.fill(BLACK)
        
        if not game_over:
            pygame.draw.rect(screen, (0, 255, 0), exit_rect, 2) 
            all_sprites.draw(screen)
        else:
            # Display Game Over Text
            text_surf = font.render("GAME OVER", True, WHITE)
            text_rect = text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            screen.blit(text_surf, text_rect)
            
            sub_text = pygame.font.SysFont("Arial", 24).render("Press any key to exit", True, WHITE)
            sub_rect = sub_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60))
            screen.blit(sub_text, sub_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()