from flask import jsonify
from models.producto_model import ProductoModel

class ProductoDetalleController:
    @staticmethod
    def get_producto(id):
        try:
            producto = ProductoModel.obtener_producto(id)
            if producto is not None:
                return jsonify({'producto': producto, 'mensaje': 'producto leído'})
            else:
                return jsonify({'mensaje': 'Producto no encontrado'})
        except Exception as ex:
            return jsonify({'mensaje': 'Error de servidor'})
