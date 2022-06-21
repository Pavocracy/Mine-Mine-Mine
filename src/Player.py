import pygame
from Paths import resource_path

class Player:
    """The Player class handles all of the attributes for a player object."""
    # TODO: Add a check if the player is off screen. Or add bounds to keep player on screen?
    
    def __init__(self, game_width: float, game_height: float) -> None:
        """Sets the intial attributes for the player object."""
        self.scale_w = game_width / 25
        self.scale_h = game_height / 25
        self.image = pygame.image.load(resource_path('assets/Player/seagull.png')).convert()
        self.image = pygame.transform.scale(self.image, (self.scale_w, self.scale_w))
        self.image.set_colorkey((0, 255, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.x = 24
        self.x_offset = 0
        self.y = 240
        self.y_offset = 0

    def CheckCollision(self, object_mask: object, object_x: int, object_y: int) -> bool:
        """Returns Bool of players position overlapping the objects position."""   
        offset = (self.x - object_x, self.y - object_y)
        return object_mask.overlap(self.mask, offset)

    def Move(self) -> None:
        """Update the position attributes for the player."""
        self.x = (self.x + self.x_offset)
        self.y = (self.y + self.y_offset)
