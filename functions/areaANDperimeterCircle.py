import math as m

print("Calculadora de perímetro e área de círculo")

def calcArea(raio):
    area = m.pi *(raio**2)
    return area

def calcPerimetro(raio):
    perimetro = 2 *m.pi *raio
    return perimetro

i=1

while(i==1):
    i = int(input("Dígite 1 para fazer o cálculo ou 0 para sair: ")) 
    if(i==1): 
        raio = float(input("Informe o raio do círculo: "))
        print(f"A área do círculo é: {calcArea(raio):.4f}")
        print(f"O perímetro do círculo é: {calcPerimetro(raio):.4f}")
    elif(i==0):
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")
        i=1




