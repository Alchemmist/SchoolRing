from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame


class HomeFrame(object):

    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(199, 351)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QtCore.QSize(190, 0))
        Frame.setStyleSheet("border-radius: 15;\n"
                            "background-color: rgba(0,127,255, 60);")
        self.label_42 = QtWidgets.QLabel(Frame)
        self.label_42.setGeometry(QtCore.QRect(50, 20, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color: white;\n"
                                    "background-color: rgb(255,160,0, 0);\n"
                                    "")
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.label_45 = QtWidgets.QLabel(Frame)
        self.label_45.setGeometry(QtCore.QRect(0, 200, 190, 61))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("color: white;\n"
                                    "background-color: rgb(255,160,0, 0);\n"
                                    "")
        self.label_45.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_45.setWordWrap(True)
        self.label_45.setObjectName("label_45")
        self.label_47 = QtWidgets.QLabel(Frame)
        self.label_47.setGeometry(QtCore.QRect(20, 290, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("color: white;\n"
                                    "background-color: rgb(255,160,0, 0);\n"
                                    "")
        self.label_47.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_47.setWordWrap(True)
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(Frame)
        self.label_48.setGeometry(QtCore.QRect(30, 260, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet("color: white;\n"
                                    "background-color: rgb(255,160,0, 0);\n"
                                    "")
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.label_43 = QtWidgets.QLabel(Frame)
        self.label_43.setGeometry(QtCore.QRect(30, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setStyleSheet("color: white;\n"
                                    "background-color: rgb(255,160,0, 0);\n"
                                    "")
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.label_46 = QtWidgets.QLabel(Frame)
        self.label_46.setGeometry(QtCore.QRect(30, 170, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text Bold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setStyleSheet("color: white;\n"
                                    "background-color: rgb(255,160,0, 0);\n"
                                    "")
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.label_44 = QtWidgets.QLabel(Frame)
        self.label_44.setGeometry(QtCore.QRect(20, 120, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color: white;\n"
                                    "background-color: rgb(255,160,0, 0);\n"
                                    "")
        self.label_44.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.label_44.setWordWrap(True)
        self.label_44.setObjectName("label_44")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_42.setText(_translate("Frame", "Урок - 1"))
        self.label_45.setText(_translate("Frame", "Пираты карипскогот моря"))
        self.label_47.setText(_translate("Frame", "Ploho, Город устал"))
        self.label_48.setText(_translate("Frame", "09:10"))
        self.label_43.setText(_translate("Frame", "08:29"))
        self.label_46.setText(_translate("Frame", "08:30"))
        self.label_44.setText(_translate("Frame", "Уведомление"))
