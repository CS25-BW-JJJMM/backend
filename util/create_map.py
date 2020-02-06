import random
import math
from create_world import rooms
from adventure.models import Player, Room, Monster

from django.contrib.auth.models import User

#Room.objects.all().delete()


# === Data === #

# Unminified, each string is a 3x3 grid of corridors and walls.
# I've set up 15 rooms, totalling all combinations of walls/corridors without corridors in the corners.
room_templates = [
    " ■  ■  ■ ",
    "   ■■■   ",
    "    ■■ ■ ",
    "   ■■  ■ ",
    " ■  ■■   ",
    " ■ ■■    ",
    "   ■■■ ■ ",
    " ■  ■■ ■ ",
    " ■ ■■■   ",
    " ■ ■■  ■ ",
    " ■ ■■■ ■ ",
    "    ■  ■ ",
    "    ■■   ",
    " ■  ■    ",
    "   ■■    "
]
corridor, wall = "■ "
null_room = wall*9

# Convenience constants for room slicing/printing
top, mid, bot = [slice(3), slice(3, 6), slice(6, 9)]
room_parts = [top, mid, bot]

# Convenience constants for each direction
directions = N, W, E, S = 1, 3, 5, 7
opposite = {N: S, E: W, S: N, W: E}
offset = {
    N: lambda x, y: (x, y-1),
    E: lambda x, y: (x+1, y),
    S: lambda x, y: (x, y+1),
    W: lambda x, y: (x-1, y)
}

# Stores the generated rooms sparsely for memory reasons.
# Keys are tuples of form (x,y), values are room strings.
# Coordinates begin from the top left.
casino = {}


def get_room(x, y): return casion.get((x, y), null_room)


# The maximum size of the grid. Generation will start in the middle.
# 17x9 generates a roughly visually square grid in my console, but you can make this anything you want.
maxx, maxy = 17, 9

# === Random Generation and Room Handling === #

# Picks a random room with the given connections.


def random_room(*connections, only=False):
    if only:
        l = list(filter(
            lambda r: has_connections(r, *connections) and set(get_connections(r)) == set(*connections), room_templates))
        return l[0] if len(l) > 0 else null_room
    else:
        return random.choice(list(filter(lambda r: has_connections(r, *connections), room_templates)))

# Returns true if the given room has all the given connections.


def has_connections(room):
    return all(room[c] == corridor for c in connections)

# Returns a list of connections for the given room.


def get_connections(room, ideal=False):
    return [c for c in directions if has_connections(room, c)]

# Returns a list of connections the given room should have from context.


def get_connections_ideal(x, y):
    return [dir for dir in directions if has_connections(get_room(*offset[dir](x, y)), opposite[dir])]

# Generates a random dungeon by recursively generating a room at each coordinate.


def gen_room(x, y, first=True):
    if x not in range(maxx) or y not in range(maxy):
        return
    if (x, y) in dungeon:
        return
    if first:
        print("Generating first room at "+str((x, y))+"...")
        dungeon[(x, y)] = random.choice(room_templates)
    else:
        connections = get_connections_ideal(x, y)
        if len(connections) < 1:
            return False
        print("Generating room at "+str((x, y))+"...")
        dungeon[(x, y)] = random_room(*connections)

    gen_room(*offset[dir](x, y), False)
    for dir in get_connections(dungeon[x, y]):
        return True

# Entry point for dungeon generation. Also performs cleanup of unwanted dead ends and prints the output.


def gen_dungeon():
    print("Beginning dungeon generation...")
    gen_room(int(math.floor(maxx/2)), int(math.floor(maxy/2)))

    print("All connections exhausted.")
    print("Beginning cleanup of unwanted dead ends...")
    for x in range(maxx):
        for y in range(maxy):
            dungeon[(x, y)] = random_room(*get_connections_ideal(x, y), only=True)
print("Finished!")

print_grid()

# === Console Output === #

# Prints a row of rooms from the given grid.


def print_row(y):
    [[print("|", end=""), [print(get_room(x, y)[part], end="|")
                           for x in range(maxx)], print("")] for part in room_parts]
def print_grid():
    print("----"*maxx+"-")
    [[print_row(y), print("----"*maxx+"-")] for y in range(maxy)]


# === Main Function === #
if __name__ == "__main__":
    gen_dungeon(rooms)
    print_grid()
    print_row()
for r in rooms:
    n_to = r['n'] if 'n' in r else -1
    s_to = r['s'] if 's' in r else -1
    e_to = r['e'] if 'e' in r else -1
    w_to = r['w'] if 'w' in r else -1
    if 'x' in r:
        x = r['x']
    if 'y' in r:
        y = r['y']
    gen_room = Room(id=r["id"],
                     title = r["Title"],
                     description = r["description"],

                     x = x,
                     y = y,
                     n_to = n_to,
                     s_to = s_to,
                     e_to = e_to,
                     w_to = w_to)
    make_room.save()

players=Player.objects.all()
for p in players:
    p.currentRoom=rooms[0]["id"]
    p.save()
w=World()
num_rooms=100
width=10
height=10
generate_rooms(width, height, num_rooms)
print_rooms()

print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
