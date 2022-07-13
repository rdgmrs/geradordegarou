#gerador de personagens
import random

nomes = ['Miguel','Arthur','Théo','Heitor','Gael','Davi','Bernardo','Gabriel','Ravi','Noah','Samuel','Pedro','Benício','Benjamin','Matheus','Isaac','Anthony','Joaquim','Lucas','Lorenzo','Helena','Alice','Laura','Manuela','Valentina','Sophia','Isabella','Heloísa','Luiza','Júlia','Lorena','Lívia','Maria Luiza','Cecília','Eloá','Giovanna',
'Maria Clara','Anahí','Mariana','Lara']
tribos = ['Andarilhos do Asfalto', 'Filhos de Gaia', 'Garras Vermelhas', 'Senhores das Sombras', 'Crias de Fenris', 'Presas de Prata','Uktena','Wendigo','Roedores de Ossos','Fianna','Fúrias Negras','Peregrinos Silenciosos','Portadores da Luz Interior',]
raças = ['Hominídea', 'Lupina', 'Impura']
augúrios = ['Ahroun', 'Galliard', 'Phillodox', 'Theurge', 'Ragabash']


#nomes
def nomesrandom(nomes):
    novonome = random.choice(nomes)
    return novonome
#print(nomesrandom(nomes))
#tribos
def tribosrandom(tribos):
  return random.choice(tribos)
#print(tribosrandom(tribos))
#raças
def racasrandom(raças):
  return random.choice(raças)
#print(racasrandom(raças))
#augúrio
def auguriosrandom(augúrios):
  return random.choice(augúrios)
#print(auguriosrandom(augúrios))


def savechartxt(): 
    nomedoarquivo = (nomesrandom(nomes))
    with open(nomedoarquivo, 'a+') as file: #escreve/cria o txt
        file.write(nomedoarquivo)     #(nomesrandom(nomes))#poe um cursor pra escrever um texto
        file.write(', '+tribosrandom(tribos))#poe um cursor pra escrever um texto
        file.write(', '+racasrandom(raças))#poe um cursor pra escrever um texto
        file.write(', '+auguriosrandom(augúrios))#poe um cursor pra escrever um texto


#o for não está repetindo o comando o numero de vezes discrito no range....
#notei rodando 10000 que não está repetindo o nome 
for x in range(0,10000,1):
  x = savechartxt()



