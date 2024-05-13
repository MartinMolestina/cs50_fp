import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Retro Car Racing Game')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define track parameters
TRACK_COLOR = WHITE
TRACK_WIDTH = 20
TRACK_RADIUS = 300

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Clear the screen
    window.fill(BLACK)  # Fill the screen with black

    # Draw background scenery
    # Example: Sky
    pygame.draw.rect(window, BLUE, (0, 0, WINDOW_WIDTH, WINDOW_HEIGHT / 2))

    # Example: Ground
    pygame.draw.rect(window, GREEN, (0, WINDOW_HEIGHT / 2, WINDOW_WIDTH, WINDOW_HEIGHT / 2))

    # Draw the track
    pygame.draw.ellipse(window, TRACK_COLOR, (WINDOW_WIDTH / 2 - TRACK_RADIUS, WINDOW_HEIGHT / 4, 2 * TRACK_RADIUS, WINDOW_HEIGHT / 2), TRACK_WIDTH)

    # Draw lane markings
    pygame.draw.line(window, WHITE, (WINDOW_WIDTH // 2 - TRACK_RADIUS, WINDOW_HEIGHT // 2), (WINDOW_WIDTH // 2 - TRACK_RADIUS, WINDOW_HEIGHT // 2 + TRACK_WIDTH * 2), TRACK_WIDTH // 2)
    pygame.draw.line(window, WHITE, (WINDOW_WIDTH // 2 + TRACK_RADIUS, WINDOW_HEIGHT // 2), (WINDOW_WIDTH // 2 + TRACK_RADIUS, WINDOW_HEIGHT // 2 + TRACK_WIDTH * 2), TRACK_WIDTH // 2)

    # Draw barriers
    pygame.draw.rect(window, RED, (TRACK_WIDTH // 2, WINDOW_HEIGHT // 4, WINDOW_WIDTH // 2 - TRACK_RADIUS + TRACK_WIDTH, TRACK_WIDTH))
    pygame.draw.rect(window, RED, (WINDOW_WIDTH // 2 + TRACK_RADIUS - TRACK_WIDTH // 2, WINDOW_HEIGHT // 4, WINDOW_WIDTH // 2 - TRACK_RADIUS + TRACK_WIDTH, TRACK_WIDTH))


    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

