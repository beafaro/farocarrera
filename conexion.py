import xlwt as xlwt
from PyQt5 import QtSql
from PyQt5.uic.properties import QtGui

import sqlite3, var, os, shutil, csv, locale, invoice
from window import *
from datetime import datetime
locale.setlocale(locale.LC_ALL, '')

class Conexion():
    def create_DB(filename):
        """

        Recibe nombre de la base de datos
        Módulo que se ejecuta al principio del programa.
        Crea las tablas y carga municipios y provincias.
        Crea los directorios necesarios.
        :rtype: Object

        """
        try:
            con = sqlite3.connect(database=filename)
            cur = con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS clientes (dni TEXT NOT NULL, alta INTEGER, apellidos TEXT NOT NULL, nombre TEXT, direccion TEXT, provincia TEXT, municipio TEXT,"
                        " sexo TEXT, pago TEXT, envio INTEGER, PRIMARY KEY(dni))")
            con.commit()

            cur.execute("CREATE TABLE IF NOT EXISTS facturas (codfac INTEGER NOT NULL, dni TEXT NOT NULL, fechafac TEXT NOT NULL, PRIMARY KEY (codfac AUTOINCREMENT))")
            con.commit()

            cur.execute("CREATE TABLE IF NOT EXISTS municipios (provincia_id INTEGER NOT NULL, municipio TEXT NOT NULL, id INTEGER NOT NULL, PRIMARY KEY(id))")
            con.commit()

            cur.execute("CREATE TABLE IF NOT EXISTS productos (codigo INTEGER NOT NULL, nombre TEXT NOT NULL, precio INTEGER NOT NULL, PRIMARY KEY(codigo AUTOINCREMENT))")
            con.commit()

            cur.execute("CREATE TABLE IF NOT EXISTS provincias (id INTEGER NOT NULL, provincia TEXT NOT NULL, PRIMARY KEY(id))")
            con.commit()

            cur.execute("CREATE TABLE IF NOT EXISTS ventas (codven INTEGER NOT NULL, codfacf INTEGER NOT NULL, codprodf INTEGER, precio REAL, cantidad REAL NOT NULL, FOREIGN KEY(codfacf)"
                        " REFERENCES facturas(codfac) on delete cascade, FOREIGN KEY(codprodf) REFERENCES productos(codigo), PRIMARY KEY(codven AUTOINCREMENT))")
            con.commit()

            cur.execute("select count() from provincias")
            numero = cur.fetchone()[0]
            print(numero)
            con.commit()
            if int(numero) == 0:
                with open("provincias.csv", "r", encoding="utf-8") as fin:
                    dr = csv.DictReader(fin)
                    to_db= [(i["id"], i["provincia"]) for i in dr]
                    cur.executemany("insert into provincias (id, provincia) VALUES (?,?);", to_db)
                    con.commit()

            con.close()

            ''' creacion de directorios '''
            if not os.path.exists('.\\informes'):
                os.mkdir('.\\informes')
            if not os.path.exists('.\\img'):
                os.mkdir('.\\img')
                #shutil.move('log-empresa.jpg','.\\img\log-empresa.jpg')
            if not os.path.exists('.\\copias'):
                os.mkdir('.\\copias')

        except Exception as error:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Aviso")
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("error")
            msg.exec()

    def db_connect(filedb):
        """

        Realiza la conexión con la base de datos al ejecutar el programa.

        :return: Boolean, True si es correcto, False si hay un error
        :rtype: Boolean

        """
        try:
            db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
            db.setDatabaseName(filedb)
            if not db.open():
                QtWidgets.QMessageBox.critical(None, "No se puede abrir la base de datos.\n" "Haz click para continuar",
                                               QtWidgets.QMessageBox.Cancel)
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
        """

        Módulo que recibe datos de un cliente y los carga en la base de datos.

        """
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
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Cliente dado de alta correctamente!")
                msg.exec()
            else:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText(query.lastError().text())
                msg.exec()
        except Exception as error:
            print("Problemas en alta cliente ", error)


    def cargarTabCli(self):
        """

        Módulo que toma datos de los clientes y los carga en la tabla de la interfaz gráfica.

        """
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
                    var.ui.tabClientes.setRowCount(index + 1)  # creamos la fila y luego cargamos datos
                    var.ui.tabClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                    var.ui.tabClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                    var.ui.tabClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                    var.ui.tabClientes.setItem(index, 3, QtWidgets.QTableWidgetItem(alta))
                    var.ui.tabClientes.setItem(index, 4, QtWidgets.QTableWidgetItem(pago))
                    index += 1

        except Exception as error:
            print("Problemas mostrar tabla clientes ", error)


    def oneCli(dni):
        """

        Módulo que seleccina un cliente según su DNI y lo devuelve a la función CargaCli del ficheros clientes.

        :return: Devuelve lista
        :rtype: lista

        """
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
        """

        Módulo que recibe DNI cliente y lo elimina de la base de datos.

        """
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
        """

        Módulo que carga provincias

        """
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
        """

        Módulo que selecciona los municipios dad un provincia y los carga en el combo provincias dada una provincia

        """
        try:
            # busco el código de la provincia
            id = 0
            var.ui.cmbMuni.clear()
            prov = var.ui.cmbProv.currentText()
            query = QtSql.QSqlQuery()
            query.prepare('SELECT id FROM provincias WHERE provincia = :prov')
            query.bindValue(':prov', str(prov))
            if query.exec_():
                while query.next():
                    id = query.value(0)
            # cargo los municipios con ese código
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
        """

        Módulo que recibe los datos del cliente y los modifica en la base de datos.

        """
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


    '''
    Módulos gestión base datos productos
    '''
    def altaProd(newProd):
        """

        Módulo que recibe datos del producto y los cagra en la base de datos.

        """
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
        """

        Módulo que recarga la tabla de productos del panel de productos siempre que se de de alta, baja o modifcar un producto.

        """
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
                    var.ui.tabProductos.item(index, 2).setTextAlignment(QtCore.Qt.AlignRight)
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
        """

        Módulo que recibe el código de un producto y lo elimina de la base de datos.

        """
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
        """

        Módulo que recibe el regustro de datos de un producto y los modifica en la base de datos.

        """
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

    #método buscaPro que recibe nombre de producto en la base de datos y devuelce al módulo de prodcutos yt las caraga en panel
    #devuelve una lista


    '''
    Módulos gestión facturas
    '''
    def buscaClifac(dni):
        """

        Busca los datos del cliente a facturar a partir de su DNI.

        :return: Datos del cliente a facturar
        :rtype: object- registro

        """
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
        """

        Dado el cliente a facturar se da de alta una factura en la base de datos a nombre de ese cliente(DNI).

        """
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
        """

        Módulo que se ejecuta siempre cada vez que se da de alta alta, baja o modificar una factura recargando en el panelde gestión de facturación la tabla facuturas.

        """
        try:
            var.ui.tabFacturas.clear()
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare("SELECT codfac, fechafac FROM facturas order by date(fechafac) DESC ")
            if query.exec_():
                while query.next():
                    codigo = query.value(0)
                    fechafac = query.value(1)
                    var.btnfacdel = QtWidgets.QPushButton()
                    iconoPapelera = QtGui.QPixmap("img/papelera.png")
                    var.btnfacdel.setFixedSize(22, 22)
                    var.btnfacdel.setIcon(QtGui.QIcon(iconoPapelera))

                    var.ui.tabFacturas.setRowCount(index + 1)
                    var.ui.tabFacturas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codigo)))
                    var.ui.tabFacturas.setItem(index, 1, QtWidgets.QTableWidgetItem(fechafac))
                    cell_widget = QtWidgets.QWidget()
                    lay_out = QtWidgets.QHBoxLayout(cell_widget)
                    lay_out.setContentsMargins(0, 0, 0, 0)
                    lay_out.addWidget(var.btnfacdel)
                    var.btnfacdel.clicked.connect(Conexion.bajaFac)
                    var.ui.tabFacturas.setCellWidget(index, 2, cell_widget)
                    var.ui.tabFacturas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabFacturas.item(index, 1).setTextAlignment(QtCore.Qt.AlignCenter)
                    index += 1
        except Exception as error:
            print("Problemas al cargar listado de facturas ", error)


    def buscaDNIFac(numfac):
        """

        Módulo que busca el dni de la tabla facturas en la base de datos.
        :return: Devuelve un dni
        :rtype: basestring

        """
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
        """

        Módulo que dado el número de factura la da de baja, además llama al módulo borra ventas para que elimine todas las ventas asociadas a esa factura de la tabla ventas de la base de datos.

        """
        try:
            numfac = var.ui.lblNumfac.text()
            query = QtSql.QSqlQuery(numfac)
            query.prepare("DELETE FROM facturas WHERE codfac = :numfac")
            query.bindValue(":numfac", int(numfac))

            if query.exec_():
                Conexion.cargarTabFacturas(self)
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Aviso")
                msg.setIcon(QtWidgets.QMessageBox.Information)
                msg.setText("Factura dada de baja")
                msg.exec()
                Conexion.delVenFac(numfac)

        except Exception as error:
            print("Problemas al dar de baja factura ", error)


    def delVenFac(numfac):
        """

        Módulo que se llama cuando se da de baja un factura en la base de datos para que elimine todas las ventas asociadas a esa factura.

        :param numfac valor de la factura
        :type numfac: int

        Recibe el número a borrar. A partir de ese código, primero selecciona todos los códigos de venta asociados a esa factura y los guarda en una lista.
        A continuación, a medida que recorre esa lista leyendo los códigos de venta los da de baja de la tabla ventas de la base de datos.
        Finalmente, recarga la tabla de ventas del panel de facturación y limpia datos.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('delete from ventas where codfacf= :numfac')
            query.bindValue(':numfac', int(numfac))
            if query.exec_():
                pass
            var.ui.tabVentas.clearContents()
            invoice.Facturas.cargaLineaVenta(0)
            var.ui.lblIVA.setText("")
            var.ui.lblSubTotal.setText("")
            var.ui.lblTotal.setText("")
        except Exception as error:
            print("Erro al eliminar lineas venta en delvenFac", error)


    def cargarCmbProducto(self):
        """

        Módulo que toma los nombres de los productos existentes de la base de datos y los carga en el panel de facturación de la tabla ventas.

        """
        try:
            var.cmbProducto.clear()
            query = QtSql.QSqlQuery()
            var.cmbProducto.addItem('')  # para que la primera línea del código esté en blanco
            query.prepare("SELECT nombre FROM productos ORDER BY nombre")
            if query.exec_():
                while query.next():
                    var.cmbProducto.addItem(str(query.value(0)))
        except Exception as error:
            print("Error al cargar combo de productos ", error)


    def obtenerCodPrecio(articulo):
        """

        Módulo que dado el nombre del producto obtenemos su precio para realizar los cálculos necasarios en la venta.
        :return: Devuelve el precio
        :rtype: object - array

        """
        try:
            dato = []
            query = QtSql.QSqlQuery()
            query.prepare("SELECT codigo, precio FROM productos WHERE nombre =:nombre")
            query.bindValue(":nombre", str(articulo))

            if query.exec_():
                while query.next():
                    dato.append(int(query.value(0)))
                    dato.append(str(query.value(1)))
            return dato

        except Exception as error:
            print("Error al obtener código y precio del artículo en Conexion ", error)


    def cargarVenta(venta):
        """

        Carga el regustro de una venta realiza en la tabla ventas de la base de datos.

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare(
                "INSERT INTO ventas (codfacf, codprodf, precio, cantidad) VALUES (:codfacf, :codprodf, :precio, :cantidad)")
            query.bindValue(":codfacf", int(venta[0]))
            query.bindValue(":codprodf", int(venta[1]))
            query.bindValue(":precio", float(venta[2]))
            query.bindValue(":cantidad", float(venta[3]))

            if query.exec_():
                var.ui.lblVenta.setStyleSheet("QLabel {color: black;}")
                var.ui.lblVenta.setText("Venta realizada!")
            else:
                var.ui.lblVenta.setStyleSheet("QLabel {color: red;}")
                var.ui.lblVenta.setText("Error en venta!")

        except Exception as error:
            print("Error al cargar venta en conexión", error)


    def buscaCodFac(self):
        """

        Módulo que selecciona el código de la factua con número más alta o la útlima en dar de alta.

        :return: Devuelve número de factura
        :rtype: entero

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare("SELECT codfac FROM facturas order by codfac desc limit 1")
            if query.exec_():
                while query.next():
                    dato = query.value(0)
            return dato

        except Exception as error:
            print("Error al obtener código factura en conexión", error)


    def cargarLineasVenta(codfac):
        """

        Módulo que carga todas las ventas asociadas a una factura de la tabla ventas del panel de facturación,
        además realiza los cálculos necesarios para el subtotal, el total y el IVA de la factura.
        A este módulo se le llama cada vez que realiza una venta.

        """
        try:
            suma = 0.0
            var.ui.tabVentas.clearContents()
            index = 0
            query = QtSql.QSqlQuery()
            query.prepare('SELECT codven, precio, cantidad, codprodf FROM ventas WHERE codfacf = :codfacf')
            query.bindValue(':codfacf', int(codfac))

            if query.exec_():
                while query.next():
                    codven = query.value(0)
                    precio = query.value(1)
                    cantidad = query.value(2)
                    nombre = Conexion.buscaArt(int(query.value(3)))
                    total = round(precio * cantidad, 2)
                    suma += total
                    var.ui.tabVentas.setRowCount(index + 1)
                    var.ui.tabVentas.setItem(index, 0, QtWidgets.QTableWidgetItem(str(codven)))
                    var.ui.tabVentas.setItem(index, 1, QtWidgets.QTableWidgetItem(str(nombre)))
                    var.ui.tabVentas.setItem(index, 2, QtWidgets.QTableWidgetItem(str(precio) + ' €'))
                    var.ui.tabVentas.setItem(index, 3, QtWidgets.QTableWidgetItem(str(cantidad)))
                    var.ui.tabVentas.setItem(index, 4, QtWidgets.QTableWidgetItem(str(total) + ' €'))
                    var.ui.tabVentas.item(index, 0).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabVentas.item(index, 2).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabVentas.item(index, 3).setTextAlignment(QtCore.Qt.AlignCenter)
                    var.ui.tabVentas.item(index, 4).setTextAlignment(QtCore.Qt.AlignCenter)
                    index = index + 1

            iva = suma * 0.21
            total = suma + iva
            var.ui.lblSubTotal.setText(str(round(suma, 2)) + ' €')
            var.ui.lblIVA.setText(str(round(iva, 2)) + ' €')
            var.ui.lblTotal.setText(str(round(total, 2)) + ' €')

            invoice.Facturas.cargaLineaVenta(index)
            var.ui.tabVentas.scrollToBottom()

        except Exception as error:
            print("Error al cargar líneas de factura", error)


    def buscaArt(codpro):
        """

        Módulo que busca el nombre de un articulo para usarlo en las ventas a partir del código.
        :return: Devuelve el nombre del artículo.
        :rtype: basestring

        """
        try:
            query = QtSql.QSqlQuery()
            query.prepare('select nombre from productos where codigo = :codpro')
            query.bindValue(':codpro', str(codpro))
            if query.exec_():
                while query.next():
                    return (query.value(0))
        except Exception as error:
            print('Error en la búsqueda de articulo')


    def borraVenta(self):
        """

        Módulo que elimina una venta de una factura.

        """
        try:
            row = var.ui.tabVentas.currentRow()
            codventa = var.ui.tabVentas.item(row, 0).text()
            query = QtSql.QSqlQuery()
            query.prepare('DELETE FROM ventas WHERE codven = :codven')
            query.bindValue(':codven', str(codventa))
            if query.exec_():
                msg1 = QtWidgets.QMessageBox()
                msg1.setWindowTitle("Aviso")
                msg1.setIcon(QtWidgets.QMessageBox.Information)
                msg1.setText("Venta eliminada")
                msg1.exec()
                codfac = var.ui.lblNumfac.text()
                Conexion.cargarLineasVenta(codfac)

        except Exception as error:
            print("Error en baja venta", error)
