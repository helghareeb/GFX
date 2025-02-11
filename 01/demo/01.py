import pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Simple Graphics")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (250, 250), 50)
    pygame.display.flip()

pygame.quit()