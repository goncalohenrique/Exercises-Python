nmrLinha = int(input("Digite o número de linhas da matriz: "))
nmrColuna = int(input("Digite o número de colunas da matriz: "))


def calcMaxValorLinha(matriz):
    maxValor = []
    for i in range(len(matriz)):
            maxValor.append(max(matriz[i]))
    return maxValor
        
        
matriz = [0]*nmrLinha

for i in range(nmrLinha):
    matriz[i] = [0]*nmrColuna

for i in range(nmrLinha):
    for j in range(nmrColuna):
      ("\n")
    
for i in range(nmrLinha):
    for j in range(nmrColuna):
        matriz[i][j] = int(input(f"Informe o valor da linha {i+1} e coluna {j+1}: "))
    print("\n")

print("Matriz preenchida: \n")
for i in range(nmrLinha):
    for j in range(nmrColuna):
        print(matriz[i][j], end=" ")
    print("\n")
    
print("Vetor com o maior valor de cada linha: ", end="")
print(calcMaxValorLinha(matriz))
