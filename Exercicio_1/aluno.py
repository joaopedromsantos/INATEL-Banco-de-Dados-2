class Aluno:
    def __init__(self, nome: str):
        self.nome = nome

    def presenca(self):
        return print(f'O aluno {self.nome} está presente.')
