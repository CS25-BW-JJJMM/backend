from django.db import models
from random import seed , randint
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid




class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(max_length=500, default="DEFAULT DESCRIPTION")
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)
    items = models.CharField(max_length=100, default="DEFAULT TITLE")
    monsters = models.IntegerField(default=0)
    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.id
        try:
            destinationRoom = Room.objects.get(id=destinationRoomID)
        except Room.DoesNotExist:
            print("That room does not exist")
        else:
            if direction == "n":
                self.n_to = destinationRoomID
            elif direction == "s":
                self.s_to = destinationRoomID
            elif direction == "e":
                self.e_to = destinationRoomID
            elif direction == "w":
                self.w_to = destinationRoomID
            else:
                print("Invalid direction")
                return
            self.save()
    def playerNames(self, currentPlayerID):
        return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]
    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = user.name
    currentRoom = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    def initialize(self):
        if self.currentRoom == 0:
            self.name = name
            self.currentRoom = Room.objects.first().id
            self.save()
    def room(self):
        try:
            return Room.objects.get(id=self.currentRoom)
        except Room.DoesNotExist:
            self.initialize()
            
            return self.room()
class Monster(models.Model):
    name = models.CharField(max_length=60,default="DEFAULT NAME")
    description = models.CharField(max_length=500,default="DEFAULT DESCRIPTION")
    current_room = models.IntegerField(default=0)
    def rand():
        for _ in range(1):
            value = randint(0,100)
        print(value)

    def initialize(self):
        if self.current_room != 101:
            self.name = name
            self.description = description
            self.current_room = Monster.rand()
            self.save()
        
        self.save()
    def spawn(self):
        if current_room != 101:
                current_room = Monster.rand()
                return current_room
    def room(self):
        try:
            return Room.objects.get(id=self.current_room)
        except Room.DoesNotExist:
            self.initialize()
            
            return self.room()
            self.save()
    

@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()



def rand():
    for _ in range(1):
        value = randint(0,100)
    print(value)

    

    
   
    

