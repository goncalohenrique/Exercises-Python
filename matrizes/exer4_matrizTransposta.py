def matrizTransposta(matriz):

    # Cria uma nova matriz com as dimensões invertidas
    transposta = [[0 for _ in range(len(matriz))] for _ in range(len(matriz[0]))]
    
    # Preenche a matriz transposta
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            transposta[j][i] = matriz[i][j]