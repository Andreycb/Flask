from flask import Flask

#Criando uma instancia da aplicação um (Objeto da classe)
app = Flask(__name__)  #O Argumento name é usado para determinar o local em que está a aplicação

#Definimos uma rota usando o decorador app.rout
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

""" #Usando o decorador app.add_url_rule
def index():
    return '<h1>Hello World!</h1>'

app.add_url_rule('/', 'index', index) """