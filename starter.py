import pygame

# constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FRAMES_PER_SECOND = 60

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scavenger Haunt")
clock = pygame.time.Clock()
running = True
dt = 0
font = pygame.font.SysFont("Comic Sans MS", 36)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # clear the screen
    text = font.render("Hello, World!", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))

    pygame.display.flip()  # display your drawing to the screen
    dt = clock.tick(FRAMES_PER_SECOND) / 1000  # limits FPS to 60

pygame.quit()
