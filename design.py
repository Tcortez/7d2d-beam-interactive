# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Main Window"))
        MainWindow.resize(342, 542)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_4.setItem(0, QtGui.QFormLayout.SpanningRole, spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setStyleSheet(_fromUtf8("font: 75 18pt \"DejaVu Sans\";\n"
"text-decoration: underline;"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_4.setWidget(1, QtGui.QFormLayout.SpanningRole, self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_4.setItem(2, QtGui.QFormLayout.SpanningRole, spacerItem1)
        self.usernameLabel = QtGui.QLabel(self.centralwidget)
        self.usernameLabel.setIndent(0)
        self.usernameLabel.setObjectName(_fromUtf8("usernameLabel"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.LabelRole, self.usernameLabel)
        self.usernameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.usernameLineEdit.setObjectName(_fromUtf8("usernameLineEdit"))
        self.formLayout_4.setWidget(3, QtGui.QFormLayout.FieldRole, self.usernameLineEdit)
        self.passwordLabel = QtGui.QLabel(self.centralwidget)
        self.passwordLabel.setIndent(0)
        self.passwordLabel.setObjectName(_fromUtf8("passwordLabel"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))
        self.formLayout_4.setWidget(4, QtGui.QFormLayout.FieldRole, self.passwordLineEdit)
        spacerItem2 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_4.setItem(5, QtGui.QFormLayout.SpanningRole, spacerItem2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setStyleSheet(_fromUtf8("font: 75 18pt \"DejaVu Sans\";\n"
"text-decoration: underline;"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setIndent(0)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_4.setWidget(6, QtGui.QFormLayout.SpanningRole, self.label_2)
        spacerItem3 = QtGui.QSpacerItem(40, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_4.setItem(7, QtGui.QFormLayout.SpanningRole, spacerItem3)
        self.hostLabel = QtGui.QLabel(self.centralwidget)
        self.hostLabel.setIndent(0)
        self.hostLabel.setObjectName(_fromUtf8("hostLabel"))
        self.formLayout_4.setWidget(8, QtGui.QFormLayout.LabelRole, self.hostLabel)
        self.hostLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.hostLineEdit.setObjectName(_fromUtf8("hostLineEdit"))
        self.formLayout_4.setWidget(8, QtGui.QFormLayout.FieldRole, self.hostLineEdit)
        self.portLabel = QtGui.QLabel(self.centralwidget)
        self.portLabel.setIndent(0)
        self.portLabel.setObjectName(_fromUtf8("portLabel"))
        self.formLayout_4.setWidget(9, QtGui.QFormLayout.LabelRole, self.portLabel)
        self.portLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.portLineEdit.setObjectName(_fromUtf8("portLineEdit"))
        self.formLayout_4.setWidget(9, QtGui.QFormLayout.FieldRole, self.portLineEdit)
        self.passwordLabel_2 = QtGui.QLabel(self.centralwidget)
        self.passwordLabel_2.setIndent(0)
        self.passwordLabel_2.setObjectName(_fromUtf8("passwordLabel_2"))
        self.formLayout_4.setWidget(10, QtGui.QFormLayout.LabelRole, self.passwordLabel_2)
        self.passwordLineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.passwordLineEdit_2.setObjectName(_fromUtf8("passwordLineEdit_2"))
        self.formLayout_4.setWidget(10, QtGui.QFormLayout.FieldRole, self.passwordLineEdit_2)
        spacerItem4 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_4.setItem(11, QtGui.QFormLayout.SpanningRole, spacerItem4)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setStyleSheet(_fromUtf8("font: 75 18pt \"DejaVu Sans\";\n"
"text-decoration: underline;"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setIndent(0)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_4.setWidget(12, QtGui.QFormLayout.SpanningRole, self.label_3)
        spacerItem5 = QtGui.QSpacerItem(40, 5, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_4.setItem(13, QtGui.QFormLayout.SpanningRole, spacerItem5)
        self.steamIDLabel = QtGui.QLabel(self.centralwidget)
        self.steamIDLabel.setIndent(0)
        self.steamIDLabel.setObjectName(_fromUtf8("steamIDLabel"))
        self.formLayout_4.setWidget(14, QtGui.QFormLayout.LabelRole, self.steamIDLabel)
        self.steamIDLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.steamIDLineEdit.setObjectName(_fromUtf8("steamIDLineEdit"))
        self.formLayout_4.setWidget(14, QtGui.QFormLayout.FieldRole, self.steamIDLineEdit)
        spacerItem6 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_4.setItem(15, QtGui.QFormLayout.SpanningRole, spacerItem6)
        self.startBtn = QtGui.QPushButton(self.centralwidget)
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        self.formLayout_4.setWidget(16, QtGui.QFormLayout.SpanningRole, self.startBtn)
        self.stopBtn = QtGui.QPushButton(self.centralwidget)
        self.stopBtn.setObjectName(_fromUtf8("stopBtn"))
        self.formLayout_4.setWidget(17, QtGui.QFormLayout.SpanningRole, self.stopBtn)
        spacerItem7 = QtGui.QSpacerItem(40, 10, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_4.setItem(18, QtGui.QFormLayout.SpanningRole, spacerItem7)
        self.verticalLayout_4.addLayout(self.formLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "BEAM INTERACTIVE LOGIN", None))
        self.usernameLabel.setText(_translate("MainWindow", "Username", None))
        self.passwordLabel.setText(_translate("MainWindow", "Password", None))
        self.label_2.setText(_translate("MainWindow", "TELNET SERVER LOGIN", None))
        self.hostLabel.setText(_translate("MainWindow", "Host", None))
        self.portLabel.setText(_translate("MainWindow", "Port", None))
        self.passwordLabel_2.setText(_translate("MainWindow", "Password", None))
        self.label_3.setText(_translate("MainWindow", "7DTD PLAYER INFO", None))
        self.steamIDLabel.setText(_translate("MainWindow", "SteamID", None))
        self.startBtn.setText(_translate("MainWindow", "Start Interactive", None))
        self.stopBtn.setText(_translate("MainWindow", "Stop Interactive", None))

