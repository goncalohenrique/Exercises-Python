def calcular_fatorial(numero):
    if numero < 0:
        return "Fatorial não é definido para números negativos."
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    return fatorial

# Solicita ao usuário um número
try:
    numero = int(input("Digite um número para calcular o fatorial: "))
    print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
# O código acima calcula o fatorial de um número inteiro não negativo.
# O fatorial de um número n é o produto de todos os inteiros positivos menores ou iguais a n.
# O fatorial de 0 é definido como 1.
# O código também lida com a entrada do usuário, garantindo que um número inteiro válido seja fornecido.
# O tratamento de exceções é usado para capturar entradas inválidas.
# O resultado é impresso na tela.
# O código é simples e direto, utilizando um loop para calcular o fatorial.
# O código pode ser melhorado com a adição de comentários e documentação.
# O código pode ser otimizado usando recursão ou memoização para melhorar a eficiência.
# O código pode ser testado com diferentes entradas para verificar sua precisão.
# O código pode ser expandido para incluir uma função que calcule o fatorial de números negativos,
# embora o fatorial não seja definido para esses números.
# O código pode ser modificado para aceitar entradas de ponto flutuante,
# embora o fatorial não seja definido para esses números.
# O código pode ser adaptado para calcular o fatorial de números muito grandes,
# embora isso possa exigir o uso de bibliotecas especializadas para lidar com grandes números.
# O código pode ser integrado a uma interface gráfica para facilitar o uso.
# O código pode ser usado como base para um programa maior que envolva cálculos matemáticos.
# O código pode ser usado como um exercício de programação para iniciantes.
# O código pode ser usado como um exemplo de boas práticas de programação,
# incluindo tratamento de exceções e validação de entrada.
# O código pode ser usado como um exemplo de como calcular o fatorial de um número
# usando um loop em vez de recursão.
# O código pode ser usado como um exemplo de como calcular o fatorial de um número
# usando recursão em vez de um loop.
# O código pode ser usado como um exemplo de como calcular o fatorial de um número