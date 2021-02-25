"""
                                                        ANOTAÇÕES

            - Quando se coloca self.[nome_qualquer] = [nome_parametro], vc está criando uma variavel e a associando ao
              parametro. Usualmente, recebem o msm nome.

            - A "variavel" so está disponível no escopo do __init__.

            - As variaveis criadas no metodo __init__ estão disponíveis por todo o código.

            - self referencia a propria instancia que o chama

            - Metodo __init__ SEMPRE é chamado quando a classe é instanciada

            - Metodos sao funcoes dentro de aula92

            - O pacote datetime foi criado para pegar o ano_atual direto do sistema, p/ sempre ficar atualizado.

            - É possível criar as variáveis da CLASSE e não apenas variáveis de INSTÂNCIAS
"""
# ---------------------------------------------------------------------------------------------------------------------

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