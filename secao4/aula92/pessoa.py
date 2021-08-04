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
from datetime import datetime

"""
- Pessoa: classe que vai ter os objetos de uma pessoa como o noem, idade, bem como os metodos
- falar: metodo da classe pessoa
"""
# class Pessoa:
#
#     ano_atual = int(datetime.strftime(datetime.now(), '%Y'))
#
#     def __init__(self, nome, idade, sexo, comendo=False, falando=False):
#         self.nome = nome
#         self.idade = idade
#         self.comendo = comendo
#         self.falando = falando
#         self.sexo = sexo
#         variavel = "Variavel qualquer"
#         #print(variavel)
#
#     def falar(self, assunto):
#         self.assunto = assunto
#
#         if self.comendo:
#             if self.sexo == 'F':
#                 print("Não pode falar comendo. Peça para ela parar_comer.")
#                 return
#             elif self.sexo == 'M':
#                 print("Não pode falar comendo. Peça para ele parar_comer.")
#                 return
#
#         if self.falando:
#             print("Já está falando.")
#             return
#
#         print(f"{self.nome} está falando sobre {self.assunto}!")
#         self.falando = True
#
#     def comer(self, alimento):
#         #self.alimento = alimento
#         if self.comendo:
#             print(f"{self.nome} já está comendo.")
#             return
#
#         print(f"{self.nome} está comendo {alimento}!")
#         self.comendo = True
#
#     def parar_comer(self):
#         if not self.comendo:
#             print(f"{self.comendo} não está comendo!!!")
#             return
#
#         print(f"{self.nome} parou de comer.")
#         self.comendo = False
#
#     def get_ano_nascimento(self):
#         return self.ano_atual - self.idade

# ---------------------------------------------------------------------------------------------------------------------
class Pessoa:
    def __init__(self, nome, idade, funcao, salario):
        self.nome = nome
        self.idade = idade
        self.funcao = funcao
        self.salario = salario

    def rendaMensal(self, entrada):
        self.entrada = entrada
        self.renda_mensal = self.salario + entrada
        return self.renda_mensal

    def despesaMensal(self, despesa_fixa, despesa_variavel):
        self.despesa_fixa = despesa_fixa
        self.despesa_variavel = despesa_variavel
        self.despesa_mensal = despesa_fixa + despesa_variavel
        return self.despesa_mensal

    def rendaTotal(self):
        if self.renda_mensal > self.despesa_mensal:
            return "Você terminou no positivo, {}\nO seu saldo é de {}".format(self.nome, self.renda_mensal - self.despesa_mensal)
        elif self.renda_mensal == self.despesa_mensal:
            return "Você está sem dívidas este mês, porém sem saldo positivo também, {}".format(self.nome)
        else:
            return "Infelizmente, você está com saldo negativo, {}O seu saldo é de {}".format(self.nome, self.renda_mensal - self.despesa_mensal)

p1 = Pessoa("Beatriz", 23, "Analista de Serviços TI", 2365.00)
p1.rendaMensal(300.00)
p1.despesaMensal(710.00, 1600.00)
print(p1.rendaTotal())