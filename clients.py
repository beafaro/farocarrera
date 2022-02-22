'''
Funciones gestion clientes
'''
from PyQt5 import QtSql

import conexion
import var
from window import *
from PyQt5.QtWidgets import QMessageBox


class Clientes():
    def validarDNI(dni):
        """

        Módulo que valida si el DNI que introducimos es correcto o falso.
        Si es correcto muestra un ckeck en verde. Si es falso muestra una cruz y el fondo del campo en rojo.

        """
        try:
            global dniValido
            dniValido = False
            dni = var.ui.txtDNI.text()
            var.ui.txtDNI.setText(dni.upper())
            tabla = "TRWAGMYFPDXBNJZSQVHLCKE" #LETRAS DNI
            dig_ext = "XYZ"                   #LETRAS NIE
            reemp_dig_ext = { "X": "0", "Y": "1", "Z": "2" }
            numeros = "1234567890"
            dni = dni.upper()  #convertir la letra en mayúsculas
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.lblValidoDNI.setStyleSheet("QLabel {color: green;}")
                    var.ui.lblValidoDNI.setText("V")
                    var.ui.txtDNI.setStyleSheet("background-color: white;")
                    dniValido= True
                    return True
                else:
                    var.ui.lblValidoDNI.setStyleSheet("QLabel {color: red;}")
                    var.ui.lblValidoDNI.setText("X")
                    var.ui.txtDNI.setStyleSheet("background-color: pink;")
            else:
                var.ui.lblValidoDNI.setStyleSheet("QLabel {color: red;}")
                var.ui.lblValidoDNI.setText("X")
                var.ui.txtDNI.setStyleSheet("background-color: pink;")
        except Exception as error:
            print("Error en módulo validar DNI", error)

    # def SelSexo(self):
    #     try:
    #         if var.ui.rbtFem.isChecked():
    #             print("Has marcado mujer")
    #         if var.ui.rbtHom.isChecked():
    #             print("Has marcado hombre")
    #     except Exception as error:
    #         print("Error en módulo seleccionar género:", error)

    # def SelPago(self):
    #     try:
    #         if var.ui.chkEfectivo.isChecked():
    #             print("Has seleccionado efectivo")
    #         if var.ui.chkTarjeta.isChecked():
    #             print("Has seleccionado tarjeta")
    #         if var.ui.chkCargoCuenta.isChecked():
    #             print("Has seleccionado cargo cuenta")
    #         if var.ui.chkTransfe.isChecked():
    #             print("Has seleccionado transferencia")
    #     except Exception as error:
    #         print("Error en módulo seleccionar forma de pago:", error)

    # def SelProv(prov):
    #     try:
    #         print("Has seleccionado la provincia de", prov)
    #         return prov
    #     except Exception as error:
    #         print("Error en módulo seleccionar provincia, ", error)

    def cargarFecha(qDate):
        """

        Módulo que carga la fecha de alta del cliente en la caja de texto correspondiente.

        """
        try:
            data = (str(qDate.day()).zfill(2) + "/" + str(qDate.month()).zfill(2) + "/" +str(qDate.year()))
            if var.ui.TabPrograma.currentIndex() == 0:
                var.ui.txtFechaAltaCli.setText(str(data))
            elif var.ui.TabPrograma.currentIndex() == 1:
                var.ui.txtFechafac.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print("Error cargar fecha de txtFecha", error)

    def letraCapital():
        """

        Módulo que pone la primera letra en mayúsculas de los campos de apellidos, nombre y dirección.

        """
        try:
            apellidos = var.ui.txtApel.text()
            var.ui.txtApel.setText(apellidos.title())

            nome = var.ui.txtNome.text()
            var.ui.txtNome.setText(nome.title())

            direccion = var.ui.txtDir.text()
            var.ui.txtDir.setText(direccion.title())
        except Exception as error:
            print("Error al poner la primera letra en mayúscula", error)

    def guardaCli(self):
        """

        Módulo que guarda todos los datos del cliente en la base de datos llamando a la función "altaCli" de Conexion.

        """
        try:
            # preparamos el registro
            newCli = [] #para la base de datos
            cliente = [var.ui.txtDNI, var.ui.txtFechaAltaCli, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]
            tabCli = [] #para la tablewidget
            client = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtFechaAltaCli, var.ui.txtDir]

            # código para cargar en la tabla el cliente y la forma de pago
            for i in cliente:
                newCli.append(i.text())
            for i in client:
                tabCli.append(i.text())

            newCli.append(var.ui.cmbProv.currentText())
            newCli.append(var.ui.cmbMuni.currentText())

            if var.ui.rbtHom.isChecked():
                newCli.append("Hombre")
            elif var.ui.rbtFem.isChecked:
                newCli.append("Mujer")

            pagos = []
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append("Cargo cuenta")
            if var.ui.chkEfectivo.isChecked():
                pagos.append("Efectivo")
            if var.ui.chkTransfe.isChecked():
                pagos.append("Transferencia")
            if var.ui.chkTarjeta.isChecked():
                pagos.append("Tarjeta")
            pagos = set(pagos) #evito duplicados
            newCli.append(", ".join(pagos))
            tabCli.append(", ".join(pagos))

            # cargamos la tabla
            if dniValido:
                row = 0
                column = 0
                var.ui.tabClientes.insertRow(row)
                for campo in tabCli:
                    cell = QtWidgets.QTableWidgetItem(str(campo))
                    var.ui.tabClientes.setItem(row, column, cell)
                    column += 1
                conexion.Conexion.altaCli(newCli)
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText("DNI no válido")
                msg.exec()

        except Exception as error:
            print("Error en guardar clientes", error)

    def limpiaFormCli(self):
        """

        Módulo que limpia el formulario que pide o muestra los datos de un cliente.

        """
        try:
            cajas = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtFechaAltaCli, var.ui.txtDir]
            for i in cajas:
                i.setText("")
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtHom.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
            var.ui.chkTarjeta.setChecked(False)
            var.ui.chkTransfe.setChecked(False)
            var.ui.chkEfectivo.setChecked(False)
            var.ui.chkCargoCuenta.setChecked(False)
            var.ui.cmbProv.setCurrentIndex(0)
            var.ui.cmbMuni.setCurrentIndex(0)
        except Exception as error:
            print("Error al limpiar formulario de clientes", error)

    def cargaCli(self):
        """

        Módulo que carga los datos de un cliente al seleccionarlo en la tabla de clientes.

        """
        try:
            Clientes.limpiaFormCli(self)
            fila = var.ui.tabClientes.selectedItems() #seleccionamos fila
            datos = [var.ui.txtDNI, var.ui.txtApel, var.ui.txtNome, var.ui.txtFechaAltaCli]
            if fila:
                row = [dato.text() for dato in fila]

            for i, dato in enumerate(datos):
                dato.setText(row[i]) #cargamos los datos en las cajas de texto

            if "Efectivo" in row[4]:
                var.ui.chkEfectivo.setChecked(True)
            if "Transferencia" in row[4]:
                var.ui.chkTransfe.setChecked(True)
            if "Tarjeta" in row[4]:
                var.ui.chkTarjeta.setChecked(True)
            if "Cargo" in row[4]:
                var.ui.chkCargoCuenta.setChecked(True)

            registro = conexion.Conexion.oneCli(row[0])
            var.ui.txtDir.setText(str(registro[0]))
            var.ui.cmbProv.setCurrentText(str(registro[1]))
            var.ui.cmbMuni.setCurrentText(str(registro[2]))
            if str(registro[3]) == 'Hombre':
                var.ui.rbtHom.setChecked(True)
            else:
                var.ui.rbtFem.setChecked(True)

        except Exception as error:
            print("Error en cargar datos de un cliente", error)

    def bajaCli(self):
        """

        Módulo que da de baja a un cliente. Utiliza de Conexion las funciones "bajaCli" y "cargarTabCli" para eliminar el cliente de la base de datos y actualizar la tabla de clientes.

        """
        try:
            dni = var.ui.txtDNI.text()
            conexion.Conexion.bajaCli(dni)
            conexion.Conexion.cargarTabCli(self)

        except Exception as error:
            print('Error en baja cliente ', error)

    def modifCli(self):
        """

        Módulo que modifica un cliente. Recoge todos los datos de un cliente seleccionado y se llama a la función "modifCli" de Conexion para guardar los cambios.

        """
        try:
            modCliente = []
            cliente = [var.ui.txtDNI, var.ui.txtFechaAltaCli, var.ui.txtApel, var.ui.txtNome, var.ui.txtDir]
            #cojo todas las celdas que hay en cliente y las voy metiendo en modCliente
            for i in cliente:
                modCliente.append(i.text())

            modCliente.append(var.ui.cmbProv.currentText())
            modCliente.append(var.ui.cmbMuni.currentText())

            if var.ui.rbtHom.isChecked():
                modCliente.append("Hombre")
            elif var.ui.rbtFem.isChecked:
                modCliente.append("Mujer")

            pagos = []
            if var.ui.chkCargoCuenta.isChecked():
                pagos.append("Cargo cuenta")
            if var.ui.chkEfectivo.isChecked():
                pagos.append("Efectivo")
            if var.ui.chkTransfe.isChecked():
                pagos.append("Transferencia")
            if var.ui.chkTarjeta.isChecked():
                pagos.append("Tarjeta")
            pagos = set(pagos) #evito duplicados
            modCliente.append(", ".join(pagos))
            conexion.Conexion.modifCli(modCliente)
            conexion.Conexion.cargarTabCli(self) #recargo la tabla
        except Exception as error:
            print("Error al modificar cliente", error)

    def recogerValorSpinbox(self):
        """

        Módulo que recoge el valor marcado en el spinbox de clientes.

        """
        try:
            valores = []
            valor = var.ui.spinEnvio.value()  # recoger valor spinbox

            if valor == 0:
                valores.append("Recogida por cliente")
                var.ui.lblEnvio.setText("Recogida por cliente")
            if valor == 1:
                print("Envío Nacional Paquetería Express Urgente")
                var.ui.lblEnvio.setText("Envío Nacional Paquetería Express Urgente")
            if valor == 2:
                print("Envío Nacional Paquetería Normal")
                var.ui.lblEnvio.setText("Envío Nacional Paquetería Normal")
            if valor == 3:
                print("Envío Internacional")
                var.ui.lblEnvio.setText("Envío Internacional")
        except Exception as error:
            print("Error al recoger valor desde spinbox", error)