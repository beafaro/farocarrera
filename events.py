'''
Fichero de eventos generales
'''
import csv
import os.path
import shutil
import sys
import var
import zipfile
from datetime import datetime

import xlrd
from PyQt5 import QtPrintSupport

import conexion
from window import *


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


    def restaurarBackup(self):
        try:
            option = QtWidgets.QFileDialog.Options()
            filename = var.dlgabrir.getOpenFileName(None, "Restaurar backup",'', "*.zip;;ALL Files", options= option)

            if var.dlgabrir.Accepted and filename != "":
                # extraer zip
                file = filename[0]
                print(file)
                with zipfile.ZipFile(str(file), "r") as bbdd:
                    bbdd.extractall()
                bbdd.close()

            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.cargarTabCli(self)

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Backup restaurada con éxito')
            msg.exec()

        except Exception as error:
            print("Error al restaurar Backup ", error)

    def imprimir(self):
        try:
            printDialog = QtPrintSupport.QPrintDialog()
            if printDialog.exec_():
                printDialog.show()
        except Exception:
            print("Error al Abrir ventana Impresora")

    def importarDatos(self):
        try:
            option = QtWidgets.QFileDialog.Options()
            archivo = var.dlgabrir.getOpenFileName(None, "Importar datos",'', "*.xls;;ALL Files", options= option)

            if var.dlgabrir.Accepted and archivo != "":
                # abrimos fichero excel
                documento = xlrd.open_workbook(archivo)
                clientes = documento.sheet_by_index(0)
                filas= clientes.nrows
                newClients = []

                for i in range(filas):
                    if i == 0:
                        pass
                    else:
                        newClients = []
                        for j in range(9):
                            newClients.append(str(clientes.cell_value(i, j)))

            conexion.Conexion.db_connect(var.filedb)
            conexion.Conexion.cargarTabCli(self)

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Importación de datos efectuada con éxito')
            msg.exec()
        except Exception as error:
            print("Error al importar los datos", error)

    def exportarDatos(self):
        try:
            writer = csv.writer("clientes.csv", "w", newline= "")

        except Exception as error:
            print("Error al exportar los datos", error)