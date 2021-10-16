import pygame

def Render(screen: object, player: object, objects: object) -> None:
    """This method will render all the assets to the pygame window."""
    screen.blit(objects.background.background, (objects.background.background_rel_x - objects.background.background.get_rect().width, 0))
    
    if objects.background.background_rel_x < objects.background.game_width:
            screen.blit(objects.background.background, (objects.background.background_rel_x, 0))

    for object in objects.objects.values():
        for item in object.items:
            screen.blit(object.image, [item["current_x"], item["current_y"]])

    screen.blit(player.image, [(player.x + player.x_offset), (player.y + player.y_offset)])
    screen.blit(objects.font.score, ((objects.background.game_width - objects.font.score_width), (objects.background.game_height - objects.font.score_height)))
