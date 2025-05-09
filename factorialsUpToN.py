print("Calculadora de fatoriais até n")

n = int(input("Informe o valor de n: "))

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1) # Multiplicação do número atual pelo fatorial dos números anteriores
    

for i in range(n + 1):
    print(f"O fatorial de {i} é: {fatorial(i)}")
    
print("Fatoriais calculados com sucesso!")
