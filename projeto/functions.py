import random

def adicionarValRandoms(matriz):
    for i in range(9):
        modelo = random.choice("Calça", "Camisa", "Blusa", "Shorts", "Casaco", "Jaqueta")
        if modelo == "Calça":
            preco = random.uniform(50, 200)
        elif modelo == "Camisa":
            preco = random.uniform(30, 150)
        elif modelo == "Blusa":
            preco = random.uniform(20, 100)
        elif modelo == "Shorts":
            preco = random.uniform(25, 80)
        elif modelo == "Casaco":
            preco = random.uniform(80, 300)
        elif modelo == "Jaqueta":
            preco = random.uniform(100, 400)
        matriz[i].append(f"Modelo: {modelo}, Preço: R${preco:.2f}")
        for j in range(i, 9):
            if modelo=="Camisa" or "Blusa" or  "Casaco" or "Jaqueta":
                tamanho = random.choice("P", "M", "G", "GG", "XG")
                matriz[i][j] = tamanho
            else:
                tamanho= random.randint(15, 30)
                matriz[i][j] = tamanho
    return matriz

def calcValorTotal(preco_unitario, quantidade):
    return preco_unitario * quantidade

def calcmaiorPreco(matriz_precos):
    maior_preco = 0
    for linha in matriz_precos:
        for preco in linha:
            if preco > maior_preco:
                maior_preco = preco
    return maior_preco

