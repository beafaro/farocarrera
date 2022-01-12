import locale
from datetime import datetime
import xlwt as xlwt
from PyQt5 import QtSql, QtWidgets, QtCore
from PyQt5.uic.properties import QtGui
import var
from window import *

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
            query.prepare('INSERT INTO clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago) '
                          'VALUES (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pago)')
            query.bindValue(":dni", str(newCli[0]))
            query.bindValue(":alta", str(newCli[1]))
            query.bindValue(":apellidos", str(newCli[2]))
            query.bindValue(":nombre", str(newCli[3]))
            query.bindValue(":direccion", str(newCli[4]))
            query.bindValue(":provincia", str(newCli[5]))
            query.bindValue(":municipio", str(newCli[6]))
            query.bindValue(":sexo", str(newCli[7]))
            query.bindValue(":pago", str(newCli[8]))

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
                          'sexo = :sexo, pago = :pago WHERE dni = :dni')
            query.bindValue(':dni', str(modCliente[0]))
            query.bindValue(":alta", str(modCliente[1]))
            query.bindValue(":apellidos", str(modCliente[2]))
            query.bindValue(":nombre", str(modCliente[3]))
            query.bindValue(":direccion", str(modCliente[4]))
            query.bindValue(":provincia", str(modCliente[5]))
            query.bindValue(":municipio", str(modCliente[6]))
            query.bindValue(":sexo", str(modCliente[7]))
            query.bindValue(":pago", str(modCliente[8]))

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
            directorio, filename = var.dlgabrir.getSaveFileName(None, 'Exportar datos', var.copia, '.xls', options=option)
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


    '''
    Módulos gestión base datos productos
    '''
    def altaProd(newProd):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('INSERT INTO productos (nombre, precio) VALUES (:nombre, :precio)')
            query.bindValue(":nombre", str(newProd[0]))
            query.bindValue(":precio", str(newProd[1]))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Producto dado de alta correctamente!")
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print("Problemas en alta producto ", error)

    def cargarTabProd(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare("SELECT codigo, nombre, precio FROM productos order by nombre")
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    nombre = query.value(1)
                    precio = query.value(2)
                    var.ui.tabProductos.setRowCount(index + 1)
                    var.ui.tabProductos.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabProductos.setItem(index, 1, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabProductos.setItem(index, 2, QtWidgets.QTableWidgetItem(precio))
                    var.ui.tabProductos.item(index,2).setTextAlignment(QtCore.Qt.AlignRight)
                    var.ui.tabProductos.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    index += 1
        except Exception as error:
            print("Problemas mostrar tabla productos ", error)

    def oneCodigo(codigo):
        try:
            record = []
            query = QtSql.QSqlQuery()
            query.prepare('SELECT nombre, precio FROM productos WHERE codigo = :codigo')
            query.bindValue(':codigo', codigo)
            if query.exec_():
                while query.next():
                    for i in range(2):
                        record.append(query.value(i))
            return record
        except Exception as error:
            print('Problemas cargar datos producto', error)

    def bajaProd(codigo):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('DELETE FROM productos WHERE codigo = :codigo')
            query.bindValue(':codigo', str(codigo))
            if query.exec_():
                print('Baja correcta')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Producto dado de baja')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print('Error baja producto en conexion ', error)

    def modifProd(modProducto):
        try:
            query = QtSql.QSqlQuery()
            query.prepare('UPDATE productos SET nombre =:nombre, precio =:precio WHERE codigo =:codigo')
            query.bindValue(':codigo', int(modProducto[0]))
            query.bindValue(':nombre', str(modProducto[1]))
            '''codigo juan carlos'''
            modProducto[2] = modProducto[2].replace('€', '')
            modProducto[2] = modProducto[2].replace(',', '.')
            modProducto[2] = float(modProducto[2])
            modProducto[2] = round(modProducto[2], 2)
            modProducto[2] = str(modProducto[2])
            modProducto[2] = locale.currency(float(modProducto[2]))
            query.bindValue(':precio', str(modProducto[2]))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Datos modificados de producto')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print("Problemas al modificar producto")


    '''
    Módulos gestión facturas
    '''
    def buscaClifac(dni):
        try:
            registro = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT dni, apellidos, nombre FROM clientes WHERE dni =:dni")
            query.bindValue(":dni", str(dni))

            if query.exec_():
                while query.next():
                    registro.append(query.value(1))
                    registro.append(query.value(2))
            return registro
        except Exception as error:
            print("Error en conexión buscar cliente", error)

    def altaFac(registro):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("INSERT INTO facturas (dni, fechafac) VALUES (:dni, :fechafac)")
            query.bindValue(":dni", str(registro[0]))
            query.bindValue(":fechafac", str(registro[1]))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText('Factura dada de alta')
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Aviso')
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText(query.lastError().text())
                msg.exec()

        except Exception as error:
            print("Error en conexión alta fac", error)

    def cargarTabFacturas(self):
        try:
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare("SELECT codfac, fechafac FROM facturas order by date(fechafac) DESC ")
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    fechafac = query.value(1)
                    var.btnfacdel = QtWidgets.QPushButton()
                    iconoPapelera = QtGui.QPixmap("img/papelera.png")
                    var.btnfacdel.setFixedSize(22,22)
                    var.btnfacdel.setIcon(QtGui.QIcon(iconoPapelera))

                    print(codigo, fechafac)
                    var.ui.tabFacturas.setRowCount(index + 1)
                    var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(fechafac))
                    cell_widget = QtWidgets.QWidget()
                    lay_out = QtWidgets.QHBoxLayout(cell_widget)
                    lay_out.setContentsMargins(0,0,0,0)
                    lay_out.addWidget(var.btnfacdel)
                    var.btnfacdel.clicked.connect(Conexion.bajaFac)
                    var.ui.tabFacturas.setCellWidget(index, 2, cell_widget)
                    var.ui.tabFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                    index += 1
        except Exception as error:
            print("Problemas al cargar listado de facturas ", error)

    def buscaDNIFac(numfac):
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT dni FROM facturas WHERE codfac = :codfac")
            query.bindValue(":codfac", int(numfac))
            if query.exec_():
                while query.next():
                    dni = query.value(0)
                return dni
        except Exception as error:
            print("Problemas al buscar cliente ", error)

    def bajaFac(self):
        try:
            numfac = var.ui.lblNumfac.text()
            query = QtSql.QSqlQuery()
            query.prepare("delete from facturas where codfac = :numfac")
            query.bindValue(":numfac", int(numfac))

            if query.exec_():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Factura dada de baja")
                msg.exec()
                Conexion.cargarTabFacturas(self)

        except Exception as error:
            print("Problemas al dar de baja factura ", error)
