from baston import *
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    hitboxes_active = []
    hitboxes_active.extend(circle(100, 100, 100))
    for box in hitboxes_active:
        pixel = pygame.Rect(box[0], box[1], 1, 1)
        pygame.draw.rect(screen, "red", pixel)

    hurtboxes_active = []
    hurtboxes_active.extend(rectangle(100, 100, 100, 100))
    for box in hurtboxes_active:
        pixel = pygame.Rect(box[0], box[1], 1, 1)
        pygame.draw.rect(screen, "blue", pixel)

    zones_active = []
    zones_active.extend(triangle(100, 100, 50))
    for box in zones_active:
        pixel = pygame.Rect(box[0], box[1], 1, 1)
        pygame.draw.rect(screen, "green", pixel)

    pygame.display.flip()

pygame.quit()
