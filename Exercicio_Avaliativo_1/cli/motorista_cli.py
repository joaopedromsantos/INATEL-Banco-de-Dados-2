from ..dao.motorista_dao import MotoristaDao
from ..models.corrida import Corrida
from ..models.passageiro import Passageiro


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")
                
                
class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_dao: MotoristaDao):
        super().__init__()
        self.motorista_model = motorista_dao
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        corridas = []

        while True:
            print("Apresente informações de um passageiro e sobre a corrida")
            print("\n------PASSAGEIRO------")
            nome = input("Nome: ")
            documento = input("Documento: ")
            passageiro = Passageiro(nome, documento).to_dict()

            print("\n------CORRIDA------")
            nota = int(input("Nota: "))
            distancia = float(input("Distância: "))
            valor = float(input("Valor: "))
            corrida = Corrida(nota=nota, distancia=distancia, valor=valor, passageiro=passageiro)

            # Adicionando a corrida na lista
            corridas.append(corrida)

            print("Deseja adicionar mais um passageiro e uma corrida?")
            response = input("Resposta: S/N\n")
            if response.lower() == "n":
                break

        print("Apresente informações do motorista")
        print("\n------MOTORISTA------")
        nota = int(input("Nota: "))

        self.motorista_model.create_motorista(nota=nota, corridas=corridas)

    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        if motorista:
            print(f"Nota: {motorista.get('nota')}")
            print("------")
            for index, corrida in enumerate(motorista.get('corridas')):
                print(f"Corrida {index}: ")
                print(f"-- Nota: {corrida.get('nota')}")
                print(f"-- Distância: {corrida.get('distancia')}")
                print(f"-- Valor: {corrida.get('valor')}")
                print(f"-- -- Passageiro:")
                print(f"Nome: {corrida.get('passageiro').get('nome')}")
                print(f"Documento: {corrida.get('passageiro').get('documento')}")
                print("------")

    def update_motorista(self):
        id = input("Enter the id: ")
        corridas = []

        while True:
            print("Apresente informações de um passageiro e sobre a corrida")
            print("\n------PASSAGEIRO------")
            nome = input("Nome: ")
            documento = input("Documento: ")
            passageiro = Passageiro(nome, documento).to_dict()

            print("\n------CORRIDA------")
            nota = int(input("Nota: "))
            distancia = float(input("Distância: "))
            valor = float(input("Valor: "))
            corrida = Corrida(nota=nota, distancia=distancia, valor=valor, passageiro=passageiro)

            # Adicionando a corrida na lista
            corridas.append(corrida)

            print("Deseja adicionar mais um passageiro e uma corrida?")
            response = input("Resposta: S/N\n")
            if response.lower() == "n":
                break

        print("Apresente informações do motorista")
        print("\n------MOTORISTA------")
        nota = int(input("Nota: "))
        self.motorista_model.update_motorista(id=id, nota=nota, corridas=corridas)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()

