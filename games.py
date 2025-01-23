import pygame
import random
import sys

# Initialize Pygame
pygame.init()

def snake_game():
    """Run the Snake Game."""
    # Screen dimensions
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)

    # Game variables
    clock = pygame.time.Clock()
    snake_pos = [100, 50]  # Initial position
    snake_body = [[100, 50], [90, 50], [80, 50]]  # Initial snake body
    direction = 'RIGHT'
    change_to = direction
    speed = 15
    score = 0

    # Food position
    food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
    food_spawn = True

    def show_score():
        font = pygame.font.SysFont('arial', 25)
        score_surface = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_surface, (10, 10))

    def game_over():
        font = pygame.font.SysFont('arial', 35)
        game_over_surface = font.render(f'Game Over! Score: {score}', True, RED)
        screen.blit(game_over_surface, (WIDTH // 2 - game_over_surface.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        return score

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # Update direction
        direction = change_to

        # Update snake position
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        food_spawn = True

        # Draw snake and food
        for block in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], 10, 10))
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Game over conditions
        if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
            return game_over()
        for block in snake_body[1:]:
            if snake_pos == block:
                return game_over()

        show_score()
        pygame.display.flip()
        clock.tick(speed)


def flappy_bird():
    """Run the Flappy Bird Game."""
    # Screen dimensions
    SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    # Colors
    WHITE = (255, 255, 255)
    BLUE = (135, 206, 250)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # Bird properties
    bird_x, bird_y = 100, 300
    bird_width, bird_height = 30, 30
    bird_velocity = 0
    gravity = 0.5
    jump_strength = -10

    # Pipe properties
    pipe_width = 60
    pipe_gap = 150
    pipe_velocity = -4
    pipes = []

    # Game variables
    score = 0
    clock = pygame.time.Clock()
    FPS = 60

    def create_pipe():
        pipe_height = random.randint(100, SCREEN_HEIGHT - pipe_gap - 100)
        top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, pipe_height)
        bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - pipe_height - pipe_gap)
        return top_pipe, bottom_pipe

    def check_collision(bird_rect, pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                return True
        if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
            return True
        return False

    def display_score():
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

    # Initialize pipes
    pipes.extend(create_pipe())

    running = True
    while running:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump_strength

        # Bird movement
        bird_velocity += gravity
        bird_y += bird_velocity
        bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)

        # Move pipes
        for pipe in pipes:
            pipe.x += pipe_velocity

        # Remove pipes out of screen
        pipes = [pipe for pipe in pipes if pipe.right > 0]

        # Add new pipes
        if len(pipes) < 4 and (not pipes or pipes[-1].x < SCREEN_WIDTH // 2):
            pipes.extend(create_pipe())

        # Draw bird
        pygame.draw.rect(screen, RED, bird_rect)

        # Draw pipes
        for pipe in pipes:
            pygame.draw.rect(screen, GREEN, pipe)

        # Collision check
        if check_collision(bird_rect, pipes):
            return score

        # Update score
        score += sum(1 for pipe in pipes if pipe.right < bird_x and not hasattr(pipe, "scored") and setattr(pipe, "scored", True))

        # Display score
        display_score()
        pygame.display.flip()
        clock.tick(FPS)

    return score











# ============================================================================================



import pygame
import random
import sys

# Initialize Pygame
pygame.init()

def snake_game():
    """Run the Snake Game."""
    # Screen dimensions
    WIDTH, HEIGHT = 600, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)

    # Game variables
    clock = pygame.time.Clock()
    snake_pos = [100, 50]  # Initial position
    snake_body = [[100, 50], [90, 50], [80, 50]]  # Initial snake body
    direction = 'RIGHT'
    change_to = direction
    speed = 15
    score = 0

    # Food position
    food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
    food_spawn = True

    def show_score():
        font = pygame.font.SysFont('arial', 25)
        score_surface = font.render(f'Score: {score}', True, BLACK)
        screen.blit(score_surface, (10, 10))

    def game_over():
        font = pygame.font.SysFont('arial', 35)
        game_over_surface = font.render(f'Game Over! Score: {score}', True, RED)
        screen.blit(game_over_surface, (WIDTH // 2 - game_over_surface.get_width() // 2, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.delay(3000)
        return score

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        # Update direction
        direction = change_to

        # Update snake position
        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        # Snake body growing
        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 10
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
        food_spawn = True

        # Draw snake and food
        for block in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], 10, 10))
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        # Game over conditions
        if snake_pos[0] < 0 or snake_pos[0] >= WIDTH or snake_pos[1] < 0 or snake_pos[1] >= HEIGHT:
            return game_over()
        for block in snake_body[1:]:
            if snake_pos == block:
                return game_over()

        show_score()
        pygame.display.flip()
        clock.tick(speed)
    return score if isinstance(score, int) else 0


