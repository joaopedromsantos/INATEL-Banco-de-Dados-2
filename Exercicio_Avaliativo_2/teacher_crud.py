class TeacherCRUD:
    def __init__(self, db):
        self.db = db

    def create(self, name, ano_nasc, cpf):
        query = """
        CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
        return f"Teacher '{name}' criado com sucesso."

    def read(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return results[0] if results else None

    def update(self, name, newCpf):
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = $newCpf
        RETURN t.name AS name, t.cpf AS updatedCpf
        """
        parameters = {"name": name, "newCpf": newCpf}
        self.db.execute_query(query, parameters)
        return f"CPF do Teacher '{name}' atualizado para {newCpf}."

    def delete(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        DELETE t
        """
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        return f"Teacher '{name}' deletado com sucesso."
