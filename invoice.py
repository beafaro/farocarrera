'''
Funciones gestion facturas
'''
from PyQt5 import QtWidgets, QtCore

import conexion, var, locale
locale.setlocale(locale.LC_ALL, '')

class Facturas():
    def buscaCli(self):
        """

        Módulo que se ejecuta con el botón búsqueda de cliente. Devuelve datos del cliente para el panel facturación.

        """
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
        """

        Módulo que a partir del DNI da de alta una factura con su número y fecha. Recarga la tabla facturas y muestra en el label el número de la factura generada.

        """
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
        """

        Módulo que al elegir una factura de la tabla facturas carga sus datos en el panel de facturación. Los datos son el DNI del cliente, fecha de factura y nombre del cliente.

        """
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
            conexion.Conexion.cargarLineasVenta(str(var.ui.lblNumfac.text()))

        except Exception as error:
            print("Error en cargar facturas", error)

    def cargaCliFac(self):
        """

        Módulo que carga datos del cliente en facturación al seleccionar en tabla Clientes.

        """
        try:
            fila = var.ui.tabClientes.selectedItems() #seleccionamos fila en tab clientes
            datos = [var.ui.txtDNIfac, var.ui.lblNomfac]
            if fila:
                row = [dato.text() for dato in fila]
            for i, dato in enumerate(datos):
                dato.setText(row[i]) #cargamos los datos en las cajas de texto
                #carga apellidos pero no nombre

        except Exception as error:
            print("Error en cargar datos de un cliente en Facturación", error)

    def cargaLineaVenta(index):
        """

        Carga una línea de venta en la fila de la tabla indicada por index correspondiente a una factura dada.
        :param index: la última línea de la tabla que carga las ventas de una factura
        :type index: int

        """
        try:
            var.cmbProducto = QtWidgets.QComboBox()
            var.cmbProducto.currentIndexChanged.connect(Facturas.procesoVenta)
            var.cmbProducto.setFixedSize(170,25)
            conexion.Conexion.cargarCmbProducto(self=None)
            var.txtCantidad = QtWidgets.QLineEdit()
            var.txtCantidad.editingFinished.connect(Facturas.totalLineaVenta)
            var.txtCantidad.setFixedSize(80,25)
            var.txtCantidad.setAlignment(QtCore.Qt.AlignCenter)

            var.ui.tabVentas.setRowCount(index +1)
            var.ui.tabVentas.setCellWidget(index, 1, var.cmbProducto)
            var.ui.tabVentas.setCellWidget(index, 3, var.txtCantidad)

        except Exception as error:
            print("Error al cargar linea venta", error)

    def procesoVenta(self):
        """

        Módulo que carga el precio de un artículo al seleccionarlo en el combo de artículos.

        """
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
        """

        Módulo que al anotar la cantidad de producto indica el total del precio de la venta realizada. Al mismo tiempo recarga la tabla de línea de venta incluyendo las anteriores y la realizada.

        """
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
            conexion.Conexion.cargarLineasVenta(codfac)

        except Exception as error:
            print("Error en total linea venta", error)
