import os, var
from datetime import datetime

from PyQt5 import QtSql
from reportlab.pdfgen import canvas

import conexion


class Informes():

    def listadoClientes(self):
        try:
            var.cv = canvas.Canvas("informes/listadoClientes.pdf")
            var.cv.setTitle("Listado Clientes")
            var.cv.setAuthor("Departamento de Administración")

            rootPath = ".\\informes"
            var.cv.setFont("Helvetica-Bold", size= 10)
            textoTitulo = "LISTADO CLIENTES"
            Informes.cabecera(self)
            Informes.pie(textoTitulo)

            var.cv.drawString(255,690, textoTitulo)
            var.cv.line(40,685,530,685)
            items = ["DNI", "Nombre", "Formas de pago"]
            var.cv.drawString(65,675,items[0])
            var.cv.drawString(210,675,items[1])
            var.cv.drawString(400,675,items[2])
            var.cv.line(40,670,530,670)

            query = QtSql.QSqlQuery()
            query.prepare("SELECT dni, apellidos, nombre, pago FROM clientes order by apellidos,nombre")
            var.cv.setFont("Helvetica", size= 8)

            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    if j <= 80:
                        var.cv.drawString(440,30, "Página siguiente...")
                        var.cv.showPage()
                        Informes.cabecera(self)
                        Informes.pie(textoTitulo)
                        var.cv.drawString(255, 690, textoTitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ["DNI", "Nombre", "Formas de pago"]
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(400, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        i = 50
                        j = 655

                    var.cv.setFont("Helvetica", size=8)
                    var.cv.drawString(i,j, str(query.value(0)))
                    var.cv.drawString(i+140, j, str(query.value(1)+", " + query.value(2)))
                    var.cv.drawString(i+310, j, str(query.value(3)))
                    j = j - 20

            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith("clientes.pdf"):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print("Error en informes clientes, ", error)

    def cabecera(self):
        try:
            logo = ".\\img\logo_empresa.jpg"
            var.cv.line(40,800,530,800)
            var.cv.setFont("Helvetica-Bold", 14)
            var.cv.drawString(50,785, "Import-Export Vigo")
            var.cv.setFont("Helvetica", 10)
            var.cv.drawString(50,770, "CIF: A00000000H")
            var.cv.drawString(50,755, "Dirección: Avenida Galicia, 101")
            var.cv.drawString(50,740, "Vigo - 36216 - Spain")
            var.cv.drawString(50,725, "e-mail: micorreo@mail.com")
            var.cv.drawImage(logo,425,710)
            var.cv.line(40,800,500,800)
            var.cv.line(40, 705, 530, 705)
        except Exception as error:
            print("Error en cabecera informe", error)

    def pie(texto):
        try:
            var.cv.line(50,50,530,50)
            fecha = datetime.today()
            fecha = fecha.strftime("%d.%m.%Y %H.%M.%S")
            var.cv.setFont("Helvetica", size=6)
            var.cv.drawString(70,40, str(fecha))
            var.cv.drawString(255,40,str(texto))
            var.cv.drawString(500,40,str("Página %s " %var.cv.getPageNumber()))
        except Exception as error:
            print("Error creación de pie de informe clientes", error)

    def listadoProductos(self):
        try:
            var.cv = canvas.Canvas("informes/listadoProductos.pdf")
            var.cv.setTitle("Listado Productos")
            var.cv.setAuthor("Departamento de Administración")

            rootPath = ".\\informes"
            var.cv.setFont("Helvetica-Bold", size= 10)
            textoTitulo = "LISTADO ARTICULOS"
            Informes.cabecera(self)
            Informes.pie(textoTitulo)

            var.cv.drawString(255,690, textoTitulo)
            var.cv.line(40,685,530,685)
            items = ["Código", "Artículo", "Precio-unidad"]
            var.cv.drawString(65,675,items[0])
            var.cv.drawString(210,675,items[1])
            var.cv.drawString(400,675,items[2])
            var.cv.line(40,670,530,670)

            query = QtSql.QSqlQuery()
            query.prepare("SELECT codigo, nombre, precio FROM productos order by nombre")
            var.cv.setFont("Helvetica", size= 8)

            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    if j <= 80:
                        var.cv.drawString(440,30, "Página siguiente...")
                        var.cv.showPage()
                        Informes.cabecera(self)
                        Informes.pie(textoTitulo)
                        var.cv.drawString(255, 690, textoTitulo)
                        var.cv.line(40, 685, 530, 685)
                        items = ["Código", "Artículo", "Precio-unidad"]
                        var.cv.drawString(65, 675, items[0])
                        var.cv.drawString(210, 675, items[1])
                        var.cv.drawString(400, 675, items[2])
                        var.cv.line(40, 670, 530, 670)
                        i = 50
                        j = 655

                    var.cv.setFont("Helvetica", size=8)
                    var.cv.drawString(i,j, str(query.value(0)))
                    var.cv.drawString(i+140, j, str(query.value(1)))
                    var.cv.drawString(i+310, j, str(query.value(2)))
                    j = j - 20

            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith(".pdf"): #"productos.pdf
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print("Error en informes productos, ", error)

    def listadoFacturas(self):
        try:
            var.cv = canvas.Canvas('informes/factura.pdf')
            var.cv.setTitle('Listado Facturas')
            var.cv.setAuthor('Departamento de Administración')
            rootPath = '.\\informes'
            var.cv.setFont('Helvetica-Bold', size=10)
            textotitulo = 'FACTURA'
            Informes.cabecera(self)
            Informes.pie(textotitulo)
            codfac = var.ui.lblNumfac.text()
            var.cv.drawString(260, 694, textotitulo + ': ' + (str(codfac)))
            var.cv.line(30, 685, 550, 685)
            items = ['Venta', 'Articulo', 'Precio', 'Cantidad', 'Total']
            var.cv.drawString(65, 673, items[0])
            var.cv.drawString(165, 673, items[1])
            var.cv.drawString(270, 673, items[2])
            var.cv.drawString(380, 673, items[3])
            var.cv.drawString(490, 673, items[4])
            suma = 0.0
            query = QtSql.QSqlQuery()
            query.prepare('select codven, precio, cantidad, codprodf from ventas where codfacf = :codfacf')
            query.bindValue(':codfacf', int(codfac))
            if query.exec_():
                i = 50
                j = 655
                while query.next():
                    codventa = query.value(0)
                    precio = query.value(1)
                    cantidad = query.value(2)
                    nombre = conexion.Conexion.buscaArt(int(query.value(3)))
                    total = round(precio * cantidad, 2)
                    suma += total
                    var.cv.setFont('Helvetica', size=9)
                    var.cv.drawString(i + 20, j, str(codventa))
                    var.cv.drawString(i + 100, j, str(nombre))
                    var.cv.drawString(i + 219, j, str(precio) + '€/kg')
                    var.cv.drawString(i + 340, j, str(cantidad))
                    var.cv.drawString(i + 442, j, str(total))
                    j = j - 20
            var.cv.save()
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('factura.pdf'):
                    os.startfile('%s/%s' % (rootPath, file))
                cont = cont + 1
        except Exception as error:
            print('Error creación informe facturas', error)