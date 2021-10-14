# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnAceptar = QtWidgets.QPushButton(self.centralwidget)
        self.btnAceptar.setGeometry(QtCore.QRect(270, 270, 81, 23))
        self.btnAceptar.setObjectName("btnAceptar")
        self.lblClientes = QtWidgets.QLabel(self.centralwidget)
        self.lblClientes.setGeometry(QtCore.QRect(270, 10, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblClientes.setFont(font)
        self.lblClientes.setStyleSheet("color: rgb(0, 170, 255);\n"
"font: 75 12pt \"Verdana\";\n"
"background-color: rgb(224, 255, 255);\n"
"align: center;\n"
"")
        self.lblClientes.setObjectName("lblClientes")
        self.btnSalir = QtWidgets.QPushButton(self.centralwidget)
        self.btnSalir.setGeometry(QtCore.QRect(370, 270, 75, 23))
        self.btnSalir.setObjectName("btnSalir")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 240, 701, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 80, 601, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblApel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblApel.setFont(font)
        self.lblApel.setObjectName("lblApel")
        self.horizontalLayout_2.addWidget(self.lblApel)
        self.txtApel = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtApel.setObjectName("txtApel")
        self.horizontalLayout_2.addWidget(self.txtApel)
        self.lblNome = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.horizontalLayout_2.addWidget(self.lblNome)
        self.txtNome = QtWidgets.QLineEdit(self.layoutWidget)
        self.txtNome.setObjectName("txtNome")
        self.horizontalLayout_2.addWidget(self.txtNome)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 30, 701, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 50, 179, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDNI = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.horizontalLayout.addWidget(self.lblDNI)
        self.txtDNI = QtWidgets.QLineEdit(self.layoutWidget1)
        self.txtDNI.setObjectName("txtDNI")
        self.horizontalLayout.addWidget(self.txtDNI)
        self.lblValidoDNI = QtWidgets.QLabel(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValidoDNI.sizePolicy().hasHeightForWidth())
        self.lblValidoDNI.setSizePolicy(sizePolicy)
        self.lblValidoDNI.setText("")
        self.lblValidoDNI.setObjectName("lblValidoDNI")
        self.horizontalLayout.addWidget(self.lblValidoDNI)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 200, 481, 22))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblFormaPago = QtWidgets.QLabel(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFormaPago.sizePolicy().hasHeightForWidth())
        self.lblFormaPago.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblFormaPago.setFont(font)
        self.lblFormaPago.setObjectName("lblFormaPago")
        self.horizontalLayout_5.addWidget(self.lblFormaPago)
        self.chkEfectivo = QtWidgets.QCheckBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkEfectivo.sizePolicy().hasHeightForWidth())
        self.chkEfectivo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkEfectivo.setFont(font)
        self.chkEfectivo.setObjectName("chkEfectivo")
        self.chkGroupPago = QtWidgets.QButtonGroup(MainWindow)
        self.chkGroupPago.setObjectName("chkGroupPago")
        self.chkGroupPago.addButton(self.chkEfectivo)
        self.horizontalLayout_5.addWidget(self.chkEfectivo)
        self.chkTarjeta = QtWidgets.QCheckBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTarjeta.sizePolicy().hasHeightForWidth())
        self.chkTarjeta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkTarjeta.setFont(font)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.chkGroupPago.addButton(self.chkTarjeta)
        self.horizontalLayout_5.addWidget(self.chkTarjeta)
        self.chkCargoCuenta = QtWidgets.QCheckBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkCargoCuenta.sizePolicy().hasHeightForWidth())
        self.chkCargoCuenta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkCargoCuenta.setFont(font)
        self.chkCargoCuenta.setObjectName("chkCargoCuenta")
        self.chkGroupPago.addButton(self.chkCargoCuenta)
        self.horizontalLayout_5.addWidget(self.chkCargoCuenta)
        self.chkTransfe = QtWidgets.QCheckBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTransfe.sizePolicy().hasHeightForWidth())
        self.chkTransfe.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.chkTransfe.setFont(font)
        self.chkTransfe.setObjectName("chkTransfe")
        self.chkGroupPago.addButton(self.chkTransfe)
        self.horizontalLayout_5.addWidget(self.chkTransfe)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(70, 170, 178, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblSexo = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblSexo.setFont(font)
        self.lblSexo.setObjectName("lblSexo")
        self.horizontalLayout_4.addWidget(self.lblSexo)
        self.rbtFem = QtWidgets.QRadioButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbtFem.setFont(font)
        self.rbtFem.setObjectName("rbtFem")
        self.rbtGroupSex = QtWidgets.QButtonGroup(MainWindow)
        self.rbtGroupSex.setObjectName("rbtGroupSex")
        self.rbtGroupSex.addButton(self.rbtFem)
        self.horizontalLayout_4.addWidget(self.rbtFem)
        self.rbtHom = QtWidgets.QRadioButton(self.layoutWidget3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rbtHom.setFont(font)
        self.rbtHom.setObjectName("rbtHom")
        self.rbtGroupSex.addButton(self.rbtHom)
        self.horizontalLayout_4.addWidget(self.rbtHom)
        self.layoutWidget4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget4.setGeometry(QtCore.QRect(71, 141, 381, 22))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblPro = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblPro.setFont(font)
        self.lblPro.setObjectName("lblPro")
        self.horizontalLayout_3.addWidget(self.lblPro)
        self.cmbProv = QtWidgets.QComboBox(self.layoutWidget4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProv.sizePolicy().hasHeightForWidth())
        self.cmbProv.setSizePolicy(sizePolicy)
        self.cmbProv.setObjectName("cmbProv")
        self.horizontalLayout_3.addWidget(self.cmbProv)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lblMuni = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblMuni.setFont(font)
        self.lblMuni.setObjectName("lblMuni")
        self.horizontalLayout_3.addWidget(self.lblMuni)
        self.cmbMuni = QtWidgets.QComboBox(self.layoutWidget4)
        self.cmbMuni.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cmbMuni.setObjectName("cmbMuni")
        self.horizontalLayout_3.addWidget(self.cmbMuni)
        self.layoutWidget5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget5.setGeometry(QtCore.QRect(71, 111, 441, 22))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblDir = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblDir.setFont(font)
        self.lblDir.setObjectName("lblDir")
        self.horizontalLayout_6.addWidget(self.lblDir)
        self.txtDir = QtWidgets.QLineEdit(self.layoutWidget5)
        self.txtDir.setObjectName("txtDir")
        self.horizontalLayout_6.addWidget(self.txtDir)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(380, 40, 291, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblFechAlta = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblFechAlta.setFont(font)
        self.lblFechAlta.setObjectName("lblFechAlta")
        self.horizontalLayout_7.addWidget(self.lblFechAlta)
        self.txtFechaAltaCli = QtWidgets.QLineEdit(self.widget)
        self.txtFechaAltaCli.setObjectName("txtFechaAltaCli")
        self.horizontalLayout_7.addWidget(self.txtFechaAltaCli)
        self.btnCalendar = QtWidgets.QPushButton(self.widget)
        self.btnCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/calendario.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon)
        self.btnCalendar.setIconSize(QtCore.QSize(32, 32))
        self.btnCalendar.setObjectName("btnCalendar")
        self.horizontalLayout_7.addWidget(self.btnCalendar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionFichero = QtWidgets.QAction(MainWindow)
        self.actionFichero.setObjectName("actionFichero")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IMPORT-EXPORT TEIS"))
        self.btnAceptar.setText(_translate("MainWindow", "Aceptar"))
        self.lblClientes.setText(_translate("MainWindow", "XESTIÓN CLIENTES"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.lblApel.setText(_translate("MainWindow", "Apellidos:"))
        self.lblNome.setText(_translate("MainWindow", "Nombre:"))
        self.lblDNI.setText(_translate("MainWindow", "DNI:"))
        self.lblFormaPago.setText(_translate("MainWindow", "Forma de pago: "))
        self.chkEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.chkTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.chkCargoCuenta.setText(_translate("MainWindow", "Cargo en cuenta"))
        self.chkTransfe.setText(_translate("MainWindow", "Transferencia"))
        self.lblSexo.setText(_translate("MainWindow", "Sexo: "))
        self.rbtFem.setText(_translate("MainWindow", "Mujer"))
        self.rbtHom.setText(_translate("MainWindow", "Hombre"))
        self.lblPro.setText(_translate("MainWindow", "Provincia:"))
        self.lblMuni.setText(_translate("MainWindow", "Municipio:"))
        self.lblDir.setText(_translate("MainWindow", "Dirección:"))
        self.lblFechAlta.setText(_translate("MainWindow", "Fecha de alta: "))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionFichero.setText(_translate("MainWindow", "Fichero"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Alt+S"))
