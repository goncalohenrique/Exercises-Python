situacao = ""

# Solicita ao usuário as notas
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))
media =  (nota1 + nota2 + nota3 + nota4) / 4

if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10) or (nota3 < 0 or nota3 > 10) or (nota4 < 0 or nota4 > 10):
    print("Nota inválida. As notas devem estar entre 0 e 10.")
    exit()
# Verifica se as notas estão dentro do intervalo válido

# Verifica a situação do aluno
if media >= 7:
    situacao = "Aprovado"
elif media >= 4:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"
# Exibe a situação e a nota do aluno


print(f"Sua média é: {media:.2f}")