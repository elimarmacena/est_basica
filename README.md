# Estatistica basica
  O codigo foi desenvolvido atraves de um trabalho proposto em uma aula de probabilidade e estatistica.<br>
  O tipo de informação trabalhada são dados tabelados em classe, mas com a inserção de mais algumas funções é possivel trabalhar com dados tabelados comum.<br><br>
  O arquivo passado para o codigo é necessario estar formadado da seguinte maneira:<br>
  < titulo dos dados analizados> na primeira linha<br>
  < limite das classes separados por - >;<frequencia>, uma linha para cada frequencia<br>
    EXEMPLO:<br>
MULHERES NÃO ALFABETIZADAS ANO 2010<br>
5-10;2181407<br>
10-15;231180 <br><br>
### Estrutura usada no codigo
  Ao ler o arquivo os dados gerados seguem a seguinte estura:<br>
  Lista contendo listas com os respectivos dados de cada variavel:<br>
  [ [informacao da classe], [informacao da classe], ...] <br>
  Estrutura da lista interna:<br>
[LISTA CLASSE(index 0), FREQUENCIA(index 1), FREQUENCIA ACUMULADA(index 2), Xi(index 3)]<br>

  Estrutura da sublista(LISTA CLASSE):<br>
[LIMITE INFERIOR(index 0), LIMITE SUPERIOR(index1)]<br>


### Biblioteca usada
  A aplicação faz uso da biblioteca matlibplot do python para o plot do boxplot, calcula media, mediana, moda(Czuber, King e Pearson), variancia, desvio padrão, quartis (1, 2 3)<br>
