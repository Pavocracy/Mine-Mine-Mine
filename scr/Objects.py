import pygame
import random
import os

class Objects:
    """The Objects class contains an objects dictionary of instantiated classes of game items."""

    def __init__(self) -> None:
        """Creates an object for each item needed for the game."""
        Objects.background = Background()
        Objects.objects = {}

        for filename in os.listdir("assets/objects"):
            name = filename.split(".")[0]
            Objects.objects[name] = Items(filename)

        Objects.font = Font()

class Items:
    """The Items class handles objects that require attributes for the game state."""

    def __init__(self, filename: str) -> None:
        """Sets the attributes for the object and calls the Create method for that object."""
        self.name = filename.split(".")[0]
        self.image = pygame.image.load(f'assets/objects/{filename}').convert()
        self.mask = pygame.mask.from_surface(self.image)
        self.eaten = 0
        self.items = []
        self.Create()

    def Create(self) -> None:
        """Creates a random number of items with random position values and stores them in Objects.objects["name"].items."""
        for i in range(random.randrange(1, 10)):
            self.new = {}
            self.new["current_x"] = ((random.randrange(0, Objects.background.game_width)) + Objects.background.game_width)
            self.new["current_y"] = (random.randrange(0, Objects.background.game_height))
            self.items.append(self.new)

class Background:
    """The Background class handles the texture, position and offset for the game background."""

    def __init__(self) -> None:
        """Creates the background object and sets the initial position and offset."""
        self.background = pygame.image.load('assets/background/background.png').convert()
        self.game_width = pygame.display.get_surface().get_width()
        self.game_height = pygame.display.get_surface().get_height()
        self.background_x = 0
        self.background_rel_x = (self.background_x % self.background.get_rect().width)

class Font:
    """The Font class handles the font types for the game."""

    def __init__(self) -> None:
        """Create the font object."""
        self.font = pygame.font.SysFont('Arial', 30)
        self.score = self.font.render(f'Score: {0}', False, (0, 0, 0))
        self.score_width = self.score.get_rect().width
        self.score_height = self.score.get_rect().height
