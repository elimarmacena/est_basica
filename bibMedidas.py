# FUNCOES AUXILIARES#############
# FUNCAO AUXILIAR PARA ORGANIZAR
def getKey(item):
    if type(item[0]) == int:
        return item[0]
    else:
        return item[0][0]


# FUNCAO AUXILIAR PARA MEDIA
def somatorioTabela(tabela):
    somatorio = 0  # SOMATORIO TOTAL
    i = 0  # CONTROLE DE LACO
    if type(tabela[0][0]) == int:
        while i < len(tabela):
            somatorio += tabela[i][0] * tabela[i][1] #valor * Fi
            i += 1
        return somatorio
    else:
        while i < len(tabela):  # CASO OS DADOS SEJAM EM CLASSE
            somatorio += tabela[i][3] * tabela[i][1] #Xi * Fi
            i += 1
        return somatorio


# FUNCAO DE BUSCA O VALOR DA POSICAO N
def getValor(tbDados, posValor):
    i = 0 #CONTROLE DE LAÇO
    if type(tbDados[0][0]) == int and posValor < getAcMax(tbDados):
        inf = 0 #LIMITE INFERIOR DO INTERVALO
        sup = tbDados[0][2] #LIMITE SUPERIOR DO INTERVALO (FREQUENCIA ACUMULADA)
        while i < len(tbDados):
            if inf < posValor < sup: #VERIFICAR SE A POSICAO ESTA NO INTERVALO
                return tbDados[i][0]
            i += 1
            inf = sup
            sup = tbDados[i][2]

    else:
        if posValor >= len(tbDados):
            print("POSSICAO INVALIDA\n")
        else:
            inf = 0 #LIMITE INFERIOR DO INTERVALO
            sup = tbDados[0][3] #LIMITE SUPERIOR DO INTERVALO(FREQUENCIA ACUMULADA)
            while i < len(tbDados):
                if inf < posValor < sup:
                    return tbDados[i][3]  # Xi DA CLASSE
                i += 1
                inf = sup
                sup = tbDados[i][3]


# NOS DA A CLASSE DE DETERMINADA POSICAO
def getClass(tbDados, posValor):
    if posValor < getAcMax(tbDados) and posValor > 0:
        contadorInferior = 0
        contadorSuperior = tbDados[0][2]
        for i in range(0,len(tbDados)) :
            if  contadorInferior<=posValor<=contadorSuperior:
                return tbDados[i][0]
            contadorInferior = contadorSuperior
            contadorSuperior = tbDados[i][2]
    else:
        print("POSICAO INVALIDA\n")


def getAcMax(tbDados):
    if type(tbDados[0][0]) == int:
        return tbDados[len(tbDados) - 1][2] #CASO SEJA DADOS TABULADOS
    else:
        return tbDados[len(tbDados) - 1][2] #CASO SEJA DADOS EM CLASSE


# SUBFUNCAO DE ORGANIZAR
###NOS DA A FREQUENCIA ACUMULADA EM CADA PONTO DA TABELA
def setFreqAc(tbDados):
    i = 0  # VAIRAVEL DE CONTROLE
    ac = 0  # ACUMULADO
    while i < len(tbDados):
        ac += tbDados[i][1] #ACUMULADO + FREQUENCIA DO ATUAL
        tbDados[i].append(ac) #ADICIONA A FREQUENCIA ACUMULADA ATE O PONTO
        i += 1
    return tbDados


#NOS DA A FREQUENCIA ACUMULADA ANTERIOR
def getFreqAnt(tbDados, cl): #RECEBE A TABELA DE DADOS E A CLASSE PARA A COMPARACAO
    i = 0
    if cl == tbDados[i][0]:
        return 0
    else:
        while cl != tbDados[i][0] and i<len(tbDados):
            i += 1
        return tbDados[i - 1][2]

#RETORNA A FREQUENCIA SIMPLES
def getFreqPos(tbDados, cl): #RECEBE A TABELA DE DADOS E A CLASSE PARA A COMPARACAO
    #CL RECEBIDA EH A CLASSE PARA COMPARACAO
    i = 0
    while cl != tbDados[i][0]:
        i += 1
    return tbDados[i + 1][1]

#NOS DA A FREQUENCIA DA CLASSE
def getFreqClass(tbDados, cl): #RECEBE A TABELA DE DADOS E A CLASSE PARA A COMPARACAO
    i=0
    while cl != tbDados[i][0]:
        i += 1
    return tbDados[i][1]

