from adventure.models import Room
import random

"""
Break things down into ambiance, function, population
"""

population = ["crowded", "sparse", "deserted"]

ambiance = ["bright", "dim", "normal", "grimy", "sterile"]

funct = ["card room", "hallway", "tunnel", "kitchen", "bar", "pool room"]

description_beginners = ["You find yourself in ",
                         "You have stumbled upon ", "You walk into "]

pop_desc = {
    "crowded": "Around you is a sea of bustling orcs and goblins.",
    "sparse": "A few goblins are milling about.",
    "deserted": "The place looks deserted"
}

ambiance_desc = {
    "bright": "The glare of the torch light is almost too much for your eyes to bear.",
    "dim": "You can barely make out any shapes in the dim light.",
    "normal": "Things look fine here.",
    "grimy": "Everything has a fine layer of dust and filth upon it.",
    "sterile": "The walls and floor are spotless"
}

functional_desc = {
    "card room": "An orc holding a deck of cards looks up and smiles as you enter.",
    "hallway": "Just a hallway, not much to do but walk on",
    "tunnel": "Water drips from the ceiling onto the muddy floor.",
    "kitchen": "An awful stench fills your nose.  Probably just roast halfling",
    "bar": "The smell of stale grog makes your stomach turn.",
    "pool room": "The felt on the pool tables is faded and splattered with dark stains"
}


def room_generator(id):
    room_population = random.choice(population)
    room_ambiance = random.choice(ambiance)
    room_function = random.choice(funct)
    room_desc_begin = random.choice(description_beginners)
    title = f"{room_population.capitalize()} {room_function}"
    description = f"{room_desc_begin} a {room_population} {room_function}. {pop_desc[room_population]} {ambiance_desc[room_ambiance]} {functional_desc[room_function]}"
    return Room(id=id, title=title, description=description)
