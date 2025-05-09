print("Achando maior e menor")

numeros = []

qtdNumeros = int(input("Informe a quantidade de números: "))

for i in range(qtdNumeros):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)

# Função para encontrar o maior e menor número
def maiorMenor(numeros):
    maior = max(numeros)
    menor = min(numeros)
    return maior, menor

print(f"O maior número é : {maiorMenor(numeros)[0]}")
print(f"O menor número é : {maiorMenor(numeros)[1]}")
