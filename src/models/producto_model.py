from flask_mysqldb import MySQL

class ProductoModel:
    @staticmethod
    def listar_productos(conexion):
        try:
            cursor = conexion.connection.cursor()
            sql = "SELECT title, description, price, stock, category, image FROM producto"
            cursor.execute(sql)
            datos = cursor.fetchall()
            productos = [{ 'title': fila[0], 'description': fila[1], 'price': fila[2],
                        'stock': fila[3], 'category': fila[4], 'image': fila[5]} for fila in datos]
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
