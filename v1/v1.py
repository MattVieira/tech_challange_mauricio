import random

print("#Solicitação de Cartão#")
nome = input("Digite seu nome: ")
cpf = input("Digite seu cpf: ")
renda = float(input("Qual a sua renda mensal: "))
score = random.randint(1, 999)

if 1 <= score <= 299:
    credito = "Reprovado"
elif 300 <= score <= 599:
    credito = 1000.00
elif 600 <= score <= 799:
    credito = renda * 0.5
    if credito < 1000:
        credito = 1000
elif 800 <= score <= 950:
    credito = renda * 2
elif 951 <= score <= 999:
    credito = 1000000.00

print(f"{nome} seu score é de {score}")
print(f"Situação do Crédito: {credito}")
