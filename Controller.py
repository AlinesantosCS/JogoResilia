from Model import cenarioConseguencias
from Model import cenarioPrincipal

def desejaJogarNovamente():
    jogarNovamente = 'S'
    while(jogarNovamente.upper() == 'S'):
        print('Jogar novamente ? - S ou N')
        jogaDeNovo = input('Digite a opção: ')
        if jogaDeNovo.upper() == 'S':
            jogaDeNovo = cenarioConseguencias()
        else:
            ('FIM DE JOGO')
            break
       
