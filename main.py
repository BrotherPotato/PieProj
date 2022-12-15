import pygame
pygame.init()

WINDOW_HEIGHT = 840
WINDOW_WIDTH = 800
WINDOW_DIMENSIONS = WINDOW_WIDTH, WINDOW_HEIGHT

pygame.init()
pygame.display.set_caption("Game")


clock = pygame.time.Clock()
#create an object to help track time. Times in pygame are represented in 
# milliseconds (1/1000 seconds). Most platforms have a limited time resolution of around 10 milliseconds, 
# so you should not expect to be able to get more accurate timing than that.
screen = pygame.display.set_mode(WINDOW_DIMENSIONS)

#event. get() handles the internal events an retrieves a list of external events 
# (the events are removed from the internal event queue). If you press the close button of the window, 
# than the causes the QUIT event and you'll get the event by for event in pygame

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

    pygame.display.update()



    #Tick is just a measure of time in PyGame. clock. tick(40) means that for every second at most 40 frames should pass.
    clock.tick(30)
pygame.quit()
