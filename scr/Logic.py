import pygame
import sys

def CheckItems(player: object, objects: object) -> None:
    """Checks attributes of items. Create new items if needed. Else remove if off screen or if there is a collision."""
    for object in objects.items.values():
        for item in object.item:
            off_screen = 0
            if item["current_x"] > pygame.display.get_surface().get_width():
                off_screen += 1
            if player.CheckCollision(object.mask, item["current_x"], item["current_y"]):
                object.item.remove(item)
                object.eaten += 1
            if item["current_x"] <= (0 - object.image.get_rect().width):
                object.item.remove(item)
        if off_screen == 0:
            object.Create()

    for background in objects.scrolling_backgrounds:
        if background["current_x"] < -pygame.display.get_surface().get_width():
            objects.scrolling_backgrounds.remove(background)

    if len(objects.scrolling_backgrounds) < 2:
        objects.backgrounds["background1"].Create()

def MoveItems(player: object, objects: object) -> None:
    """Updates values for all position attributes on the player and objects."""
    player.Move()
    for object in objects.items.values():
        for item in object.item:
            item["current_x"] -= 1

def CheckLoss(objects: object) -> None:
    """Checks to see if the game over condition is met."""
    if objects.items["ciggy"].eaten >= 3:
        sys.exit()

def ScrollBackground(objects: object) -> None:
    """Updates the background attributes to infinitely scroll."""
    for background in objects.scrolling_backgrounds:
        background["current_x"] -= 1

def SetScore(objects: object) -> None:
    """Updates the score count and the render values."""
    objects.font.score = objects.font.font.render(f'Score: {objects.items["chip"].eaten}', False, (0, 0, 0))
    objects.font.score_width = objects.font.score.get_rect().width
    objects.font.score_height = objects.font.score.get_rect().height
