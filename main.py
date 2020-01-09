import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from int import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.con = sqlite3.connect('coffee.db')
        cur = self.con.cursor()
        self.result = cur.execute('SELECT * FROM sorts').fetchall()
        if self.result:
            self.tableWidget.setRowCount(len(self.result))
            self.tableWidget.setColumnCount(len(self.result[0]))
            self.tableWidget.setHorizontalHeaderLabels(['id', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                                                        'описание вкуса', 'цена', 'объём упаковки'])
            for i, row in enumerate(self.result):
                for j, col in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(col)))
            self.tableWidget.resizeColumnsToContents()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())