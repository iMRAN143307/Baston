from baston import *
import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

starting_lives = 3
dragon_king_printed = 0

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
    dragon_king = create_character([["idle", circle(50, 0, 30)], ["idle", rectangle(50, 30, 10, 50)], ["move1", circle(50, 0, 30)], ["move1", rectangle(70, 15, 50, 10)]])
    hurtboxes_active.extend(apply_hurtboxes(dragon_king[0]["move1"], (640, 360), 1))
    for box in hurtboxes_active:
        pixel = pygame.Rect(box[0][0], box[0][1], 1, 1)
        pygame.draw.rect(screen, "blue", pixel)

    zones_active = []
    zones_active.extend(triangle(100, 100, 100, "down"))
    for box in zones_active:
        pixel = pygame.Rect(box[0], box[1], 1, 1)
        pygame.draw.rect(screen, "green", pixel)

    pygame.display.flip()

pygame.quit()
