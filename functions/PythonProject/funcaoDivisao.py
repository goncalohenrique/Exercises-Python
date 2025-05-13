print("Divisão de 2 números")

def dividir (n1,n2):
 return n1/ n2

n1 = int(input("Digíte o numerador: "))
n2 = int(input("Digíte o denominador: "))
if n2==0:
    print("O denominador não pode ser 0!!")
else:
    print(f"A divisão dos números {n1} e {n2} é {dividir(n1, n2)}")