#RETORNA O VALOR DA AMPLITUDE DA CLASSE
def amplitude(clss):
    return clss[1]-clss[0] #LIMITE SUPERIOR - LIMITE INFERIOR

#RETORNA TODOS OS DADOS DO ELEMENTO QUE MAIS SE REPETE
def maiorRepeticao(tbDados):
    i=0
    maior = tbDados[0]
    while i<len(tbDados):
        if maior[1]<tbDados[i][1]:
            maior = tbDados[i]
        i+=1
    return maior

#RETORNA O MAIOR VALOR DA TABELA DE DADOS (apenas para tabelas ordenadas)
def getMaiorV(tbDados):
    if type(tbDados[0][0]) == int:
        return tbDados[len(tbDados)-1][0]
    else:
        return tbDados[len(tbDados)-1][3]

#RETORNA O MENOR VALOR DA TABELA DE DADOS (apenas para tabelas ordenadas)
def getMenorV(tbDados):
        if type(tbDados[0][0]) == int:
            return tbDados[0][0]
        else:
            return tbDados[0][3]


#           FIM AUXILIARES              #




###ATRIBUI O VALOR XI DE TODOS ELEMENTOS DA TABELA
def setXi(tbDados):  # RECEBE A TABELA DE DADOS EM CLASSE
    i = 0
    while i < len(tbDados):
        temp = (tbDados[i][0][0] + tbDados[i][0][1]) / 2  # TEMP DADOS EH UMA VARIAVEL QUE É UTILIZADA PARA GUARDAR O VALOR DE XI
        tbDados[i].append(temp)
        i = i + 1
    return tbDados


#ORGANIZA OS VALORES DA TABELA E INSERE OS VALORES ACUMULADOS
def organizar(tbDados):  # RECEBE A TABELA DE DADOS (APERNAS TABULADOS)
    tbDados = sorted(tbDados, key=getKey)  # FAZ USO DE UMA FUNCAO AUXILIAR GETKEY
    tbDados = setFreqAc(tbDados)
    return tbDados


#ORGANIZA OS VALORES DA TABELA EM CLASSE ESTABELECENDO OS VALORES ACUMULADOS E Xi
def organizarClass(tbDados):  # RECEBE UMA TABELA DE DADOS EM CLASSE
    tbDados = sorted(tbDados, key=getKey)  # FAZ USO DE UMA FUNCAO AUXILIAR GETKEY
    tbDados = setFreqAc(tbDados)
    tbDados = setXi(tbDados)
    return tbDados


#NOS DA A MEDIA DE UMA TABELA DE DADOS
def getMedia(tbDados):
    somatorio_tb= somatorioTabela(tbDados)
    frequencia_tb=getAcMax(tbDados)
    media = somatorio_tb / frequencia_tb
    return media


