from django.contrib.auth.models import User
from adventure.models import Player, Room
Room.objects.all().delete()
          # Origin 
rooms = [{"id" : 0, "x" : 0, "y" : 0, "Title" : "Origin", "n" : 0, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is the Origin, You may Travel North, West, East, Or South."}, 
          # North of the Origin
         {"id" : 1, "x" : 0, "y" : 1, "Title" : "Hallway North One", "n" : 1, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 1 Unit."},
         {"id" : 2, "x" : 0, "y" : 2, "Title" : "Hallway North Two", "n" : 2, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 2 Units."},
         {"id" : 3, "x" : 0, "y" : 3, "Title" : "Hallway North Three", "n" : 3, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 3 Units."},
         {"id" : 4, "x" : 0, "y" : 4, "Title" : "Hallway North Four", "n" : 4, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 4 Units."},
         {"id" : 5, "x" : 0, "y" : 5, "Title" : "Hallway North Five", "n" : 5, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 5 Units."},
         {"id" : 6, "x" : 0, "y" : 6, "Title" : "Hallway North Six", "n" : 6, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 6 Units."},
         {"id" : 7, "x" : 0, "y" : 7, "Title" : "Hallway North Seven", "n" : 7, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 7 Units."},
         {"id" : 8, "x" : 0, "y" : 8, "Title" : "Hallway North Eight", "n" : 8, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 8 Units."},
         {"id" : 9, "x" : 0, "y" : 9, "Title" : "Hallway North Nine", "n" : 9, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 9 Units."},
         {"id" : 10, "x" : 0, "y" : 10, "Title" : "Hallway North Ten", "n" : 10, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 10 Units."},
          # South of the Origin
         {"id" : 11, "x" : 0, "y" : -1, "Title" : "Hallway South One", "n" : 0, "s" : 1, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 1 Unit."},
         {"id" : 12, "x" : 0, "y" : -2, "Title" : "Hallway South Two", "n" : 0, "s" : 2, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 2 Units."},
         {"id" : 13, "x" : 0, "y" : -3, "Title" : "Hallway South Three", "n" : 0, "s" : 3, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 3 Units."},
         {"id" : 14, "x" : 0, "y" : -4, "Title" : "Hallway South Four", "n" : 0, "s" : 4, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 4 Units."},
         {"id" : 15, "x" : 0, "y" : -5, "Title" : "Hallway South Five", "n" : 0, "s" : 5, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 5 Units."},
         {"id" : 16, "x" : 0, "y" : -6, "Title" : "Hallway South Six", "n" : 0, "s" : 6, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 6 Units."},
         {"id" : 17, "x" : 0, "y" : -7, "Title" : "Hallway South Seven", "n" : 0, "s" : 7, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 7 Units."},
         {"id" : 18, "x" : 0, "y" : -8, "Title" : "Hallway South Eight", "n" : 0, "s" : 8, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 8 Units."},
         {"id" : 19, "x" : 0, "y" : -9, "Title" : "Hallway South Nine", "n" : 0, "s" : 9, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 9 Units."},
         {"id" : 20, "x" : 0, "y" : -10, "Title" : "Hallway South Ten", "n" : 0, "s" : 10, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 10 Units."},
          # East of the Origin
         {"id" : 21, "x" : -1, "y" : 0, "Title" : "Hallway East One", "n" : 0, "s" : 0, "e" : 1, "w" : 0,
          "description" : "This is just East of the Origin by 1 Unit."},
         {"id" : 22, "x" : -2, "y" : 0, "Title" : "Hallway East Two", "n" : 0, "s" : 0, "e" : 2, "w" : 0,
          "description" : "This is just East of the Origin by 2 Units."},
         {"id" : 23, "x" : -3, "y" : 0, "Title" : "Hallway East Three", "n" : 0, "s" : 0, "e" : 3, "w" : 0,
          "description" : "This is just East of the Origin by 3 Units."},
         {"id" : 24, "x" : -4, "y" : 0, "Title" : "Hallway East Four", "n" : 0, "s" : 0, "e" : 4, "w" : 0,
          "description" : "This is just East of the Origin by 4 Units."},
         {"id" : 25, "x" : -5, "y" : 0, "Title" : "Hallway East Five", "n" : 0, "s" : 0, "e" : 5, "w" : 0,
          "description" : "This is just East of the Origin by 5 Units."},
         {"id" : 26, "x" : -6, "y" : 0, "Title" : "Hallway East Six", "n" : 0, "s" : 0, "e" : 6, "w" : 0,
          "description" : "This is just East of the Origin by 6 Units."},
         {"id" : 27, "x" : -7, "y" : 0, "Title" : "Hallway East Seven", "n" : 0, "s" : 0, "e" : 7, "w" : 0,
          "description" : "This is just East of the Origin by 7 Units."},
         {"id" : 28, "x" : -8, "y" : 0, "Title" : "Hallway East Eight", "n" : 0, "s" : 0, "e" : 8, "w" : 0,
          "description" : "This is just East of the Origin by 8 Units."},
         {"id" : 29, "x" : -9, "y" : 0, "Title" : "Hallway East Nine", "n" : 0, "s" : 0, "e" : 9, "w" : 0,
          "description" : "This is just East of the Origin by 9 Units."},
         {"id" : 30, "x" : -10, "y" : 0, "Title" : "Hallway East Ten", "n" : 0, "s" : 0, "e" : 10, "w" : 0,
          "description" : "This is just East of the Origin by 10 Units."},
          # West of the Origin
         {"id" : 31, "x" : 1, "y" : 0, "Title" : "Hallway West One", "n" : 0, "s" : 0, "e" : 0, "w" : 1,
          "description" : "This is just West of the Origin by 1 Unit."},
         {"id" : 32, "x" : 2, "y" : 0, "Title" : "Hallway West Two", "n" : 0, "s" : 0, "e" : 0, "w" : 2,
          "description" : "This is just West of the Origin by 2 Units."},
         {"id" : 33, "x" : 3, "y" : 0, "Title" : "Hallway West Three", "n" : 0, "s" : 0, "e" : 0, "w" : 3,
          "description" : "This is just West of the Origin by 3 Units."},
         {"id" : 34, "x" : 4, "y" : 0, "Title" : "Hallway West Four", "n" : 0, "s" : 0, "e" : 0, "w" : 4,
          "description" : "This is just West of the Origin by 4 Units."},
         {"id" : 35, "x" : 5, "y" : 0, "Title" : "Hallway West Five", "n" : 0, "s" : 0, "e" : 0, "w" : 5,
          "description" : "This is just West of the Origin by 5 Units."},
         {"id" : 36, "x" : 6, "y" : 0, "Title" : "Hallway West Six", "n" : 0, "s" : 0, "e" : 0, "w" : 6,
          "description" : "This is just West of the Origin by 6 Units."},
         {"id" : 37, "x" : 7, "y" : 0, "Title" : "Hallway West Seven", "n" : 0, "s" : 0, "e" : 0, "w" : 7,
          "description" : "This is just West of the Origin by 7 Units."},
         {"id" : 38, "x" : 8, "y" : 0, "Title" : "Hallway West Eight", "n" : 0, "s" : 0, "e" : 0, "w" : 8,
          "description" : "This is just West of the Origin by 8 Units."},
         {"id" : 39, "x" : 9, "y" : 0, "Title" : "Hallway West Nine", "n" : 0, "s" : 0, "e" : 0, "w" : 9,
          "description" : "This is just West of the Origin by 9 Units."},
         {"id" : 40, "x" : 10, "y" : 0, "Title" : "Hallway West Ten", "n" : 0, "s" : 0, "e" : 0, "w" : 10,
          "description" : "This is just West of the Origin by 10 Units."},
]
for r in rooms:
  n = r['n'] if 'n' in r else -1
  s = r['s'] if 's' in r else -1
  e = r['e'] if 'e' in r else -1
  w = r['w'] if 'w' in r else -1
  if 'x' in r: x = r['x']
  if 'y' in r: y = r['y']
  make_room = Room(id=r["id"], 
                   title=r["title"], 
                   description=r["description"], 
                   x=x, 
                   y=y, 
                   n=n, 
                   s=s, 
                   e=e, 
                   w=w)
  make_room.save()
players=Player.objects.all()
for p in players:
  p.currentRoom=rooms[0]["id"]
  p.save()

  create_world()