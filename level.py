import pygame
from constants import GRAY, RED_GEM_COLOR, BLUE_GEM_COLOR

class Platform(pygame.sprite.Sprite):
    """Simple solid platform for collisions."""
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Gem(pygame.sprite.Sprite):
    """
    Represent collectible gems.
    Design Decisions: 
    - Each gem has a color to distinguish between Fireboy (red) and Watergirl (blue) gems.
    - Uses a simple diamond-shaped polygon for visual representation.
    """
    def __init__(self, x, y, color):
        super().__init__()
        self.color = color
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        # Draw a diamond shape using a polygon
        points = [(10, 0), (20, 10), (10, 20), (0, 10)]
        pygame.draw.polygon(self.image, color, points)
        self.rect = self.image.get_rect(topleft=(x, y))

class Level:
    """Manages level structure and sprite groups."""
    def __init__(self):
        self.platforms = pygame.sprite.Group()
        self.gems = pygame.sprite.Group() # Group specifically for collectibles
        self.all_sprites = pygame.sprite.Group()
        
    def add_platform(self, platform):
        self.platforms.add(platform)
        self.all_sprites.add(platform)

    def add_gem(self, x, y, color):
        gem = Gem(x, y, color)
        self.gems.add(gem)
        self.all_sprites.add(gem)

    def create_basic_level(self):
        """Builds a basic starting level."""
        # Ground
        ground = Platform(0, 580, 800, 20)
        self.add_platform(ground)
        
        # Some simple platforms to jump on
        p1 = Platform(100, 450, 150, 20)
        p2 = Platform(350, 350, 150, 20)
        p3 = Platform(600, 250, 150, 20)
        
        self.add_platform(p1)
        self.add_platform(p2)
        self.add_platform(p3)

        # Add some collectible gems
        self.add_gem(150, 420, RED_GEM_COLOR)
        self.add_gem(400, 320, BLUE_GEM_COLOR)
        self.add_gem(650, 220, RED_GEM_COLOR)
        
        # Walls
        left_wall = Platform(0, 0, 20, 600)
        right_wall = Platform(780, 0, 20, 600)
        self.add_platform(left_wall)
        self.add_platform(right_wall)
