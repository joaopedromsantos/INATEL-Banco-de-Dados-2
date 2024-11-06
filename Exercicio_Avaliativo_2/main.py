from Exercicio_Avaliativo_2.teacher_crud import TeacherCRUD
from database import Database
from query import Query

db = Database("bolt://44.197.169.135:7687", "neo4j", "stores-receipt-sonars")
# db.drop_all()

querys = Query(db)
teacher_crud = TeacherCRUD(db)


# Questão 1
print(querys.get_name_renato())
print(querys.get_teachers_starting_with_m())
print(querys.get_all_city_names())
print(querys.get_schools_in_number_range())

# Questão 2
print(querys.get_youngest_and_oldest_teacher_year())
print(querys.get_average_city_population())
print(querys.get_city_name_with_replaced_letter())
print(querys.get_teacher_names_starting_from_third_letter())

# Questão 3
teacher_crud.create("Chris Lima", 1956, "189.052.396-66")
print(teacher_crud.read("Chris Lima"))
teacher_crud.update("Chris Lima", "162.052.777-77")
