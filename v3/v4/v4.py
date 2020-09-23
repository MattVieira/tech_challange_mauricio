import random, json
from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)


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
                return 1000.00
            else:
                return credito
        elif 800 <= self.score <= 950:
            return self.renda * 2.0
        elif 951 <= self.score <= 999:
            return 1000000.00


cliente1 = Cliente('Mauricio', '12345678901', 1900.20, random.randint(1, 999))
cliente2 = Cliente('Juliana', '98765432101', 1400.05, random.randint(1, 999))
cliente3 = Cliente('Mariselma', '12312312312', 2500.60, random.randint(1, 999))
lista = [cliente1, cliente2, cliente3]


@app.route('/')
def index():
    return render_template('lista.html', titulo='Usuários', users=lista)


@app.route('/nova')
def nova():
    return render_template('nova.html', titulo='Nova Solicitação')


@app.route('/adicionar', methods=['POST', ])
def adicionar():
    nome = request.form['nome']
    cpf = request.form['cpf']
    renda = request.form['renda']
    client = Cliente(nome, cpf, renda, random.randint(1, 999))
    lista.append(client)
    return redirect(url_for('index'))


app.run(debug=True)
