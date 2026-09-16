import pygame
from collections import defaultdict

starting_lives = 1

hitboxes_active = []

# add lists with [(x, y), activity_frames_left, player, move]

hurtboxes_active = []

# add lists with [(x, y), activity_frames_left, player]

zones_active = []

# add lists with [(x, y), type]

def rectangle(x, y, w, h, structure="list"):
    """Takes the top-left corner as (x, y)"""
    if structure == "list":
        all_points = []
        for i in range(w):
            for j in range(h):
                all_points.append((x + i, y + j))
    elif structure == "set":
        all_points = set()
        for i in range(w):
            for j in range(h):
                all_points.add((x + i, y + j))
    else:
        all_points = "You messed up somewhere"
    return all_points

def circle(x, y, size):
    """Takes the centre as (x, y)"""
    all_points = []
    x_list = [-1 * i for i in range(size)]
    x_list.append(0)
    x_list.extend(range(size))
    y_list = [-1 * i for i in range(size)]
    y_list.append(0)
    y_list.extend(range(size))
    for i in x_list:
        for j in y_list:
            if (i**2 + j**2 <= size**2):
                all_points.append((x + i, y + j))
    return all_points

def triangle(x, y, size, direction):
    """Takes the right-angle corner as (x, y) and the direction extends outward from there"""
    all_points = []
    x_list = [-1 * i for i in range(size)]
    x_list.append(0)
    x_list.extend(range(size))
    y_list = [-1 * i for i in range(size)]
    y_list.append(0)
    y_list.extend(range(size))
    if direction == "down":
        for i in x_list:
            for j in y_list:
                if (j>i) and (j>-i):
                    all_points.append((x + i, y + j))
    elif direction == "up":
        for i in x_list:
            for j in y_list:
                if (j<i) and (j<-i):
                    all_points.append((x + i, y + j))
    return all_points

def arch(x, y, w, left, right):
    pass

def horizontal_pill(x, y, size):
    pass

def vertical_pill(x, y, size):
    pass

def apply_hurtboxes(points: list, offset, player, time: int = 1):
    """Pass in a character hurtbox action, the offset from the top left, the player that it belongs to and how many frames the hurtbox should be active for"""
    hurtboxes = []
    for point in points:
        hurtboxes.append([(point[0] + offset[0], point[1] + offset[1]), time, player])
    return hurtboxes

    # add all current hurtboxes here

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

    moves look like: [[hitbox1, hitbox2], knockback, knockback angle, hitstun, damage, priority, hitstop?]

    hybrid moves look like: [[hitbox1, ["projectile", hitbox2, velocity, direction]], knockback, knockback angle, hitstun, damage, priority, hitstop?]

    projectile moves look like: [[["projectile", hitbox1, velocity, direction], ["projectile", hitbox2, velocity, direction]], knockback, knockback angle, hitstun, damage, priority, hitstop?]

    """
    for hitbox in hitboxes:
        if hitbox[0] != "projectile":
            for point in hitbox[0]:
                hitboxes_active.append([(point[0], point[1]), hitbox[1], hitbox[2], hitbox[3]])
        elif hitbox[0] == "projectile":
            create_projectile(hitbox[1], hitbox[2], hitbox[3])

def create_character(hurtboxes: list):
    """

    hurtboxes look like: ["action", shape()]

    characters look like: [hurtboxes, damage, (actionability, duration), lives]

    actionability is "grounded", "aerial", "helpless" or "stunned" and a duration or -1 for indefinite

    """

    char_hurtboxes = defaultdict(list)

    for hurtbox in hurtboxes:
        for point in hurtbox[1]:
            char_hurtboxes[hurtbox[0]].append((point[0], point[1]))

    return [char_hurtboxes, 0, ("grounded", -1), starting_lives]

    # create hurtbox(es) and add moves bound to inputs
    # hurtboxes are reusable by name
    # hurtbox x_offset and y_offset are from the top-left corner

def hitbox_on_hitbox_collision(hitbox1, hitbox2, move1, move2):
    if move1[6] or move2[6] == 0:
        pass
        #transcendent priority
    elif move1[6] > move2[6]:
        to_remove = []
        for hitbox in hitboxes_active:
            if hitbox[1] == hitbox2[1] and hitbox[2] == hitbox2[2] and hitbox[3] == hitbox2[3]:
                to_remove.append(hitbox)
        for box in to_remove:
            hitboxes_active.remove(box)
    elif move1[6] < move2[6]:
        to_remove = []
        for hitbox in hitboxes_active:
            if hitbox[1] == hitbox1[1] and hitbox[2] == hitbox1[2] and hitbox[3] == hitbox1[3]:
                to_remove.append(hitbox)
        for box in to_remove:
            hitboxes_active.remove(box)
    elif move1[6] == move2[6]:
        to_remove = []
        for hitbox in hitboxes_active:
            if (hitbox[1] == hitbox1[1] and hitbox[2] == hitbox1[2] and hitbox[3] == hitbox1[3]) or (hitbox[1] == hitbox2[1] and hitbox[2] == hitbox2[2] and hitbox[3] == hitbox2[3]):
                to_remove.append(hitbox)
        for box in to_remove:
            hitboxes_active.remove(box)

    # pass in eval(hitbox[3])

def hitbox_on_opposing_hurtbox_collision(hitbox, hurtbox, move):
    to_remove = []
    for box in hitboxes_active:
        if hitbox[1] == box[1] and hitbox[2] == box[2] and hitbox[3] == box[3]:
            to_remove.append(hitbox)
    for box in to_remove:
        hitboxes_active.remove(box)

    # pass in eval(hitbox[3])

def collision_check():
    pass

    # check all hitboxes and hurtboxes for collision
    # lower all activity_frames_left by 1
    # if activity_frames_left == 0, delete the hitbox or hurtbox
    # otherwise, if the last element in the hitbox list is "projectile", change the hitbox's (x, y) by its direction/velocity vector

def zone_set(shape: list, type: str):
    """
    zone types are: ["death", "special death", "bubble damage", "hard platform", "soft platform", "ledge"]
    """

    for point in shape:
        zones_active.append([point, type])

def zone_collision_check():
    for hitbox in hitboxes_active:
        for zone in zones_active:
            if hitbox[0] == zone[0]:
                pass
                #trigger collision based on type

    #check if any hurtboxes or hitboxes are in special zones

# have to add as many means of input handling as possible
