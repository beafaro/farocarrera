'''
Fichero de eventos generales
'''
import os.path
import sys, var, shutil
import zipfile
import xlrd

import conexion
from window import *
from datetime import date, datetime
from PyQt5 import QtPrintSupport

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
            filename = var.dlgabrir.getOpenFileName(None, "Restaurar backup",'', "*.zip", options= option)

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

    def cargarDatosExcel(self):
        try:
            option = QtWidgets.QFileDialog.Options()
            archivo = var.dlgabrir.getOpenFileName(None, "Importar datos",'', "*.xls", options= option)
            #abrimos fichero excel
            documento = xlrd.open_workbook(archivo)
            clientes = documento.sheet_by_index(0)

            baseDatos = conexion.Conexion.db_connect(var.filedb)
            #cursor para recorrer BBDD
            cursor = baseDatos.cursor()
            query = "INSERT INTO clientes (dni, apellidos, nombre, direccion, provincia, sexo, pago) " \
                    "VALUES (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pago)"

            for r in range(1, clientes.nrows):
                dni = clientes.cell(r, 0).value
                apellidos = clientes.cell(r, 1).value

                values = (dni, apellidos)

                # Ejecutar instrucción SQL
                cursor.execute(query, values)

            # Cerrar cursor
            cursor.close()

            # Enviar
            baseDatos.commit()

            # Cerrar la conexión de la base de datos
            baseDatos.close()

            msg = QtWidgets.QMessageBox()
            msg.setModal(True)
            msg.setWindowTitle('Aviso')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText('Importación efectuada con éxito')
            msg.exec()

        except Exception as error:
            print("Error al cargar los datos desde el excel", error)