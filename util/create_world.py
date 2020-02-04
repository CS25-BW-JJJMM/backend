from django.contrib.auth.models import User
from adventure.models import Player, Room

Room.objects.all().delete()
          # Origin 

rooms = [{"id" : 0, "x" : 0, "y" : 0, "Title" : "Origin", "n" : 0, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is the Origin, You may Travel North, West, East, Or South."}, 
        
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
           # North of the Origin
         {"id" : 41, "x" : 0, "y" : 11, "Title" : "Hallway North Eleven", "n" : 11, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 11 Unit."},
         {"id" : 42, "x" : 0, "y" : 12, "Title" : "Hallway North Twelve", "n" : 12, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 12 Units."},
         {"id" : 43, "x" : 0, "y" : 13, "Title" : "Hallway North Thirteen", "n" : 13, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 13 Units."},
         {"id" : 44, "x" : 0, "y" : 14, "Title" : "Hallway North Fourteen", "n" : 14, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 14 Units."},
         {"id" : 45, "x" : 0, "y" : 15, "Title" : "Hallway North Fifteen", "n" : 15, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 15 Units."},
         {"id" : 46, "x" : 0, "y" : 16, "Title" : "Hallway North Sixteen", "n" : 16, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 16 Units."},
         {"id" : 47, "x" : 0, "y" : 17, "Title" : "Hallway North Seventeen", "n" : 17, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 17 Units."},
         {"id" : 48, "x" : 0, "y" : 18, "Title" : "Hallway North Eightteen", "n" : 18, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 18 Units."},
         {"id" : 49, "x" : 0, "y" : 19, "Title" : "Hallway North Nineteen", "n" : 19, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 19 Units."},
         {"id" : 50, "x" : 0, "y" : 20, "Title" : "Hallway North Twenty", "n" : 20, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 20 Units."},
          {"id" : 51, "x" : 0, "y" : 21, "Title" : "Hallway North TwentyOne", "n" : 21, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 21 Units."},
         {"id" : 52, "x" : 0, "y" : 22, "Title" : "Hallway North TwentyTwo", "n" : 22, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 22 Units."},
         {"id" : 53, "x" : 0, "y" : 23, "Title" : "Hallway North TwentyThree", "n" : 23, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 23 Units."},
         {"id" : 54, "x" : 0, "y" : 24, "Title" : "Hallway North TwentyFour", "n" : 24, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 24 Units."},
         {"id" : 55, "x" : 0, "y" : 25, "Title" : "Hallway North TwentyFive", "n" : 25, "s" : 0, "e" : 0, "w" : 0,
          "description" : "This is just North of the Origin by 25 Units."},
          # South of the Origin
         {"id" : 56, "x" : 0, "y" : -11, "Title" : "Hallway South Eleven", "n" : 0, "s" : 11, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 11 Unit."},
         {"id" : 57, "x" : 0, "y" : -12, "Title" : "Hallway South Twelve", "n" : 0, "s" : 12, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 12 Units."},
         {"id" : 58, "x" : 0, "y" : -13, "Title" : "Hallway South Thirteen", "n" : 0, "s" : 13, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 13 Units."},
         {"id" : 59, "x" : 0, "y" : -14, "Title" : "Hallway South Fourteen", "n" : 0, "s" : 14, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 14 Units."},
         {"id" : 60, "x" : 0, "y" : -15, "Title" : "Hallway South Fifteen", "n" : 0, "s" : 15, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 15 Units."},
         {"id" : 61, "x" : 0, "y" : -16, "Title" : "Hallway South Sixteen", "n" : 0, "s" : 16, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 16 Units."},
         {"id" : 62, "x" : 0, "y" : -17, "Title" : "Hallway South Seventeen", "n" : 0, "s" : 17, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 17 Units."},
         {"id" : 63, "x" : 0, "y" : -18, "Title" : "Hallway South Eightteen", "n" : 0, "s" : 18, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 18 Units."},
         {"id" : 64, "x" : 0, "y" : -19, "Title" : "Hallway South Nineteen", "n" : 0, "s" : 19, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 19 Units."},
         {"id" : 65, "x" : 0, "y" : -20, "Title" : "Hallway South Twenty", "n" : 0, "s" : 20, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 20 Units."},
          {"id" : 66, "x" : 0, "y" : -21, "Title" : "Hallway South TwentyOne", "n" : 0, "s" : 21, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 21 Units."},
         {"id" : 67, "x" : 0, "y" : -22, "Title" : "Hallway South TwentyTwo", "n" : 0, "s" : 22, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 22 Units."},
         {"id" : 68, "x" : 0, "y" : -23, "Title" : "Hallway South TwentyThree", "n" : 0, "s" : 23, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 23 Units."},
         {"id" : 69, "x" : 0, "y" : -24, "Title" : "Hallway South TwentyFour", "n" : 0, "s" : 24, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 24 Units."},
         {"id" : 70, "x" : 0, "y" : -25, "Title" : "Hallway South TwentyFive", "n" : 0, "s" : 25, "e" : 0, "w" : 0,
          "description" : "This is just South of the Origin by 25 Units."},
          # East of the Origin
         {"id" : 71, "x" : -11, "y" : 0, "Title" : "Hallway East Eleven", "n" : 0, "s" : 0, "e" : 11, "w" : 0,
          "description" : "This is just East of the Origin by 11 Unit."},
         {"id" : 72, "x" : -12, "y" : 0, "Title" : "Hallway East Twelve", "n" : 0, "s" : 0, "e" : 12, "w" : 0,
          "description" : "This is just East of the Origin by 12 Units."},
         {"id" : 73, "x" : -13, "y" : 0, "Title" : "Hallway East Thirteen", "n" : 0, "s" : 0, "e" : 13, "w" : 0,
          "description" : "This is just East of the Origin by 13 Units."},
         {"id" : 74, "x" : -14, "y" : 0, "Title" : "Hallway East Fourteen", "n" : 0, "s" : 0, "e" : 14, "w" : 0,
          "description" : "This is just East of the Origin by 14 Units."},
         {"id" : 75, "x" : -15, "y" : 0, "Title" : "Hallway East Fifteen", "n" : 0, "s" : 0, "e" : 15, "w" : 0,
          "description" : "This is just East of the Origin by 15 Units."},
         {"id" : 76, "x" : -16, "y" : 0, "Title" : "Hallway East Sixteen", "n" : 0, "s" : 0, "e" : 16, "w" : 0,
          "description" : "This is just East of the Origin by 16 Units."},
         {"id" : 77, "x" : -17, "y" : 0, "Title" : "Hallway East Seventeen", "n" : 0, "s" : 0, "e" : 17, "w" : 0,
          "description" : "This is just East of the Origin by 17 Units."},
         {"id" : 78, "x" : -18, "y" : 0, "Title" : "Hallway East Eightteen", "n" : 0, "s" : 0, "e" : 18, "w" : 0,
          "description" : "This is just East of the Origin by 18 Units."},
         {"id" : 79, "x" : -19, "y" : 0, "Title" : "Hallway East Nineteen", "n" : 0, "s" : 0, "e" : 19, "w" : 0,
          "description" : "This is just East of the Origin by 19 Units."},
         {"id" : 80, "x" : -20, "y" : 0, "Title" : "Hallway East Twenty", "n" : 0, "s" : 0, "e" : 20, "w" : 0,
          "description" : "This is just East of the Origin by 20 Units."},
          {"id" : 81, "x" : -21, "y" : 0, "Title" : "Hallway East TwentyOne", "n" : 0, "s" : 0, "e" : 21, "w" : 0,
          "description" : "This is just East of the Origin by 21 Units."},
         {"id" : 82, "x" : -22, "y" : 0, "Title" : "Hallway East TwentyTwo", "n" : 0, "s" : 0, "e" : 22, "w" : 0,
          "description" : "This is just East of the Origin by 22 Units."},
         {"id" : 83, "x" : -23, "y" : 0, "Title" : "Hallway East TwentyThree", "n" : 0, "s" : 0, "e" : 23, "w" : 0,
          "description" : "This is just East of the Origin by 23 Units."},
         {"id" : 84, "x" : -24, "y" : 0, "Title" : "Hallway East TwentyFour", "n" : 0, "s" : 0, "e" : 24, "w" : 0,
          "description" : "This is just East of the Origin by 24 Units."},
         {"id" : 85, "x" : -25, "y" : 0, "Title" : "Hallway East TwentyFive", "n" : 0, "s" : 0, "e" : 25, "w" : 0,
          "description" : "This is just East of the Origin by 25 Units."},
          # West of the Origin
         {"id" : 86, "x" : 11, "y" : 0, "Title" : "Hallway West Eleven", "n" : 0, "s" : 0, "e" : 0, "w" : 11,
          "description" : "This is just West of the Origin by 11 Unit."},
         {"id" : 87, "x" : 12, "y" : 0, "Title" : "Hallway West Twelve", "n" : 0, "s" : 0, "e" : 0, "w" : 12,
          "description" : "This is just West of the Origin by 12 Units."},
         {"id" : 88, "x" : 13, "y" : 0, "Title" : "Hallway West Thirteen", "n" : 0, "s" : 0, "e" : 0, "w" : 13,
          "description" : "This is just West of the Origin by 13 Units."},
         {"id" : 89, "x" : 14, "y" : 0, "Title" : "Hallway West Fourteen", "n" : 0, "s" : 0, "e" : 0, "w" : 14,
          "description" : "This is just West of the Origin by 14 Units."},
         {"id" : 90, "x" : 15, "y" : 0, "Title" : "Hallway West Fifteen", "n" : 0, "s" : 0, "e" : 0, "w" : 15,
          "description" : "This is just West of the Origin by 15 Units."},
         {"id" : 91, "x" : 16, "y" : 0, "Title" : "Hallway West Sixteen", "n" : 0, "s" : 0, "e" : 0, "w" : 16,
          "description" : "This is just West of the Origin by 16 Units."},
         {"id" : 92, "x" : 17, "y" : 0, "Title" : "Hallway West Seventeen", "n" : 0, "s" : 0, "e" : 0, "w" : 17,
          "description" : "This is just West of the Origin by 17 Units."},
         {"id" : 93, "x" : 18, "y" : 0, "Title" : "Hallway West Eightteen", "n" : 0, "s" : 0, "e" : 0, "w" : 18,
          "description" : "This is just West of the Origin by 18 Units."},
         {"id" : 94, "x" : 19, "y" : 0, "Title" : "Hallway West Nineteen", "n" : 0, "s" : 0, "e" : 0, "w" : 19,
          "description" : "This is just West of the Origin by 19 Units."},
         {"id" : 95, "x" : 20, "y" : 0, "Title" : "Hallway West Twenty", "n" : 0, "s" : 0, "e" : 0, "w" : 20,
          "description" : "This is just West of the Origin by 20 Units."},
          {"id" : 96, "x" : 21, "y" : 0, "Title" : "Hallway West TwentyOne", "n" : 0, "s" : 0, "e" : 0, "w" : 21,
          "description" : "This is just West of the Origin by 21 Units."},
         {"id" : 97, "x" : 22, "y" : 0, "Title" : "Hallway West TwentyTwo", "n" : 0, "s" : 0, "e" : 0, "w" : 22,
          "description" : "This is just West of the Origin by 22 Units."},
         {"id" : 98, "x" : 23, "y" : 0, "Title" : "Hallway West TwentyThree", "n" : 0, "s" : 0, "e" : 0, "w" : 23,
          "description" : "This is just West of the Origin by 23 Units."},
         {"id" : 99, "x" : 24, "y" : 0, "Title" : "Hallway West TwentyFour", "n" : 0, "s" : 0, "e" : 0, "w" : 24,
          "description" : "This is just West of the Origin by 24 Units."},
         {"id" : 100, "x" : 25, "y" : 0, "Title" : "Hallway West TwentyFive", "n" : 0, "s" : 0, "e" : 0, "w" : 25,
          "description" : "This is just West of the Origin by 25 Units."},

]
for r in rooms:
  n_to = r['n'] if 'n' in r else -1
  s_to = r['s'] if 's' in r else -1
  e_to = r['e'] if 'e' in r else -1
  w_to = r['w'] if 'w' in r else -1
  if 'x' in r: x = r['x']
  if 'y' in r: y = r['y']
  make_room = Room(id=r["id"], 
                   title=r["Title"], 
                   description=r["description"], 
                   x=x, 
                   y=y, 
                   n_to=n_to , 
                   s_to=s_to, 
                   e_to=e_to, 
                   w_to=w_to)
  
  make_room.save()

players=Player.objects.all()
for p in players:
  p.currentRoom=rooms[0]["id"]
  p.save()