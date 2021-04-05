from Model import cenarioConseguencias
from Model import cenarioPrincipal
from Controller import desejaJogarNovamente
print('~'*100)
print("{0:^60}".format("""


    ____  ________  ___   _    _______   ______  ___       ___ 
   / __ )/ ____/  |/  /  | |  / /  _/ | / / __ \/   |     /   |
  / __  / __/ / /|_/ /   | | / // //  |/ / / / / /| |    / /| |
 / /_/ / /___/ /  / /    | |/ // // /|  / /_/ / ___ |   / ___ |
/_____/_____/_/  /_/     |___/___/_/ |_/_____/_/  |_|  /_/  |_|
                                                               
 

"""))
print("{0:^60}".format("""


 _    __________  ___       ____  ______   ____  ____  ____  __________  ___    __  ______    ____  ____  ____ 
| |  / /  _/ __ \/   |     / __ \/ ____/  / __ \/ __ \/ __ \/ ____/ __ \/   |  /  |/  /   |  / __ \/ __ \/ __ 
| | / // // / / / /| |    / / / / __/    / /_/ / /_/ / / / / / __/ /_/ / /| | / /|_/ / /| | / / / / / / / /_/ /
| |/ // // /_/ / ___ |   / /_/ / /___   / ____/ _, _/ /_/ / /_/ / _, _/ ___ |/ /  / / ___ |/ /_/ / /_/ / _, _/ 
|___/___/_____/_/  |_|  /_____/_____/  /_/   /_/ |_|\____/\____/_/ |_/_/  |_/_/  /_/_/  |_/_____/\____/_/ |_|  
                                                                                                               

 

"""))

print('~'*100)



print("{0:*^60}".format("""

 _    __________  ___       _____ ___   __  ______   ___    __________ 
| |  / /  _/ __ \/   |     / ___//   | / / / / __ \_/_/ |  / / ____/ / 
| | / // // / / / /| |     \__ \/ /| |/ / / / / / / _ | | / / __/ / /  
| |/ // // /_/ / ___ |    ___/ / ___ / /_/ / /_/ / __ | |/ / /___/ /___
|___/___/_____/_/  |_|   /____/_/  |_\____/_____/_/ |_|___/_____/_____/
                                                                       

"""))
print('~'*100)

print("{0:^60}".format("\nSeu sonho é trabalhar em lugar possa ser valorizado e que goste de trabalhar.\n Para que seu objetivo possa chegar em algum lugar é decidido que comece a estudar."))
print("{0:*^60}".format('~ No final do jogo você vai ver qual personagem é próximo ao seu comportamento <3 ~'))

print("... Algum tempo depois houve uma oportunidade de um curso de programação gratuita...")


cenarioPrincipal()
cenarioConseguencias()
resultadoCenario = cenarioConseguencias()
desejaJogarNovamente()

if resultadoCenario >= 40:
    
    print('\n\n\nVocê combina com o personagem LISA SIMPSON')
    print('Bastante inteligente e determinada(o)!\n')
    
   
elif resultadoCenario >= 20:
    
    print('\n\n\nVocê combina com o personagem SHIKAMARU NARA')
    print('Preguiçoso, mas com grande potencial, encontre a sua motivação e atinja o seu melhor!\n')
    
   
elif resultadoCenario < 20 :
    
    print('\n\n\nVocê combina com o personagem CORAGEM, O CÃO COVARDE')
    print('Bastante estressada, emocionalmente cansada só que com bastante coragem para mudar\n')
    

if resultadoCenario >= 40:
    print('~'*70)
    print("{0:^60}".format('CENÁRIO ESCRITÓRIO'))
    print('ESTARÁ FELIZ DA VIDA NO ESCRITÓRIO DO IFOOD, OLHANDO PELA JANELINHA ')
    print('~'*70)
    print(f' PONTUAÇÃO: {resultadoCenario}')   
elif resultadoCenario == 30:
    print('~'*60)
    print("{0:^60}".format('CENÁRIO ESCRITÓRIO'))
    print('VOCÊ VIROU UM FARIA LIMER, TRABALHANDO EM ALGUM BANCO DIGITAL POR LÁ')
    print('~'*60)
    print(f' PONTUAÇÃO: {resultadoCenario}')
elif resultadoCenario == 22:
    print('~'*90)
    print("{0:^60}".format('CENÁRIO CASINHA'))
    print('VOCÊ INFELIZMENTE CONTINUA DESEMPREGADO POR CONTA DA PROCRASTINAÇÃO, MAS COM VONTADE DE MUDAR E CONTINUAR NA CARREIRA')
    print('~'*90)
    print(f' PONTUAÇÃO: {resultadoCenario}')
elif resultadoCenario == 20:
    print('~'*90)
    print("{0:^60}".format('CENÁRIO CASINHA'))
    print('VOCÊ INFELIZMENTE CONTINUA DESEMPREGADO POR CONTA DA PROCRASTINAÇÃO E DESISTIU DA CARREIRA')
    print('~'*90)
    print(f' PONTUAÇÃO: {resultadoCenario}')
elif resultadoCenario == 12:
    print('~'*60)
    print("{0:^60}".format('CENÁRIO HOSPITAL'))
    print('VOCÊ SOFREU BURNOUT, MAS VAI SOBREVIVER')
    print('~'*60)
    print(f' PONTUAÇÃO: {resultadoCenario}')
elif resultadoCenario == 4:
    print('~'*60)
    print("{0:^60}".format('CENÁRIO HOSPITAL'))
    print('VOCÊ INFARTOU E INFELIZMENTE MORREU')
    print('~'*60)
    print(f' PONTUAÇÃO: {resultadoCenario}')

