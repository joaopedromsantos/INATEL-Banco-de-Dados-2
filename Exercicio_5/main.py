from Exercicio_5.cli import LivroCLI
from database import Database
from livro_model import LivroModel

db = Database(database="relatorio_5", collection="Livros")

Livros = LivroModel(database=db)

livrsoCli = LivroCLI(Livros)

livrsoCli.run()