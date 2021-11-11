'''
Fichero de eventos generales
'''
import os.path
import sys, var, shutil
import zipfile

import conexion
from window import *
from datetime import date, datetime

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
            print("Error al abrir el calendario", error)

    def resizeTablaCli(self):
        try:
            header = var.ui.tabClientes.horizontalHeader()
            for i in range(5):
               header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
               if i == 0 or i == 3:
                   header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
        except Exception as error:
            print("Error al redimensionar tabla clientes", error)

    def Abrir(self):
        try:
            var.dlgabrir.show()
        except Exception as error:
            print("Error al abrir cuadro de diálogo", error)

    def crearBackup(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime("%Y.%m.%d.%H.%M.%S")
            var.copia = (str(fecha) + "_backup.zip")

            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, "Guardar copia", var.copia, ".zip", options = option)
            if var.dlgabrir.Accepted and filename != "":
                fichzip = zipfile.ZipFile(var.copia, "w")
                fichzip.write(var.filedb, os.path.basename(var.filedb), zipfile.ZIP_DEFLATED)
                fichzip.close()
                shutil.move(str(var.copia), str(directorio))

                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Base creada con éxito')
                msg.exec()

        except Exception as error:
            print("Error al crear Backup: ", error)

    #restaurar backup
    def restaurarBackup(self):
        try:
            dirpro = os.getcwd()
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getOpenFileName(None, "Restaurar backup",'', "*.zip;;ALL", options= option)

            if var.dlgabrir.Accepted and filename != "":
                # extraer zip
                file = filename[0]
                with zipfile.ZipFile(str(file), "r") as bbdd:
                    bbdd.extractall()
                bbdd.close()
                shutil.move("bbdd.sqlite", str(dirpro))
            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.cargarTabCli()



        except Exception as error:
            print("Error al restaurar Backup ", error)