from flask import Flask, render_template, redirect, url_for

import cliente_form
from cliente import Cliente
from cliente_dao import ClienteDAO
from cliente_form import ClienteForm

app = Flask(__name__)

titulo_app = 'Zona Fit (GYM)'

app.config['SECRET_KEY'] = 'llave_secreta'

@app.route('/')
@app.route('/index')
def inicio():
    app.logger.debug('Entramos al path de inicio /')
    #Recuperamos clientes de la db
    clientes_db = ClienteDAO.seleccionar()

    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/guardar', methods=['POST'])
def guardar():
    cliente = Cliente()
    cliente_forma = ClienteForm(obj=cliente)
    if cliente_forma.validate_on_submit():
        cliente_forma.populate_obj(cliente)
        if not cliente.id:
            ClienteDAO.insertar(cliente)
        else:
            ClienteDAO.actualizar(cliente)
        return redirect(url_for('inicio'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    cliente_forma = ClienteForm(obj=cliente)
    clientes_db = ClienteDAO.seleccionar()
    return render_template('/index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)

@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))

@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    cliente = Cliente(id=id)
    ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))

if __name__ == "__main__":
    app.run(debug=True)