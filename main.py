from flask import Flask, render_template, request, url_for, redirect
import repositorio

app = Flask(__name__)

@app.route('/')
def home():
    dicionario = repositorio.retornar_personagens()
    return render_template("index.html", dados=dicionario)

@app.route("/adicionar_personagem", methods=['GET', 'POST'])
def adicionar_personagem():
    if request.method == "POST":
        nome = request.form['nome']
        tipo = request.form['personagem']
        origem = request.form['origem']
        
        novo_id = repositorio.criar_personagem(nome, tipo, origem)
        
        return redirect(url_for('home'))
    else:
        return render_template("cadastro.html")

@app.route("/excluir_personagem/<int:id>", methods=['POST'])
def excluir_personagem(id):
    if request.method == "POST":
        repositorio.remover_personagem(id)
    return redirect(url_for('home'))

@app.route("/personagem/<int:id>", methods=['GET', 'POST'])
def editar_personagem(id):
    if request.method == "POST":
        if "excluir" in request.form:
            repositorio.remover_personagem(id)
            return redirect(url_for('home'))
        else:
            if 'nome' in request.form:
                nome = request.form['nome']
                tipo = request.form['personagem']
                origem = request.form['origem']
                
                repositorio.editar_personagem(id, nome, tipo, origem)
                
                return redirect(url_for('home'))
            else:
                # Tratar o caso em que o campo 'nome' não está presente no formulário
                return "Erro: Nome não encontrado no formulário."
    else:
        personagem = repositorio.retornar_personagem(id)
        personagem['id'] = id
        return render_template("cadastro.html", **personagem)


app.run(debug=True)
