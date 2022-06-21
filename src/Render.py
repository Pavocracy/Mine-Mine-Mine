def Render(screen: object, player: object, objects: object) -> None:
    """This method will render all the assets to the pygame window."""
    for background in objects.scrolling_backgrounds:
        screen.blit(objects.backgrounds[(background["name"])]["background_image"], (background["current_x"], 0))

    for item in objects.scrolling_items:
        screen.blit(objects.items[item["name"]]["item_image"], (item["current_x"], item["current_y"]))

    screen.blit(player.image, [(player.x + player.x_offset), (player.y + player.y_offset)])

    screen.blit(objects.score_font, ((objects.game_width - objects.score_width), (objects.game_height - objects.score_height)))
