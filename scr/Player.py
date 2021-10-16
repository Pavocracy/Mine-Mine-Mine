import pygame
import math

class Player:
    """The Player class handles all of the attributes for a player object."""

    def __init__(self) -> None:
        """Sets the intial attributes for the player object"""
        self.image = pygame.image.load('assets/player/seagull.png').convert()
        self.x = 24
        self.x_offset = 0
        self.y = 240
        self.y_offset = 0

    def CheckCollision(self, object_x: int, object_y: int) -> bool:
        """Returns True if the players position is overlapping the objects position."""   
        distance = math.sqrt((math.pow(self.x - object_x, 2)) + (math.pow(self.y - object_y, 2)))
        if distance < (self.image.get_rect().width) and object_y > 0:
            return True

    def Move(self) -> None:
        """Update the position attributes for the player."""
        self.x = (self.x + self.x_offset)
        self.y = (self.y + self.y_offset)
