from django.contrib.auth.models import User
from adventure.models import Player, Room
import random

Room.objects.all().delete()

num_room = 100
height = 20
width = 20

rooms = []

for id in range(num_room):
    rooms.append(
        Room(id=id, title=f"test_room {id}", description="I'm a test room"))

# for room in rooms:
#     room.save()

opposite = {
    "n": "s",
    "s": "n",
    "e": "w",
    "w": "e"
}

world = dict()


def popomatic():
    dir_int = random.randint(0, 3)
    dir = {
        0: "n",
        1: "s",
        2: "e",
        3: "w"
    }
    return dir[dir_int]

# takes in a direction and coordinate list (y, x), returns appropriate
# list representing 1 move in that direction


def move_coord(dir, coord_list):
    if dir == "n":
        return [coord_list[0] - 1, coord_list[1]]
    elif dir == "s":
        return [coord_list[0] + 1, coord_list[1]]
    elif dir == "e":
        return [coord_list[0], coord_list[1] + 1]
    else:
        return [coord_list[0], coord_list[1] - 1]


def hashable(list):
    hashableCoord = (list[0], list[1])
    return hashableCoord


# grab the first room
new_room = rooms.pop()
# mark this room as the origin point
origin = new_room
# find middle of nested list
current_coord = [height // 2, width // 2]
# record position of room in dict
world[hashable(current_coord)] = new_room
# set room coordinates
new_room.x = current_coord[1]
new_room.y = current_coord[0]
# save room to database
new_room.save()
# set current moving direction
cur_dir = popomatic()
stepper = random.randint(1, 5)
# move coordinates
# current_coord = move_coord(cur_dir, current_coord)
print(current_coord)
last_room = new_room

while len(rooms) > 0:
    # get the next room
    new_room = rooms.pop()
    # if stepper is <= 0, change direction, and reset stepper
    if stepper <= 0:
        stepper = random.randint(1, 5)
        cur_dir = popomatic()
    # while there is a room in cur_dir
    next_coord = move_coord(cur_dir, current_coord)
    # TODO Almost there, just have to figure out how to avoid the key error
    while hashable(next_coord) in world:
        # if there is, move to it, connect the rooms
        last_room = world[hashable(current_coord)]
        curr_room = world[hashable(next_coord)]
        last_room.connectRooms(curr_room, cur_dir)
        curr_room.connectRooms(last_room, opposite[cur_dir])
        # save the room
        # last_room.save()
        # curr_room.save()
        # continue until there is no existing room at curr_coord
        current_coord = next_coord
        next_coord = move_coord(cur_dir, next_coord)
    # set new room in empty spot
    world[hashable(next_coord)] = new_room
    new_room.x = next_coord[1]
    new_room.y = next_coord[0]
    new_room.save()
    last_room.connectRooms(new_room, cur_dir)
    new_room.connectRooms(last_room, opposite[cur_dir])
    last_room = new_room
    curr_room = new_room
    current_coord = next_coord
    stepper -= 1


players = Player.objects.all()
for p in players:
    p.currentRoom = origin.id
    p.save()

print(world)