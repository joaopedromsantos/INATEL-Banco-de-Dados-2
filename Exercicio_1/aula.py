from professor import Professor


class Aula:
    def __init__(self, professor: Professor, assunto: str, alunos: list = None):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos if alunos else []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')
        for aluno in self.alunos:
            aluno.presenca()
