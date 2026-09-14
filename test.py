from baston import *
import pygame
import os
import sys
import random

SONG_END = pygame.USEREVENT + 1

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

starting_lives = 3
dragon_king_printed = 0

def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def load_and_scale(filename, size=None, transparency=None):
    if transparency is not None:
        unscaled = pygame.image.load(resource_path(f"{filename}.png")).convert()
    else:
        unscaled = pygame.image.load(resource_path(f"{filename}.png")).convert_alpha()
    if size is not None:
        return pygame.transform.scale(unscaled, size)
    else:
        return unscaled

dragon_king_left = load_and_scale("dragon-king", None, True)
dragon_king_right = pygame.transform.flip(dragon_king_left, True, False)
bg = load_and_scale("bg", (1280, 720))
fist_right = load_and_scale("fist", None, True)
fist_left = pygame.transform.flip(fist_right, True, False)
ball = load_and_scale("ball", None, True)



song0 = "default1.wav"
song1 = "default2.wav"
playlist = [song0, song1]
pygame.mixer.music.set_endevent(SONG_END)
song_index = random.randint(0, 1)
pygame.mixer.music.load(playlist[song_index])
pygame.mixer.music.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SONG_END:
            song_index = (song_index + 1) % len(playlist)
            pygame.mixer.music.load(playlist[song_index])
            pygame.mixer.music.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        pass
    if keys[pygame.K_a]:
        pass
    if keys[pygame.K_s]:
        pass
    if keys[pygame.K_d]:
        pass
    if keys[pygame.K_q]:
        pass
    if keys[pygame.K_e]:
        pass
    if keys[pygame.K_i]:
        pass
    if keys[pygame.K_j]:
        pass
    if keys[pygame.K_k]:
        pass
    if keys[pygame.K_l]:
        pass
    if keys[pygame.K_u]:
        pass
    if keys[pygame.K_o]:
        pass

    screen.blit(bg, (0, 0))
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


    pygame.display.flip()

pygame.quit()
