import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


radius = 25
x, y = WIDTH // 2, HEIGHT // 2
speed = 20

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed

    
    if x - radius > WIDTH:
        x = -radius
    elif x + radius < 0:
        x = WIDTH + radius
    if y - radius > HEIGHT:
        y = -radius
    elif y + radius < 0:
        y = HEIGHT + radius


    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.flip()


    clock.tick(30)
