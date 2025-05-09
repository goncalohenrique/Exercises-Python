nome = str(input("Digite seu nome: "))
qtdNotas = int(input("Imforme a quantidade de notas: "))


i = 0
notas = []


while (i<qtdNotas):
    nota = float(input(f"Digite a nota {i+1}: " ))
    if(nota < 0 or nota > 10):
        print("Nota inválida, digite novamente")
    else:
        i += 1
        notas.append(nota)

media = sum(notas)/len(notas)
media = round(media, 2)

print(f"A média do aluno {nome} é {media}!")

if media >= 7:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado!")
    
    