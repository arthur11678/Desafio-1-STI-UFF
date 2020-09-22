from Aluno import Aluno
import csv


class Consulta:                                                                                                                                            #Cria uma classe Consulta

    def __init__(self, matricula, aluno):                                                                                                                  #Constroi a classe Consulta
        self.matricula = matricula
        self.aluno = aluno

    def alunopodecriaruffmail(self):                                                                                                                        #Define o método quem verifica se o aluno pode crair o UFFmail
        with open('alunos.csv', 'r') as alunos:                                                                                                             #O método retorna um erro caso não seja possivel criar o UFFmail
            alunos_csv = csv.DictReader(alunos)
            matriculaIsmissing = True
            for linha in alunos_csv:
                if self.matricula == linha['matricula']:
                    matriculaIsmissing = False
                    if linha['status'] == 'Ativo':
                        if linha['uffmail'] == '':
                            aluno = Aluno(linha['nome'], linha['matricula'], linha['telefone'], linha['email'], linha['uffmail'], linha['status'])
                            return aluno
                        else:
                            return -1
                    else:
                        return -2
            if matriculaIsmissing:
                return -3
