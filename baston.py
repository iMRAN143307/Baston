import pygame
from collections import defaultdict

hitboxes_active = []

# add lists with [(x, y), activity_frames_left, player, move]

hurtboxes_active = []

# add lists with [(x, y), player]

zones_active = []

# add lists with [(x, y), type]

def rectangle(x, y, w, h):
    """Takes the top-left corner as (x, y)"""
    all_points = []
    for i in range(w):
        for j in range(h):
            all_points.append((x + i, y + j))
    return all_points

def circle(x, y, size):
    """Takes the centre as (x, y)"""
    all_points = []
    for i in range(size):
        for j in range(size):
            if (i**2 + j**2 <= size**2):
                all_points.append((x + i, y + j))
    return all_points

def triangle(x, y, size):
    """Takes the centre as (x, y)"""
    all_points = []
    for i in range(size):
        for j in range(size):
            if (j <= (i + size) * 1.73205081) and (j <= (i - size) * -1.73205081):
                all_points.append((x + i, y + j))
    return all_points

def arch(x, y, w, left, right):
    pass

def horizontal_pill(x, y, size):
    pass

def vertical_pill(x, y, size):
    pass

def create_projectile(hitbox, velocity, direction):
    """DO NOT CALL YOUR MOVE 'PROJECTILE'! IT IS BAD CODE DESIGN AND MAY LEAD TO ISSUES WITH BASTON'S HITBOX HANDLER"""
    for point in hitbox[0]:
        hitboxes_active.append([(point[0], point[1]), hitbox[1], hitbox[2], hitbox[3], (direction[0] * velocity, direction[1] * velocity), "projectile"])
    # create a projectile with certain properties
    # combine velocity and direction into one 2D vector
    # append "projectile" to the end of the added hitbox

def use_move(hitboxes: list):
    """

    hitboxes look like: [shape(), frames_active, player, move]

    moves look like: [[hitbox1, hitbox2], knockback, knockback angle, hitstun, hitstop?, damage, i-frames?, priority?]

    hybrid moves look like: [[hitbox1, ["projectile", hitbox2, velocity, direction]], knockback, knockback angle, hitstun, hitstop?, damage, i-frames?, priority?]

    projectile moves look like: [[["projectile", hitbox1, velocity, direction], ["projectile", hitbox2, velocity, direction]], knockback, knockback angle, hitstun, hitstop?, damage, i-frames?, priority?]

    """
    for hitbox in hitboxes:
        if hitbox[0] != "projectile":
            for point in hitbox[0]:
                hitboxes_active.append([(point[0], point[1]), hitbox[1], hitbox[2], hitbox[3]])
        elif hitbox[0] == "projectile":
            create_projectile(hitbox[1], hitbox[2], hitbox[3])

def create_character(hurtboxes: list):
    """

    hurtboxes look like: ["move_name", (x_offset, y_offset), shape()]

    """

    char_hitboxes = defaultdict(list)

    for hurtbox in hurtboxes:
        for point in hurtbox[2]:
            char_hitboxes[hurtbox[0]].append((point[0] + hurtbox[1][0], point[1] + hurtbox[1][1]))

    return char_hitboxes

    # create hurtbox(es) and add moves bound to inputs
    # hurtboxes are reusable by name
    # hurtbox x_offset and y_offset are from the top-left corner

def hitbox_on_hitbox_collision():
    pass

    #refer back to the move for all the information

def hitbox_on_opposing_hurtbox_collision():
    pass

    #refer back to the move for all the information

def collision_check():
    pass

    # check all hitboxes and hurtboxes for collision
    # lower all activity_frames_left by 1
    # if activity_frames_left == 0, delete the hitbox
    # otherwise, if the last element in the hitbox list is "projectile", change the hitbox's (x, y) by its direction/velocity vector

def zone_set(shape: list, type: str):
    """
    zone types are: ["death", "special death", "bubble damage", "hard platform", "soft platform", "ledge"]
    """

    for point in shape:
        zones_active.append([point, type])

def zone_collision_check():
    pass

    #check if any hurtboxes or hitboxes are in special zones

# have to add as many means of input handling as possible
