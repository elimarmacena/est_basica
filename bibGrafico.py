import bibMedidas as med
import matplotlib.pyplot as plt


#RETORNA O TITULO DO TIPO DA INFORMACAO
def titulo(arq):
    linha=arq.readline()
    return linha

#CONSTROI A TABELA DE CLASSE
def tbClass(arq):
    tabela=[]
    linha=arq.readline()
    while linha!="":
        dado=[]
        linha=linha.split(" ")
        freq=int(linha[1])
        cls=[int (x) for x in linha[0].split("-")] #JA FAZ O APPEND CONVERTENDO A STRING PARA INTEIRO
        dado.append(cls)
        dado.append(freq)
        tabela.append(dado)
        linha=arq.readline()
    return tabela

def printTabela(tb):
    i=0
    while i<len(tb):
        for j in range(len(tb[i])):
            print("%s"%tb[i][j],end=" - ")
        print("\n")
        i += 1

def boxplot(tbDados):
    quartil1 = med.getQuartil(tbDados,1)
    quartil2 = med.getQuartil(tbDados, 2)
    quartil3 = med.getQuartil(tbDados, 3)
    aiq = med.getAiq(tbDados)
    if type(tbDados[0][0]) == int:
        if tbDados[0][0] > quartil1-(1.5*aiq): #CASO O PRIMEIRO VALOR SEJA MAIOR, ELE SERA O VALOR MINIMO
            vMin = tbDados[0][0]
        else:
            vMin = quartil1-(1.5*aiq)
        if (tbDados[len(tbDados)-1][0]) < quartil3+(1.5*aiq): #CASO O ULTIMO VALOR SEJA MENOR, ELE SERA O VALOR MAX
            vMax = tbDados[len(tbDados)-1][0]
        else:
            vMax = quartil3+(1.5*aiq)
    else:
        if tbDados[0][0][0] > quartil1-(1.5*aiq): #CASO O PRIMEIRO VALOR SEJA MAIOR, ELE SERA O VALOR MINIMO
            vMin = tbDados[0][0][0]
        else:
            vMin = quartil1-(1.5*aiq)
        if (tbDados[len(tbDados)-1][0][1]) < quartil3+(1.5*aiq): #CASO O ULTIMO VALOR SEJA MENOR, ELE SERA O VALOR MAX
            vMax = tbDados[len(tbDados)-1][0][1]
        else:
            vMax = quartil3+(1.5*aiq)

    print("AIQ: %f"%aiq,end=" ")
    print("VALOR MINIMO %.2f" % vMin, end=" ")
    print("VALOR MAXIMO %.2f"%vMax,end=" ")
    print("QUARTIL 1: %.2f"%quartil1,end=" ")
    print("QUARTIL 2: %.2f" % quartil2, end=" ")
    print("QUARTIL 3: %.2f" % quartil3)
    data=[]
    for i in range(len(tbDados)):
        data.append(quartil1)
        data.append(quartil2)
        data.append(quartil3)
        data.append(vMax)
        data.append(vMin)

    plt.boxplot(data)

    plt.show()

def histogram(tbDados):
    classe_id=[]
    frequencia_classe=[]
    for i in range(len(tbDados)):
        classe_id.append(tbDados[i][0])
        #MUDAR
        frequencia_classe.append(tbDados[i][1])
    arquivo=open("base_histograma.xls","w")
    for i in range(len(classe_id)):
        arquivo.write("%d-%d;%d\n"% (classe_id[i][0],classe_id[i][1],frequencia_classe[i]))
    arquivo.close()
