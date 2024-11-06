from database import Database

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.197.169.135:7687", "neo4j", "stores-receipt-sonars")
# db.drop_all()
print('ok')