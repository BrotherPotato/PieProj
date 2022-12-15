import pygame

WINDOW_HEIGHT = 840
WINDOW_WIDTH = 800
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT

clock = pygame.time.Clock()
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)

def play_game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        clock.tick(30)

play_game()