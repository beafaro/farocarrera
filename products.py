'''
Funciones gestión productos
'''

import conexion
import var
from window import *

class Productos():
    def guardaProd(self):
        try:
            newProd = []
            producto = [var.ui.txtCodigo, var.ui.txtNomProd, var.ui.txtPrecio]
            tabProd = []
            product = [var.ui.txtCodigo, var.ui.txtNomProd, var.ui.txtPrecio]

            for i in producto:
                newProd.append(i.text())
            for i in product:
                tabProd.append(i.text())

            row = 0
            column = 0
            var.ui.tabProductos.insertRow(row)
            for campo in tabProd:
                cell = QtWidgets.QTableWidgetItem(str(campo))
                var.ui.tabProductos.setItem(row, column, cell)
                column += 1
            conexion.Conexion.altaProd(newProd)
        except Exception as error:
            print("Error en guardar productos", error)

    def limpiaFormProd(self):
        try:
            cajas = [var.ui.txtCodigo, var.ui.txtNomProd, var.ui.txtPrecio]
            for i in cajas:
                i.setText("")
        except Exception as error:
            print("Error al limpiar formulario de productos", error)

    def cargaProd(self):
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
        try:
            codigo = var.ui.txtCodigo.text()
            conexion.Conexion.bajaProd(codigo)
            conexion.Conexion.cargarTabProd(self)
        except Exception as error:
            print('Error en baja cliente ', error)

    def modifProd(self):
        try:
            modProducto = []
            producto = [var.ui.txtCodigo, var.ui.txtNomProd, var.ui.txtPrecio]
            for i in producto:
                modProducto.append(i.text())
            conexion.Conexion.modifProd(modProducto)
            conexion.Conexion.cargarTabProd(self)
        except Exception as error:
            print("Error al modificar producto", error)