# def flappy_bird():
#     """Run the Flappy Bird Game."""
#     # Screen dimensions
#     SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
#     screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#     pygame.display.set_caption("Flappy Bird")

#     # Colors
#     BLUE = (135, 206, 250)
#     GREEN = (0, 255, 0)
#     RED = (255, 0, 0)
#     BLACK = (0, 0, 0)

#     # Bird properties
#     bird_x, bird_y = 100, 300
#     bird_width, bird_height = 30, 30
#     bird_velocity = 0
#     gravity = 0.5
#     jump_strength = -10

#     # Pipe properties
#     pipe_width = 60
#     pipe_gap = 150
#     pipe_velocity = -4
#     pipes = []

#     # Game variables
#     score = 0
#     clock = pygame.time.Clock()
#     FPS = 60

#     def create_pipe():
#         pipe_height = random.randint(100, SCREEN_HEIGHT - pipe_gap - 100)
#         top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, pipe_height)
#         bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - pipe_height - pipe_gap)
#         return top_pipe, bottom_pipe

#     def check_collision(bird_rect, pipes):
#         for pipe in pipes:
#             if bird_rect.colliderect(pipe):
#                 return True
#         if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
#             return True
#         return False

#     def display_score():
#         font = pygame.font.Font(None, 36)
#         score_text = font.render(f"Score: {score}", True, BLACK)
#         screen.blit(score_text, (10, 10))

#     # Initialize pipes
#     pipes.extend(create_pipe())

#     running = True
#     while running:
#         screen.fill(BLUE)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     bird_velocity = jump_strength

#         # Bird movement
#         bird_velocity += gravity
#         bird_y += bird_velocity
#         bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)

#         # Move pipes
#         for pipe in pipes:
#             pipe.x += pipe_velocity

#         # Remove pipes out of screen
#         pipes = [pipe for pipe in pipes if pipe.right > 0]

#         # Add new pipes
#         if len(pipes) < 2 or (pipes[-1].x < SCREEN_WIDTH // 2):
#             pipes.extend(create_pipe())

#         # Draw bird
#         pygame.draw.rect(screen, RED, bird_rect)

#         # Draw pipes
#         for pipe in pipes:
#             pygame.draw.rect(screen, GREEN, pipe)

#         # Collision check
#         if check_collision(bird_rect, pipes):
#             return score

#         # Update score
#         for pipe in pipes:
#             if pipe.right < bird_x and not getattr(pipe, "scored", False):
#                 setattr(pipe, "scored", True)
#                 score += 1

#         # Display score
#         display_score()
#         pygame.display.flip()
#         clock.tick(FPS)

#     return score if isinstance(score, int) else 0


