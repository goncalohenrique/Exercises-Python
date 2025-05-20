import random as aleatorio

nmrLinha_a = int(input("Digite o número de linhas da matriz A: "))
nmrColuna_a = int(input("Digite o número de colunas da matriz A: "))

def adicionarNumRandoms(matriz, numLin, numCol):
    for i in range(numLin):
     for j in range(numCol):
         num = aleatorio.randint(0, 10)
         matriz[i][j] = num
    return matriz


def concatMatrizes(matrizA, matrizB):
    if(len(matrizA)==(len(matrizB))):
        matrizC = [0]*len(matrizA)
        for i in range(len(matrizA)):
            matrizC[i] = [0]*(len(matrizA[i])+len(matrizB[i]))
            for j in range(len(matrizA[i])):
                matrizC[i][j] = matrizA[i][j]
            for j in range(len(matrizB[i])):
                matrizC[i][j+len(matrizA[i])] = matrizB[i][j]
        return matrizC
    else:
        print("As matrizes não possuem o mesmo número de linhas")
        return None


class MatrizA: 
    
    matriz_a = [0]*nmrLinha_a

    for i in range(nmrLinha_a):
        matriz_a[i] = [0]*nmrColuna_a


    matriz_a = adicionarNumRandoms(matriz_a, nmrLinha_a, nmrColuna_a)

    print("\nMatriz A preenchida: \n")
    for i in range(nmrLinha_a):
        for j in range(nmrColuna_a):
            print(matriz_a[i][j], end=" ")
        print("\n")
        
class MatrizB:

    nmrLinha_b = int(input("Digite o número de linhas da matriz B: "))
    nmrColuna_b = int(input("Digitne o número de colunas da matriz B: "))

    matriz_b = [0]*nmrLinha_b

    for i in range(nmrLinha_b):
        matriz_b[i] = [0]*nmrColuna_b

    matriz_a = adicionarNumRandoms(matriz_b, nmrLinha_b, nmrColuna_b)
    print("Matriz B preenchida: \n")
    for i in range(nmrLinha_b):
        for j in range(nmrColuna_b):
            print(matriz_b[i][j], end=" ")
        print("\n")

matrizC = concatMatrizes(MatrizA.matriz_a, MatrizB.matriz_b)
if matrizC != None:
    print("Matriz C: \n")
    for i in range(len(matrizC)):
        for j in range(len(matrizC[i])):
            print(matrizC[i][j], end=" ")
        print("\n")

