class Solution:
    numeros = list(map(int, input("Informe os números separados por espaço: ").split()))
    target = int(input("Informe o valor alvo: "))
    '''nums = [2, 7, 11, 15]
    target = 9'''

    #função que retorna os índices dos números que somam o valor alvo
    def twoSum(nums, target):
        numComplementares =  []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    #numComplementares.append(i, j)
                    return i, j
        return numComplementares


    result = twoSum(numeros, target)
    if result:
        print(f"Os números que somam {target} são: {result}")
    else:
        print(f"Não há números que somam {target} na lista.")

  
    

