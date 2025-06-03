
def calcular_valor_total_em_estoque(preco_unitario, quantidade):
    """Calcula o valor total em estoque."""
    return preco_unitario * quantidade
def encontrar_maior_preco(matriz_precos):
    """Encontra o maior preço na matriz de preços."""
    maior_preco = float('-inf')  # Inicializa com o menor valor possível
    for linha in matriz_precos:
        for preco in linha:
            if preco > maior_preco:
                maior_preco = preco
    return maior_preco

nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade_estoque = int(input("Digite a quantidade em estoque: "))
    
    # Lista de fornecedores
fornecedores = []
num_fornecedores = int(input("Quantos fornecedores existem? "))
for _ in range(num_fornecedores):
    fornecedor = input("Digite o nome do fornecedor: ")
    fornecedores.append(fornecedor)
    
# Matriz de preços por modelo e tamanho
num_modelos = int(input("Quantos modelos existem? "))
num_tamanhos = int(input("Quantos tamanhos existem? "))
    
matriz_precos = []
for i in range(num_modelos):
    linha_precos = []
    for j in range(num_tamanhos):
        preco = float(input(f"Digite o preço do modelo {i+1}, tamanho {j+1}: "))
        linha_precos.append(preco)
        matriz_precos.append(linha_precos)
    
valor_total_estoque = calcular_valor_total_em_estoque(preco_unitario, quantidade_estoque)
maior_preco = encontrar_maior_preco(matriz_precos)
    
print(f"Valor total em estoque do produto '{nome_produto}': R$ {valor_total_estoque:.2f}")
print(f"Maior preço na matriz de preços: R$ {maior_preco:.2f}")