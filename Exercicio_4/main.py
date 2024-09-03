from database import Database
from helper.writeAJson import writeAJson
from product_analyzer import ProductAnalyzer

db = Database(database="mercado", collection="compras")
db.resetDatabase()

Prod = ProductAnalyzer(db)

Prod.total_vendas()
Prod.produto_mais_vendido()
Prod.cliente_que_mais_gastou()
Prod.produtos_acima_uma_unidade()
