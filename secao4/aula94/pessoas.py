# criando classe Pessoa
from datetime import datetime

class Pessoa():

    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, sexo, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.sexo = sexo
        variavel = "Variavel qualquer"
        #print(variavel)

    def falar(self, assunto):
        self.assunto = assunto

        if self.comendo:
            if self.sexo == 'F':
                print("Não pode falar comendo. Peça para ela parar_comer.")
                return
            elif self.sexo == 'M':
                print("Não pode falar comendo. Peça para ele parar_comer.")
                return

        if self.falando:
            print("Já está falando.")
            return

        print(f"{self.nome} está falando sobre {self.assunto}!")
        self.falando = True

    def comer(self, alimento):
        #self.alimento = alimento
        if self.comendo:
            print(f"{self.nome} já está comendo.")
            return

        print(f"{self.nome} está comendo {alimento}!")
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.comendo} não está comendo!!!")
            return

        print(f"{self.nome} parou de comer.")
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade