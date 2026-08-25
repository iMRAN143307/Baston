import pygame

hitboxes_active = []

# add lists with [(x, y), activity_frames_left, player, move]

hurtboxes_active = []

#add lists with [(x, y), player]

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

def create_projectile():
    pass
    # create a projectile with certain properties

def use_move(hitboxes: list):
    for hitbox in hitboxes:
        if hitbox[0] != "projectile":
            for point in hitbox[0]:
                hitboxes_active.append([(point[0], point[1]), hitbox[1], hitbox[2], hitbox[3]])
                # [(x, y), frames_active, player, move]
        elif hitbox[0] == "projectile":
            pass
            #create a projectile

    # info includes: knockback, knockback angle, hitstun, hitstop?, damage, i-frames?
    # projectile info includes: knockback, knockback angle, hitstun, hitstop?, damage, i-frames?, velocity, direction

def create_character():
    pass
    # create hurtbox(es) and add moves

def hitbox_on_hitbox_collision():
    pass

def hitbox_on_opposing_hurtbox_collision():
    pass

def collision_check():
    pass

    # check all hitboxes and hurtboxes for collision
    # lower all activity_frames_left by 1
    # if activity_frames_left == 0, delete the hitbox

def zone_set():
    pass

    #set a special zone such as: blast zone bubble, death zone, special death zone, king of the hill zone, solid object zone

def zone_collision_check():
    pass

    #check if any hurtboxes or hitboxes are in special zones

# have to add as many means of input handling as possible
