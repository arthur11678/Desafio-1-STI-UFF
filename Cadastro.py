import csv


class Cadastro:                                                                             #Cria a classe Cadastro

    def __init__(self, aluno, opcoes):                                                      #Constroi a classe Cadastro
        self.aluno = aluno
        self.opcoes = opcoes

    def escrevercsv(self):                                                                  #Cria o método para editar o CSV
        linhas_arq = list()
        with open('alunos.csv', 'r') as arquivo:                                            #Abre o CSV em mode de leitura e armazena seu conteudo na variavel 'alunos_csv'
            alunos_csv = csv.DictReader(arquivo)
            for linha in alunos_csv:                                                        #Executa um for comparando o conteudo das linhas do arquivo com a matricula do aluno a ser escrito no CSV
                if self.aluno.matricula == linha['matricula']:
                    linha['uffmail'] = self.aluno.uffmail                                   #Escreve o UFFmail do usuario na linha                                                   #Arnazena todas as linha, ja atualizadas, numa nova variavel
        cabecalho = ['nome', 'matricula', 'telefone', 'email', 'uffmail', 'status']         #Cria um cabeçalho para o arquivo CVS
        with open('alunos.csv', 'w') as arquivo:                                            #Abre o arquivo em modo de escrita 
            escrever = csv.DictWriter(arquivo, fieldnames= cabecalho)                       
            escrever.writeheader()
            escrever.writerows(linhas_arq)                                                  #Escreve as linhas no arquivo

    def escolheropcoes(self, nome):                                                         #Define o metodo que printa os possiveis UFFmails e recebe a escolha do usuario

        print("{}, por favor escolha uma das opcoes abaixo para o seu UFFmail\n1 - {}\n2 - {}\n3 - {}\n4 - {}\n5 - {}\n".format(nome[0], self.opcoes[0], self.opcoes[1], self.opcoes[2], self.opcoes[3], self.opcoes[4]))
        opcao = int(input())
        self.aluno.uffmail = self.opcoes[opcao-1]

    def printarconfirmacao(self):                                                           #Printa a confirmação de que o UFFmail sera criado
        print("A criação de seu e-mail ({}) será feita nos próximos minutos.Um SMS foi enviado para {} com a sua senha de acesso.".format(self.aluno.uffmail, self.aluno.telefone))

    def geraropecoes(self):                                                                 #Gera as opçoes de UFFmail para o usuario
        const = "@id.uff.br"
        nome = self.aluno.nome.split()
        opcao1 = nome[0] + "_" + nome[1] + const
        opcao2 = nome[0] + nome[1][0] + nome[2][0] + const
        opcao3 = nome[0] + nome[2] + const
        opcao4 = nome[0][0] + nome[2] + const
        opcao5 = nome[0][0] + nome[1] + nome[2] + const
        self.opcoes = opcao1.lower(), opcao2.lower(), opcao3.lower(), opcao4.lower(), opcao5.lower()
        self.escolheropcoes(nome)                                                           #Chama os metodos que escolhe a opção, printa a confirmação e escreve no CSV
        self.printarconfirmacao()
        self.escrevercsv()
