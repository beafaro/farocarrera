'''
Funciones gestión productos
'''

import conexion
import var
import locale
locale.setlocale(locale.LC_ALL, '')

class Productos():
    def guardaProd(self):
        """

        Módulo que guarda un producto en la base de datos.

        """
        try:
            newProd = []
            producto = var.ui.txtNomProd.text()
            producto = producto.title()
            newProd.append(producto)

            precio = var.ui.txtPrecio.text()
            precio = precio.replace (',','.')
            precio = locale.currency(float(precio))
            newProd.append(precio)

            conexion.Conexion.altaProd(newProd)
            conexion.Conexion.cargarTabProd(self)
            conexion.Conexion.cargarCmbProducto(self)

        except Exception as error:
            print("Error en guardar productos", error)

    def limpiaFormProd(self):
        """

        Módulo que limpia el formulario que pide o muestra los datos de un producto.

        """
        try:
            #file = var.ui.tabProd.selectItems()
            cajas = [var.ui.txtCodigo, var.ui.txtNomProd, var.ui.txtPrecio]
            for i in cajas:
                i.setText("")
        except Exception as error:
            print("Error al limpiar formulario de productos", error)

    def cargaProd(self):
        """

        Módulo que carga los datos de un producto seleccionado.

        """
        try:
            Productos.limpiaFormProd(self)
            fila = var.ui.tabProductos.selectedItems()
            datos = [var.ui.txtCodigo, var.ui.txtNomProd, var.ui.txtPrecio]
            if fila:
                row = [dato.text() for dato in fila]

            for i, dato in enumerate(datos):
                dato.setText(row[i])

            registro = conexion.Conexion.oneCodigo(row[0])
            var.ui.txtNomProd.setText(str(registro[0]))
            var.ui.txtPrecio.setText(str(registro[1]))
        except Exception as error:
            print("Error en cargar datos de un producto", error)

    def bajaProd(self):
        """

        Módulo que da de baja un producto haciendo llamada a la función "bajaProd" de conexión.

        """
        try:
            codigo = var.ui.txtCodigo.text()
            conexion.Conexion.bajaProd(codigo)
            conexion.Conexion.cargarTabProd(self)
        except Exception as error:
            print('Error en baja cliente ', error)

    def modifProd(self):
        """

        Módulo que permite modificar un producto haciendo llamada a la función "modifProd" de conexion y después volviendo a cargar la tabla de productos.

        """
        try:
            modProducto = []
            producto = [var.ui.txtCodigo, var.ui.txtNomProd, var.ui.txtPrecio]
            for i in producto:
                modProducto.append(i.text())
            conexion.Conexion.modifProd(modProducto)
            conexion.Conexion.cargarTabProd(self)
        except Exception as error:
            print("Error al modificar producto", error)
