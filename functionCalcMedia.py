
# Função para calcular a média de 3 notas
def calcularMedia(nota1, nota2, nota3):
    
    return (nota1 + nota2 + nota3) / 3


qntdLoop = int(input("Deseja calcular a média de quantos alunos? "))
i = 0

if(qntdLoop>0):

    for i in range(qntdLoop):
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))

        if(nota1 >= 0 and nota1 <=10)and (nota2 >= 0 and nota2 <= 10) and (nota3 >= 0 and nota3 <= 10):
            print(f"A média do aluno {i+1}, é: {calcularMedia(nota1, nota2, nota3)}")
        else:
            print("Notas inválidas, informe notas entre 0 e 10")
            break;
else: 
    print("Número de loops inválido, informe um número maior que 0!")