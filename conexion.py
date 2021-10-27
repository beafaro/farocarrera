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
            query.prepare("INSERT INTO clientes (dni, alta, apellidos, nombre, direccion, provincia, municipio, sexo, pago) "
                          "VALUES (:dni, :alta, :apellidos, :nombre, :direccion, :provincia, :municipio, :sexo, :pago)")
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