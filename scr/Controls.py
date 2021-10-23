import pygame
import sys

def KeyPressed(player: object) -> None:
    """Checks the event loop for KEY press, and sets player position offsets."""
    offset = int((pygame.display.get_surface().get_width() / 500)) # This is so assets move relative to window size.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # pygame key events behave oddly if you dont use a variable turned on and off by key up and key down.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                    player.y_offset = -offset
            if event.key == pygame.K_RIGHT:
                    player.x_offset = offset
            if event.key == pygame.K_DOWN:
                    player.y_offset = offset
            if event.key == pygame.K_LEFT:
                    player.x_offset = -(offset + 1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                    player.y_offset = 0
            if event.key == pygame.K_RIGHT:
                    player.x_offset = 0
            if event.key == pygame.K_DOWN:
                    player.y_offset = 0
            if event.key == pygame.K_LEFT:
                    player.x_offset = 0
   