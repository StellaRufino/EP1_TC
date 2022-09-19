import os.path
import sys
from sys import argv

def maquina(entrada, fita, transicoes, qtd_transicoess, qtd_estados):
  
  estado = 1 #estado em que a maquina irá iniciar
  
  ponto = 0 #ponto em que a fita irá iniciar
  #ent_leitura de input
  ent_leitura = str(fita) #palavra que vai ser inserida para leitura

  fita += "-"
  #quebra a string simbolo por simbolo em uma lista para ser iterada
  fita = list(fita)
  #caso chegue ao estado de aceitacao sai do while e estado_aceitacao = OK
  estado_aceitacao = "Aceita"

  #equanto a maquina nao chega a um estado de aceitacao/recusa.
  while estado != qtd_estados:
    simbolo = fita[ponto]
    #procura no estado de transicao aquele que deve ler o simbolo 
    procura_estado = False
    for i in range(0, len(transicoes[estado])):
      #se encontrar entao muda o simbolo da fita de acordo com a tabela.
      if transicoes[estado][i][:1] == simbolo:
        fita[ponto] = transicoes[estado][i][1:2] 
        procura_estado = True
        break

    #se este estado nao le o simbolo, rejeite. (quebra o while) 
    if not procura_estado:
      estado_aceitacao = "not OK"
      estado = qtd_estados
    #se nao, entao movimente a fita para o lado respectivo.
    #e muda o estado de transicao para o proximo correto.
    else:
      #move para a direita
      if transicoes[estado][i][2:3] == "D":
        ponto += 1
      #move para a esquerda
      else:
        ponto -= 1

      #muda para o proximo estado de transicao.
      estado = int(transicoes[estado][i][3:4])

  #retorna a ent_leitura de input + estado_aceitacao (OK/not OK)
  return f"{ent_leitura} {estado_aceitacao} " 



def main():
  
 arq_leitura = "" #arquivo txt para maquina fazer leitura
# entrada de entrada aceito pela máquina de turing 
 entrada = []
# estados de transição da maquina
 qtd_estados = 0 # numeros de estados que a maquina possui
 transicoes = {} #transições de estados da maquina (ex q0 --> q1)
 qtd_transicoes = 0
 qtd_fitas = 0 #quantidades de fitas que a maquina possue
 fitas = [] #as fitas em si

 if len(argv) > 1:
        arq_leitura = argv[1]
        
    #leitura do arquivo txt para iniciar a maquina
 if os.path.exists(arq_leitura):
        leitura = open(arq_leitura, 'r') # abre e le o arquivo
        pula_linha =  leitura.readlines()

        for i in range(0, len(pula_linha)):
        #utilizando o metodo strip para tirar os espaços antes e depois dos
        #simbolos para facilitar a leitura da maquina e ela nao confundir os espaços em branco
            pula_linha[i] = pula_linha[i].strip('\n') 


            try:
                #adiciona cada simbolo do entrada para a lista entrada
                for i in range(0, len(pula_linha[0])):
                    entrada.append(pula_linha[0][i])
                
                #adiciona o numero de estados
                qtd_estados = int(pula_linha[1])

                #adiciona o numero de transicoes
                qtd_transicoes= int(pula_linha[2])
                
                #cria um dicionario para organizar os estados
                #a chave eh o estado (Qn). E o valor sao: lendo, gravar na fita,
                #mover fita, va para o estado.
                for i in range(0, qtd_estados-1):
                    #{N:[]}
                    transicoes[i+1] = []
                    
                #adiciona as transicoes para cada chave (estado)
                for i in range(3, qtd_transicoes+3):
                    ent_leitura = pula_linha[i].replace(" ", "")
                    transicoes[int(ent_leitura[:1])].append(ent_leitura[1:len(ent_leitura)])
                    
                #adiciona o numero de ent_leituras testadas
                qtd_fitas = int(pula_linha[qtd_transicoes+3])

                #adiciona as ent_leitura a serem testadas (aabb, aaabbb..)
                for i in range(qtd_transicoes+4, qtd_transicoes+4+qtd_fitas):
                    fitas.append(pula_linha[i])
            except:
                    #caso a leitura do input falhe.
                    print("\nEntrada Inválida.")
                    quit()
            else:
                    #caso o arquivo de input nao exista.
                    print("\nNão foi possível encontrar o arquivo.")
                    quit()
        
        #se tudo foi carregado corretamente.. Rodar a maquina passando a fita.

        
        

        #para cada ent_leitura, rodar a fita correspondente na maquina de turing
 for i in range(0, qtd_fitas):
    resposta = maquina(entrada, fitas[i], transicoes, qtd_transicoes, qtd_estados)
    print(f"\n{i+1}: {resposta}")
    print()





if __name__ == "__main__":
  main()      