from Aluno import Aluno
import csv


class Consulta:

    def __init__(self, matricula, aluno):
        self.matricula = matricula
        self.aluno = aluno

    def setaluno(self, aluno):
        self.aluno = aluno

    def alunopodecriaruffmail(self):
        with open('alunos.csv', 'r') as alunos:
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
