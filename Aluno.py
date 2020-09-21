
class Aluno:
    def __init__(self, nome, matricula, telefone, email, uffmail, status):
        self.nome = nome
        self.matricula = matricula
        self.telefone = telefone
        self.email = email
        self.uffmail = uffmail
        self.status = status

    def getnome(self):
        return self.nome

    def getmatricula(self):
        return self.matricula

    def gettelefone(self):
        return self.telefone

    def getemail(self):
        return self.email

    def getuffmail(self):
        return self.uffmail

    def getstatus(self):
        return self.status

    def setnome(self, nome):
        self.nome = nome

    def settelefone(self, telefone):
        self.telefone = telefone

    def setemail(self, email):
        self.email = email

    def setuffmail(self, uffmail):
        self.uffmail = uffmail

    def setstatus(self, status):
        self.status = status
