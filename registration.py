# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/registration.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Registration(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(425, 557)
        Dialog.setBaseSize(QtCore.QSize(0, 34))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../icons/main_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color:     #333333")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, -20, 431, 121))
        self.frame.setStyleSheet("background-color: #0080ff;\n"
"border-radius: 13;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(180, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Text Bold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: white;\n"
"background-color: #0080ff;")
        self.label_13.setObjectName("label_13")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(110, 40, 61, 51))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/../icons/registration/hello.png"))
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(60, 110, 321, 431))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 327, 642))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("color: white")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 11, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("ui/icons/FIO.png"))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: white")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("ui/icons/Schoolnumber.png"))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)
        self.FIO_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FIO_lineEdit.sizePolicy().hasHeightForWidth())
        self.FIO_lineEdit.setSizePolicy(sizePolicy)
        self.FIO_lineEdit.setMinimumSize(QtCore.QSize(291, 41))
        self.FIO_lineEdit.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        self.FIO_lineEdit.setFont(font)
        self.FIO_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.FIO_lineEdit.setStyleSheet("border-radius: 9; \n"
"border: 2px solid white;\n"
"color: white")
        self.FIO_lineEdit.setText("")
        self.FIO_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.FIO_lineEdit.setObjectName("FIO_lineEdit")
        self.gridLayout.addWidget(self.FIO_lineEdit, 3, 0, 1, 4)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: white")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 2, 1, 1)
        self.school_num_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.school_num_lineEdit.sizePolicy().hasHeightForWidth())
        self.school_num_lineEdit.setSizePolicy(sizePolicy)
        self.school_num_lineEdit.setMinimumSize(QtCore.QSize(291, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        self.school_num_lineEdit.setFont(font)
        self.school_num_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.school_num_lineEdit.setStyleSheet("border-radius: 9; \n"
"border: 2px solid white;\n"
"color: white")
        self.school_num_lineEdit.setText("")
        self.school_num_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.school_num_lineEdit.setObjectName("school_num_lineEdit")
        self.gridLayout.addWidget(self.school_num_lineEdit, 12, 0, 1, 3)
        self.login_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_lineEdit.sizePolicy().hasHeightForWidth())
        self.login_lineEdit.setSizePolicy(sizePolicy)
        self.login_lineEdit.setMinimumSize(QtCore.QSize(291, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        self.login_lineEdit.setFont(font)
        self.login_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.login_lineEdit.setStyleSheet("border-radius: 9; \n"
"border: 2px solid white;\n"
"color: white")
        self.login_lineEdit.setText("")
        self.login_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.gridLayout.addWidget(self.login_lineEdit, 6, 0, 1, 4)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap("ui/icons/building.png"))
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 13, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: white")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 13, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("ui/icons/login.png"))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap("ui/icons/phone.png"))
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 15, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: white")
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 15, 2, 1, 1)
        self.building_num_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.building_num_lineEdit.sizePolicy().hasHeightForWidth())
        self.building_num_lineEdit.setSizePolicy(sizePolicy)
        self.building_num_lineEdit.setMinimumSize(QtCore.QSize(291, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        self.building_num_lineEdit.setFont(font)
        self.building_num_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.building_num_lineEdit.setStyleSheet("border-radius: 9; \n"
"border: 2px solid white;\n"
"color: white")
        self.building_num_lineEdit.setText("")
        self.building_num_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.building_num_lineEdit.setObjectName("building_num_lineEdit")
        self.gridLayout.addWidget(self.building_num_lineEdit, 14, 0, 1, 3)
        self.phone_num_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phone_num_lineEdit.sizePolicy().hasHeightForWidth())
        self.phone_num_lineEdit.setSizePolicy(sizePolicy)
        self.phone_num_lineEdit.setMinimumSize(QtCore.QSize(291, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        self.phone_num_lineEdit.setFont(font)
        self.phone_num_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.phone_num_lineEdit.setStyleSheet("border-radius: 9; \n"
"border: 2px solid white;\n"
"color: white")
        self.phone_num_lineEdit.setText("")
        self.phone_num_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.phone_num_lineEdit.setObjectName("phone_num_lineEdit")
        self.gridLayout.addWidget(self.phone_num_lineEdit, 16, 0, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("ui/icons/password.png"))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.concoct_pw_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.concoct_pw_lineEdit.sizePolicy().hasHeightForWidth())
        self.concoct_pw_lineEdit.setSizePolicy(sizePolicy)
        self.concoct_pw_lineEdit.setMinimumSize(QtCore.QSize(291, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        self.concoct_pw_lineEdit.setFont(font)
        self.concoct_pw_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.concoct_pw_lineEdit.setStyleSheet("border-radius: 9; \n"
"border: 2px solid white;\n"
"color: white")
        self.concoct_pw_lineEdit.setText("")
        self.concoct_pw_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.concoct_pw_lineEdit.setObjectName("concoct_pw_lineEdit")
        self.gridLayout.addWidget(self.concoct_pw_lineEdit, 8, 0, 1, 3)
        self.go_sistem_button_reg = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_sistem_button_reg.sizePolicy().hasHeightForWidth())
        self.go_sistem_button_reg.setSizePolicy(sizePolicy)
        self.go_sistem_button_reg.setMinimumSize(QtCore.QSize(170, 50))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display Bold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.go_sistem_button_reg.setFont(font)
        self.go_sistem_button_reg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.go_sistem_button_reg.setStyleSheet("color: white;\n"
"background-color: #0080ff;\n"
"border-radius: 15;\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/../icons/registration/ring.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("ui/../icons/registration/ring.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("ui/../icons/registration/ring.png"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("ui/../icons/registration/ring.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("ui/../icons/registration/ring.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        icon1.addPixmap(QtGui.QPixmap("ui/../icons/registration/ring.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap("ui/../icons/registration/ring.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.go_sistem_button_reg.setIcon(icon1)
        self.go_sistem_button_reg.setIconSize(QtCore.QSize(30, 30))
        self.go_sistem_button_reg.setObjectName("go_sistem_button_reg")
        self.gridLayout.addWidget(self.go_sistem_button_reg, 17, 2, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("ui/icons/password.png"))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: white")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 2, 1, 1)
        self.repeat_pw_lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.repeat_pw_lineEdit.sizePolicy().hasHeightForWidth())
        self.repeat_pw_lineEdit.setSizePolicy(sizePolicy)
        self.repeat_pw_lineEdit.setMinimumSize(QtCore.QSize(291, 41))
        font = QtGui.QFont()
        font.setFamily("Yandex Sans Display")
        font.setPointSize(12)
        self.repeat_pw_lineEdit.setFont(font)
        self.repeat_pw_lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.repeat_pw_lineEdit.setStyleSheet("border-radius: 9; \n"
"border: 2px solid white;\n"
"color: white")
        self.repeat_pw_lineEdit.setText("")
        self.repeat_pw_lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.repeat_pw_lineEdit.setObjectName("repeat_pw_lineEdit")
        self.gridLayout.addWidget(self.repeat_pw_lineEdit, 10, 0, 1, 3)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("ui/../icons/registration/FIO.png"))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("ui/../icons/registration/login.png"))
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("ui/../icons/registration/password.png"))
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 7, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setText("")
        self.label_20.setPixmap(QtGui.QPixmap("ui/../icons/registration/password.png"))
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 9, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setText("")
        self.label_21.setPixmap(QtGui.QPixmap("ui/../icons/registration/Schoolnumber.png"))
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 11, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setText("")
        self.label_22.setPixmap(QtGui.QPixmap("ui/../icons/registration/building.png"))
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 13, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy)
        self.label_23.setText("")
        self.label_23.setPixmap(QtGui.QPixmap("ui/../icons/registration/phone.png"))
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 15, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_13.setText(_translate("Dialog", "Hello!"))
        self.label_14.setText(_translate("Dialog", "School number *"))
        self.label_2.setText(_translate("Dialog", "FIO *"))
        self.label_3.setText(_translate("Dialog", "Login *"))
        self.label_16.setText(_translate("Dialog", "Building number *"))
        self.label_18.setText(_translate("Dialog", "Phone number"))
        self.go_sistem_button_reg.setText(_translate("Dialog", "Ring!"))
        self.label_5.setText(_translate("Dialog", "Repeat the password *"))
        self.label_4.setText(_translate("Dialog", " Сoncoct password *"))
