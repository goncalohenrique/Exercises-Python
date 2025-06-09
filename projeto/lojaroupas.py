import functions as fun

nomeProd = input("Digite o nome do produto: ")
precoUnit = float(input("Digite o preço unitário do produto: "))
qtdEstoque= int(input("Digite a quantidade em estoque: "))

# Lista de fornecedores
num = int(input("Digíte 0 para informar os forneceores: "))
fornecedores = []
if num == 0:
    print("Informe os fornecedores:")
    for i in range(10):
        fornecedor = input(f"Digite o nome do fornecedor {i+1}: ")
        fornecedores.append(fornecedor)
else:
    print("Nenhum fornecedor informado.")
    
# Matriz de preços por tamanhos
matModelos = [0]*10
for i in range(10):
    matModelos[i] = [0]*10
matModelos = fun.adicionarValRandoms(matModelos)

maiorPreco = fun.calcmaiorPreco(matModelos)
valor_total_estoque = fun.calcValorTotal(precoUnit, qtdEstoque)


print("\nMatriz de preços por modelos e tamanhos: \n")
for i in range(10):
    for j in range(10):
        print(matModelos[i][j], end=' ')
    print("\n")

if fornecedores==[]:
    print("Nenhum fornecedor informado.")
else:
    print("Lista de fornecedores: ")
    for i in range(9):
        print(f"Fornecedor {i+1}: {fornecedores[i]}")

print(f"\nValor total em estoque do produto {nomeProd}: R$ {valor_total_estoque:.2f}")
print(f"Maior preço na matriz de preços: R$ {maiorPreco:.2f}")