def flappy_bird():
    """Run the Flappy Bird Game."""
    # Screen dimensions
    SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flappy Bird")

    # Colors
    BLUE = (135, 206, 250)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # Bird properties
    bird_x, bird_y = 100, 300
    bird_width, bird_height = 30, 30
    bird_velocity = 0
    gravity = 0.5
    jump_strength = -10

    # Pipe properties
    pipe_width = 60
    pipe_gap = 150
    pipe_velocity = -4
    pipes = []

    # Game variables
    score = 0
    clock = pygame.time.Clock()
    FPS = 60

    def create_pipe():
        pipe_height = random.randint(100, SCREEN_HEIGHT - pipe_gap - 100)
        top_pipe = pygame.Rect(SCREEN_WIDTH, 0, pipe_width, pipe_height)
        bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + pipe_gap, pipe_width, SCREEN_HEIGHT - pipe_height - pipe_gap)
        return top_pipe, bottom_pipe

    def check_collision(bird_rect, pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                return True
        if bird_rect.top <= 0 or bird_rect.bottom >= SCREEN_HEIGHT:
            return True
        return False

    def display_score():
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))

    # Initialize pipes
    pipes.extend(create_pipe())

    # This will track which pipes the bird has passed to update the score correctly.
    passed_pipes = []

    running = True
    while running:
        screen.fill(BLUE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump_strength

        # Bird movement
        bird_velocity += gravity
        bird_y += bird_velocity
        bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)

        # Move pipes
        for pipe in pipes:
            pipe.x += pipe_velocity

        # Remove pipes out of screen
        pipes = [pipe for pipe in pipes if pipe.right > 0]

        # Add new pipes if necessary
        if len(pipes) < 2 or pipes[-1].x < SCREEN_WIDTH // 2:
            pipes.extend(create_pipe())

        # Check if the bird passes a pipe (update score)
        for pipe in pipes:
            if pipe.right < bird_x and pipe not in passed_pipes:
                passed_pipes.append(pipe)
                score += 1

        # Draw bird
        pygame.draw.rect(screen, RED, bird_rect)

        # Draw pipes
        for pipe in pipes:
            pygame.draw.rect(screen, GREEN, pipe)

        # Collision check
        if check_collision(bird_rect, pipes):
            return score

        # Display score
        display_score()
        pygame.display.flip()
        clock.tick(FPS)

    return score



def falling_blocks():
    """Run the Falling Blocks Game."""
    # Set the width and height of the window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set the window title
    pygame.display.set_caption("Dodge the Falling Blocks!")

    # Colors
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

    # Player settings
    player_width = 50
    player_height = 50
    player_x = screen_width // 2 - player_width // 2
    player_y = screen_height - player_height - 10
    player_speed = 5

    # Block settings
    block_width = 50
    block_height = 50
    block_speed = 5
    block_frequency = 30
    blocks = []

    # Set up font for text display
    font = pygame.font.SysFont(None, 30)

    # Clock to control the frame rate
    clock = pygame.time.Clock()

    def draw_player(x, y):
        pygame.draw.rect(screen, BLUE, [x, y, player_width, player_height])

    def draw_block(x, y):
        pygame.draw.rect(screen, RED, [x, y, block_width, block_height])

    def display_score(score):
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])

    def check_collision(player_x, player_y, block_x, block_y):
        return (
            player_x < block_x + block_width and
            player_x + player_width > block_x and
            player_y < block_y + block_height and
            player_y + player_height > block_y
        )

    running = True
    score = 0

    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed

        # Add new blocks
        if random.randint(1, block_frequency) == 1:
            block_x = random.randint(0, screen_width - block_width)
            blocks.append([block_x, 0])

        # Move and remove blocks
        for block in blocks[:]:
            block[1] += block_speed
            if block[1] > screen_height:
                blocks.remove(block)
                score += 1

            # Check for collision
            if check_collision(player_x, player_y, block[0], block[1]):
                running = False

            draw_block(block[0], block[1])

        # Draw player
        draw_player(player_x, player_y)

        # Display score
        display_score(score)

        # Update display
        pygame.display.flip()
        clock.tick(60)
    # Game Over screen
    screen.fill(BLACK)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, RED)
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

    # Ensure an integer score is always returned
    return score if isinstance(score, int) else 0