from database import Database
from game_database import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.83.65.33", "neo4j", "stocks-catchers-swords")
db.drop_all()

# Cria uma instância da classe GameDatabase usando a instância db
game_db = GameDatabase(db)

game_db.create_player("1", "João")
game_db.create_player("2", "Maria")
game_db.create_player("3", "José")

game_db.create_match("3000", ["1", "2"], "1 win")
game_db.create_match("4000", ["2", "3"], "2 win")
game_db.create_match("5000", ["1", "3"], "3 win")


game_db.update_player("1", "Pedro")

historia_pedro = game_db.get_player_history("1")
print("Histórico de partidas de Pedro:")
for partida in historia_pedro:
    print(f"ID da Partida: {partida['id']}, Resultado: {partida['result']}")

game_db.delete_player("3")
game_db.delete_match("5000")

# Fechando a conexão com o banco de dados
db.close()
