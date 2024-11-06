class Query:
    def __init__(self, db):
        self.db = db

    def get_name_renato(self):
        query = "MATCH (t:Teacher {name: 'Renzo'}) RETURN t.ano_nasc AS year, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [{"Year of birth": results[0]["year"], "CPF": results[0]["cpf"]}]

    def get_teachers_starting_with_m(self):
        query = "MATCH (t:Teacher) WHERE t.name STARTS WITH 'M' RETURN t.name AS name, t.cpf AS cpf"
        results = self.db.execute_query(query)
        return [{"Name": record["name"], "CPF": record["cpf"]} for record in results]

    def get_all_city_names(self):
        query = "MATCH (c:City) RETURN c.name AS city_name"
        results = self.db.execute_query(query)
        return [{"City": record["city_name"]} for record in results]

    def get_schools_in_number_range(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name AS school_name, s.address AS address, s.number AS number
        """
        results = self.db.execute_query(query)
        return [{"School": record["school_name"], "Address": record["address"], "Number": record["number"]} for record in results]

    def get_youngest_and_oldest_teacher_year(self):
        query = """
        MATCH (t:Teacher)
        RETURN MAX(t.ano_nasc) AS young, MIN(t.ano_nasc) AS oldest
        """
        results = self.db.execute_query(query)
        return [{"Young": results[0]["young"], "Oldest": results[0]["oldest"]}]

    def get_average_city_population(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS average_population"
        results = self.db.execute_query(query)
        return [{"Average Population": results[0]["average_population"]}]

    def get_city_name_with_replaced_letter(self):
        query = """
        MATCH (c:City {cep: '37540-000'})
        RETURN REPLACE(c.name, 'a', 'A') AS modified_name
        """
        results = self.db.execute_query(query)
        return [{"Modified Name": results[0]["modified_name"]}]

    def get_teacher_names_starting_from_third_letter(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 2) AS name_start, t.name AS full_name"
        results = self.db.execute_query(query)
        return [{f"Teacher {record["full_name"]}": record["name_start"]} for record in results]
