import bibMedidas as med
import bibGrafico as build


def main():
    #PASSAGEM DO ARQUIVO PARA A LEITURA
    base_dado=open("estatistica.txt", "r") #VARIAVEL PARA GUARDAR O ARQUIVO

    tema=build.titulo(base_dado) #TEMA DA ESTATISTICA APRESENTADA
    print("TEMA DOS DADOS:%s\n"%tema)
    tbDados=build.tbClass(base_dado) #CRIANDO A TABELA APARTIR DO ARQUIVO
    tbDados=med.organizarClass(tbDados) #ORGANIZANDO OS VALORES
    while True:
        operacao = input("ESCOLHA UMA OPCAO:\n1-MOSTRAR TABELA\n2-MOSTRAR MEDIA\n3-MOSTRAR MEDIANA\n4-MOSTRAR MODAS\n5-MOSTRAR VARIANCIA\n6-MOSTRAR DESVIO PADRAO\n7-BOXPLOT\n0-SAIR\nOPCAO: ")
        if operacao == "1":
            build.printTabela(tbDados)
        elif operacao == "2":
            media=med.getMedia(tbDados)
            print("MEDIA DOS DADOS: %.2f\n"%media)
        elif operacao == "3":
            mediana=med.getMediana(tbDados)
            print("MEDIANA DOS DADOS: %.2f\n"%mediana)
        elif operacao == "4":
            moda_czu = med.getModaCzuber(tbDados)
            moda_king = med.getModaKing(tbDados)
            moda_pear = med.getModaPearson(tbDados)
            print("MODA DE CZUBER: %.2f \nMODA KING: %.2f\nMODA PEARSON: %.2f\n"%(moda_czu,moda_king,moda_pear))
        elif operacao == "5":
            variancia = med.getVarianciaA(tbDados)
            print("VARIANCIA DOS DADOS: %f\n"%variancia)
        elif operacao == "6":
            desv_padrao = med.getDesvioPadraoA(tbDados)
            print("DESVIO PADRAO DOS DADOS: %f\n"%desv_padrao)
        elif operacao == "7":
            build.boxplot(tbDados)
        elif operacao == "0":
            exit(0)
    #end while


if __name__ == '__main__':
    import sys
    sys.exit(main())