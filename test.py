import unittest, clients, conexion, var
from PyQt5 import QtSql

class MyTestCase(unittest.TestCase):
    def test_conexion(self):
        value = conexion.Conexion.db_connect(var.filedb)
        msg = 'Conexión no válida'
        self.assertTrue(value, msg)

    def test_dni(self):
        dni = '00000000T'
        value = clients.Clientes.validarDNI(dni)
        msg = 'Error DNI'
        self.assertTrue(value, msg)

    def test_factura(self):
        try:
            msg='Cálculos incorrectos'
            total = 19.3
            codfac = 18
            valor = 23.35
            query = QtSql.QSqlQuery()
            query.prepare('select precio, cantidad from ventas where codfacf= :codfacf')
            query.bindValue(':codfacf', int(codfac))
            if query.exec_():
                while query.next():
                    precio = query.value(0)
                    cantidad = query.value(1)
                    total= total + round(float(cantidad) * float(precio), 2)

            total = round(total + total*0.21, 2)
        except Exception as error:
            print('Error listado de la tabla de ventas: %s ' %str(error))
        self.assertEqual(round(float(valor),2), round(float(total),2), msg)


if __name__ == '__main__':
    unittest.main()
