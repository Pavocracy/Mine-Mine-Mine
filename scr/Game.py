import pygame
import Player
import Objects
import Controls
import Logic
import Render

if __name__ == '__main__':
    # Initialize Game Items
    pygame.init()
    game_height = pygame.display.Info().current_h * 0.75
    game_width = game_height * 1.777
    game_FPS = 60
    screen = pygame.display.set_mode((game_width, game_height))
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
        clock.tick(game_FPS)
