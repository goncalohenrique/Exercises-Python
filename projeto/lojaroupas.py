import functions as fun
 
nomeProd = input("Digite o nome do produto: ")
precoUnit = float(input("Digite o preço unitário do produto: "))
qtdEstoque= int(input("Digite a quantidade em estoque: "))

valor_total_estoque = fun.calcValorTotal(precoUnit, qtdEstoque)
maiorPreco = fun.calcmaiorPreco(matPrecos)
    
print(f"Valor total em estoque do produto '{nomeProd}': R$ {valor_total_estoque:.2f}")
print(f"Maior preço na matriz de preços: R$ {maiorPreco:.2f}")

    # Lista de fornecedores
fornecedores = []
for i in range(9):
    fornecedor = input(f"Digite o nome do fornecedor {i+1}: ")
    fornecedores.append(fornecedor)
    
    # Matriz de preços por modelo e tamanho
matModelos = [0]*9
for i in range(9):
    matModelos[i] = [0]*9
matModelos = fun.adicionarValRandoms(matModelos)



print("Matriz de modelos e tamanhos:")
for i in range(9):
    print(f"Modelo {i+1}: {matModelos[i]}", end=' ')
    for j in range(9):
        if matModelos[i][j] != 0:
            print(f"Preço {j+1}: {matModelos[i][j]}", end=' ')
    print("\n")

