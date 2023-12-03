import re
from functools import reduce


with open("data/02.txt") as f:
    read_data = f.read().splitlines()


cubes = { "red":12, "green":13, "blue":14 }


def balls(draw):
    return int(draw.strip().split(' ')[0])


def color(draw):
    return draw.strip().split(' ')[1]


def game(line):
    return re.split(r'[,;]', line.split(':')[1])


def game_id(line):
    return int(line.split(':')[0].split(' ')[-1])


def is_valid(game):
    return all([balls(draw) <= cubes[color(draw)] for draw in game])
 

def game_min_cubes(game):
    min_cubes = {}
    draw_tups = [(balls(draw), color(draw)) for draw in game]
    for d in draw_tups:
        min_cubes[d[1]] = d[0] if d[1] not in min_cubes or (d[1] in min_cubes and min_cubes[d[1]] < d[0]) else min_cubes[d[1]]
    return min_cubes


print( "Part 1:", 
    sum(
        [game_id(line) if is_valid(game(line)) else 0 for line in read_data]
    )
)


print( "Part 2:",
        sum(
            [reduce(lambda x, y: x * y, game_min_cubes(game(line)).values()) for line in read_data]
        )
)