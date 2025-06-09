import random

def adicionarValRandoms(matrizmod):
    modelos_roupa = ["Calça", "Camisa", "Blusa", "Shorts", "Casaco", "Jaqueta"]
    tamanhos_roupa = ["PP", "P", "M", "G", "GG", "XG"]
    for i in range(10):
        for j in range(10):
            if i == 0:
                if j == 0:
                    matrizmod[i][j] = "Tamanho"
                else:
                    modelo = random.choice(modelos_roupa)
                    matrizmod[0][j] = modelo
            else:
                if j == 0:
                    if modelo == "Camisa" or  "Blusa" or"Casaco" or "Jaqueta":
                        tamanho = random.choice(tamanhos_roupa)
                        matrizmod[i][0] = tamanho
                    else:
                        tamanho = random.randint(15, 30)
                        matrizmod[i][0] = tamanho
                else:
                    preco = random.uniform(100, 400)
                    matrizmod[i][j] = round(preco, 2)
    return matrizmod

def calcValorTotal(preco_unitario, quantidade):
    return preco_unitario * quantidade

def calcmaiorPreco(mat):
    maiorPreco = 0
    for i in range(1, 10):
        for j in range(1, 10):
            preco = mat[i][j]
            if preco > maiorPreco:
                maiorPreco = preco
    return maiorPreco


