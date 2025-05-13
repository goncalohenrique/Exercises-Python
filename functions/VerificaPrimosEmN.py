numLimite = int(input("Informe o número limíte: "))

i = 2

def VerificaPrimosEmN(numLimi):
    qtdPrimos = 0
    primos = [] 
    for i in range(2, numLimi+1):
        j=2
        primo = True
        #Faz um loop de 2, ate a raiz quadrada do número
        for j in range(2, int(i**0.5)+1):
            # Verifica se o número é divisível por algum número menor que ele
            # e maior que 1
            # Se for divisível, não é primo
            if (i%j==0):
                primo = False
                break
            j +=1
        if (primo):
            qtdPrimos +=1
            primos.append(i)    
        i+=1

    return qtdPrimos, primos

qtdPrimos, primos = VerificaPrimosEmN(numLimite)

print(f"Há {qtdPrimos} números primos entre 0 e {numLimite} \nEles são: {primos}")
        
            
          