import random
import game_data

#### LISTA PARA JOGAR
lista_random = [*range(50)]
random.shuffle(lista_random)
listacompara = game_data.data
pontos = 0
ok = True


#### FUNCAO COMPARAR
def compara(primeiro, segundo):
    a = listacompara[lista_random[primeiro]]["name"]
    b = listacompara[lista_random[segundo]]["name"]
    c = listacompara[lista_random[primeiro]]["follower_count"]
    d = listacompara[lista_random[segundo]]["follower_count"]
    print(f"Comparando pesquisas semanais no google, achas que este - {a} - tem mais ou menos que este - {b} - ??  ")
    resposta = input("Escreve mais ou menos: \n")
    real = ""

    if int(listacompara[lista_random[primeiro]]["follower_count"]) > int(
            listacompara[lista_random[segundo]]["follower_count"]):
        real = "mais"
    else:
        real = "menos"
    if resposta == real:
        return print(f"Boa! Acertaste.. era {c} mil contra {d} mil \n")
    else:
        return False


#### LOOP DO JOGO
for i in range(49):
    a = compara(lista_random[i], lista_random[i + 1])
    pontos += 1
    if a == False:
        print("\n Parece que falhaste.. o jogo acabou boy :( \n \n")
        break
    print (f"pontos acumulados: {pontos}\n")

########### TESTES ##############
# print(listacompara[lista_random[2]]["name"])
# print(lista_random)



##########################################################################################################
##########################################################################################################



import random
import game_data

#### LISTA PARA JOGAR
lista_random = [*range(50)]
random.shuffle(lista_random)
listacompara = game_data.data
pontos = 0
ok = True


#### FUNCAO COMPARAR
def compara(primeiro, segundo):
    a = listacompara[lista_random[primeiro]]["name"]
    b = listacompara[lista_random[segundo]]["name"]
    c = listacompara[lista_random[primeiro]]["follower_count"]
    d = listacompara[lista_random[segundo]]["follower_count"]
    print(f"Comparando pesquisas semanais no google, achas que este - {a} - tem mais ou menos que este - {b} - ??  ")
    resposta = input("Escreve mais ou menos: \n")
    real = ""

    if int(listacompara[lista_random[primeiro]]["follower_count"]) > int(
            listacompara[lista_random[segundo]]["follower_count"]):
        real = "mais"
    else:
        real = "menos"
    if resposta == real:
        return print(f"Boa! Acertaste.. era {c} mil contra {d} mil \n")
    else:
        return False


#### LOOP DO JOGO
for i in range(49):
    a = compara(lista_random[i], lista_random[i + 1])
    pontos += 1
    if a == False:
        print("\n Parece que falhaste.. o jogo acabou boy :( \n \n")
        break
    print (f"pontos acumulados: {pontos}\n")

########### TESTES ##############
# print(listacompara[lista_random[2]]["name"])
# print(lista_random)


##########################################################################################################
##########################################################################################################



import random
from collections import Counter

mylist = ["Ganhar", "DRAW", "Perder"]
lista_al = random.choices(mylist, weights = [38, 2, 60], k = 100)
contagem = Counter(lista_al)
lista = []

for n in range(100):
    x = random.choices(mylist, weights = [38, 2, 60], k = 100)
    print("\n",x)


##########################################################################################################
##########################################################################################################
        ## Tape reading cripto bot


import random
import time

a = ["Compra já crl!!!", "Compra!", "Toca a comprar!!!!", "Olha!! Agora é pa comprar!!!", "Compra tudo agora caralho"]
b = ["Põe à venda!!", "Vende!!!", "Caga, vende tudo agora!", "VENDE!!!", "Esquece, vende tudo já"]
s = 3

time.sleep(2)
print("Loading.......")
time.sleep(s)
print("Connecting to all stock markets.....")
time.sleep(s)
print("Creating safe link to brokers.....")
time.sleep(1)
print("Connecting your account......")
time.sleep(s)
print("CONNECTION SUCCESS!!")
time.sleep(1)
print("Ready")
time.sleep(1)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

while 2>1:
    c = random.randint(1, 5)
    d = random.randint(1, 2)
    time.sleep(c)
    if d == 1:
        print(a[c-1])
    else:
        print(b[c-1])


##########################################################################################################
##########################################################################################################
