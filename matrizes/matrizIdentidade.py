tam = int(input("Informe o tamanho da matriz: "))
# Criação da matriz
# Inicializa a matriz com listas vazias
# e depois preenche com zeros

matriz = [0] * tam
for i in range(tam):
    matriz[i] = [0] * tam
print(matriz)


for i in range(tam):
    for j in range(tam):
        if i == j:
            matriz[i][j] = 1
        else:
            matriz[i][j] = 0
            
            
            
print("Matriz identidade:")
for i in range(tam):
    for j in range(tam):
        print(matriz[i][j], end=" ")
    print("\n")