import random

def adicionarValRandoms(matriz):
    modelos_roupa = ["Calça", "Camisa", "Blusa", "Shorts", "Casaco", "Jaqueta"]
    tamanhos_roupa = ["P", "M", "G", "GG", "XG"]
    for i in range(10):
        for j in range(10):
            if i == 0:
                if j == 0:
                    matriz[i][j] = "Tamanho"
                else:
                    modelo = random.choice(modelos_roupa)
                    matriz[0][j] = modelo
            else:
                if j == 0:
                    if modelo == "Camisa" or  "Blusa" or"Casaco" or "Jaqueta":
                        tamanho = random.choice(tamanhos_roupa)
                        matriz[i][0] = tamanho
                    else:
                        tamanho = random.randint(15, 30)
                        matriz[i][0] = tamanho
                else:
                    preco = random.uniform(100, 400)
                    matriz[i][j] = round(preco, 2)
    return matriz

def calcValorTotal(preco_unitario, quantidade):
    return preco_unitario * quantidade

def calcmaiorPreco(mat):
    maior_preco = 0
    for i in range(1, 10):
        for j in range(1, 10):
            preco = mat[i][j]
            if preco > maior_preco:
                maior_preco = preco
    return maior_preco

import random

