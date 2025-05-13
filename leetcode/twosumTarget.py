target = int(input("Informe o valor alvo: "))

numeros = list(map(int, input("Informe os números separados por espaço: ").split()))

def two_sum(nums, target):
    numComplementares =  []
    for i in range(len(nums)):
        complemento = target - nums[i]
        if complemento not in numComplementares: # Verifica se o complemento já foi encontrado   
            if complemento in nums[i+1:]:
                # Verifica se o complemento não é o próprio número
                numComplementares.append((nums[i], complemento))
    return numComplementares

result = two_sum(numeros, target)
if result:
    print(f"Os números que somam {target} são: {result}")
else:
    print(f"Não há números que somam {target} na lista.")