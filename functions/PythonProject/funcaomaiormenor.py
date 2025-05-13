print("Funçao achar maior e menor númeor")

def maiormenor(lista):
 return max(lista), min(lista)

listanum=[]
num = int(input("Informe quantos números deseja: "))
if(num>0):
    for i in range (num):
         numero = int(input(f"Número {i+1}: "))
         listanum.append(numero)

maior, menor = maiormenor(listanum)
print(f"O maior número é {maior} e o menor é {menor} ")
