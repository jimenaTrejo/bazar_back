from flask import Flask, jsonify, request, make_response
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
from config import config
from models.producto_model import ProductoModel

app = Flask(__name__)
conexion = MySQL(app)

# Habilita CORS solo para las rutas específicas
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


# Rutas
@app.route('/')
def listar():
    return ("hoolaa")


# Rutas
@app.route('/productos', methods=['GET', 'OPTIONS'])
@cross_origin()
def listar_productos():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    productos = ProductoModel.listar_productos(conexion)
    if productos is not None:
        return jsonify({'productos': productos, 'mensaje': 'productos listados'})
    else:
        return jsonify({'mensaje': 'Error de servidor'})




@app.route('/productos/<int:id>')
def leer_producto(id):
    producto = ProductoModel.obtener_producto(conexion, id)
    if producto is not None:
        return jsonify({'producto': producto, 'mensaje': 'producto leído'})
    else:
        return jsonify({'mensaje': 'Producto no encontrado'})

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
