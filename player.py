import pygame
from constants import GRAVITY, PLAYER_SPEED, JUMP_FORCE

class Player(pygame.sprite.Sprite):
    """
    Base Player class for Fireboy and Watergirl.
    Handles movement, jumping, and collision detection.
    
    Design Decisions:
    - Inherits from pygame.sprite.Sprite to easily use group features.
    - Uses a velocity-based movement system for smoother physics.
    - Uses collision flags (on_ground) to handle jumping stability.
    - Added score tracking for collected gems.
    """
    def __init__(self, x, y, image_path, controls):
        super().__init__()
        
        # Load and scale character sprite
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            # Scale to a standard character size (approx 40x50 pixels)
            self.image = pygame.transform.scale(self.image, (40, 50))
        except pygame.error:
            # Fallback if image fails to load
            self.image = pygame.Surface((40, 50))
            self.image.fill((255, 0, 0)) # Red default
            
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Gameplay state
        self.score = 0
        
        # Physics state
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False
        
        # Control mapping (dict containing keys for 'left', 'right', 'jump')
        self.controls = controls

    def apply_gravity(self):
        """Adds gravity to vertical velocity."""
        self.vel_y += GRAVITY
        # Terminal velocity to prevent excessive speed
        if self.vel_y > 10:
            self.vel_y = 10

    def move(self, keys, platforms):
        """
        Handles horizontal movement based on input keys.
        Checks for horizontal platform collisions.
        """
        self.vel_x = 0
        if keys[self.controls['left']]:
            self.vel_x = -PLAYER_SPEED
        if keys[self.controls['right']]:
            self.vel_x = PLAYER_SPEED
            
        # Move horizontally
        self.rect.x += self.vel_x
        
        # Resolve horizontal collisions
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_x > 0: # Moving right
                    self.rect.right = platform.rect.left
                elif self.vel_x < 0: # Moving left
                    self.rect.left = platform.rect.right

    def jump(self, platforms):
        """Triggers a jump if the player is on solid ground."""
        if self.on_ground:
            self.vel_y = JUMP_FORCE
            self.on_ground = False

    def vertical_movement(self, platforms):
        """
        Applies gravity and horizontal movement.
        Checks for vertical platform collisions.
        """
        self.apply_gravity()
        self.rect.y += self.vel_y
        
        self.on_ground = False # Reset before checking collisions
        
        # Resolve vertical collisions
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.vel_y > 0: # Falling
                    self.rect.bottom = platform.rect.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0: # Moving up (hit head)
                    self.rect.top = platform.rect.bottom
                    self.vel_y = 0

    def update(self, keys, platforms):
        """Main update function called every frame."""
        self.move(keys, platforms)
        
        # Handle jump input separately to allow buffered jumps if needed, 
        # but here we keep it simple.
        if keys[self.controls['jump']]:
            self.jump(platforms)
            
        self.vertical_movement(platforms)
