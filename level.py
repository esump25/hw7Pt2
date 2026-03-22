import pygame
from constants import GRAY, RED_GEM_COLOR, BLUE_GEM_COLOR

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Gem(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        points = [(10, 0), (20, 10), (10, 20), (0, 10)]
        pygame.draw.polygon(self.image, color, points)
        self.rect = self.image.get_rect(topleft=(x, y))

class Level:
    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.gems = pygame.sprite.Group() 
        self.all_sprites = pygame.sprite.Group()
        
    def add_platform(self, platform):
        self.platforms.add(platform)
        self.all_sprites.add(platform)

    def add_gem(self, x, y, color):
        gem = Gem(x, y, color)
        self.gems.add(gem)
        self.all_sprites.add(gem)

    def clear_level(self):
        self.platforms.empty()
        self.gems.empty()
        self.all_sprites.empty()

    def load_level(self, level_num):
        self.clear_level()
        # Boundaries
        self.add_platform(Platform(0, 580, 800, 20)) # Floor
        self.add_platform(Platform(0, 0, 20, 600))   # Left Wall
        self.add_platform(Platform(780, 0, 20, 600)) # Right Wall

        if level_num == 1:
            # Gaps of 110 pixels (580 -> 470 -> 360 -> 250)
            self.add_platform(Platform(100, 470, 300, 20))
            self.add_platform(Platform(450, 360, 250, 20))
            self.add_platform(Platform(150, 250, 300, 20)) # Top Platform
            
            # Gems for Level 1
            self.add_gem(150, 440, RED_GEM_COLOR)
            self.add_gem(500, 330, BLUE_GEM_COLOR)
            
        elif level_num == 2:
            # Middle divider
            self.add_platform(Platform(390, 150, 20, 430)) 
            
            # Fireboy side (Left)
            self.add_platform(Platform(20, 470, 150, 20))
            self.add_platform(Platform(200, 360, 150, 20))
            self.add_gem(50, 440, RED_GEM_COLOR)   # Added Gem
            self.add_gem(250, 330, RED_GEM_COLOR)  # Added Gem
            
            # Watergirl side (Right)
            self.add_platform(Platform(610, 470, 150, 20))
            self.add_platform(Platform(430, 360, 150, 20))
            self.add_gem(650, 440, BLUE_GEM_COLOR) # Added Gem
            self.add_gem(480, 330, BLUE_GEM_COLOR) # Added Gem

            # Final Goal Platform
            self.add_platform(Platform(300, 250, 200, 20))        