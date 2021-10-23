import pygame

def Render(screen: object, player: object, objects: object) -> None:
    """This method will render all the assets to the pygame window."""
    for background in objects.scrolling_backgrounds:
        screen.blit(objects.backgrounds[(background["name"])].image, (background["current_x"], 0))

    for object in objects.items.values():
        for item in object.item:
            screen.blit(object.image, [item["current_x"], item["current_y"]])

    screen.blit(player.image, [(player.x + player.x_offset), (player.y + player.y_offset)])
    screen.blit(objects.font.score, ((pygame.display.get_surface().get_width() - objects.font.score_width), (pygame.display.get_surface().get_height() - objects.font.score_height)))
