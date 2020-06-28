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
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 686)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/ytu_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(36, 36))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
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
        self.label_input = QtWidgets.QLabel(self.splitter)
        self.label_input.setMinimumSize(QtCore.QSize(90, 0))
        self.label_input.setMaximumSize(QtCore.QSize(90, 95545))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_input.setFont(font)
        self.label_input.setAlignment(QtCore.Qt.AlignCenter)
        self.label_input.setObjectName("label_input")
        self.lineEdit_input = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_input.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_input.setFont(font)
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.pushButton_input = QtWidgets.QPushButton(self.splitter)
        self.pushButton_input.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_input.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_input.setFont(font)
        self.pushButton_input.setObjectName("pushButton_input")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_output = QtWidgets.QLabel(self.splitter_3)
        self.label_output.setMinimumSize(QtCore.QSize(90, 0))
        self.label_output.setMaximumSize(QtCore.QSize(90, 95545))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_output.setFont(font)
        self.label_output.setAlignment(QtCore.Qt.AlignCenter)
        self.label_output.setObjectName("label_output")
        self.lineEdit_output = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_output.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_output.setFont(font)
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.pushButton_output = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_output.setMinimumSize(QtCore.QSize(120, 30))
        self.pushButton_output.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_output.setFont(font)
        self.pushButton_output.setObjectName("pushButton_output")
        self.verticalLayout.addWidget(self.splitter_4)
        self.verticalLayout_6.addWidget(self.groupBox_2)
        self.splitter_9 = QtWidgets.QSplitter(self.centralwidget)
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
        self.groupBox_5.setMaximumSize(QtCore.QSize(45454, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_startDate = QtWidgets.QLabel(self.groupBox_5)
        self.label_startDate.setMinimumSize(QtCore.QSize(90, 0))
        self.label_startDate.setMaximumSize(QtCore.QSize(90, 95545))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_startDate.setFont(font)
        self.label_startDate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_startDate.setObjectName("label_startDate")
        self.horizontalLayout.addWidget(self.label_startDate)
        self.comboBox_startDate = QtWidgets.QComboBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_startDate.setFont(font)
        self.comboBox_startDate.setObjectName("comboBox_startDate")
        self.horizontalLayout.addWidget(self.comboBox_startDate)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_endDate = QtWidgets.QLabel(self.groupBox_5)
        self.label_endDate.setMinimumSize(QtCore.QSize(90, 0))
        self.label_endDate.setMaximumSize(QtCore.QSize(90, 95545))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_endDate.setFont(font)
        self.label_endDate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_endDate.setObjectName("label_endDate")
        self.horizontalLayout_2.addWidget(self.label_endDate)
        self.comboBox_endDate = QtWidgets.QComboBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.comboBox_endDate.setFont(font)
        self.comboBox_endDate.setObjectName("comboBox_endDate")
        self.horizontalLayout_2.addWidget(self.comboBox_endDate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_6.addWidget(self.splitter_9)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_start.setMinimumSize(QtCore.QSize(200, 30))
        self.pushButton_start.setMaximumSize(QtCore.QSize(45646, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.verticalLayout_6.addWidget(self.pushButton_start)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 400))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_movements = QtWidgets.QLabel(self.tab)
        self.label_movements.setText("")
        self.label_movements.setScaledContents(True)
        self.label_movements.setMinimumSize(QtCore.QSize(0, 0))
        self.label_movements.setMaximumSize(QtCore.QSize(674, 351))
        self.label_movements.setObjectName("label_movements")
        self.verticalLayout_4.addWidget(self.label_movements)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textEdit_log = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_log.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_log.setMaximumSize(QtCore.QSize(4564, 45454))
        self.textEdit_log.setObjectName("textEdit_log")
        font = QtGui.QFont()
        font.setPointSize(8)
        self.textEdit_log.setFont(font)
        self.verticalLayout_7.addWidget(self.textEdit_log)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_6.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##################################

        self.pushButton_input.clicked.connect(lambda: self.browseFile("input"))
        self.pushButton_output.clicked.connect(lambda: self.browseFile("output"))
        self.pushButton_deposit.clicked.connect(self.deposit)
        self.comboBox_startDate.currentTextChanged.connect(self.onStartDateChange)
        self.pushButton_start.clicked.connect(self.start)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Influence of News on Bitcoin Price"))
        self.label_input.setText(_translate("MainWindow", "Input"))
        self.pushButton_input.setText(_translate("MainWindow", "Browse"))
        self.label_output.setText(_translate("MainWindow", "Output"))
        self.pushButton_output.setText(_translate("MainWindow", "Browse"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Balance"))
        self.label_balance.setText(_translate("MainWindow", "0.00000000 BTC / $0.00"))
        self.pushButton_deposit.setText(_translate("MainWindow", "Deposit"))
        self.label_startDate.setText(_translate("MainWindow", "Start Date:"))
        self.label_endDate.setText(_translate("MainWindow", "End Date:"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Movements"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Summary"))



    def browseFile(self, id):
        if (id == "input"):
            filenames = QFileDialog.getOpenFileName(self, 'Open File', 'c\\', '*.csv *.txt')
            firstFile = filenames[0]
            self.lineEdit_input.setText(firstFile)

            self.input_path = self.lineEdit_input.text()
            self.df_test = pd.read_csv(self.input_path)
            self.comboBox_startDate.addItems(self.df_test['date'])
            self.startDate = self.comboBox_startDate.currentText()
            self.comboBox_endDate.addItems(self.df_test['date'][self.df_test['date']>self.startDate])
            self.endDate = self.comboBox_endDate.currentText()

        else:
            filenames = QFileDialog.getOpenFileName(self, 'Open File', 'c\\')
            firstFile = filenames[0]
            self.lineEdit_output.setText(firstFile)

    def onStartDateChange(self):
        self.startDate = self.comboBox_startDate.currentText()
        self.comboBox_endDate.clear()
        self.comboBox_endDate.addItems(self.df_test['date'][self.df_test['date'] > self.startDate])
        self.endDate = self.comboBox_endDate.currentText()

        self.row = self.df_test[self.df_test['date'] == self.startDate]['open']
        self.current_bitcoin_price = round(self.row.values[0], 2)


        if self.label_balance.text() != "0.00000000 BTC / $0.00":
            self.balance_btc = round(self.balance_usd / self.current_bitcoin_price, 8)
            self.label_balance.setText(str(self.balance_btc) + " BTC / $" + str(round(self.balance_usd, 2)))
            self.INITIAL_BALANCE_USER = self.balance_usd

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

        self.output_path = self.lineEdit_output.text()

        if self.isValid():

            self.movements = {}

            self.endDate = self.comboBox_endDate.currentText()

            predictions = np.loadtxt(self.output_path, delimiter=',')
            y_test = np.loadtxt(OUTPUT_PATH + "y_test", delimiter=',')


            self.textEdit_log.setText("")
            self.row = self.df_test[self.df_test['date'] == self.startDate]['open']
            self.current_bitcoin_price = round(self.row.values[0], 2)

            self.df_new_test = self.df_test[self.df_test['date'] >= self.startDate]
            self.df_new_test = self.df_new_test[self.df_new_test['date'] <= self.endDate]

            self.samples_count = self.df_new_test.shape[0]

            self.trueCount = 0
            for i in range(self.samples_count):
                # Daily BTC-USD
                self.current_bitcoin_price = self.df_new_test.iloc[i, CLOSE_COLUMN]

                # Date and Percent change
                self.date = self.df_new_test.iloc[i, DATE_COLUMN]
                self.change = self.df_new_test.iloc[i, CHANGE_COLUMN]

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

        save('LSTM-Sentiment_movements.json', self.movements)
        plot_movements(self.df_new_test)
        self.label_movements.setPixmap(QtGui.QPixmap("./img/movements.png"))

        self.print_log(MESSAGE_PERIOD)
        self.print_log(MESSAGE_RESULT)
        self.print_log(MESSAGE_PROFIT)
        self.print_log(MESSAGE_COUNT)
        self.print_log(MESSAGE_ACC)

    def isValid(self):
        if len(self.input_path) > 0 and len(self.output_path) > 0:
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
                                  "price_change = {:5}, " \
                                  "current_balance = ${:2}, " \
                                  "total_profit = {:5} \n".format(self.date,
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
            MESSAGE_ACC: "\n" + "accuracy: %{:.2f}".format(self.trueCount / self.samples_count),
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
