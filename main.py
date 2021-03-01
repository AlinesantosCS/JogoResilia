print('~'*60)
print("{0:^60}".format('BEM VINDO A VIDA DE PROGRAMADOR'))
print('~'*60)

print("{0:*^60}".format('VIDA SAUDÁVEL'))

print("{0:^60}".format("\nSeu sonho é trabalhar em lugar possa ser valorizado e que goste de trabalhar.\n Para que seu objetivo possa chegar em algum lugar é decidido que comece a estudar."))

print("... Algum tempo depois houve uma oportunidade de um curso de programação gratuita...")

def cenarioPrincipal():
    # PRIMEIRO CENÁRIO - PRINCIPAL
    print('\nDesafios aparecem e como é difícil conciliar sua vida pessoal com os estudos, Neste momento \nvocê está no curso e alguns emprevistos acontecem, cheio de trabalhos e demandas da casa, qual das alternativas é a melhor opção ?')

    print('1 - Escolhe fazer somente as demandas da casa.')
    print('2 - Procrastina, mas faz pelo menos uma atividade do curso.')
    print('3 - Repensa seus horários e revê o que é possível realizar.')
    alternativa = input('Escolha um número: ')

    return alternativa


def cenarioConseguencias():
    alternativa = cenarioPrincipal()
    total = 0
    if alternativa == '1':
        total+=2
    elif alternativa == '2':
        total+=10
    elif alternativa == '3':
        total+=20

    print(total)

    
    if alternativa == '1':

        # SEGUNDO CENÁRIO - CASO FOR 1
        print('~'*60)
        print("{0:^60}".format('CADÊ SUAS PRIORIDADES ?'))
        print('~'*60)

        print('Está dividido entre aos afazeres da casa eo curso, qual dessas alternativas tem a melhor opção ?')

        print('1 - Escolhe ambos, no entanto terá um preço de estudar até de madrugada.')
        print('2 - Diminui o horário para estudar e prioriza limpar a casa')
        print('3 - Diminui o horário para limpar a casa e priorizaos estudos')
        alternativa =input('Escolha um número: ')
        if alternativa == '1':
            total+=2
        elif alternativa == '2':
            total+=10
        elif alternativa == '3':
            total+=20
       

    elif alternativa == '2':
        #  TERCEIRO CENÁRIO - CASO FOR 2
        print('~'*60)
        print("{0:^60}".format('TENHA CORAGEM!'))
        print('~'*60)

        print('Poderá ir mais longe, mesmo não realizando todas as atividades do curso aprendeu basntante conteúdos,\n po este motivo passou no processo seletivo para a resilia educação, está pronto para se tornar uma analista de dados?')
        print('Aqui está seu desafio de caminhada, organizar vida pessoas, casa e mais dois cursos, o que fará  com tudo isso ?')

        print('1 - Tendo muitas demandas, acabou escolhendo determinadas atividades sendo casa ou estudos e \ndeixou outras tarefas de lado.')
        print('2 - Priorizou os seus estdos e não tem nehum tempo para respirar.')
        print('3 - Priorizou os seus estudos e negocia com pessoas que convive com você, então passou a administração das tarefas de casa\n para outros integrantes da casa e cominicou que fará somente o básico.')
        alternativa = input('Escolha um número: ')
        if alternativa == '1':
            total+=2
        elif alternativa == '2':
            total+=10
        elif alternativa == '3':
            total+=20
    
    elif alternativa == '3':   
        #  QUARTO CENÁRIO - CASO FOR 3
        print('~'*60)
        print("{0:^60}".format('CAMINHO CERTO <3'))
        print('~'*60)

        print('Rumo a realização do seu sonho, parabéns conseguiu um emprego na tua tão sonhada área, \nsurgiu novos problemas relacionado ao seu trabalho. A engenheira de dados lhe passa tarefas para realizar porém, está acontecento problemas de comunicação\n pois, demandas que são dadas você não faz ideia enquanto tempo levará para fazer-los, logo está te trazendo bastante insegurança, o que fará ?')

        print('1 - Você é novo no trabalho, o que falar vai fazer ou falar toda diferença na visão como profissional, \nmelhor segurar as pontas e depois de um tempo falar com a lider.')
        print('2 - Você é novo na empresa, precisa gerar boas expectativas ou seja, escolha momentos quando a engenheira esteja passando tarefas para deixar claro e perguntar da expectativa do seu trabalho')
        print('3 - Comunique com a engenheira de dados e conte a ela sobre a situação de insegurança\n e qual a melhor maneira para entrarem em um acordo para deixa-la segura da situação.')
        alternativa = input('Escolha um número: ')
        if alternativa == '1':
            total+=2
        elif alternativa == '2':
            total+=10
        elif alternativa == '3':
            total+=20
      

    return total

def desejaJogarNovamente():
    jogarNovamente = 'S'
    while(jogarNovamente == 'S'):
        print('Jogar novamente ? - S ou N')
        jogaDeNovo = input('Digite a opção: ')
        if jogaDeNovo == 'S':
            jogaDeNovo = cenarioConseguencias()
        else:
            ('FIM DE JOGO')
            print(jogaDeNovo)
            break
    

     

resultadoCenario = cenarioConseguencias()
jogueNovamente = desejaJogarNovamente()

if resultadoCenario >= 20:
    print('CENÁRIO ESCRITÓRIO DO IFOOD')
    print('ESTARÁ FELIZ DA VIDA OLHANDO PELA JANELA EM ')
    print(f' PONTUAÇÃO: {resultadoCenario}')
elif resultadoCenario >= 10:
    print('CENÁRIO CASSINHA')
    print('TENDÊNCIA A PROCRASTINAÇÃO, INFELIZMENTE DEIXOU VOCÊ DESEMPREGADA(O)')
    print(f' PONTUAÇÃO: {resultadoCenario}')
elif resultadoCenario <= 9:
    print('CENÁRIO HOSPITAL')
    print('VOCÊ PAROU EM HOSPITAL POR SOBRECARGA DE ESTRESSE')
    print(f' PONTUAÇÃO: {resultadoCenario}')











