from flask import jsonify
from models.producto_model import ProductoModel

class ProductoController:
    @staticmethod
    def get_productos():
        productos = ProductoModel.listar_productos()
        if productos is not None:
            return jsonify({'productos': productos, 'mensaje': 'productos listados'})
        else:
            return jsonify({'mensaje': 'Error de servidor'})
