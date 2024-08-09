from aluno import Aluno
from aula import Aula
from professor import Professor

professor = Professor("Gabriel")

aluno1 = Aluno("Roberto")
aluno2 = Aluno("Lucas")
aluno3 = Aluno("Marta")

aula = Aula(professor, "Cálculo 2")

aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno3)

professor.ministrar_aula("Cálculo 2")

aula.listar_presenca()


