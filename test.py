from baston import *
import pygame
import os
import sys
import random
import copy

SONG_END = pygame.USEREVENT + 1

pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

starting_lives = 3
p1coords = [360, 350]
p2coords = [820, 350]
p1accel = [0, 0]
p2accel = [0, 0]
stage = (256, 470, 1024, 570)
jump_buffer1 = 60
jump_buffer2 = 60

dragon_king1 = create_character([["idle", circle(65, 40, 23)], ["idle", rectangle(45, 30, 40, 80)], ["idle", triangle(65, 85, 35, "down")]])
dragon_king2 = copy.deepcopy(dragon_king1)
punch = [[hitbox1, hitbox2], knockback, knockback angle, 10, 10, 2] #knockback angle will be smash bros

def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def load_and_scale(filename, size=None, transparency=None):
    if transparency is not None:
        unscaled = pygame.image.load(resource_path(f"{filename}.png")).convert_alpha()
    else:
        unscaled = pygame.image.load(resource_path(f"{filename}.png")).convert()
    if size is not None:
        return pygame.transform.scale(unscaled, size)
    else:
        return unscaled

dragon_king_left = load_and_scale("dragon-king", (128, 128), True)
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
    if keys[pygame.K_w] and dragon_king1[2][0] == "aerial" and jump_buffer1 < 0:
        p1accel[1] = -60
        dragon_king1[2] = ("helpless", 0)
    elif keys[pygame.K_w] and dragon_king1[2][0] == "grounded":
        p1accel[1] = -55
        dragon_king1[2] = ("aerial", 0)
        jump_buffer1 = 7
    elif dragon_king1[2][0] == "aerial":
        jump_buffer1 -= 1
    if keys[pygame.K_a]:
        p1accel[0] -= 15
    if keys[pygame.K_s]:
        pass
    if keys[pygame.K_d]:
        p1accel[0] += 15
    if keys[pygame.K_q]:
        pass
    if keys[pygame.K_e]:
        pass
    if keys[pygame.K_i] and dragon_king2[2][0] == "aerial" and jump_buffer2 < 0:
        p2accel[1] = -60
        dragon_king2[2] = ("helpless", 0)
    elif keys[pygame.K_i] and dragon_king2[2][0] == "grounded":
        p2accel[1] = -55
        dragon_king2[2] = ("aerial", 0)
        jump_buffer2 = 7
    elif dragon_king2[2][0] == "aerial":
        jump_buffer2 -= 1
    if keys[pygame.K_j]:
        p2accel[0] -= 15
    if keys[pygame.K_k]:
        pass
    if keys[pygame.K_l]:
        p2accel[0] += 15
    if keys[pygame.K_u]:
        pass
    if keys[pygame.K_o]:
        pass

    p1coords = [p1coords[0] + p1accel[0], p1coords[1] + p1accel[1]]
    if p1accel[0] > 0:
        p1accel[0] -= max(abs(p1accel[0]//2), 1)
    elif p1accel[0] < 0:
        p1accel[0] += max(abs(p1accel[0]//2), 1)
    if p1accel[1] > 0:
        p1accel[1] -= 2
    elif p1accel[1] < 0:
        p1accel[1] += 2
    p1accel[0] = min(p1accel[0], 40)
    p1accel[0] = max(p1accel[0], -40)

    p2coords = [p2coords[0] + p2accel[0], p2coords[1] + p2accel[1]]
    if p2accel[0] > 0:
        p2accel[0] -= max(abs(p2accel[0]//2), 1)
    elif p2accel[0] < 0:
        p2accel[0] += max(abs(p2accel[0]//2), 1)
    if p2accel[1] > 0:
        p2accel[1] -= 2
    elif p2accel[1] < 0:
        p2accel[1] += 2
    p2accel[0] = min(p2accel[0], 40)
    p2accel[0] = max(p2accel[0], -40)

    p1accel[1] += 6
    p2accel[1] += 6

    hitboxes_active = []
    hitboxes_active.extend(circle(100, 100, 100))
    for box in hitboxes_active:
        pixel = pygame.Rect(box[0], box[1], 1, 1)
        pygame.draw.rect(screen, "red", pixel)

    hurtboxes_active = []
    hurtboxes_active.extend(apply_hurtboxes(dragon_king1[0]["idle"], p1coords, 1))
    hurtboxes_active.extend(apply_hurtboxes(dragon_king2[0]["idle"], p2coords, 2))

    for point in hurtboxes_active:
        if point[0][0] >= stage[0] and point[0][0] <= stage[2] and point[0][1] >= stage[1] and point[0][1] <= stage[3]:
            if point[2] == 1:
                if p1accel[1] >= 0:
                    if dragon_king1[2][1] == 0:
                        dragon_king1[2] = ("grounded", -1)
                    p1coords[1] = 351
                    p1accel[1] = 0
                else:
                    p1coords[1] = 479
                    p1accel[1] = 0
            elif point[2] == 2:
                if p2accel[1] >= 0:
                    if dragon_king2[2][1] == 0:
                        dragon_king2[2] = ("grounded", -1)
                    p2coords[1] = 351
                    p2accel[1] = 0
                else:
                    p2coords[1] = 479
                    p2accel[1] = 0

    screen.blit(bg, (0, 0))
    screen.blit(dragon_king_left, p1coords)
    screen.blit(dragon_king_right, p2coords)

    for box in hurtboxes_active:
        pixel = pygame.Rect(box[0][0], box[0][1], 1, 1)
        pygame.draw.rect(screen, "blue", pixel)

    pygame.display.flip()

pygame.quit()
