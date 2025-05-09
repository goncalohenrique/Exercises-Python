print("Encontrando o menor número")

numeros = []
qtdNumeros = int(input("Informe a quantidade de números: "))
for i in range(qtdNumeros):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)
    
def menorNumero(numeros):
    menor = min(numeros)
    return menor
    
print(f"O menor número é : {menorNumero(numeros)}")