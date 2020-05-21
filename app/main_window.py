from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QInputDialog, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon

import pandas as pd
import numpy as np

from config.variables import INITIAL_BTC_PRICE
from config.variables import MESSAGE_DAILY_STATUS
from config.variables import MESSAGE_RESULT
from config.variables import MESSAGE_PERIOD
from config.variables import MESSAGE_AVERAGE
from config.variables import MESSAGE_COUNT
from config.variables import MESSAGE_DEFAULT
from config.variables import INCREASE
from config.variables import DECREASE

from util.model_functions import get_model
from util.model_functions import get_predictions
from util.model_functions import get_price_data
from util.model_functions import init_model


class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):
        self.CURRENT_BTC_PRICE = 5095.76
        self.INITIAL_BTC_PRICE = 5095.76
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(774, 564)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/ytu_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(36, 36))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_7 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_7.setGeometry(QtCore.QRect(20, 20, 740, 501))
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_4 = QtWidgets.QSplitter(self.groupBox_2)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter = QtWidgets.QSplitter(self.splitter_4)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setMinimumSize(QtCore.QSize(90, 0))
        self.label.setMaximumSize(QtCore.QSize(90, 95545))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_X_test = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_X_test.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_X_test.setFont(font)
        self.lineEdit_X_test.setObjectName("lineEdit_X_test")
        self.pushButton_X_test = QtWidgets.QPushButton(self.splitter)
        self.pushButton_X_test.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_X_test.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_X_test.setFont(font)
        self.pushButton_X_test.setObjectName("pushButton_X_test")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_4 = QtWidgets.QLabel(self.splitter_3)
        self.label_4.setMinimumSize(QtCore.QSize(90, 0))
        self.label_4.setMaximumSize(QtCore.QSize(90, 95545))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_Y_test = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_Y_test.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_Y_test.setFont(font)
        self.lineEdit_Y_test.setObjectName("lineEdit_Y_test")
        self.pushButton_Y_test = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_Y_test.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_Y_test.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Y_test.setFont(font)
        self.pushButton_Y_test.setObjectName("pushButton_Y_test")
        self.verticalLayout.addWidget(self.splitter_4)
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.groupBox = QtWidgets.QGroupBox(self.splitter_6)
        self.groupBox.setMinimumSize(QtCore.QSize(172, 94))
        self.groupBox.setMaximumSize(QtCore.QSize(172, 94))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_5 = QtWidgets.QSplitter(self.groupBox)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.radioButton_CNNLSTM = QtWidgets.QRadioButton(self.splitter_5)
        self.radioButton_CNNLSTM.setMinimumSize(QtCore.QSize(140, 20))
        self.radioButton_CNNLSTM.setMaximumSize(QtCore.QSize(140, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_CNNLSTM.setFont(font)
        self.radioButton_CNNLSTM.setObjectName("radioButton_CNNLSTM")
        self.radioButton_SentimentLSTM = QtWidgets.QRadioButton(self.splitter_5)
        self.radioButton_SentimentLSTM.setMinimumSize(QtCore.QSize(140, 20))
        self.radioButton_SentimentLSTM.setMaximumSize(QtCore.QSize(140, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_SentimentLSTM.setFont(font)
        self.radioButton_SentimentLSTM.setObjectName("radioButton_SentimentLSTM")
        self.verticalLayout_2.addWidget(self.splitter_5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.splitter_6)
        self.groupBox_3.setMinimumSize(QtCore.QSize(320, 94))
        self.groupBox_3.setMaximumSize(QtCore.QSize(320, 94))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.splitter_2 = QtWidgets.QSplitter(self.groupBox_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_10 = QtWidgets.QLabel(self.splitter_2)
        self.label_10.setMinimumSize(QtCore.QSize(300, 20))
        self.label_10.setMaximumSize(QtCore.QSize(300, 45652))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.pushButton_deposit = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_deposit.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_deposit.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_deposit.setFont(font)
        self.pushButton_deposit.setObjectName("pushButton_deposit")
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.splitter_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_setStopLoss = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_setStopLoss.setGeometry(QtCore.QRect(20, 40, 200, 30))
        self.pushButton_setStopLoss.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_setStopLoss.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_setStopLoss.setFont(font)
        self.pushButton_setStopLoss.setObjectName("pushButton_setStopLoss")
        self.pushButton_start = QtWidgets.QPushButton(self.splitter_7)
        self.pushButton_start.setMinimumSize(QtCore.QSize(740, 30))
        self.pushButton_start.setMaximumSize(QtCore.QSize(740, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.textEdit_log = QtWidgets.QTextEdit(self.splitter_7)
        self.textEdit_log.setMinimumSize(QtCore.QSize(740, 250))
        self.textEdit_log.setMaximumSize(QtCore.QSize(740, 250))
        self.textEdit_log.setObjectName("textEdit_log")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 774, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.TEST_SET_Y = 1
        self.TEST_SET_X = 2
        self.CNN_LSTM = 3
        self.SENTIMENT_LSTM = 4

        self.pushButton_X_test.clicked.connect(lambda: self.browseFile(self.TEST_SET_X))
        self.pushButton_Y_test.clicked.connect(lambda: self.browseFile(self.TEST_SET_Y))
        self.pushButton_deposit.clicked.connect(self.deposit)
        self.pushButton_setStopLoss.clicked.connect(self.show_popup)
        self.pushButton_start.clicked.connect(self.start)

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "Exploring the Influence of News on Bitcoin Price"))
        self.groupBox_2.setTitle(_translate("MainScreen", "Upload Datasets"))
        self.label.setText(_translate("MainScreen", "X_test"))
        self.pushButton_X_test.setText(_translate("MainScreen", "Browse"))
        self.label_4.setText(_translate("MainScreen", "y_test"))
        self.pushButton_Y_test.setText(_translate("MainScreen", "Browse"))
        self.groupBox.setTitle(_translate("MainScreen", "Select a model"))
        self.radioButton_CNNLSTM.setText(_translate("MainScreen", "CNN-LSTM"))
        self.radioButton_SentimentLSTM.setText(_translate("MainScreen", "Sentiment-LSTM"))
        self.groupBox_3.setTitle(_translate("MainScreen", "Balance"))
        self.label_10.setText(_translate("MainScreen", "0.00000000 BTC / $0.00"))
        self.pushButton_deposit.setText(_translate("MainScreen", "Deposit"))
        self.groupBox_5.setTitle(_translate("MainScreen", "Options"))
        self.pushButton_setStopLoss.setText(_translate("MainScreen", "Set Stop Loss"))
        self.pushButton_start.setText(_translate("MainScreen", "Start"))

    def browseFile(self, id):
        filenames = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', '*.csv *.txt')
        firstFile = filenames[0]

        if (id == self.TEST_SET_X):
            print('X_test: ' + firstFile)
            self.lineEdit_X_test.setText(firstFile)
        else:
            print('y_test: ' + firstFile)
            self.lineEdit_Y_test.setText(firstFile)

    def deposit(self):
        text, ok = QInputDialog.getText(self, "Deposit", "Update your account", QLineEdit.Normal)

        if ok and text is not None:
            self.balance_usd = float(text)
            self.balance_btc = round(self.balance_usd / self.CURRENT_BTC_PRICE, 8)
            self.label_10.setText(str(self.balance_btc) + " BTC / $" + str(self.balance_usd))
            self.INITIAL_BALANCE_USER = self.balance_usd

    def update_balance(self):
        price_change = (self.balance_usd * self.CHANGE) / 100
        self.balance_usd += price_change
        self.balance_btc = round(self.balance_usd / self.CURRENT_BTC_PRICE, 8)
        self.label_10.setText(str(self.balance_btc) + " BTC / $" + str(round(self.balance_usd, 2)))

    def show_popup(self):
        message = QMessageBox()
        message.setWindowTitle("Coming Soon")
        message.setText("This feature is not available now!")
        message.setIcon(QMessageBox.Information)
        message.exec_()

    def show_popup_error(self):
        message = QMessageBox()
        message.setWindowTitle("Error")
        message.setText(self.error_message)
        message.setIcon(QMessageBox.Critical)
        message.exec_()

    def start(self):
        self.textEdit_log.setText("")

        self.CURRENT_BTC_PRICE = INITIAL_BTC_PRICE

        self.x_test_path = self.lineEdit_X_test.text()
        self.y_test_path = self.lineEdit_Y_test.text()

        if self.isValid():
            init_model(self)
            self.trueCount = 0
            for i in range(0, self.last):
                # Daily BTC-USD
                self.CURRENT_BTC_PRICE = self.price_data[i][6]

                # Price movement
                if self.price_data[i][-1] == 1:
                    self.ACUTAL_MOVEMENT = INCREASE
                else:
                    self.ACUTAL_MOVEMENT = DECREASE

                # Date and Percent change
                self.DATE = self.price_data[i][0]
                self.CHANGE = self.price_data[i][-4]

                # Movement prediction
                if self.predictions[i] == 1:
                    self.CURRENT_MOVEMENT_PREDICTION = INCREASE
                    self.update_balance()
                else:
                    self.CURRENT_MOVEMENT_PREDICTION = DECREASE

                if self.CURRENT_MOVEMENT_PREDICTION == self.ACUTAL_MOVEMENT:
                    self.trueCount += 1

                self.print_log(MESSAGE_DAILY_STATUS)

        self.print_log(MESSAGE_PERIOD)
        self.print_log(MESSAGE_RESULT)
        self.print_log(MESSAGE_AVERAGE)
        self.print_log(MESSAGE_COUNT)

    def without_using_the_model(self):
        initial_btc_amount = self.INITIAL_BALANCE_USER / self.INITIAL_BTC_PRICE
        current_money = initial_btc_amount * self.CURRENT_BTC_PRICE
        return str(self.INITIAL_BALANCE_USER - current_money)

    def print_log(self, message_code):
        self.textEdit_log.setText(self.textEdit_log.toPlainText() + self.get_message(message_code))

    def get_message(self, message_code):
        return {
            MESSAGE_DAILY_STATUS: "date = {}, " \
                                  "prediction =  {:4}, " \
                                  "actual = {:4}, " \
                                  "price_change = {:5}, " \
                                  "current_balance = ${:2}, " \
                                  "total_profit = {:5} \n".format(self.DATE,
                                                                  str(self.CURRENT_MOVEMENT_PREDICTION),
                                                                  str(self.ACUTAL_MOVEMENT),
                                                                  str(self.CHANGE),
                                                                  str(self.balance_usd),
                                                                  str(round(
                                                                      self.balance_usd - self.INITIAL_BALANCE_USER, 2))
                                                                  ),
            MESSAGE_RESULT: "\n" + "initial BTC price = {:2}, "
                                   "current BTC price = {:2}, "
                                   "total profit without using the model = {:2}".format(
                self.INITIAL_BTC_PRICE,
                self.CURRENT_BTC_PRICE,
                self.without_using_the_model()),
            MESSAGE_PERIOD: "\n" + "test period = " + str(len(self.price_data)) + " days",
            MESSAGE_AVERAGE: "\n" + "average daily profit = {:2}, "
                                    "average weekly profit = {:2}, "
                                    "average monthly profit = {:2}".format(
                round(self.balance_usd - self.INITIAL_BALANCE_USER, 2) / len(self.price_data),
                round(self.balance_usd - self.INITIAL_BALANCE_USER, 2) / (len(self.price_data) / 7),
                round(self.balance_usd - self.INITIAL_BALANCE_USER, 2) / (len(self.price_data) / 30)),
            MESSAGE_COUNT: "\n" + "Total: {}, True: {}, False: {}".format(self.total, self.trueCount,
                                                                          self.total - self.trueCount),
            MESSAGE_DEFAULT: ""

        }.get(message_code, MESSAGE_DEFAULT)

    def isValid(self):
        if len(self.x_test_path) > 0 and len(self.y_test_path) > 0:
            if self.label_10.text() != "0.00000000 BTC / $0.00":
                return True
            else:
                self.error_message = "Check your balance!"
                self.show_popup_error()
                return False
        else:
            self.error_message = "Please, fill all fields!"
            self.show_popup_error()
            return False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('img/ytu_logo.png'))

    MainScreen = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainScreen)
    MainScreen.show()
    sys.exit(app.exec_())
