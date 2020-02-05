from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()

# Origin

rooms = [{"id": 0, "x": 0, "y": 0, "Title": "Origin", "n": 1, "s": 11, "e": 21, "w": 31,
          "description": "This is the Origin, You may Travel North, West, East, Or South."},

         {"id": 1, "x": 0, "y": 1, "Title": "Hallway North One", "n": 2, "s": 0, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 1 Unit."},
         {"id": 2, "x": 0, "y": 2, "Title": "Hallway North Two", "n": 3, "s": 1, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 2 Units."},
         {"id": 3, "x": 0, "y": 3, "Title": "Hallway North Three", "n": 4, "s": 2, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 3 Units."},
         {"id": 4, "x": 0, "y": 4, "Title": "Hallway North Four", "n": 5, "s": 3, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 4 Units."},
         {"id": 5, "x": 0, "y": 5, "Title": "Hallway North Five", "n": 6, "s": 4, "e": 116, "w": -1,
          "description": "This is just North of the Origin by 5 Units."},
         {"id": 6, "x": 0, "y": 6, "Title": "Hallway North Six", "n": 7, "s": 5, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 6 Units."},
         {"id": 7, "x": 0, "y": 7, "Title": "Hallway North Seven", "n": 7, "s": 6, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 7 Units."},
         {"id": 8, "x": 0, "y": 8, "Title": "Hallway North Eight", "n": 8, "s": 7, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 8 Units."},
         {"id": 9, "x": 0, "y": 9, "Title": "Hallway North Nine", "n": 9, "s": 8, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 9 Units."},
         {"id": 10, "x": 0, "y": 10, "Title": "Hallway North Ten", "n": 41, "s": 9, "e": 117, "w": -1,
          "description": "This is just North of the Origin by 10 Units."},
         # South of the Origin
         {"id": 11, "x": 0, "y": -1, "Title": "Hallway South One", "n": 0, "s": 12, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 1 Unit."},
         {"id": 12, "x": 0, "y": -2, "Title": "Hallway South Two", "n": 11, "s": 13, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 2 Units."},
         {"id": 13, "x": 0, "y": -3, "Title": "Hallway South Three", "n": 12, "s": 14, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 3 Units."},
         {"id": 14, "x": 0, "y": -4, "Title": "Hallway South Four", "n": 13, "s": 15, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 4 Units."},
         {"id": 15, "x": 0, "y": -5, "Title": "Hallway South Five", "n": 14, "s": 16, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 5 Units."},
         {"id": 16, "x": 0, "y": -6, "Title": "Hallway South Six", "n": 15, "s": 17, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 6 Units."},
         {"id": 17, "x": 0, "y": -7, "Title": "Hallway South Seven", "n": 16, "s": 18, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 7 Units."},
         {"id": 18, "x": 0, "y": -8, "Title": "Hallway South Eight", "n": 17, "s": 19, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 8 Units."},
         {"id": 19, "x": 0, "y": -9, "Title": "Hallway South Nine", "n": 18, "s": 20, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 9 Units."},
         {"id": 20, "x": 0, "y": -10, "Title": "Hallway South Ten", "n": 19, "s": 56, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 10 Units."},
         # East of the Origin
         {"id": 21, "x": -1, "y": 0, "Title": "Hallway East One", "n": -1, "s": -1, "e": 22, "w": 0,
          "description": "This is just East of the Origin by 1 Unit."},
         {"id": 22, "x": -2, "y": 0, "Title": "Hallway East Two", "n": -1, "s": -1, "e": 23, "w": 22,
          "description": "This is just East of the Origin by 2 Units."},
         {"id": 23, "x": -3, "y": 0, "Title": "Hallway East Three", "n": -1, "s": -1, "e": 24, "w": 23,
          "description": "This is just East of the Origin by 3 Units."},
         {"id": 24, "x": -4, "y": 0, "Title": "Hallway East Four", "n": -1, "s": -1, "e": 25, "w": 24,
          "description": "This is just East of the Origin by 4 Units."},
         {"id": 25, "x": -5, "y": 0, "Title": "Hallway East Five", "n": -1, "s": -1, "e": 26, "w": 25,
          "description": "This is just East of the Origin by 5 Units."},
         {"id": 26, "x": -6, "y": 0, "Title": "Hallway East Six", "n": -1, "s": -1, "e": 27, "w": 26,
          "description": "This is just East of the Origin by 6 Units."},
         {"id": 27, "x": -7, "y": 0, "Title": "Hallway East Seven", "n": -1, "s": -1, "e": 28, "w": 27,
          "description": "This is just East of the Origin by 7 Units."},
         {"id": 28, "x": -8, "y": 0, "Title": "Hallway East Eight", "n": -1, "s": -1, "e": 29, "w": 28,
          "description": "This is just East of the Origin by 8 Units."},
         {"id": 29, "x": -9, "y": 0, "Title": "Hallway East Nine", "n": -1, "s": -1, "e": 30, "w": 29,
          "description": "This is just East of the Origin by 9 Units."},
         {"id": 30, "x": -10, "y": 0, "Title": "Hallway East Ten", "n": -1, "s": -1, "e": 31, "w": 71,
          "description": "This is just East of the Origin by 10 Units."},
         # West of the Origin
         {"id": 31, "x": 1, "y": 0, "Title": "Hallway West One", "n": -1, "s": -1, "e": 0, "w": 32,
          "description": "This is just West of the Origin by 1 Unit."},
         {"id": 32, "x": 2, "y": 0, "Title": "Hallway West Two", "n": -1, "s": -1, "e": 31, "w": 33,
          "description": "This is just West of the Origin by 2 Units."},
         {"id": 33, "x": 3, "y": 0, "Title": "Hallway West Three", "n": -1, "s": -1, "e": 32, "w": 34,
          "description": "This is just West of the Origin by 3 Units."},
         {"id": 34, "x": 4, "y": 0, "Title": "Hallway West Four", "n": -1, "s": -1, "e": 33, "w": 35,
          "description": "This is just West of the Origin by 4 Units."},
         {"id": 35, "x": 5, "y": 0, "Title": "Hallway West Five", "n": -1, "s": -1, "e": 34, "w": 36,
          "description": "This is just West of the Origin by 5 Units."},
         {"id": 36, "x": 6, "y": 0, "Title": "Hallway West Six", "n": -1, "s": -1, "e": 35, "w": 37,
          "description": "This is just West of the Origin by 6 Units."},
         {"id": 37, "x": 7, "y": 0, "Title": "Hallway West Seven", "n": -1, "s": -1, "e": 36, "w": 38,
          "description": "This is just West of the Origin by 7 Units."},
         {"id": 38, "x": 8, "y": 0, "Title": "Hallway West Eight", "n": -1, "s": -1, "e": 37, "w": 39,
          "description": "This is just West of the Origin by 8 Units."},
         {"id": 39, "x": 9, "y": 0, "Title": "Hallway West Nine", "n": -1, "s": -1, "e": 38, "w": 40,
          "description": "This is just West of the Origin by 9 Units."},
         {"id": 40, "x": 10, "y": 0, "Title": "Hallway West Ten", "n": -1, "s": -1, "e": 39, "w": 86,
          "description": "This is just West of the Origin by 10 Units."},
         # North of the Origin
         {"id": 41, "x": 0, "y": 11, "Title": "Hallway North Eleven", "n": 42, "s": 10, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 11 Unit."},
         {"id": 42, "x": 0, "y": 12, "Title": "Hallway North Twelve", "n": 43, "s": 41, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 12 Units."},
         {"id": 43, "x": 0, "y": 13, "Title": "Hallway North Thirteen", "n": 44, "s": 42, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 13 Units."},
         {"id": 44, "x": 0, "y": 14, "Title": "Hallway North Fourteen", "n": 45, "s": 43, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 14 Units."},
         {"id": 45, "x": 0, "y": 15, "Title": "Hallway North Fifteen", "n": 46, "s": 44, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 15 Units."},
         {"id": 46, "x": 0, "y": 16, "Title": "Hallway North Sixteen", "n": 47, "s": 45, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 16 Units."},
         {"id": 47, "x": 0, "y": 17, "Title": "Hallway North Seventeen", "n": 48, "s": 46, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 17 Units."},
         {"id": 48, "x": 0, "y": 18, "Title": "Hallway North Eightteen", "n": 49, "s": 47, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 18 Units."},
         {"id": 49, "x": 0, "y": 19, "Title": "Hallway North Nineteen", "n": 50, "s": 48, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 19 Units."},
         {"id": 50, "x": 0, "y": 20, "Title": "Hallway North Twenty", "n": 51, "s": 49, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 20 Units."},
         {"id": 51, "x": 0, "y": 21, "Title": "Hallway North TwentyOne", "n": 52, "s": 50, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 21 Units."},
         {"id": 52, "x": 0, "y": 22, "Title": "Hallway North TwentyTwo", "n": 53, "s": 51, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 22 Units."},
         {"id": 53, "x": 0, "y": 23, "Title": "Hallway North TwentyThree", "n": 54, "s": 52, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 23 Units."},
         {"id": 54, "x": 0, "y": 24, "Title": "Hallway North TwentyFour", "n": 55, "s": 53, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 24 Units."},
         {"id": 55, "x": 0, "y": 25, "Title": "Hallway North TwentyFive", "n": -1, "s": 54, "e": -1, "w": -1,
          "description": "This is just North of the Origin by 25 Units."},
         # South of the Origin
         {"id": 56, "x": 0, "y": -11, "Title": "Hallway South Eleven", "n": 20, "s": 57, "e": -1, "w": 86,
          "description": "This is just South of the Origin by 11 Unit."},
         {"id": 57, "x": 0, "y": -12, "Title": "Hallway South Twelve", "n": 56, "s": 58, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 12 Units."},
         {"id": 58, "x": 0, "y": -13, "Title": "Hallway South Thirteen", "n": 57, "s": 59, "e": -1, "w": 88,
          "description": "This is just South of the Origin by 13 Units."},
         {"id": 59, "x": 0, "y": -14, "Title": "Hallway South Fourteen", "n": 58, "s": 60, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 14 Units."},
         {"id": 60, "x": 0, "y": -15, "Title": "Hallway South Fifteen", "n": 59, "s": 61, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 15 Units."},
         {"id": 61, "x": 0, "y": -16, "Title": "Hallway South Sixteen", "n": 60, "s": 62, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 16 Units."},
         {"id": 62, "x": 0, "y": -17, "Title": "Hallway South Seventeen", "n": 61, "s": 63, "e": -1, "w": 92,
          "description": "This is just South of the Origin by 17 Units."},
         {"id": 63, "x": 0, "y": -18, "Title": "Hallway South Eightteen", "n": 62, "s": 64, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 18 Units."},
         {"id": 64, "x": 0, "y": -19, "Title": "Hallway South Nineteen", "n": 63, "s": 65, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 19 Units."},
         {"id": 65, "x": 0, "y": -20, "Title": "Hallway South Twenty", "n": 64, "s": 66, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 20 Units."},
         {"id": 66, "x": 0, "y": -21, "Title": "Hallway South TwentyOne", "n": 65, "s": 67, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 21 Units."},
         {"id": 67, "x": 0, "y": -22, "Title": "Hallway South TwentyTwo", "n": 66, "s": 68, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 22 Units."},
         {"id": 68, "x": 0, "y": -23, "Title": "Hallway South TwentyThree", "n": 67, "s": 69, "e": -1, "w": 98,
          "description": "This is just South of the Origin by 23 Units."},
         {"id": 69, "x": 0, "y": -24, "Title": "Hallway South TwentyFour", "n": 68, "s": 70, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 24 Units."},
         {"id": 70, "x": 0, "y": -25, "Title": "Hallway South TwentyFive", "n": 69, "s": -1, "e": -1, "w": -1,
          "description": "This is just South of the Origin by 25 Units."},
         # East of the Origin
         {"id": 71, "x": -11, "y": 0, "Title": "Hallway East Eleven", "n": -1, "s": -1, "e": 72, "w": 30,
          "description": "This is just East of the Origin by 11 Unit."},
         {"id": 72, "x": -12, "y": 0, "Title": "Hallway East Twelve", "n": -1, "s": -1, "e": 73, "w": 71,
          "description": "This is just East of the Origin by 12 Units."},
         {"id": 73, "x": -13, "y": 0, "Title": "Hallway East Thirteen", "n": -1, "s": -1, "e": 74, "w": 72,
          "description": "This is just East of the Origin by 13 Units."},
         {"id": 74, "x": -14, "y": 0, "Title": "Hallway East Fourteen", "n": -1, "s": 113, "e": 75, "w": 73,
          "description": "This is just East of the Origin by 14 Units."},
         {"id": 75, "x": -15, "y": 0, "Title": "Hallway East Fifteen", "n": -1, "s": -1, "e": 76, "w": 74,
          "description": "This is just East of the Origin by 15 Units."},
         {"id": 76, "x": -16, "y": 0, "Title": "Hallway East Sixteen", "n": -1, "s": 112, "e": 77, "w": 75,
          "description": "This is just East of the Origin by 16 Units."},
         {"id": 77, "x": -17, "y": 0, "Title": "Hallway East Seventeen", "n": -1, "s": -1, "e": 78, "w": 76,
          "description": "This is just East of the Origin by 17 Units."},
         {"id": 78, "x": -18, "y": 0, "Title": "Hallway East Eightteen", "n": -1, "s": -1, "e": 79, "w": 77,
          "description": "This is just East of the Origin by 18 Units."},
         {"id": 79, "x": -19, "y": 0, "Title": "Hallway East Nineteen", "n": -1, "s": -1, "e": 80, "w": 78,
          "description": "This is just East of the Origin by 19 Units."},
         {"id": 80, "x": -20, "y": 0, "Title": "Hallway East Twenty", "n": -1, "s": -1, "e": 81, "w": 79,
          "description": "This is just East of the Origin by 20 Units."},
         {"id": 81, "x": -21, "y": 0, "Title": "Hallway East TwentyOne", "n": -1, "s": -1, "e": 82, "w": 80,
          "description": "This is just East of the Origin by 21 Units."},
         {"id": 82, "x": -22, "y": 0, "Title": "Hallway East TwentyTwo", "n": -1, "s": -1, "e": 83, "w": 81,
          "description": "This is just East of the Origin by 22 Units."},
         {"id": 83, "x": -23, "y": 0, "Title": "Hallway East TwentyThree", "n": -1, "s": 115, "e": 84, "w": 82,
          "description": "This is just East of the Origin by 23 Units."},
         {"id": 84, "x": -24, "y": 0, "Title": "Hallway East TwentyFour", "n": -1, "s": -1, "e": 85, "w": 83,
          "description": "This is just East of the Origin by 24 Units."},
         {"id": 85, "x": -25, "y": 0, "Title": "Hallway East TwentyFive", "n": -1, "s": -1, "e": -1, "w": 84,
          "description": "This is just East of the Origin by 25 Units."},
         # West of the Origin
         {"id": 86, "x": 11, "y": 0, "Title": "Hallway West Eleven", "n": -1, "s": 56, "e": 40, "w": 87,
          "description": "This is just West of the Origin by 11 Unit."},
         {"id": 87, "x": 12, "y": 0, "Title": "Hallway West Twelve", "n": -1, "s": -1, "e": 85, "w": 88,
          "description": "This is just West of the Origin by 12 Units."},
         {"id": 88, "x": 13, "y": 0, "Title": "Hallway West Thirteen", "n": -1, "s": 58, "e": 86, "w": 89,
          "description": "This is just West of the Origin by 13 Units."},
         {"id": 89, "x": 14, "y": 0, "Title": "Hallway West Fourteen", "n": -1, "s": -1, "e": 87, "w": 90,
          "description": "This is just West of the Origin by 14 Units."},
         {"id": 90, "x": 15, "y": 0, "Title": "Hallway West Fifteen", "n": -1, "s": -1, "e": 89, "w": 91,
          "description": "This is just West of the Origin by 15 Units."},
         {"id": 91, "x": 16, "y": 0, "Title": "Hallway West Sixteen", "n": -1, "s": -1, "e": 90, "w": 92,
          "description": "This is just West of the Origin by 16 Units."},
         {"id": 92, "x": 17, "y": 0, "Title": "Hallway West Seventeen", "n": -1, "s": 62, "e": 91, "w": 93,
          "description": "This is just West of the Origin by 17 Units."},
         {"id": 93, "x": 18, "y": 0, "Title": "Hallway West Eightteen", "n": -1, "s": -1, "e": 92, "w": 94,
          "description": "This is just West of the Origin by 18 Units."},
         {"id": 94, "x": 19, "y": 0, "Title": "Hallway West Nineteen", "n": -1, "s": -1, "e": 93, "w": 95,
          "description": "This is just West of the Origin by 19 Units."},
         {"id": 95, "x": 20, "y": 0, "Title": "Hallway West Twenty", "n": -1, "s": -1, "e": 94, "w": 96,
          "description": "This is just West of the Origin by 20 Units."},
         {"id": 96, "x": 21, "y": 0, "Title": "Hallway West TwentyOne", "n": -1, "s": -1, "e": 95, "w": 97,
          "description": "This is just West of the Origin by 21 Units."},
         {"id": 97, "x": 22, "y": 0, "Title": "Hallway West TwentyTwo", "n": -1, "s": -1, "e": 96, "w": 98,
          "description": "This is just West of the Origin by 22 Units."},
         {"id": 98, "x": 23, "y": 0, "Title": "Hallway West TwentyThree", "n": -1, "s": 68, "e": 97, "w": 99,
          "description": "This is just West of the Origin by 23 Units."},
         {"id": 99, "x": 24, "y": 0, "Title": "Hallway West TwentyFour", "n": -1, "s": -1, "e": 98, "w": 100,
          "description": "This is just West of the Origin by 24 Units."},
         {"id": 100, "x": 25, "y": 0, "Title": "Hallway West TwentyFive", "n": -1, "s": -1, "e": 99, "w": -1,
          "description": "This is just West of the Origin by 25 Units."},

         # North West Wing
         {"id": 101, "x": 25, "y": 1, "Title": "NorthWest Labyrinth", "n": -1, "s": 100, "e": 102, "w": -1,
          "description": "You have entered the labrinth..."},

         {"id": 102, "x": 24, "y": 2, "Title": "NorthWest Labyrinth", "n": 103, "s": -1, "e": -1, "w": 101,
          "description": "You have entered the labrinth..."},

         {"id": 103, "x": 24, "y": 3, "Title": "NorthWest Labyrinth", "n": -1, "s": 102, "e": 104, "w": -1,
          "description": "TYou have entered the labrinth..."},

         {"id": 104, "x": 23, "y": 2, "Title": "NorthWest Labyrinth", "n": 105, "s": -1, "e": -1, "w": 103,
          "description": "You have entered the labrinth..."},

         {"id": 105, "x": 23, "y": 3, "Title": "NorthWest Labyrinth", "n": -1, "s": 104, "e": 106, "w": -1,
          "description": "You have entered the labrinth...."},

         {"id": 106, "x": 23, "y": 2, "Title": "NorthWest Labyrinth", "n": 107, "s": -1, "e": -1, "w": 105,
          "description": "You have entered the labrinth..."},

         {"id": 107, "x": 23, "y": 3, "Title": "NorthWest Labyrinth", "n": -1, "s": 106, "e": 108, "w": -1,
          "description": "You have entered the labrinth..."},

         {"id": 108, "x": 23, "y": 2, "Title": "NorthWest Labyrinth", "n": 109, "s": -1, "e": -1, "w": 107,
          "description": "You have entered the labrinth..."},

         {"id": 109, "x": 23, "y": 3, "Title": "NorthWest Labyrinth", "n": -1, "s": 108, "e": 110, "w": -1,
          "description": "You have entered the labrinth..."},

         {"id": 110, "x": 23, "y": 2, "Title": "NorthWest Labyrinth", "n": 111, "s": -1, "e": -1, "w": 109,
          "description": "You have entered the labrinth..."},

         {"id": 111, "x": 23, "y": 3, "Title": "NorthWest Labyrinth", "n": -1, "s": 110, "e": 55, "w": -1,
          "description": "You have entered the labrinth..."},


         # Lambda Quadrant(South East)
         {"id": 112, "x": 23, "y": 3, "Title": "Lambda Quadrant", "n": 76, "s": -1, "e": 115, "w": 113,
          "description": "You have reached the land of Firehose Pace Learning, Peer Programming, and Airtables."},

         {"id": 113, "x": 23, "y": 3, "Title": "Lambda Quadrant", "n": 74, "s": 114, "e": 112, "w": -1,
          "description": "You have reached the land of Firehose Pace Learning, Peer Programming, and Airtables."},

         {"id": 114, "x": 23, "y": 3, "Title": "Lambda Quadrant", "n": -1, "s": -1, "e": 115, "w": 113,
          "description": "You have reached the land of Firehose Pace Learning, Peer Programming, and Airtables."},

         {"id": 115, "x": 23, "y": 3, "Title": "Lambda Quadrant", "n": 112, "s": 114, "e": -1, "w": -1,
          "description": "You have reached the land of Firehose Pace Learning, Peer Programming, and Airtables."},


         # Zig Zag Maze North East
         {"id": 116, "x": 23, "y": 3, "Title": "Zig Zag Maze", "n": 5, "s": 76, "e": -1, "w": -1,
          "description": "Lots of Zigging and Zagging is happening all around you."},

         {"id": 117, "x": 23, "y": 3, "Title": "Zig Zag Maze", "n": 10, "s": 74, "e": -1, "w": 5,
          "description": "Lots of Zigging and Zagging is happening all around you."},


         # Secret Rooms








         ]


for r in rooms:
    n_to = r['n'] if 'n' in r else -1
    s_to = r['s'] if 's' in r else -1
    e_to = r['e'] if 'e' in r else -1
    w_to = r['w'] if 'w' in r else -1
    if 'x' in r:
        x = r['x']
    if 'y' in r:
        y = r['y']
    make_room = Room(id=r["id"],
                     title=r["Title"],
                     description=r["description"],

                     x=x,
                     y=y,
                     n_to=n_to,
                     s_to=s_to,
                     e_to=e_to,
                     w_to=w_to)
    make_room.save()

players = Player.objects.all()
for p in players:
    p.currentRoom = rooms[0]["id"]
    p.save()
