nmrLin = int(input("Digite o número de linhas da matriz: "))
nmrCol = int(input("Digite o número de colunas da matriz: "))

matriz = [0] * nmrLin



for i in range(nmrLin):
    matriz[i] = [0] * nmrCol
    
for i in range(nmrLin):
    for j in range(nmrCol):
        matriz[i][j] = int(input(f"Informe o valor da linha {i+1} e coluna {j+1}: "))
    print("\n")
    
print("Matriz preenchida: \n")
for i in range(nmrLin):
    for j in range(nmrCol):
        print(matriz[i][j], end=" ")
    print("\n")

escalar = int(input("Informe o valor escalar: "))

for i in range(nmrLin):
    for j in range(nmrCol):
        matriz[i][j]*= escalar
        
print("Matriz Escalar: \n")
for i in range(nmrLin):
    for j in range(nmrCol):
        print(matriz[i][j], end=" ")
    print("\n")