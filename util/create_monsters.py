from adventure.models import Player, Monster

Monster.objects.all().delete()

monsters = [{"id":0,"name":"Big_Ugly", "description": "A big ugly monster" ,"currentRoom":None},
           {"id":1,",name":"Big_Ugly", "description": "A big ugly monster" ,"currentRoom":None},
           ]


monsters=Monster.objects.all()

for m in monsters:
    m.save()   
    print("m")


