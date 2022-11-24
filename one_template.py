# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/one_template.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(120, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QtCore.QSize(120, 150))
        Frame.setStyleSheet("border-radius: 15;\n"
"background-color: rgba(85,85,255, 230);")
        self.title = QtWidgets.QLabel(Frame)
        self.title.setGeometry(QtCore.QRect(10, 0, 101, 71))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: white;\n"
"background-color: rgb(255,160,0, 0);\n"
"")
        self.title.setLineWidth(2)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(True)
        self.title.setIndent(0)
        self.title.setObjectName("title")
        self.edit_template = QtWidgets.QPushButton(Frame)
        self.edit_template.setGeometry(QtCore.QRect(30, 80, 61, 61))
        self.edit_template.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_template.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../icons/main_window/templte/edit_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_template.setIcon(icon)
        self.edit_template.setIconSize(QtCore.QSize(50, 50))
        self.edit_template.setObjectName("edit_template")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.title.setText(_translate("Frame", "NewYear"))
