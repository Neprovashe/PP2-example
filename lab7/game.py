import pygame
import sys
import time
import math

pygame.init()
size = (1000,1000)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mickey mouse")
clock = pygame.time.Clock()


clocks = pygame.image.load("base_micky.jpg").convert_alpha()
minute = pygame.image.load("minute.png").convert_alpha()
second = pygame.image.load("second.png").convert_alpha()

center = (size[0]//2, size[1]//2)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    t = time.localtime()
    seconds = t.tm_sec
    minutes = t.tm_min

    sec_angle = -(seconds / 60.0) * 360.0
    min_angle = -(minutes / 60.0) * 360.0

    minute_hand = pygame.transform.rotate(minute, min_angle)
    minute_rect = minute_hand.get_rect(center = center)

    second_hand = pygame.transform.rotate(second, sec_angle)
    second_rect = second_hand.get_rect(center = center)

    screen.fill((255,255,255))
    face_rect = clocks.get_rect(center = center)
    screen.blit(clocks, face_rect)
    screen.blit(minute_hand, minute_rect)
    screen.blit(second_hand, second_rect)

    pygame.display.flip()
    clock.tick(2)

pygame.quit()
sys.exit()
