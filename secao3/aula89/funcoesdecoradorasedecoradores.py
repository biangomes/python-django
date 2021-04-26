# Uma funcao é responsavel apenas para criar OUTRA funcao
def master(funcao):
    def slave():
        funcao()
        #slave()     permite executar a funcao mais interna
    return slave()      # agr eh uma funcao esperando pra ser executada


def fala_oi():
    print('Oi')


master(fala_oi)