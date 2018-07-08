from functools import reduce
from operator import or_
from itertools import starmap

GRID = {(col, row) for col in range(ord('A'), ord('L') + 1) for row in range(1, 10)}

def neighbours(c, r):
    if c % 2:
        return {(c, r-1), (c+1, r-1), (c+1, r), (c, r+1), (c-1, r), (c-1, r-1)} 
    return {(c, r-1), (c+1, r), (c+1, r+1), (c, r+1), (c-1, r+1), (c-1, r)}

def expand(positions):
    return reduce(or_, starmap(neighbours, positions), positions) & GRID

def coords(c, r):
    return ord(c), int(r)

def coords_set(positions):
    return set(starmap(coords, positions))

def supply_line(pos, supply, enemies):
    visited = expand(coords_set(enemies))
    supply = coords_set(supply) - visited

    steps, to_visit = 0, {coords(*pos)}
    while to_visit:
        steps += 1
        to_visit = expand(to_visit) - visited
        visited |= to_visit
        if visited & supply:
            return steps
