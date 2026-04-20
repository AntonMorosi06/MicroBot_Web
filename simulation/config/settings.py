"""
MicroBot System - Simulation Settings
-------------------------------------
Global configuration values for the swarm simulation module.
"""

# Window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "MicroBot System - Swarm Simulation"

# Timing
FPS = 60

# Colors
BACKGROUND_COLOR = (10, 14, 24)
BOT_COLOR = (0, 220, 255)
LINK_COLOR = (60, 100, 140)
TEXT_COLOR = (230, 235, 245)
ACCENT_COLOR = (90, 180, 255)

# World
WORLD_PADDING = 60

# Bots
NUM_BOTS = 16
BOT_RADIUS = 7
BOT_MAX_SPEED = 2.2
BOT_DETECTION_RADIUS = 110
BOT_SEPARATION_DISTANCE = 22

# Rule strengths
ALIGNMENT_STRENGTH = 0.030
COHESION_STRENGTH = 0.0025
SEPARATION_STRENGTH = 0.055

# Rendering options
SHOW_LINKS = True
SHOW_HUD = True
SHOW_CENTER_OF_MASS = False

SHOW_CENTER_OF_MASS = True
