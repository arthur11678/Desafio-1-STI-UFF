from Consulta import Consulta
from Cadastro import Cadastro
matricula_aluno = input("\nDigite sua matricula\n")
consulta = Consulta(matricula_aluno, None)
aluno = Consulta.alunopodecriaruffmail(consulta)
if aluno == -1:
    print("O aluno ja possui UFFmail")
elif aluno == -2:
    print("A matricula do alunos consta como inativa")
elif aluno == -3:
    print("A matricula nao foi encontrada no banco de dados")
else:
    Cadastro(aluno, None).geraropecoes()
