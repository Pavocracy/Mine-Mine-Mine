import pygame
import random
import os

class Objects:
    """The Objects class contains an objects dictionary of instantiated classes of game items."""

    def __init__(self) -> None:
        """Creates an object for each item needed for the game."""
        Objects.backgrounds = {} # Dictionary will contain the class objects.
        Objects.scrolling_backgrounds = [] # List to keep track of 2 random backgrounds to render.
        for filename in os.listdir("Assets/Backgrounds"):
            name = filename.split(".")[0]
            Objects.backgrounds[name] = Backgrounds(filename)

        Objects.items = {} # Dictionary will contain the class objects.
        Objects.items_count = len(os.listdir("Assets/Items"))
        for filename in os.listdir("Assets/Items"):
            name = filename.split(".")[0]
            Objects.items[name] = Items(filename)

        Objects.font = Font()

class Items:
    """The Items class handles objects that require attributes for the game state."""

    def __init__(self, filename: str) -> None:
        """Sets the attributes for the object and calls the Create method for that object."""
        self.name = filename.split(".")[0]
        self.image = pygame.image.load(f'Assets/Items/{filename}').convert()
        self.image.set_colorkey((0, 255, 0))
        self.mask = pygame.mask.from_surface(self.image)
        self.eaten = 0
        self.item = [] # List of random n of x,y coordinate pairs to render the class object n times.
        self.Create()

    def Create(self) -> None:
        """Creates a random number of items with random position values and stores them in Objects.objects["name"].items."""
        for i in range(random.randrange(1, int(((pygame.display.get_surface().get_width() / 75) / Objects.items_count)))):
            self.new = {}
            self.new["current_x"] = ((random.randrange(0, pygame.display.get_surface().get_width())) + pygame.display.get_surface().get_width())
            self.new["current_y"] = (random.randrange(0, pygame.display.get_surface().get_height()))
            self.item.append(self.new)

class Backgrounds:
    """The Background class handles the texture, position and offset for the game background."""

    def __init__(self, filename: str) -> None:
        """Creates the background object and sets the initial position and offset."""
        self.name = filename.split(".")[0]
        self.image = pygame.image.load(f'Assets/Backgrounds/{filename}').convert()
        self.image = pygame.transform.scale(self.image, (pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height()))
        self.ocean = pygame.image.load(f'Assets/Backgrounds/{filename}').convert()
        self.ocean = pygame.transform.scale(self.image, (pygame.display.get_surface().get_width(), pygame.display.get_surface().get_height()))
        self.ocean.set_colorkey((10, 188, 255))
        self.ocean_mask = pygame.mask.from_surface(self.ocean)
        self.ocean_mask.invert()
        self.Create()

    def Create(self) -> None:
        """Picks a random background to use as the next background to scroll."""
        if len(Objects.scrolling_backgrounds) == 1:
            self.new = {} # Dictonary containing name,current_x keys to add to list of backgrounds to render.
            self.new["name"] = self.name
            self.new["current_x"] = pygame.display.get_surface().get_width()
            Objects.scrolling_backgrounds.append(self.new)
        if len(Objects.scrolling_backgrounds) == 0:
            self.new = {}
            self.new["name"] = self.name
            self.new["current_x"] = 0
            Objects.scrolling_backgrounds.append(self.new)

    def CheckOceanOverlap(self, mask: object, object_x: int, object_y: int) -> bool:
        """Returns True if the items position is overlapping the ocean part of the background."""
        for background in Objects.scrolling_backgrounds:
            offset = (background["current_x"] - object_x, 0 - object_y)
            collision = mask.overlap(Objects.backgrounds[background["name"]].ocean_mask, offset)
            if collision:
                return True

class Font:
    """The Font class handles the font types for the game."""

    def __init__(self) -> None:
        """Create the font object."""
        self.font = pygame.font.SysFont('Arial', 30)
        self.score = self.font.render(f'Score: {0}', False, (0, 0, 0))
        self.score_width = self.score.get_rect().width
        self.score_height = self.score.get_rect().height
