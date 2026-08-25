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

def create_projectile(hitboxes, velocity, direction):
    pass
    # create a projectile with certain properties
    # combine velocity and direction into one 2D vector
    # append "projectile" to the end of the added hitbox

def use_move(hitboxes: list):
    for hitbox in hitboxes:
        if hitbox[0] != "projectile":
            for point in hitbox[0]:
                hitboxes_active.append([(point[0], point[1]), hitbox[1], hitbox[2], hitbox[3]])
                #hitbox = [[(x1, y1), (x2, y2)], frames_active, player, move]
        elif hitbox[0] == "projectile":
            create_projectile(hitbox[1], hitbox[2], hitbox[3])

    # moves look like: [[hitbox1, hitbox2], knockback, knockback angle, hitstun, hitstop?, damage, i-frames?, priority?]
    # hybrid moves look like: [[hitbox1, ["projectile", hitbox2, velocity, direction]], knockback, knockback angle, hitstun, hitstop?, damage, i-frames?, priority?]
    # projectile moves look like: [[["projectile", hitbox1, velocity, direction], ["projectile", hitbox2, velocity, direction]], knockback, knockback angle, hitstun, hitstop?, damage, i-frames?, priority?]

def create_character():
    pass
    # create hurtbox(es) and add moves

def hitbox_on_hitbox_collision():
    pass

def hitbox_on_opposing_hurtbox_collision():
    pass

    #refer back to the move for all the information

def collision_check():
    pass

    # check all hitboxes and hurtboxes for collision
    # lower all activity_frames_left by 1
    # if activity_frames_left == 0, delete the hitbox
    # otherwise, if the last element in the hitbox list is "projectile", change the hitbox's (x, y) by it's direction/velocity vector

def zone_set():
    pass

    #set a special zone such as: blast zone bubble, death zone, special death zone, king of the hill zone, solid object zone

def zone_collision_check():
    pass

    #check if any hurtboxes or hitboxes are in special zones

# have to add as many means of input handling as possible
