'''
Fichero de eventos generales
'''
import os.path
import shutil
import sys

import xlrd as xlrd

import var
import zipfile
from datetime import datetime

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
                newcli = []
                contador = 0
                option = QtWidgets.QFileDialog.Options()
                ruta_excel = var.dlgabrir.getOpenFileName(None, 'Importar Excel', '', '*.xls;;ALL Files', options=option)

                if var.dlgabrir.Accepted and ruta_excel != '':
                    fichero = ruta_excel[0]
                workbook = xlrd.open_workbook(fichero)
                hoja = workbook.sheet_by_index(0)
                while contador < hoja.nrows:
                    for i in range(6):
                        # if i==1:
                        #     newcli.append((str)(date.today()))
                        # if i==5:
                        #     newcli.append('')
                        newcli.append(hoja.cell_value(contador + 1, i))
                    # newcli.append('Efectivo')
                    conexion.Conexion.altaCli2(newcli)
                    conexion.Conexion.cargarTabCli(newcli)
                    newcli.clear()
                    contador = contador + 1
            except Exception as error:
                print('Error al importar ', error)

    def exportarDatos(self):
        try:
            conexion.Conexion.exportExcel(self)
            try:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setIcon(QtWidgets.QMessageBox.Information)
                msgBox.setText("Datos exportados con éxito.")
                msgBox.setWindowTitle("Operación completada")
                msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msgBox.exec()
            except Exception as error:
                print('Error en mensaje generado exportar datos ', error)
        except Exception as error:
            print('Error en evento exportar datos ', error)


    '''Eventos produtos'''
    def resizeTablaProd(self):
        try:
            header = var.ui.tabProductos.horizontalHeader()
            for i in range(3):
               header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        except Exception as error:
            print("Error al redimensionar tabla productos", error)


    def resizeTablaFac(self):
        try:
            header = var.ui.tabFacturas.horizontalHeader()
            for i in range(3):
                header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)

        except Exception as error:
            print("Error al redimensionar tabla productos", error)