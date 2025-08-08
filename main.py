import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True
dt = 0

paddle_score = 0
paddle_score2 = 0

font = pygame.font.SysFont("Arial", 20)

# Player 1 Paddle Position and Size
paddle_pos = pygame.Vector2(0, screen.get_height() / 2)
paddle_size = pygame.Vector2(10, 90)

# Player 2 Paddle Position and Size
paddle_pos2 = pygame.Vector2(screen.get_width() - 10, screen.get_height() / 2)
paddle_size2 = pygame.Vector2(10, 90)

# Ball Position and Radius
ball_pos_x = screen.get_width() / 2
ball_pos_y = screen.get_height() / 2
ball_radius = 15

# Ball Velocity
ball_vel_x = random.randint(400, 500)
ball_vel_y = random.randint(400, 500)

# Main Loop
while running:
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

  # Players Movement
  keys = pygame.key.get_pressed()
  if keys[pygame.K_w]:
      paddle_pos.y -= 660 * dt
  if keys[pygame.K_s]:
      paddle_pos.y += 660 * dt

  if keys[pygame.K_UP]:
    paddle_pos2.y -= 660 * dt
  if keys[pygame.K_DOWN]:
    paddle_pos2.y += 660 * dt

  # Filling Screen with black
  screen.fill("#1f1f1f")
  # Score Text
  text_surface = font.render(f"Player 1 Score: {paddle_score}", True, "white")
  text_surface2 = font.render(f"Player 2 Score: {paddle_score2}", True, "white")

  # Intilizing Paddles
  paddle1 = pygame.Rect(paddle_pos, paddle_size)
  paddle2 = pygame.Rect(paddle_pos2, paddle_size2)

  # Fixing Offscreen Paddle Problem
  paddle_pos.y = max(0, min(screen.get_height() - paddle_size.y, paddle_pos.y))
  paddle_pos2.y = max(0, min(screen.get_height() - paddle_size2.y, paddle_pos2.y))

  # Intilizing Ball
  ball = pygame.Rect((ball_pos_x - ball_radius, ball_pos_y - ball_radius), (ball_radius * 2, ball_radius * 2))

  # Rendering Text
  screen.blit(text_surface, (0, 0))
  screen.blit(text_surface2, (screen.get_width() - 157, 0))

  # Drawing Paddles
  pygame.draw.rect(screen, "white", paddle1)
  pygame.draw.rect(screen, "white", paddle2)

  # Drawing the Ball
  pygame.draw.circle(screen, "white", (ball_pos_x, ball_pos_y), ball_radius)

  # Random Movement for the ball
  ball_pos_x += ball_vel_x * dt
  ball_pos_y += ball_vel_y * dt

  # Ball Screen limits
  if ball.top <= 0:
    ball_vel_y = abs(ball_vel_y)

  if ball.bottom >= screen.get_height():
    ball_vel_y = -abs(ball_vel_y)

  if ball.right >= screen.get_width():
    paddle_score += 1
    ball_pos_x = screen.get_width() / 2
    ball_pos_y = screen.get_height() / 2
    ball_vel_x = -abs(ball_vel_x)
    ball_vel_y = random.choice([0, 200])

  if ball.left <= 0:
    paddle_score2 += 1
    ball_pos_x = screen.get_width() / 2
    ball_pos_y = screen.get_height() / 2
    ball_vel_x = abs(ball_vel_x)
    ball_vel_y = random.choice([-200, 200])

  # Colliding with Paddles
  if ball.colliderect(paddle1):
    ball_pos_x = paddle1.right + ball_radius
    ball_vel_x = abs(ball_vel_x)
    offset = (ball_pos_y - paddle1.y) / (paddle1.height / 2)
    ball_vel_y = offset * 100

  if ball.colliderect(paddle2):
    ball_pos_x = paddle2.left - ball_radius
    ball_vel_x = -abs(ball_vel_x)
    offset = (ball_pos_y - paddle2.y) / (paddle2.height / 2)
    ball_vel_y = offset * 300

  # Changing Window Title
  pygame.display.set_caption("Ping Pong Game (Full of Issues)")

  # Rendering Game
  pygame.display.flip()
  dt = clock.tick(60) / 1000

pygame.quit()