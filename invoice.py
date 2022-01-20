'''
Funciones gestion facturas
'''
from PyQt5 import QtWidgets, QtCore

import conexion
import var
import locale
locale.setlocale(locale.LC_ALL, '')

class Facturas():
    def buscaCli(self):
        try:
            dni = var.ui.txtDNIfac.text().upper()
            var.ui.txtDNIfac.setText(dni)
            registro = conexion.Conexion.buscaClifac(dni)
            if registro:
                nombre = registro[0] + ", " + registro[1]
                var.ui.lblNomfac.setText(nombre)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("No existe el cliente")
                msg.exec()
        except Exception as error:
            print("Error al buscar cliente en Facturas", error)

    def facturar(self):
        try:
            registro = []
            dni = var.ui.txtDNIfac.text().upper()
            registro.append(str(dni))
            var.ui.txtDNIfac.setText(dni)
            fechaFac = var.ui.txtFechafac.text()
            registro.append(str(fechaFac))

            conexion.Conexion.altaFac(registro)
            conexion.Conexion.cargarTabFacturas(self)

            codFac = conexion.Conexion.buscaCodFac(self)
            var.ui.lblNumfac.setText(str(codFac))

        except Exception as error:
            print("Error al facturar cliente en Facturas", error)

    def cargaFac(self):
        try:
            fila = var.ui.tabFacturas.selectedItems()
            datos = [var.ui.lblNumfac, var.ui.txtFechafac]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i])
            #aqui cargamos el dni y el nombre cliente
            dni = conexion.Conexion.buscaDNIFac(row[0])
            var.ui.txtDNIfac.setText(str(dni))
            registro = conexion.Conexion.buscaClifac(dni)
            if registro:
                nombre = registro[0] + ", " + registro[1]
                var.ui.lblNomfac.setText(nombre)

        except Exception as error:
            print("Error en cargar facturas", error)

    def cargaCliFac(self):
        # carga datos de cliente en Facturación al seleccionar en tabla Clientes
        try:
            fila = var.ui.tabClientes.selectedItems() #seleccionamos fila en tab clientes
            datos = [var.ui.txtDNIfac, var.ui.lblNomfac]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i]) #cargamos los datos en las cajas de texto

            '''carga el dni y los apellidos, falta nombre'''

        except Exception as error:
            print("Error en cargar datos de un cliente en Facturación", error)

    def cargarLineaVenta(self):
        try:
            index = 0
            var.cmbProducto = QtWidgets.QComboBox()
            var.cmbProducto.setFixedSize(180,25)
            #cargar el combo
            conexion.Conexion.cargarCmbProducto(self)

            #var.txtCantidad = QtWidgets.QLineEdit()
            var.txtCantidad.setFixedSize(70,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)

            var.ui.tabVentas.setRowCount(index+1)
            var.ui.tabVentas.setCellWidget(index,1,var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index,3,var.txtCantidad)

        except Exception as error:
            print("Error al cargar linea venta", error)

    def procesoVenta(self):
        try:
            row = var.ui.tabVentas.currentRow()
            articulo= var.cmbProducto.currentText()
            dato = conexion.Conexion.obtenerCodPrecio(articulo)
            var.codpro = dato[0]
            var.ui.tabVentas.setItem(row, 2, QtWidgets.QTableWidgetItem(str(dato[1])))
            var.ui.tabVentas.item(row, 2).setTextAlignment(QtCore.Qt.AlignCenter)
            precio = dato[1].replace('€', '')
            var.precio = precio.replace(',', '.')

        except Exception as error:
            print("Error en proceso venta", error)

    def totalLineaVenta(self=None):
        try:
            venta = []
            row = var.ui.tabVentas.currentRow()
            cantidad = round(float(var.txtCantidad.text().replace(',', '.')),2)
            total_linea = round(float(var.precio) * float(cantidad),2)
            var.ui.tabVentas.setItem(row, 4, QtWidgets.QTableWidgetItem(str(total_linea) +" €"))
            var.ui.tabVentas.item(row, 4).setTextAlignment(QtCore.Qt.AlignRight)

            codfac= var.ui.lblNumfac.text()
            venta.append(int(codfac))
            venta.append(int(var.codpro))
            venta.append(float(var.precio))
            venta.append(float(cantidad))
            conexion.Conexion.cargarVenta(venta)
            var.txtCantidad.clearFocus()

        except Exception as error:
            print("Error en total linea venta", error)
