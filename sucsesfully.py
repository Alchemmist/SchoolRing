# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/sucsesfully.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sucsesfully(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(416, 204)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../icons/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color:     #333333")
        self.suc_button = QtWidgets.QPushButton(Dialog)
        self.suc_button.setGeometry(QtCore.QRect(180, 110, 61, 61))
        self.suc_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.suc_button.setStyleSheet("color: white;\n"
"border-radius: 30;")
        self.suc_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/../icons/message/sucsesfully.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.suc_button.setIcon(icon1)
        self.suc_button.setIconSize(QtCore.QSize(80, 80))
        self.suc_button.setObjectName("suc_button")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 341, 71))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text Bold")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "sucsesfully"))