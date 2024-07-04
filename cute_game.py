import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Catch the Falling Stars')

# Load images
basket_img = pygame.image.load('basket.png')
star_img = pygame.image.load('star.png')

# Basket settings
basket_width = 64
basket_height = 64
basket_x = screen_width // 2 - basket_width // 2
basket_y = screen_height - basket_height - 10
basket_speed = 7

# Star settings
star_width = 32
star_height = 32
star_speed = 5
star_frequency = 25  # Lower is more frequent
stars = []

# Font settings
font = pygame.font.SysFont(None, 55)

# Score
score = 0

def display_score(score):
    text = font.render(f'Score: {score}', True, black)
    screen.blit(text, (10, 10))

def game_loop():
    global basket_x, score, stars
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < screen_width - basket_width:
            basket_x += basket_speed
        
        # Add new stars
        if random.randint(1, star_frequency) == 1:
            star_x = random.randint(0, screen_width - star_width)
            stars.append([star_x, 0])
        
        # Move stars
        for star in stars:
            star[1] += star_speed
        
        # Check for basket catching stars
        for star in stars[:]:
            if basket_y < star[1] + star_height and basket_x < star[0] + star_width and basket_x + basket_width > star[0]:
                stars.remove(star)
                score += 1
        
        # Remove stars that fall out of screen
        stars = [star for star in stars if star[1] < screen_height]

        # Clear screen
        screen.fill(white)

        # Draw basket
        screen.blit(basket_img, (basket_x, basket_y))
        
        # Draw stars
        for star in stars:
            screen.blit(star_img, star)
        
        # Display score
        display_score(score)
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
