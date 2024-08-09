class Professor:
    def __init__(self, nome: str):
        self.nome = nome

    def ministrar_aula(self, assunto):
        return print(f'O professor {self.nome} está ministrando uma aula sobre {assunto}.\n')
