especie = str(input("Informe a espécie do animal: "))
peso = float(input("Informe o peso do animal: "))
altura = float(input("Informe a altura do animal: "))
cor = str(input("Informe a cor do animal: "))
idade = int(input("Informe a idade do animal: "))
# Definindo a classe Animal

class Animal:
    def __init__(self, especie, peso, altura, cor, idade):
        self.especie = especie
        self.peso = peso
        self.altura = altura
        self.cor = cor
        self.idade = idade

    def __str__(self):
        return f"Espécie: {self.especie}, Peso: {self.peso}, Altura: {self.altura}, Cor: {self.cor}, Idade: {self.idade}"
    def __repr__(self):
        return f"Animal({self.especie}, {self.peso}, {self.altura}, {self.cor}, {self.idade})"
    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.especie == other.especie and self.peso == other.peso and self.altura == other.altura and self.cor == other.cor and self.idade == other.idade
        return False
    def __ne__(self, other):
        if isinstance(other, Animal):
            return not self.__eq__(other)
        return True
    def __lt__(self, other):
        if isinstance(other, Animal):
            return self.idade < other.idade
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Animal):
            return self.idade <= other.idade
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Animal):
            return self.idade > other.idade
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, Animal):
            return self.idade >= other.idade
        return NotImplemented
    
    