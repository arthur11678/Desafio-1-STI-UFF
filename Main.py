from Consulta import Consulta                                   #Importa a classe Consulta da biblioteca Consulta
from Cadastro import Cadastro                                   #Importa a classe Cadastro da biblioteca Cadastro
matricula_aluno = input("\nDigite sua matricula\n")             #Pergunta ao usuário sua matrícula
consulta = Consulta(matricula_aluno, None)                      #Instancia a classe Consulta
aluno = Consulta.alunopodecriaruffmail(consulta)                #Chama o método da classe Consulta que verifica se o aluno pode criar o uffmail, caso haja algum erro ele retorna o número do erro
if aluno == -1:                                                 #As próximas são executadas para tratamento de erros
    print("O aluno ja possui UFFmail")
elif aluno == -2:
    print("A matricula do alunos consta como inativa")
elif aluno == -3:
    print("A matricula nao foi encontrada no banco de dados")
else:
    Cadastro(aluno, None).geraropecoes()                        #Gera as opções de email, printa a confirmação e edita o arquivo CVS100
