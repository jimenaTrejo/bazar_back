from flask_mysqldb import MySQL

class ProductoModel:
    @staticmethod
    def listar_productos(conexion):
        try:
            cursor = conexion.connection.cursor()
            # sql = "SELECT id, title, description, price, stock, category, image FROM productos"
            sql = "SELECT * FROM productos"

            cursor.execute(sql)
            datos = cursor.fetchall()
            productos = [
                {
                    'id': fila[0],
                    'title': fila[1],
                    'description': fila[2],
                    'price': fila[3],
                    'discountPercentage': fila[4],
                    'rating': fila[5],
                    'stock': fila[6],
                    'brand': fila[7],
                    'category': fila[8],
                    'thumbnail': fila[9],
                    'images': fila[10],  # Suponiendo que las imágenes están almacenadas como JSON
                }
                for fila in datos
            ]
            return productos
        except Exception as ex:
            return None

    @staticmethod
    def obtener_producto(conexion, id):
        try:
            cursor = conexion.connection.cursor()
            sql = "SELECT id, title, description, price, stock, category, image FROM producto WHERE id = %s"
            cursor.execute(sql, (id,))
            datos = cursor.fetchone()
            if datos is not None:
                producto = {'id': datos[0], 'title': datos[1], 'description': datos[2], 'price': datos[3],
                            'stock': datos[4], 'category': datos[5], 'image': datos[6]}
                return producto
            else:
                return None
        except Exception as ex:
            return None
