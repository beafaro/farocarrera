'''

Funciones gestion clientes

'''
import var


class Clientes():
    def validarDNI():
        try:
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
                else:
                    var.ui.lblValidoDNI.setStyleSheet("QLabel {color: red;}")
                    var.ui.lblValidoDNI.setText("X")
                    var.ui.txtDNI.setStyleSheet("background-color: pink;}")
            else:
                var.ui.lblValidoDNI.setStyleSheet("QLabel {color: red;}")
                var.ui.lblValidoDNI.setText("X")
                var.ui.txtDNI.setStyleSheet("background-color: pink;}")
        except Exception as error:
            print("Error en módulo validar DNI", error)

    def SelSexo(self):
        try:
            if var.ui.rbtFem.isChecked():
                print("Marcado fememino")
            if var.ui.rbtHom.isChecked():
                print("Marcado masculino")
        except Exception as error:
            print("Error en módulo seleccionar género:", error)

    def SelPago(self):
        try:
            if var.ui.chkEfectivo.isChecked():
                print("has seleccionado efectivo")
            if var.ui.chkTarjeta.isChecked():
                print("Has seleccionado tarjeta")
            if var.ui.chkCargoCuenta.isChecked():
                print("Has seleccionado cargo cuenta")
            if var.ui.chkTransfe.isChecked():
                print("Has seleccionado transferencia")
        except Exception as error:
            print("Error en módulo seleccionar forma de pago:", error)

    def CargarProv_(self):
        try:
            var.ui.cmbProv.clear()
            prov = ["", "A Coruña", "Lugo", "Ourense", "Pontevedra", "Vigo"]
            for i in prov:
                var.ui.cmbProv.addItem(i)

        except Exception as error:
            print("Error en módulo cargar provincias, ", error)

    def SelProv(prov):
        try:
            print("Has seleccionado la provincia de", prov)
            return prov
        except Exception as error:
            print("Error selcción provincia, ", error)