from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista fixa de filmes
filmes = [
    {'codigo': 1, 'nome': 'Pânico', 'gênero': 'Terror slasher', 'ano': 1999},
    {'codigo': 2, 'nome': 'Sabrina', 'gênero': 'Romance, Comédia', 'ano': 1954},
    {'codigo': 3, 'nome': 'Orgulho e Preconceito', 'gênero': 'Romance', 'ano': 2005}
]

@app.route('/')
def index():
    return render_template('index.html', filmes=filmes)

@app.route('/adicionar_filme', methods=['GET', 'POST'])
def adicionar_filme():
    if request.method == 'POST':
        nome = request.form['nome']
        genero = request.form['genero']
        ano = int(request.form['ano'])
        codigo = len(filmes) + 1  # Define um novo código para o filme
        filmes.append({'codigo': codigo, 'nome': nome, 'gênero': genero, 'ano': ano})
        return redirect('/')
    else:
        return render_template('adicionar_filme.html')

@app.route('/editar_filme/<int:codigo>', methods=['GET', 'POST'])
def editar_filme(codigo):
    filme = next((f for f in filmes if f['codigo'] == codigo), None)
    if request.method == 'POST':
        filme['nome'] = request.form['nome']
        filme['gênero'] = request.form['genero']
        filme['ano'] = int(request.form['ano'])
        return redirect('/')
    else:
        return render_template('editar_filme.html', filme=filme)

@app.route('/apagar_filme/<int:codigo>')
def apagar_filme(codigo):
    global filmes
    filmes = [f for f in filmes if f['codigo'] != codigo]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
