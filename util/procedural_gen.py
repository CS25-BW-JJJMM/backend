from django.contrib.auth.models import User
from adventure.models import Player, Room
import random

Room.objects.all().delete()

population = ["crowded", "normal", "deserted"]

ambiance = ["bright", "dim", "normal", "grimy", "sterile"]

funct = ["card room", "hallway", "tunnel", "kitchen", "bar", "pool room"]

description_beginners = ["You find yourself in ",
                         "You have stumbled upon ", "You walk into "]

pop_desc = {
    "crowded": "Around you is a sea of bustling orcs and goblins.",
    "normal": "A few goblins are milling about.",
    "deserted": "The place looks deserted."
}

ambiance_desc = {
    "bright": "The glare of the torch light is almost too much for your eyes to bear.",
    "dim": "You can barely make out any shapes in the dim light.",
    "normal": "Things look fine here.",
    "grimy": "Everything has a fine layer of dust and filth upon it.",
    "sterile": "The walls and floor are spotless."
}

functional_desc = {
    "card room": "An orc holding a deck of cards looks up and smiles as you enter.",
    "hallway": "Just a hallway, not much to do but walk on.",
    "tunnel": "Water drips from the ceiling onto the muddy floor.",
    "kitchen": "An awful stench fills your nose.  Probably just roast halfling.",
    "bar": "The smell of stale grog makes your stomach turn.",
    "pool room": "The felt on the pool tables is faded and splattered with dark stains."
}


def room_generator(id):
    room_population = random.choice(population)
    room_ambiance = random.choice(ambiance)
    room_function = random.choice(funct)
    room_desc_begin = random.choice(description_beginners)
    title = f"{room_population.capitalize()} {room_function}"
    description = f"{room_desc_begin} a {room_population} {room_function}. {pop_desc[room_population]} {ambiance_desc[room_ambiance]} {functional_desc[room_function]}"
    return Room(id=id, title=title, description=description)


num_room = 150
height = 20
width = 20

rooms = []

for id in range(num_room):
    random_room = room_generator(id)
    rooms.append(random_room)

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
        stepper = random.randint(1, 3)
        cur_dir = popomatic()
    # while there is a room in cur_dir
    next_coord = move_coord(cur_dir, current_coord)
    # determine if within bounds, change direction if not
    # while (0 > next_coord[0] or next_coord[0] > width) or (0 > next_coord[1] or next_coord[1] > height):
    #     cur_dir = popomatic()
    #     next_coord = move_coord(cur_dir, next_coord)
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