#NOS DA A MEDIANA DE UMA TABELA DE DADOS
def getMediana(tbDados):
    if type(tbDados[0][0]) == int:
        if getAcMax(tbDados) % 2 == 0:
            vmediano = getValor(tbDados, (getAcMax(tbDados) / 2)) + getValor(tbDados, (getAcMax(tbDados) / 2) + 2)
            vmediano = vmediano / 2
            return vmediano
        else:
            vmediano = getValor(tbDados, (getAcMax(tbDados) + 1) / 2)
            return vmediano
    else:
        #VALORES PARA A FORMULA DA MEDIANA
        medianaInf = getClass(tbDados, (getAcMax(tbDados)) // 2)[0]  #FORMATACAO PARA PEGAR APENAS O VALOR INFEIOR DA CLASSE
        fanterior = getFreqAnt(tbDados, getClass(tbDados, (getAcMax(tbDados)) // 2))
        freqMediana = getFreqClass(tbDados, getClass(tbDados, (getAcMax(tbDados)) // 2))
        classeMediana = getClass(tbDados, (getAcMax(tbDados) // 2))
        ampli= amplitude(classeMediana)
        #FIM DA BUSCA DE VALORES
        valorMediano= (( (getAcMax(tbDados)/2 - fanterior) /freqMediana) *ampli) +medianaInf
        return valorMediano


###NOS DA A MODA DE KING (DADOS EM CLASSE)
def getModaKing(tbDados):
    clModa = maiorRepeticao(tbDados)
    freqAnt = getFreqAnt(tbDados,clModa[0])
    freqPos = getFreqPos(tbDados,clModa[0])
    moda = clModa[0][0] + amplitude(clModa[0]) * (freqPos/(freqAnt+freqPos))
    return moda

###NOS DA A MODA DE CZUBER(DADOS EM CLASSE)
def getModaCzuber(tbdados):
    clModa = maiorRepeticao(tbdados)
    inf_moda=clModa[0][0]
    freqModa = getFreqClass(tbdados,clModa[0])
    freqAnt = getFreqAnt(tbdados,clModa[0])
    freqPos = getFreqPos(tbdados,clModa[0])
    ampli= amplitude(clModa[0])
    moda= inf_moda + ampli * ( (freqModa-freqAnt)/(2*freqModa-(freqAnt+freqPos)) )
    return moda

###NOS DA A MODA DE PEARSON
def getModaPearson(tbDados):
    mediana= getMediana(tbDados)
    media= getMedia(tbDados)
    moda = (3 * mediana) - (2 * media)
    return moda

###NOS DA A VARIANCIA AMOSTRAL
def getVarianciaA(tbDados):
    i = 0
    media = getMedia(tbDados)
    varianciaA = 0
    if type(tbDados[0][0]) == int:
        while i<len(tbDados):
            varianciaA+=(tbDados[i][0] - media) ** 2
            i+=1
        varianciaA = varianciaA / (getAcMax(tbDados) - 1)
        return varianciaA
    else:
        while i<len(tbDados):
            varianciaA+= (tbDados[i][3] - media) ** 2
            i+=1
        varianciaA = varianciaA / (getAcMax(tbDados) - 1)
        return  varianciaA

#NOS DA O DESVIO PADRAO AMOSTRAL
def getDesvioPadraoA(tbDados):
    return (getVarianciaA(tbDados)) ** (1 / 2)

###NOS DA A VARIANCIA POPULACIONAL
def getVarianciaP(tbDados):
    i = 0
    media = getMedia(tbDados)
    varianciaP = 0
    if type(tbDados[0]) == int:
        while i<len(tbDados):
            varianciaP+=(tbDados[i][0] - media) ** 2
            i+=1
        varianciaP = varianciaP / getAcMax(tbDados)
        return varianciaP
    else:
        while i<len(tbDados):
            varianciaP+= (tbDados[i][3] - media) ** 2
            i+=1
        varianciaP = varianciaP / getAcMax(tbDados)
        return  varianciaP

#NOS DA O DESVIO PADRAO POPULACIONAL
def getDesvioPadraoP(tbDados):
    return (getVarianciaP(tbDados)) ** (1 / 2)

#NOS DA O QUARTIL N
#TAL QUE N DEVE SER PASSADO PARA A FUNCAO
def getQuartil(tbDados,pos):
    if pos != 1 and pos != 2 and pos != 3: #CASO A POSSICAO PASSADA NAO SEJA UMA DAS PRE DETERMINADAS.
        return 0
    if type(tbDados[0][0]) == int:
        if type((pos*25)*len(tbDados)/100)== int: #VERIFICANDO SE O QUARTIL*TAMANO DA LISTA DIVIDO POR 100 EH UM INTEIRO
            quartil = getValor(tbDados,(pos*25)*len(tbDados)/100)
            return quartil
        else:
            valor1 = getValor(tbDados,(pos*25)*len(tbDados)//100)
            valor2 = getValor(tbDados, ((pos * 25) * len(tbDados) // 100)+1)
            return (valor1+valor2)/2
    else:
        percentil = ( (pos*25)* getAcMax(tbDados)) /100
        classe_percentil=getClass(tbDados, percentil)
        inf_class = classe_percentil[0]  #FORMATACAO PARA PEGAR APENAS O VALOR INFEIOR DA CLASSE
        f_anterior = getFreqAnt(tbDados, classe_percentil)
        freq_classe = getFreqClass(tbDados, classe_percentil)
        ampli= amplitude(classe_percentil)
        #FIM DA BUSCA DE VALORES
        quartil = (( (percentil - f_anterior) /freq_classe) *ampli) +inf_class
        return quartil


def getAiq(tbDados):
    quartil3=getQuartil(tbDados,3)
    quartil1=getQuartil(tbDados,1)
    aiq = quartil3-quartil1
    return aiq