from datetime import datetime

import xlwt as xlwt
from PyQt5 import QtSql, QtWidgets

import var

class Conexion():
    def db_connect(filedb):
        try:
            db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(filedb)
            if not db.open():
                QtWidgets.QMessageBox.critical(None, "No se puede abrir la base de datos.\n" "Haz click para continuar", QtWidgets.QMessageBox.Cancel)
                return False
            else:
                print("Conexión establecida")
                return True
        except Exception as error:
            print("Problemas en conexión ", error)

    '''
    Módulos gestión base datos cliente
    '''
    def altaCli(newCli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago, envio) "
                          "VALUES (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pago, :envio)")
            query.bindValue(":dni", str(newCli[0]))
            query.bindValue(":alta", str(newCli[1]))
            query.bindValue(":apellidos", str(newCli[2]))
            query.bindValue(":nombre", str(newCli[3]))
            query.bindValue(":direccion", str(newCli[4]))
            query.bindValue(":provincia", str(newCli[5]))
            query.bindValue(":municipio", str(newCli[6]))
            query.bindValue(":sexo", str(newCli[7]))
            query.bindValue(":pago", str(newCli[8]))
            query.bindValue(":envio", str(newCli[9]))

            if query.exec_():
                msg= QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Cliente dado de alta correctamente!")
                msg.exec()
            else:
                msg= QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print("Problemas en alta cliente ", error)

    def cargarTabCli(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare("SELECT dni, apellidos, nombre, alta, pago FROM clientes")
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                    apellidos = query.value(1)
                    nombre = query.value(2)
                    alta = query.value(3)
                    pago = query.value(4)
                    var.ui.tabClientes.setRowCount(index+1) #creamos la fila y luego cargamos datos
                    var.ui.tabClientes.setItem(index,0,QtWidgets.QTableWidgetItem(dni))
                    var.ui.tabClientes.setItem(index,1,QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tabClientes.setItem(index,2,QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabClientes.setItem(index,3,QtWidgets.QTableWidgetItem(alta))
                    var.ui.tabClientes.setItem(index,4,QtWidgets.QTableWidgetItem(pago))
                    index += 1

        except Exception as error:
            print("Problemas mostrar tabla clientes ", error)

    def oneCli(dni):
        try:
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT direccion, provincia, municipio, sexo from clientes WHERE dni = :dni')
            query.bindValue(':dni', dni)
            if query.exec_():
                while query.next():
                    for i in range(4):
                        record.append(query.value(i))
            return record
        except Exception as error:
            print('Problemas cargar datos cliente', error)

    def bajaCli(dni):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('DELETE FROM clientes WHERE dni = :dni')
            query.bindValue(':dni', str(dni))
            if query.exec_():
                print('Baja correcta')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente dado de baja')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error baja cliente en conexion ', error)


    def cargarProv(self):
        try:
            var.ui.cmbProv.clear()
            query = QtSql.QSqlQuery()
            query.prepare("SELECT provincia FROM provincias")
            if query.exec_():
                var.ui.cmbProv.addItem('')
                while query.next():
                    var.ui.cmbProv.addItem(query.value(0))

        except Exception as error:
            print("Error al cargar combo provincias ", error)

    def selMuni(self):
        try:
            #busco el código de la provincia
            id = 0
            var.ui.cmbMuni.clear()
            prov = var.ui.cmbProv.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('SELECT id FROM provincias WHERE provincia = :prov')
            query.bindValue(':prov', str(prov))
            if query.exec_():
                while query.next():
                    id = query.value(0)
            #cargo los municipios con ese código
            query1 = QtSql.QSqlQuery()
            query1.prepare('SELECT municipio FROM municipios WHERE provincia_id = :id')
            query1.bindValue(':id', int(id))
            if query1.exec_():
                var.ui.cmbMuni.addItem('')
                while query1.next():
                    var.ui.cmbMuni.addItem(query1.value(0))

        except Exception as error:
            print("Error al cargar combo municipios ", error)

    def modifCli(modCliente):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('UPDATE clientes SET alta = :alta, apellidos = :apellidos, nombre = :nombre, '
                          'direccion = :direccion, provincia = :provincia, municipio = :municipio, '
                          'sexo = :sexo, pago = :pago, envio = :envio WHERE dni = :dni')
            query.bindValue(':dni', str(modCliente[0]))
            query.bindValue(":alta", str(modCliente[1]))
            query.bindValue(":apellidos", str(modCliente[2]))
            query.bindValue(":nombre", str(modCliente[3]))
            query.bindValue(":direccion", str(modCliente[4]))
            query.bindValue(":provincia", str(modCliente[5]))
            query.bindValue(":municipio", str(modCliente[6]))
            query.bindValue(":sexo", str(modCliente[7]))
            query.bindValue(":pago", str(modCliente[8]))
            query.bindValue(":envio", str(modCliente[9]))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Datos modificados de Cliente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print("Problemas al modificar cliente")

    def altaCli2(newcli):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO clientes (dni, apellidos, nombre, direccion, provincia, sexo) VALUES '
                          '(:dni, :apellidos, :nombre, :direccion, :provincia, :sexo)')
            query.bindValue(':dni', str(newcli[0]))
            query.bindValue(':apellidos', str(newcli[1]))
            query.bindValue(':nombre', str(newcli[2]))
            query.bindValue(':direccion', str(newcli[3]))
            query.bindValue(':provincia', str(newcli[4]))
            query.bindValue(':sexo', str(newcli[5]))

            if query.exec_():
                print('Insercción correcta')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Cliente dado de alta correctamente')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Problemas alta cliente', error)

    def exportExcel(self):
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_dataExport.xls')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar datos', var.copia, '.xls',
                                                                options=option)
            wb = xlwt.Workbook()
            sheet1 = wb.add_sheet('Hoja 1')

            # Cabeceras
            sheet1.write(0, 0, 'DNI')
            sheet1.write(0, 1, 'ALTA')
            sheet1.write(0, 2, 'APELLIDOS')
            sheet1.write(0, 3, 'NOMBRE')
            sheet1.write(0, 4, 'DIRECCION')
            sheet1.write(0, 5, 'PROVINCIA')
            sheet1.write(0, 6, 'MUNICIPIO')
            sheet1.write(0, 7, 'SEXO')
            sheet1.write(0, 8, 'PAGO')
            f = 1
            query = QtSql.QSqlQuery()
            query.prepare('SELECT *  FROM clientes')
            if query.exec_():
                while query.next():
                    for c in range(8):
                        sheet1.write(f, c, query.value(c))
                    f += 1
            wb.save(directorio)

        except Exception as error:
            print('Error en conexión para exportar excel ', error)