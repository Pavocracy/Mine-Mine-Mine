import sys

# The same objects are passed multiple times here, and the same dictonaries iterated through multiple times. This IS bad.

def CheckItems(player: object, objects: object) -> None:
    """Checks attributes of items. Create new items if needed. Else remove if off screen or if there is a collision."""
    off_screen = 0

    for item in objects.scrolling_items:
        if item["current_x"] > objects.game_width:
            off_screen += 1

        if player.CheckCollision(objects.items[item["name"]]["item_mask"], item["current_x"], item["current_y"]):
            objects.scrolling_items.remove(item)
            objects.items[item["name"]]["eaten"] += 1

        if objects.CheckOceanOverlap(objects.items[item["name"]]["item_mask"], item["current_x"], item["current_y"]):
            item["current_y"] -= 0.1

        if item["current_x"] <= (0 - objects.items[item["name"]]["item_image"].get_rect().width) \
        or item["current_y"] <= (0 - objects.items[item["name"]]["item_image"].get_rect().height):
            objects.scrolling_items.remove(item)

    if off_screen == 0:
        objects.Create_Items()

    for background in objects.scrolling_backgrounds:
        if background["current_x"] < -objects.game_width:
            objects.scrolling_backgrounds.remove(background)

    if len(objects.scrolling_backgrounds) < 2:
        objects.Create_Backgrounds()

def MoveItems(player: object, objects: object) -> None:
    """Updates values for all position attributes on the player and objects."""
    player.Move()
    for item in objects.scrolling_items:
        item["current_x"] -= 1

def CheckLoss(objects: object) -> None:
    """Checks to see if the game over condition is met."""
    eaten = 0
    for item in objects.items.keys():
        if item.startswith("ciggy"):
            eaten += objects.items[item]["eaten"]
    
    if eaten >= 3:
        # TODO: Add a loss screen instead of just exit.
        sys.exit()

def ScrollBackground(objects: object) -> None:
    """Updates the background attributes to infinitely scroll."""
    for background in objects.scrolling_backgrounds:
        background["current_x"] -= 1

def SetScore(objects: object) -> None:
    """Updates the score count and the render values."""
    eaten = 0
    for item in objects.items.keys():
        if item.startswith("chip"):
            eaten += objects.items[item]["eaten"]

    objects.score_font = objects.font.render(f'Score: {eaten}', False, (0, 0, 0))
    objects.score_width = objects.score_font.get_rect().width
    objects.score_height = objects.score_font.get_rect().height
