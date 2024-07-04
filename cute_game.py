import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Star Falling Catch")

# Clock to control frame rate
clock = pygame.time.Clock()

# Font for text
font = pygame.font.Font(None, 36)

# Class for the star
class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed_y = random.randrange(1, 5)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.y > SCREEN_HEIGHT:
            self.rect.y = random.randrange(-100, -40)
            self.rect.x = random.randrange(SCREEN_WIDTH - self.rect.width)

# Sprite groups
all_sprites = pygame.sprite.Group()
stars = pygame.sprite.Group()

# Create stars
for i in range(10):
    star = Star()
    all_sprites.add(star)
    stars.add(star)

# Game variables
score = 0
countdown_timer = 30  # seconds
game_over = False
game_start = False

# Function to start the game
def start_game():
    global game_start, game_over, score, countdown_timer
    game_start = True
    game_over = False
    score = 0
    countdown_timer = 30
    all_sprites.empty()
    stars.empty()
    for i in range(10):
        star = Star()
        all_sprites.add(star)
        stars.add(star)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_start and start_button_rect.collidepoint(event.pos):
                start_game()
            elif game_start and not game_over:
                # Check if the mouse click hits any star
                pos = pygame.mouse.get_pos()
                hits = pygame.sprite.spritecollide(star, stars, True)
                for hit in hits:
                    score += 1
                    print(f"Score: {score}")

    # Update
    if game_start and not game_over:
        all_sprites.update()
        countdown_timer -= 1 / 60  # decrease by 1 second per second

        if countdown_timer <= 0:
            game_over = True

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Draw UI
    if not game_start:
        # Draw start button
        start_button_rect = pygame.draw.rect(screen, WHITE, (300, 250, 200, 50))
        start_text = font.render("Start Game", True, BLACK)
        screen.blit(start_text, (330, 260))
    else:
        # Draw countdown timer
        countdown_text = font.render(f"Time left: {int(countdown_timer)}", True, WHITE)
        screen.blit(countdown_text, (10, 10))

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (SCREEN_WIDTH - 150, 10))

        # Draw game over message
        if game_over:
            game_over_text = font.render("Game Over", True, WHITE)
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 80, SCREEN_HEIGHT // 2))

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
