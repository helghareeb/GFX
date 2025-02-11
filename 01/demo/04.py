import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Set the title of the window
pygame.display.set_caption("Computer Graphics Basics with Pygame")

# Define colors using RGB format
WHITE = (255, 255, 255)  # Background color
RED = (255, 0, 0)  # Rectangle color
BLUE = (0, 0, 255)  # Circle color
GREEN = (0, 255, 0)  # Line color
BLACK = (0, 0, 0)  # Score text color

# Font for displaying score
font = pygame.font.Font(None, 36)

# Circle properties
circle_x, circle_y = WIDTH // 2, HEIGHT // 2  # Initial position of the circle
circle_radius = 30  # Radius of the circle
circle_dx, circle_dy = 4, 4  # Speed and direction of movement

# Rectangle properties
rect_x, rect_y = 100, 500  # Initial position of the rectangle
rect_width, rect_height = 100, 50  # Dimensions of the rectangle
rect_speed = 5  # Speed of movement for the rectangle

# Score
score = 0

# Game loop to keep the window open and handle interactions
running = True
while running:
    # Fill the screen with white to clear the previous frame
    screen.fill(WHITE)  
    
    # Event handling loop to check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks the close button, exit the loop
            running = False
    
    # Capture the state of the keyboard
    keys = pygame.key.get_pressed()
    # Move rectangle based on arrow key presses
    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= rect_speed  # Move left
    if keys[pygame.K_RIGHT] and rect_x < WIDTH - rect_width:
        rect_x += rect_speed  # Move right
    if keys[pygame.K_UP] and rect_y > 0:
        rect_y -= rect_speed  # Move up
    if keys[pygame.K_DOWN] and rect_y < HEIGHT - rect_height:
        rect_y += rect_speed  # Move down
    
    # Move the circle (simulating a bouncing ball)
    circle_x += circle_dx
    circle_y += circle_dy
    
    # Bounce the circle off the edges of the screen
    if circle_x - circle_radius <= 0 or circle_x + circle_radius >= WIDTH:
        circle_dx *= -1  # Reverse horizontal direction
    if circle_y - circle_radius <= 0 or circle_y + circle_radius >= HEIGHT:
        circle_dy *= -1  # Reverse vertical direction
    
    # Check for collision between the ball and the rectangle
    if (rect_x < circle_x < rect_x + rect_width) and (rect_y < circle_y + circle_radius < rect_y + rect_height):
        circle_dy *= -1  # Reverse the ball's vertical direction
        score += 1  # Increase score when collision happens
    
    # Draw a red rectangle at the updated position
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))
    # Draw a blue circle at the updated position
    pygame.draw.circle(screen, BLUE, (circle_x, circle_y), circle_radius)
    # Draw a green horizontal line across the screen for reference
    pygame.draw.line(screen, GREEN, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)
    
    # Render score text
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))  # Display score at top-left corner
    
    # Refresh the screen with the updated drawings
    pygame.display.flip()
    # Introduce a small delay to control the frame rate
    pygame.time.delay(30)  

# Quit pygame when the loop ends
pygame.quit()
sys.exit()
