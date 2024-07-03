from config import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/listar_animais")
def listar_animais():
    with db_session:
        # obtém os animais
        animais = Animal.select() 
        return render_template("listar_.html", animais=animais)

@app.route("/form_adicionar_pessoa")
def form_adicionar_pessoa():
    return render_template("form_adicionar_pessoa.html")

@app.route("/adicionar_pessoa")
def adicionar_pessoa():
    # obter os parâmetros
    nome = request.args.get("nome")
    email = request.args.get("email")
    telefone = request.args.get("telefone")
    # salvar
    with db_session:
        # criar a pessoa
        p = Pessoa(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_pessoas")

app. run(debug=True)