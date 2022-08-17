class aluno:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = 0.0

    def calcula_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media

    def dados(self):
        print('Nome: ', self.nome)
        print('Nota 1: ', self.nota1)
        print('Nota 2: ', self.nota2)
        print('Média: ', self.media)

    def resultado(self):
        if self.media >= 6.0:
            print('Aprovado')
        else:
            print('Reprovado')

aluno1 = aluno("Gabriel", 7.0, 8.0)
media = aluno1.calcula_media()
aluno1.dados()
aluno1.resultado()
print('\n')
aluno2 = aluno("Lorenzo", 9.0, 10.0)
media = aluno2.calcula_media()
aluno2.dados()
aluno2.resultado()