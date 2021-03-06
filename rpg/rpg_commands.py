import random

attribute_bonus_dict = {
    0: -5,
    1: -5,
    2: -4,
    3: -4,
    4: -3,
    5: -3,
    6: -2,
    7: -2,
    8: -1,
    9: -1,
    10: 0,
    11: 0,
    12: 1,
    13: 1,
    14: 2,
    15: 2,
    16: 3,
    17: 3,
    18: 4,
    19: 4,
    20: 5,
    21: 5,
    22: 6,
    23: 6,
    24: 7,
    25: 7,
    26: 8,
    27: 8,
    28: 9,
    29: 9,
    30: 10,
    31: 10,
    32: 11,
    33: 11,
    34: 12,
    35: 12,
    36: 13,
    37: 13,
    38: 14,
    39: 14,
    40: 15,
}

def roll_die(faces):
    roll_result = str(random.randint(1, faces))
    return int(roll_result)