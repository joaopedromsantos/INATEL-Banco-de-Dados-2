from Exercicio_Avaliativo_1.cli.motorista_cli import MotoristaCLI
from Exercicio_Avaliativo_1.dao.motorista_dao import MotoristaDao
from database import Database
from models.corrida import Corrida
from models.passageiro import Passageiro
from models.motorista import Motorista

passageiro_1 = Passageiro(nome="Lucas Emanuel", documento="123.456.765-09")
corrida_1 = Corrida(nota=8, distancia=12.6, valor=48.67, passageiro=passageiro_1)

passageiro_2 = Passageiro(nome="Evelyn Carmen", documento="108.876.234-08")
corrida_2 = Corrida(nota=10, distancia=3.4, valor=12.20, passageiro=passageiro_2)

motorista = Motorista(nota=9, corridas=[corrida_1, corrida_2])

db = Database(database="MyDatabase", collection="Motoristas")

crud_motorista = MotoristaDao(db)

interface_crud_motorista = MotoristaCLI(crud_motorista)

interface_crud_motorista.run()
