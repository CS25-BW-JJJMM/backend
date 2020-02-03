from django.conf import settings
from graphene_django import DjangoObjectType
from django.db import models
import graphene
from adventure.models import Room,Player
import json
class RoomType(DjangoObjectType):
    class Meta:
        model = Room
        interfaces = (graphene.Node,)

class PlayerType(DjangoObjectType):
    class Meta:
        model = Player
    
        interfaces = (graphene.Node,)

class Query(graphene.ObjectType):
    rooms = graphene.List(RoomType)
    player = graphene.List(PlayerType)
    def resolve_querry(self, info):
        Room.objects.all() and Player.objects.all()
        return JsonResponse({"rooms":Room,"players":Player})


schema = graphene.Schema(query=Query)

