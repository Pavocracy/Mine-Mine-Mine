import pygame
import Player
import Objects
import Controls
import Logic
import Render

if __name__ == '__main__':
    # Initialize Game Items
    pygame.init()
    screen = pygame.display.set_mode((640, 480)) # Window Resolution
    clock = pygame.time.Clock()
    player = Player.Player()
    objects = Objects.Objects()

    while True:
        # Process Inputs
        Controls.KeyPressed(player)

        # Update Game State
        Logic.CheckItems(player, objects)
        Logic.MoveItems(player, objects)
        Logic.CheckLoss(objects)
        Logic.SetScore(objects)
        Logic.ScrollBackground(objects)
        
        # Render Game
        Render.Render(screen, player, objects)
        pygame.display.update()
        clock.tick(60) # Frames Per Second
