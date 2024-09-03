from Exercicio_4.helper.writeAJson import writeAJson


class ProductAnalyzer:
    def __init__(self, database):
        self.db = database

    def total_vendas(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$data_compra", "total_vendas": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"_id": 1}}
        ])

        writeAJson(result, "Total de Vendas")

    def produto_mais_vendido(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total_quantidade": -1}},
            {"$limit": 1}
        ])

        writeAJson(result, "Produto Mais Vendido")

    def cliente_que_mais_gastou(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$cliente_id",
                        "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total_gasto": -1}},
            {"$limit": 1}
        ])

        writeAJson(result, "Cliente Que Mais Gastou")

    def produtos_acima_uma_unidade(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.descricao", "total_quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"total_quantidade": {"$gt": 1}}},
            {"$sort": {"total_quantidade": -1}}
        ])

        writeAJson(result, "Produtos Acima de Uma Unidade")
