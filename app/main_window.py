import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog, QInputDialog, QLineEdit, QMessageBox

from config.variables import *
from movements_window import Ui_MovementsWindow
from util.json import save
from util.plot import plot_movements


class Ui_MainWindow(QDialog):
    def setupUi(self, MainWindow):

        self.current_bitcoin_price = INITIAL_BITCOIN_PRICE

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 543)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/ytu_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(36, 36))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.splitter_7 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_7.setGeometry(QtCore.QRect(20, 20, 740, 471))
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.splitter_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle("")
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
        self.lineEdit_testData = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_testData.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_testData.setFont(font)
        self.lineEdit_testData.setObjectName("lineEdit_testData")
        self.pushButton_testData = QtWidgets.QPushButton(self.splitter)
        self.pushButton_testData.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_testData.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_testData.setFont(font)
        self.pushButton_testData.setObjectName("pushButton_testData")
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
        self.lineEdit_predictions = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_predictions.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_predictions.setFont(font)
        self.lineEdit_predictions.setObjectName("lineEdit_predictions")
        self.pushButton_predictions = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_predictions.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_predictions.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_predictions.setFont(font)
        self.pushButton_predictions.setObjectName("pushButton_predictions")
        self.verticalLayout.addWidget(self.splitter_4)
        self.splitter_9 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
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
        self.label_balance = QtWidgets.QLabel(self.splitter_2)
        self.label_balance.setMinimumSize(QtCore.QSize(300, 20))
        self.label_balance.setMaximumSize(QtCore.QSize(300, 45652))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_balance.setFont(font)
        self.label_balance.setAlignment(QtCore.Qt.AlignCenter)
        self.label_balance.setObjectName("label_balance")
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
        self.groupBox_5.setEnabled(True)
        self.groupBox_5.setMaximumSize(QtCore.QSize(415, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_showMovements = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_showMovements.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_showMovements.setMaximumSize(QtCore.QSize(430, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_showMovements.setFont(font)
        self.pushButton_showMovements.setObjectName("pushButton_showMovements")
        self.verticalLayout_5.addWidget(self.pushButton_showMovements)
        self.pushButton_start = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_start.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_start.setMaximumSize(QtCore.QSize(430, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout_5.addWidget(self.pushButton_start)
        self.textEdit_log = QtWidgets.QTextEdit(self.splitter_7)
        self.textEdit_log.setMinimumSize(QtCore.QSize(740, 250))
        self.textEdit_log.setMaximumSize(QtCore.QSize(740, 250))
        self.textEdit_log.setObjectName("textEdit_log")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #################################################

        self.pushButton_testData.clicked.connect(lambda: self.browseFile("testdata"))
        self.pushButton_predictions.clicked.connect(lambda: self.browseFile("predictions"))
        self.pushButton_deposit.clicked.connect(self.deposit)
        self.pushButton_showMovements.clicked.connect(self.open_window)
        self.pushButton_start.clicked.connect(self.start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Influence of News on Bitcoin Price"))
        self.label.setText(_translate("MainWindow", "Test data"))
        self.pushButton_testData.setText(_translate("MainWindow", "Browse"))
        self.label_4.setText(_translate("MainWindow", "Predictions"))
        self.pushButton_predictions.setText(_translate("MainWindow", "Browse"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Balance"))
        self.label_balance.setText(_translate("MainWindow", "0.00000000 BTC / $0.00"))
        self.pushButton_deposit.setText(_translate("MainWindow", "Deposit"))
        self.pushButton_showMovements.setText(_translate("MainWindow", "Show Movements"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))

    def browseFile(self, id):
        if (id == "testdata"):
            filenames = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', '*.csv *.txt')
            firstFile = filenames[0]
            self.lineEdit_testData.setText(firstFile)
        else:
            filenames = QFileDialog.getOpenFileName(self, 'Open File', 'c\\')
            firstFile = filenames[0]
            self.lineEdit_predictions.setText(firstFile)

    def deposit(self):
        text, ok = QInputDialog.getText(self, "Deposit", "Update your account", QLineEdit.Normal)

        if ok and text is not None:
            self.balance_usd = float(text)
            self.balance_btc = round(self.balance_usd / self.current_bitcoin_price, 8)
            self.label_balance.setText(str(self.balance_btc) + " BTC / $" + str(self.balance_usd))
            self.INITIAL_BALANCE_USER = self.balance_usd

    def open_window(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MovementsWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def show_popup(self):
        message = QMessageBox()
        message.setWindowTitle("Coming Soon")
        message.setText("This feature is not available now!")
        message.setIcon(QMessageBox.Information)
        message.exec_()

    def start(self):

        self.testData_path = self.lineEdit_testData.text()
        self.predictions_path = self.lineEdit_predictions.text()

        if self.isValid():

            self.movements = {}

            self.textEdit_log.setText("")
            self.current_bitcoin_price = INITIAL_BITCOIN_PRICE

            df_test = pd.read_csv(self.testData_path)
            predictions = np.loadtxt(self.predictions_path, delimiter=',')
            y_test = np.loadtxt(OUTPUT_PATH + "y_test", delimiter=',')
            self.samples_count = len(y_test)

            self.trueCount = 0
            for i in range(self.samples_count):
                # Daily BTC-USD
                self.current_bitcoin_price = df_test.iloc[i, CLOSE_COLUMN]

                # Date and Percent change
                self.date = df_test.iloc[i, DATE_COLUMN]
                self.change = df_test.iloc[i, CHANGE_COLUMN]

                # Price movement
                if y_test[i] == 1:
                    self.ACUTAL_MOVEMENT = INCREASE
                else:
                    self.ACUTAL_MOVEMENT = DECREASE

                # Movement prediction
                if predictions[i] == 1:
                    self.CURRENT_MOVEMENT_PREDICTION = INCREASE
                    self.update_balance()
                else:
                    self.CURRENT_MOVEMENT_PREDICTION = DECREASE

                if self.CURRENT_MOVEMENT_PREDICTION == self.ACUTAL_MOVEMENT:
                    self.trueCount += 1
                    self.movements[self.date] = True
                else:
                    self.movements[self.date] = False

                self.print_log(MESSAGE_DAILY_STATUS)

        save('LSTM-Sentiment_movements.json', self.movements)
        plot_movements(self.testData_path)

        self.print_log(MESSAGE_PERIOD)
        self.print_log(MESSAGE_RESULT)
        self.print_log(MESSAGE_PROFIT)
        self.print_log(MESSAGE_COUNT)
        self.print_log(MESSAGE_AVG)

    def isValid(self):
        if len(self.testData_path) > 0 and len(self.predictions_path) > 0:
            if self.label_balance.text() != "0.00000000 BTC / $0.00":
                return True
            else:
                self.error_message = "Check your balance!"
                self.show_popup_error()
                return False
        else:
            self.error_message = "Please, fill all fields!"
            self.show_popup_error()
            return False

    def update_balance(self):
        price_change = (self.balance_usd * self.change) / 100
        self.balance_usd += price_change
        self.balance_btc = round(self.balance_usd / self.current_bitcoin_price, 8)
        self.label_balance.setText(str(self.balance_btc) + " BTC / $" + str(round(self.balance_usd, 2)))

    def print_log(self, message_code):
        self.textEdit_log.setText(self.textEdit_log.toPlainText() + self.get_message(message_code))

    def get_message(self, message_code):
        return {
            MESSAGE_DAILY_STATUS: "date = {}, " \
                                  "prediction =  {:4}, " \
                                  "actual = {:4}, " \
                                  "price_change = {:5}, " \
                                  "current_balance = ${:2}, " \
                                  "total_profit = {:5} \n".format(self.date,
                                                                  str(self.CURRENT_MOVEMENT_PREDICTION),
                                                                  str(self.ACUTAL_MOVEMENT),
                                                                  str(self.change),
                                                                  str(self.balance_usd),
                                                                  str(round(
                                                                      self.balance_usd - self.INITIAL_BALANCE_USER, 2))
                                                                  ),
            MESSAGE_RESULT: "\n" + "initial BTC price = {:2}, "
                                   "current BTC price = {:2}\n".format(
                INITIAL_BITCOIN_PRICE,
                self.current_bitcoin_price),
            MESSAGE_PROFIT: "total profit with the model = ${:.2f}, "
                            "total profit without the model = ${:.2f}".format(
                self.balance_usd - self.INITIAL_BALANCE_USER, self.without_using_the_model()),
            MESSAGE_PERIOD: "\n" + "test period = " + str(self.samples_count) + " days",
            MESSAGE_AVERAGE: "\n" + "average daily profit = {:.2f}, "
                                    "average weekly profit = {:.2f}, "
                                    "average monthly profit = {:.2f}".format(
                round(self.balance_usd - self.INITIAL_BALANCE_USER, 2) / self.samples_count,
                round(self.balance_usd - self.INITIAL_BALANCE_USER, 2) / (self.samples_count / 7),
                round(self.balance_usd - self.INITIAL_BALANCE_USER, 2) / (self.samples_count / 30)),
            MESSAGE_COUNT: "\n" + "Total: {}, True: {}, False: {}".format(self.samples_count, self.trueCount,
                                                                          self.samples_count - self.trueCount),
            MESSAGE_AVG: "\n" + "average: {:.2f}".format(self.trueCount / self.samples_count),
            MESSAGE_DEFAULT: ""

        }.get(message_code, MESSAGE_DEFAULT)

    def without_using_the_model(self):
        initial_btc_amount = self.INITIAL_BALANCE_USER / INITIAL_BITCOIN_PRICE
        current_money = initial_btc_amount * self.current_bitcoin_price
        return current_money - self.INITIAL_BALANCE_USER


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
