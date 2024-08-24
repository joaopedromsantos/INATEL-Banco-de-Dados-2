from database import Database
from helper.writeAJson import writeAJson


class Pokedex:
    def __init__(self, db: Database):
        self.database = db

    def find_type_fire(self):
        pokemons = db.collection.find({"type":"Fire"})
        writeAJson(pokemons, "find_type_fire")

    def find_egg_origin(self):
        pokemons = db.collection.find({"egg": {"$ne": "Not in Eggs"}})
        writeAJson(pokemons, "find_egg_origin")

    def chance_to_spawn(self):
        pokemons = db.collection.find({"spawn_chance": {"$gt": 0.4, "$lt": 0.5}})
        writeAJson(pokemons, "chance_to_spawn")

    def weaknesses_ground(self):
        pokemons = db.collection.find({"weaknesses": "Ground"})
        writeAJson(pokemons, "weaknesses_ground")

    def id_greater_than_100(self):
        pokemons = db.collection.find({"id": {"$gt": 100}})
        writeAJson(pokemons, "id_greater_than_100")


db = Database(database="pokedex", collection="pokemons")

pokedex = Pokedex(db)

pokedex.find_type_fire()
pokedex.find_egg_origin()
pokedex.chance_to_spawn()
pokedex.weaknesses_ground()
pokedex.id_greater_than_100()

