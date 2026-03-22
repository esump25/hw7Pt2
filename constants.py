import pygame

# --- Screen Settings ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)
GREEN = (0, 255, 0)

# --- Gem Colors ---
RED_GEM_COLOR = (255, 50, 50)
BLUE_GEM_COLOR = (50, 50, 255)

# --- Physics Constants ---
GRAVITY = 0.8
PLAYER_SPEED = 5
JUMP_FORCE = -14

# --- Assets ---
# Paths to sprites provided by user
FIREBOY_SPRITE_PATH = "assets/fireboy_sprite.webp"
WATERGIRL_SPRITE_PATH = "assets/watergirl_sprite.webp"
