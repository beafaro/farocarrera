# This is a sample Python script.
from window import *
from windowaviso import *
import sys, var, events

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class DialogAviso(QtWidgets.QDialog):
    def __init__(self):
        '''

        Clase que instancia la ventana de avisos

        '''
        super(DialogAviso, self).__init__()
        var.dlgaviso = Ui_windowaviso()
        var.dlgaviso.setupUi(self)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        '''
        Eventos de botón
        '''
        var.ui.btnSalir.clicked.connect(events.Eventos.Salir)
        '''
        Eventos de la barra de menús
        '''
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgaviso = DialogAviso()
    window.show()
    sys.exit(app.exec())
