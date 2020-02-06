from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

num_room = 100

rooms = []

for id in range(num_room):
    rooms.append(Room(id=id, title="test_room", description="I'm a test room"))

for room in rooms:
    room.save()

opposite = {
    "n": "s",
    "s": "n",
    "e": "w",
    "w": "e"
}

current_room = rooms.pop()
origin = current_room
current_coord = [0, 0]
while len(rooms) > 0:
    # get the next room
    next_room = rooms.pop()
    print(next_room)
    # place current room
    current_room.x = current_coord[0]
    current_room.y = current_coord[1]
    # connect next room to current room
    current_room.connectRooms(next_room, "n")
    next_room.connectRooms(current_room, opposite["n"])
    # make next room current room
    current_room = next_room
    current_coord[1] += 1
    print(current_coord)

players = Player.objects.all()
for p in players:
    p.currentRoom = origin.id
    p.save()
