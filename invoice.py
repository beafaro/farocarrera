'''
Funciones gestion clientes
'''
import conexion
import window
import var


class Facturas():
    def buscaCli(self):
        try:
            dni = var.ui.txtDNIfac.text().upper()
            var.ui.txtDNIfac.setText(dni)
            registro = conexion.Conexion.buscaClifac(dni)
            nombre = registro[0] + ", " + registro[1]
            var.ui.lblNomfac.setText(nombre)

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

        except Exception as error:
            print("Error en cargar facturas", error)
