import pygame
pygame.init()

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT

pygame.init()
pygame.display.set_caption("Game")

#Font for the game
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('GAMING', True, (0, 255, 0), (0, 0, 128))
textRect = text.get_rect()
# set the center of the rectangular object.
textRect.center = ((textRect.left+67),(textRect.top+16))

clock = pygame.time.Clock()
#create an object to help track time. Times in pygame are represented in 
# milliseconds (1/1000 seconds). Most platforms have a limited time resolution of around 10 milliseconds, 
# so you should not expect to be able to get more accurate timing than that.
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)

#event. get() handles the internal events an retrieves a list of external events 
# (the events are removed from the internal event queue). If you press the close button of the window, 
# than the causes the QUIT event and you'll get the event by for event in pygame

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white  
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.draw.rect(screen,(20,135,100),(400, 400, 20, 20), 75)
    screen.blit(text, textRect)

    pygame.display.update()

    

    #Tick is just a measure of time in PyGame. clock. tick(40) means that for every second at most 40 frames should pass. 
    # This is useful for games, because you don't want the game to run faster on a faster computer.
    # If you don't call clock. tick() at all, the program will run as fast as possible.
    # FPS = 1000 / 17 = 58.82 frames per second
    clock.tick(17)
pygame.quit()
