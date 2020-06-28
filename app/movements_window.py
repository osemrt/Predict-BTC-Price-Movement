from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MovementsWindow(object):
    def setupUi(self, MovementsWindow):
        MovementsWindow.setObjectName("MovementsWindow")
        MovementsWindow.resize(997, 728)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/ytu_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MovementsWindow.setWindowIcon(icon)
        MovementsWindow.setAutoFillBackground(False)
        MovementsWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MovementsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_movements = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_movements.sizePolicy().hasHeightForWidth())
        self.label_movements.setSizePolicy(sizePolicy)
        self.label_movements.setMinimumSize(QtCore.QSize(750, 450))
        self.label_movements.setMaximumSize(QtCore.QSize(1920, 1080))
        self.label_movements.setAutoFillBackground(False)
        self.label_movements.setText("")
        self.label_movements.setPixmap(QtGui.QPixmap("./img/movements.png"))
        self.label_movements.setScaledContents(True)
        self.label_movements.setAlignment(QtCore.Qt.AlignCenter)
        self.label_movements.setObjectName("label_movements")
        self.verticalLayout.addWidget(self.label_movements)
        MovementsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MovementsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 997, 21))
        self.menubar.setObjectName("menubar")
        MovementsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MovementsWindow)
        self.statusbar.setObjectName("statusbar")
        MovementsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MovementsWindow)
        QtCore.QMetaObject.connectSlotsByName(MovementsWindow)

    def retranslateUi(self, MovementsWindow):
        _translate = QtCore.QCoreApplication.translate
        MovementsWindow.setWindowTitle(_translate("MovementsWindow", "The Influence of News on Bitcoin Price"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MovementsWindow = QtWidgets.QMainWindow()
    ui = Ui_MovementsWindow()
    ui.setupUi(MovementsWindow)
    MovementsWindow.show()
    sys.exit(app.exec_())
