# -*- coding: utf-8 -*

#!/usr/bin/env python
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import*
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui, QtCore
import coletabeta
from datetime import datetime
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import Qt
import sqlite3


class imporSA(QWidget):
    def __init__(self, parent=None):
        super(imporSA, self).__init__(parent)
        QDialog.__init__(self)
        global input1

        self.title = "Dados SA1"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 400
        global ex
        self.save = ex

        self.creatingTables()

        self.show()

    def savecell(self):
        index = (self.tableWidget.selectionModel().currentIndex())
        value = index.sibling(index.row(), index.column()).data()
        input1.setText(value)
        self.save.displayInfo()
        print(value)

    def loadtable(self):
        connection = sqlite3.connect('coletabeta.db')
        query = "SELECT * FROM Sa1"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def creatingTables(self):
        layout = QVBoxLayout(self)

        btn_layout = QHBoxLayout()
        # !!!
        btn_layout.addItem(QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        btn5 = QPushButton("Atualizar")
        btn5.clicked.connect(self.loadtable)
        btn6 = QPushButton("Salvar")
        btn6.clicked.connect(self.savecell)

        btn_layout.addWidget(btn5)
        btn_layout.addWidget(btn6)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(16)

        self.tableWidget.setHorizontalHeaderLabels(('Número da Análise', 'Análise SA1', 'Fornecedor', 'Fator1', 'Fator2', 'Fator3', 'Fator4', 'Fator5', 'Fator6', 'Fator7', 'Fator8', 'Fator9', 'Fator10', 'Fator11', 'Fator12', 'Parâmetro de Qualidade 1'))

        layout.addWidget(self.tableWidget)

        layout.addLayout(btn_layout)


class imporSA_2(QWidget):
    def __init__(self, parent=None):
        super(imporSA_2, self).__init__(parent)
        QDialog.__init__(self)
        global input2

        self.title = "Dados SA2"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 400
        global ex
        self.save = ex

        self.creatingTables()

        self.show()

    def savecell(self):
        index = (self.tableWidget.selectionModel().currentIndex())
        value = index.sibling(index.row(), index.column()).data()
        input2.setText(value)
        self.save.displayInfo()
        print(value)

    def loadtable(self):
        connection = sqlite3.connect('coletabeta.db')
        query = "SELECT * FROM Sa2"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(
                    row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        connection.close()

    def creatingTables(self):
        layout = QVBoxLayout(self)

        btn_layout = QHBoxLayout()
        # !!!
        btn_layout.addItem(QSpacerItem(
            0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum))

        btn7 = QPushButton("Atualizar")
        btn7.clicked.connect(self.loadtable)
        btn8 = QPushButton("Salvar")
        btn8.clicked.connect(self.savecell)

        btn_layout.addWidget(btn7)
        btn_layout.addWidget(btn8)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(15)

        self.tableWidget.setHorizontalHeaderLabels(('Número da Análise', 'Análise SA2', 'Fator12', 'Fator13', 'Fator14', 'Fator15', 'Fator16', 'Fator17', 'Fator18', 'Fator19', 'Fator20', 'Fator21', 'Parâmetro de Qualidade 2', 'Parâmetro de Qualidade 3'))

        layout.addWidget(self.tableWidget)

        layout.addLayout(btn_layout)


class tabdemo(QTabWidget):
    def __init__(self, parent=None):
        super(tabdemo, self).__init__(parent)
        global input1, value

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        
        self.addTab(self.tab1, "Tab 1")
        self.addTab(self.tab2, "Tab 2")
        self.addTab(self.tab3, "Tab 3")

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.setWindowIcon(QIcon('logo.png'))
        self.setWindowTitle("Coleta de Fatores")

    def tab1UI(self):
        global combo1, qline1, qline2, qline3, qline4, qline5, qline6, qline7, qline8, qline9, qline10, qline11, qline88
        layout = QFormLayout()

        combo1 = QComboBox(self)
        combo1.addItem(" ")
        combo1.addItem("Fornecedor A")
        combo1.addItem("Fornecedor B")
        combo1.addItem("Fornecedor C")
        layout.addRow("Fornecedor", combo1)

        combo1.currentText()

        qline1 = QLineEdit("", self)
        qline1.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 1"), qline1)

        qline2 = QLineEdit("", self)
        qline2.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 2"), qline2)

        qline3 = QLineEdit("", self)
        qline3.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 3"), qline3)

        qline4 = QLineEdit("", self)
        qline4.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 4"), qline4)

        qline5 = QLineEdit("", self)
        qline5.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 5"), qline5)

        qline6 = QLineEdit("", self)
        qline6.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 6"), qline6)

        qline7 = QLineEdit("", self)
        qline7.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 7"), qline7)

        qline8 = QLineEdit("", self)
        qline8.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 8"), qline8)

        qline9 = QLineEdit("", self)
        qline9.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 9"), qline9)

        qline10 = QLineEdit("", self)
        qline10.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 10"), qline10)

        qline11 = QLineEdit("", self)
        qline11.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 11"), qline11)

        qlabel1 = QLabel("Parâmetro de Qualidade", self)
        layout.addRow(QLabel(""), qlabel1)
        qlabel1.setAlignment(QtCore.Qt.AlignCenter)
        qlabel1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        qlabel1.setStyleSheet(
            "background-color: lightblue; border: 1px solid black;")

        qline88 = QLineEdit("", self)
        qline88.setValidator(QIntValidator())
        layout.addRow(QLabel("Parâmetro de Qualidade 1"), qline88)

        self.setTabText(0, "SA1")
        self.tab1.setLayout(layout)

        btn1 = QPushButton("Salvar", self)
        layout.addRow(QLabel(""), btn1)
        btn1.clicked.connect(self.saveAba1)

    def saveAba1(self):
        global combo1, qline1, qline2, qline3, qline4, qline5, qline6, qline7, qline8, qline9, qline10, qline11, qline88, time, combo22
        combo1 = combo1.currentText()
        text1 = qline1.text()
        text2 = qline2.text()
        text3 = qline3.text()
        text4 = qline4.text()
        text5 = qline5.text()
        text6 = qline6.text()
        text7 = qline7.text()
        text8 = qline8.text()
        text9 = qline9.text()
        text10 = qline10.text()
        text11 = qline11.text()
        text88 = qline88.text()
        print(combo1)
        time = datetime.now().strftime("%B %d, %Y %I:%M%p")
        nome = "ANÁLISE SA1 - "
        nt = (nome + time)
        print(nt)
        coletabeta.cursor.execute('''
	INSERT INTO Sa1(DataSA1, Fornecedor, Fator1, Fator2, Fator3, Fator4, Fator5, Fator6, Fator7, Fator8, Fator9, Fator10, Fator11, ParametrodeQualidade1) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (nt, combo1, text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text88))
        coletabeta.conn.commit()

        QMessageBox.information(
            self, 'Coleta de Fatores', 'Dados salvos no Banco de Dados')

    def tab2UI(self):
        global qline12, qline13, qline14, qline15, qline16, qline17, qline18, qline19, qline20, qline21, qline22, combo22, qline37, qline38, input1, value
        layout = QFormLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)

        btn22 = QPushButton("Importar SA1", self)
        layout.addRow(QLabel(""), btn22)
        self.tab2.close()
        btn22.clicked.connect(self.imporSA1)

        input1 = QLineEdit()
        layout.addRow(QLabel("SA1"), input1)

        qline12 = QLineEdit("", self)
        qline12.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 12"), qline12)

        qline13 = QLineEdit("", self)
        qline13.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 13"), qline13)

        qline14 = QLineEdit("", self)
        qline14.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 14"), qline14)

        qline15 = QLineEdit("", self)
        qline15.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 15"), qline15)

        qline16 = QLineEdit("", self)
        qline16.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 16"), qline16)

        qline17 = QLineEdit("", self)
        qline17.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 17"), qline17)

        qline18 = QLineEdit("", self)
        qline18.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 18"), qline18)

        qline19 = QLineEdit("", self)
        qline19.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 19"), qline19)

        qline20 = QLineEdit("", self)
        qline20.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 20"), qline20)

        qline21 = QLineEdit("", self)
        qline21.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 21"), qline21)

        qline22 = QLineEdit("", self)
        qline22.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 22"), qline22)

        qlabel1 = QLabel("Parâmetro de Qualidade", self)
        layout.addRow(QLabel(""), qlabel1)
        qlabel1.setAlignment(QtCore.Qt.AlignCenter)
        qlabel1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        qlabel1.setStyleSheet(
            "background-color: lightblue; border: 1px solid black;")

        qline37 = QLineEdit("", self)
        qline37.setValidator(QIntValidator())
        layout.addRow(QLabel("Parametro de Qualidade 2"), qline37)

        qline38 = QLineEdit("", self)
        qline38.setValidator(QIntValidator())
        layout.addRow(QLabel("Parametro de Qualidade 3"), qline38)

        self.setTabText(1, "SA2")
        self.tab2.setLayout(layout)

        btn2 = QPushButton("Salvar", self)
        layout.addRow(QLabel(""), btn2)
        btn2.clicked.connect(self.saveAba2)
        btn2.resize(10, 400)

    def saveAba2(self):
        global qline12, qline13, qline14, qline15, qline16, qline17, qline18, qline19, qline20, qline21, qline22, combo22, qline37, qline38, time, input1
        input1 = input1.text()
        text12 = qline12.text()
        text13 = qline13.text()
        text14 = qline14.text()
        text15 = qline15.text()
        text16 = qline16.text()
        text17 = qline17.text()
        text18 = qline18.text()
        text19 = qline19.text()
        text20 = qline20.text()
        text21 = qline21.text()
        text22 = qline22.text()
        text37 = qline37.text()
        text38 = qline38.text()
        time = datetime.now().strftime("%B %d, %Y %I:%M%p")
        nome = "ANÁLISE SA2 - "
        nt2 = (nome + time)
        print(nt2)
        coletabeta.cursor.execute('''
	INSERT INTO Sa2(SA1, Fator12, Fator13, Fator14, Fator15, Fator16, 	Fator17, Fator18, Fator19, Fator20, Fator21, Fator22, 		ParametrodeQualidade2, ParametrodeQualidade3, DataSA2) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (input1, text12, text13, text14, text15, text16, text17, text18, text19, text20, text21, text22, text37, text38, nt2))
        coletabeta.conn.commit()

        QMessageBox.information(
            self, 'Coleta de Fatores', 'Dados salvos no Servidor')

    def imporSA1(self):
        self.anotherwindow = imporSA()
        self.anotherwindow.show()

    def displayInfo(self):
        self.show()

    def tab3UI(self):
        global qline23, qline24, qline25, qline26, qline27, qline28, qline29, combo23, qline31, qline39, qline40, input2
        layout = QFormLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)

        btn23 = QPushButton("Importar SA2", self)
        layout.addRow(QLabel(""), btn23)
        self.tab3.close()
        btn23.clicked.connect(self.imporSA2)

        input2 = QLineEdit()
        layout.addRow(QLabel("SA2"), input2)

        qline23 = QLineEdit("", self)
        qline23.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 23"), qline23)

        qline24 = QLineEdit("", self)
        qline24.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 24"), qline24)

        qline25 = QLineEdit("", self)
        qline25.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 25"), qline25)

        qline26 = QLineEdit("", self)
        qline26.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 26"), qline26)

        qline27 = QLineEdit("", self)
        qline27.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 27"), qline27)

        qline28 = QLineEdit("", self)
        qline28.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 28"), qline28)

        qline29 = QLineEdit("", self)
        qline29.setValidator(QIntValidator())
        layout.addRow(QLabel("Fator 29"), qline29)

        qlabel1 = QLabel("Parâmetro de Qualidade", self)
        layout.addRow(QLabel(""), qlabel1)
        qlabel1.setAlignment(QtCore.Qt.AlignCenter)
        qlabel1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        qlabel1.setStyleSheet(
            "background-color: lightblue; border: 1px solid black;")

        qline31 = QLineEdit("", self)
        qline31.setValidator(QIntValidator())
        layout.addRow(QLabel("Parametro de Qualidade 4"), qline31)

        qline39 = QLineEdit("", self)
        qline39.setValidator(QIntValidator())
        layout.addRow(QLabel("Parametro de Qualidade 5"), qline39)

        qline40 = QLineEdit("", self)
        qline40.setValidator(QIntValidator())
        layout.addRow(QLabel("Parametro de Qualidade 6"), qline40)

        self.setTabText(2, "SA3")
        self.tab3.setLayout(layout)

        btn6 = QPushButton("Salvar", self)
        layout.addRow(QLabel(""), btn6)
        btn6.clicked.connect(self.saveAba3)
        btn6.move(0, 400)

    def saveAba3(self):
        global qline23, qline24, qline25, qline26, qline27, qline28, qline29, combo23, qline31, qline38, qline40, time, input2
        input2 = input2.text()
        text23 = qline23.text()
        text24 = qline24.text()
        text25 = qline25.text()
        text26 = qline26.text()
        text27 = qline27.text()
        text28 = qline28.text()
        text29 = qline29.text()
        text31 = qline31.text()
        text39 = qline39.text()
        text40 = qline40.text()
        time = datetime.now().strftime("%B %d, %Y %I:%M%p")
        nome = "ANALISE SA3 - "
        nt3 = (nome + time)
        print(nt3)
        coletabeta.cursor.execute('''
	INSERT INTO Sa3(SA2, Fator23, Fator24, Fator25, Fator26, Fator27, 	Fator28, Fator29, ParametrodeQualidade4, 			ParametrodeQualidade5, ParametrodeQualidade6, DataSA3) VALUES 		(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (input2, text23, text24, text25, text26, text27, text28, text29, text31, text39, text40, nt3))
        coletabeta.conn.commit()

        print("dados salvos")

        QMessageBox.information(
            self, 'Coleta de Fatores', 'Dados salvos no Servidor')

    def imporSA2(self):
        self.anotherwindow = imporSA_2()
        self.anotherwindow.show()

    def displayInfo(self):
        self.show()


def main():
    app = QApplication(sys.argv)
    global ex
    ex = tabdemo()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()
