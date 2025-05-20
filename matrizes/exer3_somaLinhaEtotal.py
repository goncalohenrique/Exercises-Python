def somarLinha(matriz, linha):
    Msoma = []
    soma = 0
    for i in range(linha):
        for j in range(len(matriz[i])):
            soma += matriz[i][j]
        Msoma.append(soma)
        soma = 0
    return Msoma

def somarTotal(soma):
    total = 0
    for i in range(len(soma)):
        total += soma[i]
    return total


matriz = [0] *3

for i in range(3):
    matriz[i] = [0] * 2

for i in range(3):
    for j in range(2):
        matriz[i][j] = int(input(f"Informe o valor da linha {i+1} e coluna {j+1}: "))
    print("\n")
    
print("Matriz preenchida: \n") 
for i in range(3):
    for j in range(2):
        print(matriz[i][j], end=" ") 
    print("\n")

Msoma = somarLinha(matriz, 3)
print("Soma de cada linha: ", end="")  
for i in range(len(Msoma)):
    print(Msoma[i], end=" ")

print(f"\n Total: {somarTotal(Msoma)}")