# This is a sample Python script.
import clients
import conexion
import invoice
import products
from window import *
from windowaviso import *
from windowcal import *
import sys, var, events, locale, informes
from datetime import *
locale.setlocale(locale.LC_ALL, "es-ES")

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class FileDialogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        '''
        ventana abrir explorador de windows
        '''
        super(FileDialogAbrir, self).__init__()


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        '''
        ventana calendario
        '''
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_windowcal()
        var.dlgcalendar.setupUi(self)
        diaactual= datetime.now().day
        mesactual= datetime.now().month
        anoactual= datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate(QtCore.QDate(anoactual,mesactual,diaactual))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)


class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        '''
        Clase que instancia la ventana de avisos
        '''
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)
        var.dlgaviso.btnBoxAviso.accepted.connect(self.accept)
        var.dlgaviso.btnBoxAviso.rejected.connect(self.reject)


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''
        Eventos de botón
        '''
        var.ui.btnCalendar.clicked.connect(events.Eventos.abrircal)
        # var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.SelSexo)
        # var.ui.chkGroupPago.buttonClicked.connect(clients.Clientes.SelPago)
        var.ui.btnGrabaCli.clicked.connect(clients.Clientes.guardaCli)
        var.ui.btnLimpiaCli.clicked.connect(clients.Clientes.limpiaFormCli)
        var.ui.btnBajaCli.clicked.connect(clients.Clientes.bajaCli)
        var.ui.btnModifCli.clicked.connect(clients.Clientes.modifCli)
        var.ui.btnVisualiza.clicked.connect(informes.Informes.listadoClientes)

        #Eventos botón de Productos
        var.ui.btnGuardaProd.clicked.connect(products.Productos.guardaProd)
        var.ui.btnLimpiaProd.clicked.connect(products.Productos.limpiaFormProd)
        var.ui.btnBajaProd.clicked.connect(products.Productos.bajaProd)
        var.ui.btnModifProd.clicked.connect(products.Productos.modifProd)
        var.ui.btnVisualizaProd.clicked.connect(informes.Informes.listadoProductos)


        '''
        Eventos botón de Facturas
        '''
        var.ui.btnBuscaClifac.clicked.connect(invoice.Facturas.buscaCli)
        var.ui.btnFechafac.clicked.connect(events.Eventos.abrircal)
        var.ui.btnFacturar.clicked.connect(invoice.Facturas.facturar)

        '''
        Eventos de la barra de menús y de herramientas
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionAbrir.triggered.connect(events.Eventos.Abrir)
        var.ui.actionCrear_Backup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionRestaurar_Backup.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionImprimir.triggered.connect(events.Eventos.imprimir)
        var.ui.actionImportar_datos.triggered.connect(events.Eventos.importarDatos)
        var.ui.actionExportar_datos.triggered.connect(events.Eventos.exportarDatos)


        '''
        Eventos de la barra de herramientas
        '''
        var.ui.actionbarSalir.triggered.connect(events.Eventos.Salir)
        var.ui.actionbarAbrirCarpeta.triggered.connect(events.Eventos.Abrir)
        var.ui.actionbarCrearBackup.triggered.connect(events.Eventos.crearBackup)
        var.ui.actionbarRestaurarBackup.triggered.connect(events.Eventos.restaurarBackup)
        var.ui.actionbarImprimir.triggered.connect(events.Eventos.imprimir)


        '''
        Eventos caja de texto
        '''
        var.ui.txtDNI.editingFinished.connect(clients.Clientes.validarDNI)
        # poner la primera letra de cada palabra en mayúscula
        var.ui.txtApel.editingFinished.connect(clients.Clientes.letraCapital)
        var.ui.txtNome.editingFinished.connect(clients.Clientes.letraCapital)
        var.ui.txtDir.editingFinished.connect(clients.Clientes.letraCapital)

        '''
        Eventos QTabWidget
        '''
        events.Eventos.resizeTablaCli(self)
        var.ui.tabClientes.clicked.connect(clients.Clientes.cargaCli)
        var.ui.tabClientes.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        #Eventos QTabWidget productos
        events.Eventos.resizeTablaProd(self)
        var.ui.tabProductos.clicked.connect(products.Productos.cargaProd)
        var.ui.tabProductos.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        #tabla facturas
        events.Eventos.resizeTablaFac(self)
        var.ui.tabFacturas.clicked.connect(invoice.Facturas.cargaFac)
        var.ui.tabFacturas.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        var.ui.tabClientes.clicked.connect(invoice.Facturas.cargaCliFac)

        '''
        Base de datos
        '''
        conexion.Conexion.db_connect(var.filedb)
        conexion.Conexion.cargarTabCli(self)
        conexion.Conexion.cargarTabProd(self)
        conexion.Conexion.cargarTabFacturas(self)

        '''
        Eventos de comboBox
        '''
        conexion.Conexion.cargarProv(self)
        var.ui.cmbProv.currentIndexChanged.connect(conexion.Conexion.selMuni)

        '''
        Barra de estado
        '''
        var.ui.statusbar.addPermanentWidget(var.ui.lblFecha, 1)
        var.ui.lblFecha.setText("Import-Export Vigo")
        day = datetime.now()
        var.ui.lblFecha.setText(day.strftime("%A, %d de %B de %Y %H:%M").capitalize())

        '''
        Eventos spinbox
        '''
        var.ui.spinEnvio.valueChanged.connect(clients.Clientes.recogerValorSpinbox)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    #instanciamos por si llegase a hacer falta
    var.dlgaviso = DialogAviso()
    var.dlgcalendar = DialogCalendar()
    var.dlgabrir = FileDialogAbrir()
    window.show()
    sys.exit(app.exec())
