import random


class Cliente:
    def __init__(self, nome, cpf, renda, score):
        self.nome = nome
        self.cpf = cpf
        self.renda = renda
        self.score = score

    def credito(self):
        if 1 <= self.score <= 299:
            return "Reprovado"
        elif 300 <= self.score <= 599:
            return 1000.00
        elif 600 <= self.score <= 799:
            credito = self.renda * 0.5
            if credito < 1000:
                return 1000
            else:
                return credito
        elif 800 <= self.score <= 950:
            return self.renda * 2
        elif 951 <= self.score <= 999:
            return 1000000.00


cliente1 = Cliente('Mauricio', '12345678901', 1900.00, random.randint(1, 999))

print(f"{cliente1.nome} seu score é de {cliente1.score}")
print(f"Situação do Crédito: {cliente1.credito()}")
