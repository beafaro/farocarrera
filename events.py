'''

Fichero de eventos generales

'''
import sys, var

class Eventos():
    def Salir(self):
        try:
            var.dlgaviso.show()
            if var.dlgaviso.exec():
                sys.exit()
            else:
                var.dlgaviso.hide()
        except Exception as error:
            print("Error en módulo salir", error)

    def abrircal(self):
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print("Error al abrir el calnedario", error)