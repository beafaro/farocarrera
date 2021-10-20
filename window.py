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
        MainWindow.resize(1024, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblClientes = QtWidgets.QLabel(self.centralwidget)
        self.lblClientes.setGeometry(QtCore.QRect(410, 10, 171, 20))
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
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(140, 30, 731, 281))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(10, 20, 701, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 160, 204, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lblSexo = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblSexo.setFont(font)
        self.lblSexo.setObjectName("lblSexo")
        self.horizontalLayout_4.addWidget(self.lblSexo)
        self.rbtFem = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.rbtFem.setFont(font)
        self.rbtFem.setObjectName("rbtFem")
        self.rbtGroupSex = QtWidgets.QButtonGroup(MainWindow)
        self.rbtGroupSex.setObjectName("rbtGroupSex")
        self.rbtGroupSex.addButton(self.rbtFem)
        self.horizontalLayout_4.addWidget(self.rbtFem)
        self.rbtHom = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.rbtHom.setFont(font)
        self.rbtHom.setObjectName("rbtHom")
        self.rbtGroupSex.addButton(self.rbtHom)
        self.horizontalLayout_4.addWidget(self.rbtHom)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(51, 101, 441, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lblDir = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblDir.setFont(font)
        self.lblDir.setObjectName("lblDir")
        self.horizontalLayout_6.addWidget(self.lblDir)
        self.txtDir = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.txtDir.setFont(font)
        self.txtDir.setObjectName("txtDir")
        self.horizontalLayout_6.addWidget(self.txtDir)
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(10, 210, 701, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(51, 131, 521, 26))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblPro = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblPro.setFont(font)
        self.lblPro.setObjectName("lblPro")
        self.horizontalLayout_3.addWidget(self.lblPro)
        self.cmbProv = QtWidgets.QComboBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbProv.sizePolicy().hasHeightForWidth())
        self.cmbProv.setSizePolicy(sizePolicy)
        self.cmbProv.setObjectName("cmbProv")
        self.horizontalLayout_3.addWidget(self.cmbProv)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.lblMuni = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblMuni.setFont(font)
        self.lblMuni.setObjectName("lblMuni")
        self.horizontalLayout_3.addWidget(self.lblMuni)
        self.cmbMuni = QtWidgets.QComboBox(self.layoutWidget2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbMuni.sizePolicy().hasHeightForWidth())
        self.cmbMuni.setSizePolicy(sizePolicy)
        self.cmbMuni.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cmbMuni.setObjectName("cmbMuni")
        self.horizontalLayout_3.addWidget(self.cmbMuni)
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(50, 190, 565, 22))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lblFormaPago = QtWidgets.QLabel(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblFormaPago.sizePolicy().hasHeightForWidth())
        self.lblFormaPago.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblFormaPago.setFont(font)
        self.lblFormaPago.setObjectName("lblFormaPago")
        self.horizontalLayout_5.addWidget(self.lblFormaPago)
        self.chkEfectivo = QtWidgets.QCheckBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkEfectivo.sizePolicy().hasHeightForWidth())
        self.chkEfectivo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.chkEfectivo.setFont(font)
        self.chkEfectivo.setObjectName("chkEfectivo")
        self.chkGroupPago = QtWidgets.QButtonGroup(MainWindow)
        self.chkGroupPago.setObjectName("chkGroupPago")
        self.chkGroupPago.setExclusive(False)
        self.chkGroupPago.addButton(self.chkEfectivo)
        self.horizontalLayout_5.addWidget(self.chkEfectivo)
        self.chkTarjeta = QtWidgets.QCheckBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTarjeta.sizePolicy().hasHeightForWidth())
        self.chkTarjeta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.chkTarjeta.setFont(font)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.chkGroupPago.addButton(self.chkTarjeta)
        self.horizontalLayout_5.addWidget(self.chkTarjeta)
        self.chkCargoCuenta = QtWidgets.QCheckBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkCargoCuenta.sizePolicy().hasHeightForWidth())
        self.chkCargoCuenta.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.chkCargoCuenta.setFont(font)
        self.chkCargoCuenta.setObjectName("chkCargoCuenta")
        self.chkGroupPago.addButton(self.chkCargoCuenta)
        self.horizontalLayout_5.addWidget(self.chkCargoCuenta)
        self.chkTransfe = QtWidgets.QCheckBox(self.layoutWidget3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chkTransfe.sizePolicy().hasHeightForWidth())
        self.chkTransfe.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.chkTransfe.setFont(font)
        self.chkTransfe.setObjectName("chkTransfe")
        self.chkGroupPago.addButton(self.chkTransfe)
        self.horizontalLayout_5.addWidget(self.chkTransfe)
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget4.setGeometry(QtCore.QRect(50, 70, 601, 26))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblApel = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblApel.setFont(font)
        self.lblApel.setObjectName("lblApel")
        self.horizontalLayout_2.addWidget(self.lblApel)
        self.txtApel = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.txtApel.setFont(font)
        self.txtApel.setObjectName("txtApel")
        self.horizontalLayout_2.addWidget(self.txtApel)
        self.lblNome = QtWidgets.QLabel(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblNome.setFont(font)
        self.lblNome.setObjectName("lblNome")
        self.horizontalLayout_2.addWidget(self.lblNome)
        self.txtNome = QtWidgets.QLineEdit(self.layoutWidget4)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.txtNome.setFont(font)
        self.txtNome.setObjectName("txtNome")
        self.horizontalLayout_2.addWidget(self.txtNome)
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget5.setGeometry(QtCore.QRect(50, 40, 179, 26))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget5)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDNI = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblDNI.setFont(font)
        self.lblDNI.setObjectName("lblDNI")
        self.horizontalLayout.addWidget(self.lblDNI)
        self.txtDNI = QtWidgets.QLineEdit(self.layoutWidget5)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.txtDNI.setFont(font)
        self.txtDNI.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtDNI.setObjectName("txtDNI")
        self.horizontalLayout.addWidget(self.txtDNI)
        self.lblValidoDNI = QtWidgets.QLabel(self.layoutWidget5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblValidoDNI.sizePolicy().hasHeightForWidth())
        self.lblValidoDNI.setSizePolicy(sizePolicy)
        self.lblValidoDNI.setText("")
        self.lblValidoDNI.setObjectName("lblValidoDNI")
        self.horizontalLayout.addWidget(self.lblValidoDNI)
        self.btnGrabaCli = QtWidgets.QPushButton(self.groupBox)
        self.btnGrabaCli.setGeometry(QtCore.QRect(260, 230, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btnGrabaCli.setFont(font)
        self.btnGrabaCli.setObjectName("btnGrabaCli")
        self.btnSalir = QtWidgets.QPushButton(self.groupBox)
        self.btnSalir.setGeometry(QtCore.QRect(360, 230, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.btnSalir.setFont(font)
        self.btnSalir.setObjectName("btnSalir")
        self.btnLimpiaCli = QtWidgets.QPushButton(self.groupBox)
        self.btnLimpiaCli.setGeometry(QtCore.QRect(240, 40, 24, 24))
        self.btnLimpiaCli.setMaximumSize(QtCore.QSize(16777211, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/limpiaForm.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLimpiaCli.setIcon(icon)
        self.btnLimpiaCli.setIconSize(QtCore.QSize(16, 16))
        self.btnLimpiaCli.setObjectName("btnLimpiaCli")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(361, 32, 307, 34))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lblFechAlta = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblFechAlta.setFont(font)
        self.lblFechAlta.setObjectName("lblFechAlta")
        self.horizontalLayout_7.addWidget(self.lblFechAlta)
        self.txtFechaAltaCli = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.txtFechaAltaCli.setFont(font)
        self.txtFechaAltaCli.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtFechaAltaCli.setObjectName("txtFechaAltaCli")
        self.horizontalLayout_7.addWidget(self.txtFechaAltaCli)
        self.btnCalendar = QtWidgets.QPushButton(self.widget)
        self.btnCalendar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/calendario.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalendar.setIcon(icon1)
        self.btnCalendar.setIconSize(QtCore.QSize(24, 24))
        self.btnCalendar.setObjectName("btnCalendar")
        self.horizontalLayout_7.addWidget(self.btnCalendar)
        self.tabClientes = QtWidgets.QTableWidget(self.centralwidget)
        self.tabClientes.setGeometry(QtCore.QRect(140, 340, 731, 261))
        self.tabClientes.setMaximumSize(QtCore.QSize(800, 600))
        self.tabClientes.setAlternatingRowColors(True)
        self.tabClientes.setObjectName("tabClientes")
        self.tabClientes.setColumnCount(5)
        self.tabClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabClientes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabClientes.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabClientes.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 21))
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
        self.lblClientes.setText(_translate("MainWindow", "XESTIÓN CLIENTES"))
        self.groupBox.setTitle(_translate("MainWindow", "Datos Personales"))
        self.lblSexo.setText(_translate("MainWindow", "Sexo: "))
        self.rbtFem.setText(_translate("MainWindow", "Mujer"))
        self.rbtHom.setText(_translate("MainWindow", "Hombre"))
        self.lblDir.setText(_translate("MainWindow", "Dirección:"))
        self.lblPro.setText(_translate("MainWindow", "Provincia:"))
        self.lblMuni.setText(_translate("MainWindow", "Municipio:"))
        self.lblFormaPago.setText(_translate("MainWindow", "Forma de pago: "))
        self.chkEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.chkTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.chkCargoCuenta.setText(_translate("MainWindow", "Cargo en cuenta"))
        self.chkTransfe.setText(_translate("MainWindow", "Transferencia"))
        self.lblApel.setText(_translate("MainWindow", "Apellidos:"))
        self.lblNome.setText(_translate("MainWindow", "Nombre:"))
        self.lblDNI.setText(_translate("MainWindow", "DNI:"))
        self.btnGrabaCli.setText(_translate("MainWindow", "Guardar"))
        self.btnSalir.setText(_translate("MainWindow", "Salir"))
        self.lblFechAlta.setText(_translate("MainWindow", "Fecha de alta: "))
        item = self.tabClientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tabClientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tabClientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tabClientes.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Fecha de alta"))
        item = self.tabClientes.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Forma de pago"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.actionFichero.setText(_translate("MainWindow", "Fichero"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Alt+S"))
