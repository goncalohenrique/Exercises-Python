print("Calculando qunatidade de números pares entre 1 e n")

n = int(input("Informe um valor inteiro positivo para n: "))

def qtdPares(n):
    if(n <0):
        return 0
    else:
        if(n % 2 == 0):
            return 1 + qtdPares(n - 1)
        else:
            return qtdPares(n - 1)

# Chama a função e imprime o resultado
for i in range(n + 1):
    print(f"O número {i} é par? {'Sim' if i % 2 == 0 else 'Não'}")

print(f"A quantidade de números pares entre 0 e {n} é: {qtdPares(n)}")
