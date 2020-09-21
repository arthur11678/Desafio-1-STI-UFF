import csv


class Cadastro:

    def __init__(self, aluno, opcoes):
        self.aluno = aluno
        self.opcoes = opcoes

    def escrevercsv(self):
        linhas_arq = list()
        with open('alunos.csv', 'r') as arquivo:
            alunos_csv = csv.DictReader(arquivo)
            for linha in alunos_csv:
                if self.aluno.matricula == linha['matricula']:
                    linha['uffmail'] = self.aluno.uffmail
                linhas_arq.append(linha)
        print(linhas_arq)
        cabecalho = ['nome', 'matricula', 'telefone', 'email', 'uffmail', 'status']
        with open('alunos.csv', 'w') as arquivo:
            escrever = csv.DictWriter(arquivo, fieldnames= cabecalho)
            escrever.writeheader()
            escrever.writerows(linhas_arq)

    def escolheropcoes(self, nome):

        print("{}, por favor escolha uma das opcoes abaixo para o seu UFFmail\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n".format(nome[0], self.opcoes[0], self.opcoes[1], self.opcoes[2], self.opcoes[3], self.opcoes[4]))
        opcao = int(input())
        self.aluno.uffmail = self.opcoes[opcao-1]

    def printarconfirmacao(self):
        print("A criação de seu e-mail ({}) será feita nos próximos minutos.Um SMS foi enviado para {} com a sua senha de acesso.".format(self.aluno.uffmail, self.aluno.telefone))

    def geraropecoes(self):
        const = "@id.uff.br"
        nome = self.aluno.nome.split()
        opcao1 = nome[0] + "_" + nome[1] + const
        opcao2 = nome[0] + nome[1][0] + nome[2][0] + const
        opcao3 = nome[0] + nome[2] + const
        opcao4 = nome[0][0] + nome[2] + const
        opcao5 = nome[0][0] + nome[1] + nome[2] + const
        self.opcoes = opcao1.lower(), opcao2.lower(), opcao3.lower(), opcao4.lower(), opcao5.lower()
        self.escolheropcoes(nome)
        self.printarconfirmacao()
        self.escrevercsv()
