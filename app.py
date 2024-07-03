from config import *
from model import *

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/listar_cabelos")
def listar_cabelos():
    with db_session:
        # obtém os cabelos
        cabelos = Cabelo.select() 
        return render_template("listar_cabelos.html", cabelos=cabelos)

@app.route("/form_adicionar_cabelo")
def form_adicionar_cabelo():
    return render_template("form_adicionar_cabelo.html")

@app.route("/adicionar_cabelo")
def adicionar_cavelo():
    # obter os parâmetros
    tipo = request.args.get("tipo")
    corte = request.args.get("corte")
    cor = request.args.get("cor")
    idade= request.args.get("idade")
    comprimento = request.args.get("comprimento")
    # salvar
    with db_session:
        # criar o cabelo
        a = Cabelo(**request.args)
        # salvar
        commit()
        # encaminhar de volta para a listagem
        return redirect("listar_cabelos")
    
app.run(debug=True)