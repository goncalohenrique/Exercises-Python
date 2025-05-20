matriz = [0] *3 

# Criação da matriz
# Inicializa a matriz com listas vazias
# e depois preenche com zeros
for i in range(3):
    lin = [0] * 2
    matriz[i] = lin
    
matriz[0][1] = 3

# Preenchendo a matriz com valores
for i in range(3):
    for j in range(2):
      matriz[i][j] = int(input(f"Informe o valor da linha {i+1} e coluna {j+1}: "))
    print("\n")


for i in range(3):
    for j in range(2):
      print(matriz[i][j], end=" ") 
    print("\n")

print("Número de linhas: ", len(matriz))
print("Número de colunas da primeira linha: ", len(matriz[0]))

