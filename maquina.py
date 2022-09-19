import os.path
from sys import argv

#REFERENCIAS MAQUINA TURING PYTHON
# https://www.vivaolinux.com.br/script/Maquina-de-Turing-em-Python-3 (PRINCIPAL)
# https://github.com/gabrielcasag/maquina-de-turing-universal/blob/master/Maquina.py

#FUNCAO DA MAQUINA COM SUAS VERIAVEIS, CONDIÇÃO DE TRANSIÇÃO DE ESTADO E ACEITAÇÃO
def maquina(alfabeto, transicoes, qtd_transicoes, fita, qtd_estados):
  #DECLARAÇÃO DE VARIÁVEIS DA MAQUINA
  estado = 1
  posicao = 0
  resultado = "Accept"
  palavra = str(fita)
  fita += "_"
  fita = list(fita)
  
  #LOOPING PARA CONTINUAR ENQUANTO NAO ENCONTRAR ESTADO DE ACEITAÇÃO OU NAO
  while estado != qtd_estados:
    simbolo = fita[posicao]
    encontrou = False
    for i in range(0, len(transicoes[estado])):
      if transicoes[estado][i][:1] == simbolo:
        fita[posicao] = transicoes[estado][i][1:2] 
        encontrou = True
        break
  
    #CONDIÇÕES DE ESTADO DE ACEITAÇÃO OU NAO ACEITAÇÃO
    if not encontrou:
      resultado = "Not Accept"
      estado = qtd_estados
    else:
      #mover para direita
      if transicoes[estado][i][2:3] == "R":
        posicao += 1
      else:
        #move para esquerda
        posicao -= 1

      #EVOLUI PARA PROXIMO ESTADO
      estado = int(transicoes[estado][i][3:4])

  #RETORNO RESULTADO E A PALAVRA DE ENTRADA
  return f"{palavra} {resultado}" 
###########################################################
def main():
  arquivo_entrada = ""
  alfabeto = []
  fitas = []
  transicoes = {}
  qtd_estados = 0
  qtd_transicoes = 0
  qtd_fitas = 0
  
  if len(argv) > 1:
    arquivo_entrada = argv[1]
    
  #LEITURA DO ARQUIVO
  if os.path.exists(arquivo_entrada):
    arquivo = open(arquivo_entrada, 'r') 
    linhas = arquivo.readlines()
    #NORMALIZAÇAO DE DADOS
    for i in range(0, len(linhas)):
      linhas[i] = linhas[i].strip('\n')#retira os valores que a máquina não consegue ler

    try:
      for i in range(0, len(linhas[0])):
        alfabeto.append(linhas[0][i])
      
      qtd_estados = int(linhas[1])

      qtd_transicoes = int(linhas[2])
      
      for i in range(0, qtd_estados-1):
        transicoes[i+1] = []
        
      for i in range(3, qtd_transicoes+3):
        palavra = linhas[i].replace(" ", "")#retirar os espaços 
        transicoes[int(palavra[:1])].append(palavra[1:len(palavra)])#add transição por estado
        
      qtd_fitas = int(linhas[qtd_transicoes+3]) #add palavras testadas

      #LOGAR ERROS DE LEITURA DO ARQUIVO DE ENTRADA
      for i in range(qtd_transicoes+4, qtd_transicoes+4+qtd_fitas):
        fitas.append(linhas[i])
    except:
      print("\nInput invalido. Abortado..")
  else:
    print("\nArquivo de input nao encontrado!")
  
  #Executado...
  print("\n *********MAQUINA DE TURING********\n")
  print("\nSaida:")

  for i in range(0, qtd_fitas):
    resposta = maquina(alfabeto, transicoes, qtd_transicoes, fitas[i], qtd_estados)
    print(f"\n{i+1}: {resposta}")
  print() 

if __name__ == "__main__":
  main()