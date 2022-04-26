PLACEHOLDER = "[name]"

with open("fileA.txt") as fileA:
    data1 = fileA.read().splitlines()

with open("fileB.txt") as fileB:
    data2 = fileB.read().splitlines()

nomes_iguais = [num for num in data1 if num in data2]

import random

# dicionario
resultados = {estudantes:random.randint(1,100) for estudantes in data1}
# print(resultados)

passaram = {aprovados: notaFinal for (aprovados,notaFinal) in resultados.items() if notaFinal>60}
# passaram = {new_key:new_value for (key,value) in resultados.items() if test}

# for (Alunos,Notas) in passaram.items():
#     print(Alunos)


import pandas

aprovados_frame = pandas.DataFrame(passaram,index=["notas"])
print(aprovados_frame)


print(nomes_iguais)
###############################

frase = "Qual é a tua frase preferida para contar as letras de cada palavra!"
lista_palavras = frase.split()
contagem = {palavra:len(palavra) for palavra in lista_palavras}


print(frase)
print(lista_palavras)
print(contagem)


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

