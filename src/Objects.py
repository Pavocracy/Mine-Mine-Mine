import pygame
import random
import os
import copy
from Paths import resource_path

class Objects:
    """The Objects class contains object dictionarys of instantiated game assets."""

    def __init__(self, game_width: float, game_height: float) -> None:
        """Creates an object for each item needed for the game."""
        self.game_width = game_width
        self.game_height = game_height

        self.backgrounds = {}
        self.scrolling_backgrounds = []
        for filename in os.listdir(resource_path("assets/Backgrounds")):
            name = filename.split(".")[0]
            self.backgrounds[name] = self.Backgrounds(filename)
        self.Create_Backgrounds()

        self.items = {}
        self.scrolling_items = []
        for filename in os.listdir(resource_path("assets/Items")):
            name = filename.split(".")[0]
            self.items[name] = self.Items(filename)
        self.Create_Items()

        self.font = self.Font()

    def Backgrounds(self, filename: str) -> dict:
        """Creates the background object and sets the initial position and offset."""
        background = {}
        background_image = pygame.image.load(resource_path(f'assets/Backgrounds/{filename}')).convert()
        background_image = pygame.transform.scale(background_image, (self.game_width, self.game_height))
        background["background_image"] = background_image
        background_ocean = copy.copy(background_image)
        background_ocean.set_colorkey((10, 188, 255))
        background["background_ocean"] = background_ocean
        background_ocean_mask = pygame.mask.from_surface(background_ocean)
        background_ocean_mask.invert()
        background["background_ocean_mask"] = background_ocean_mask
        return background

    def Create_Backgrounds(self) -> None:
        """Picks a random background to use as the next background to scroll."""
        backgrounds_list = [background for background in self.backgrounds]
        backgrounds_count = len(backgrounds_list)
        if len(self.scrolling_backgrounds) == 1:
            new = {}
            new["name"] = backgrounds_list[random.randrange(0, backgrounds_count)]
            new["current_x"] = self.game_width
            self.scrolling_backgrounds.append(new)
        if len(self.scrolling_backgrounds) == 0:
            new = {}
            new["name"] = backgrounds_list[random.randrange(0, backgrounds_count)]
            new["current_x"] = 0
            self.scrolling_backgrounds.append(new)

    def CheckOceanOverlap(self, object_mask: object, object_x: int, object_y: int) -> bool:
        """Returns Bool of item position overlapping the ocean part of the background."""
        for background in self.scrolling_backgrounds:
            offset = (background["current_x"] - object_x, 0 - object_y)
            if object_mask.overlap(self.backgrounds[background["name"]]["background_ocean_mask"], offset):
                return True
        return False

    def Items(self, filename: str) -> dict:
        """Sets the attributes for the object and calls the Create method for that object."""
        item = {}
        item_scale_w = self.game_width / 50
        item_scale_h = self.game_width / 50
        item_image = pygame.image.load(resource_path(f'assets/Items/{filename}')).convert()
        item_image = pygame.transform.scale(item_image, (item_scale_w, item_scale_h))
        item_image.set_colorkey((0, 255, 0))
        item["item_image"] = item_image
        item["item_mask"] = pygame.mask.from_surface(item_image)
        item["eaten"] = 0
        return item

    def Create_Items(self) -> list:
        items_list = [item for item in self.items]
        items_count = len(items_list)
        item_limit = self.game_width / 50
        for i in range(random.randrange(1, int(item_limit))):
            new = {}
            new["name"] = items_list[random.randrange(0, items_count)]
            new["current_x"] = random.randrange(0, int(self.game_width)) + self.game_width
            new["current_y"] = random.randrange(0, int(self.game_height))
            self.scrolling_items.append(new)

    def Font(self) -> pygame.font.Font:
        """Create the font object."""
        font = pygame.font.Font(resource_path('assets/Fonts/arial.ttf'), 30)
        self.score = 0
        self.score_font = font.render(f'Score: {self.score}', False, (0, 0, 0))
        self.score_width = self.score_font.get_rect().width
        self.score_height = self.score_font.get_rect().height
        return font
