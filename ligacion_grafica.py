#*******************************************************************************
#
# Date: 09/03/2022
# 
# Programa gráfico para el calculo de la ligación.
# Genera una interfaz gráfica amigable con el usario para calcular el volumen
# o la concentración de inserto o vector con las proporciones deseadas
#
# Adaptado para: IATA - Lab 003
#
# Autor: Juan Carlos Torrat Noves
# email: carlos.torrat@gmail.com
#
#*******************************************************************************

import sys
from PyQt5 import uic, QtWidgets, QtCore
import pip
import os

def importar_paquetes(paquete):
    try:
        __import__(paquete)
    except ImportError:
        pip.main(["install",paquete])

#qtCreatorFile = "ligacion.ui" # Nombre del archivo aquí.

#Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 786)
        MainWindow.setStyleSheet("background-color: rgb(42, 43, 43);\n"
"")
        self.label_14 = QtWidgets.QLabel(MainWindow)
        self.label_14.setGeometry(QtCore.QRect(680, 120, 91, 51))
        self.label_14.setObjectName("label_14")
        self.splitter = QtWidgets.QSplitter(MainWindow)
        self.splitter.setGeometry(QtCore.QRect(600, 290, 257, 78))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_9 = QtWidgets.QLabel(self.splitter)
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.concentracion_vector = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.concentracion_vector.setStyleSheet("color: rgb(255, 255, 255);")
        self.concentracion_vector.setObjectName("concentracion_vector")
        self.verticalLayout_5.addWidget(self.concentracion_vector)
        self.tamano_vector = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.tamano_vector.setStyleSheet("color: rgb(255, 255, 255);")
        self.tamano_vector.setObjectName("tamano_vector")
        self.verticalLayout_5.addWidget(self.tamano_vector)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_6.addWidget(self.label_8)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 0, 2, 1, 1)
        self.splitter_2 = QtWidgets.QSplitter(MainWindow)
        self.splitter_2.setGeometry(QtCore.QRect(600, 200, 260, 78))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_10 = QtWidgets.QLabel(self.splitter_2)
        self.label_10.setObjectName("label_10")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.concentracion_inserto = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.concentracion_inserto.setStyleSheet("color: rgb(255, 255, 255);")
        self.concentracion_inserto.setObjectName("concentracion_inserto")
        self.verticalLayout_3.addWidget(self.concentracion_inserto)
        self.tamano_inserto = QtWidgets.QDoubleSpinBox(self.layoutWidget1)
        self.tamano_inserto.setStyleSheet("color: rgb(255, 255, 255);")
        self.tamano_inserto.setObjectName("tamano_inserto")
        self.verticalLayout_3.addWidget(self.tamano_inserto)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(MainWindow)
        self.splitter_3.setGeometry(QtCore.QRect(600, 530, 261, 91))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_13 = QtWidgets.QLabel(self.splitter_3)
        self.label_13.setObjectName("label_13")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.resultado_inserto = QtWidgets.QTextEdit(self.layoutWidget2)
        self.resultado_inserto.setStyleSheet("background-color: rgb(231, 255, 232);")
        self.resultado_inserto.setObjectName("resultado_inserto")
        self.verticalLayout_7.addWidget(self.resultado_inserto)
        self.resultado_vector = QtWidgets.QTextEdit(self.layoutWidget2)
        self.resultado_vector.setStyleSheet("background-color: rgb(231, 255, 232);")
        self.resultado_vector.setObjectName("resultado_vector")
        self.verticalLayout_7.addWidget(self.resultado_vector)
        self.gridLayout_4.addLayout(self.verticalLayout_7, 0, 1, 1, 1)
        self.splitter_4 = QtWidgets.QSplitter(MainWindow)
        self.splitter_4.setGeometry(QtCore.QRect(600, 390, 257, 51))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_15 = QtWidgets.QLabel(self.splitter_4)
        self.label_15.setObjectName("label_15")
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_8.addWidget(self.label_16)
        self.gridLayout_5.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.volumen_final = QtWidgets.QDoubleSpinBox(self.layoutWidget_2)
        self.volumen_final.setStyleSheet("color: rgb(255, 255, 255);")
        self.volumen_final.setObjectName("volumen_final")
        self.verticalLayout_9.addWidget(self.volumen_final)
        self.gridLayout_5.addLayout(self.verticalLayout_9, 0, 1, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_10.addWidget(self.label_18)
        self.gridLayout_5.addLayout(self.verticalLayout_10, 0, 2, 1, 1)
        self.splitter_5 = QtWidgets.QSplitter(MainWindow)
        self.splitter_5.setGeometry(QtCore.QRect(600, 450, 257, 51))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.label_17 = QtWidgets.QLabel(self.splitter_5)
        self.label_17.setObjectName("label_17")
        self.layoutWidget_3 = QtWidgets.QWidget(self.splitter_5)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_19.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_11.addWidget(self.label_19)
        self.gridLayout_6.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.relacion_inserto = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.relacion_inserto.setEnabled(True)
        self.relacion_inserto.setAcceptDrops(True)
        self.relacion_inserto.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.relacion_inserto.setAutoFillBackground(False)
        self.relacion_inserto.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.relacion_inserto.setObjectName("relacion_inserto")
        self.horizontalLayout.addWidget(self.relacion_inserto)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_20.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_20.setObjectName("label_20")
        self.horizontalLayout.addWidget(self.label_20)
        self.relacion_vector = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.relacion_vector.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.relacion_vector.setObjectName("relacion_vector")
        self.horizontalLayout.addWidget(self.relacion_vector)
        self.verticalLayout_12.addLayout(self.horizontalLayout)
        self.gridLayout_6.addLayout(self.verticalLayout_12, 0, 1, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.gridLayout_6.addLayout(self.verticalLayout_13, 0, 2, 1, 1)
        self.calcular = QtWidgets.QPushButton(MainWindow)
        self.calcular.setGeometry(QtCore.QRect(690, 640, 75, 24))
        self.calcular.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.calcular.setObjectName("calcular")
        self.error = QtWidgets.QLabel(MainWindow)
        self.error.setGeometry(QtCore.QRect(520, 690, 441, 41))
        self.error.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.error.setStyleSheet("color: rgb(252, 0, 24);")
        self.error.setObjectName("error")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dialog"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Ligación</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Vector</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Concentracion</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Tamaño</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">ng/ul</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">kb</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Inserto</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Concentracion</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Tamaño</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">ng/ul</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">kb</span></p></body></html>"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Resultado</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Volumen vector</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Volumen inserto </span></p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Volumen final</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Volumen</span></p></body></html>"))
        self.label_18.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">ul</span></p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; color:#ffffff;\">Relacion </span></p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "<html><head/><body><p>Inserto:Vector</p></body></html>"))
        self.relacion_inserto.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">3</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", ":"))
        self.relacion_vector.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1</span></p></body></html>"))
        self.calcular.setText(_translate("MainWindow", "Calcular"))
        self.error.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        #Aqui van botones
        self.calcular.clicked.connect(self.calculos)
    #Aqui posibles funciones
    def calculos(self):
        C_inserto = float(self.concentracion_inserto.value())
        L_inserto = float(self.tamano_inserto.value())
        C_vector = float(self.concentracion_vector.value())
        L_vector = float(self.tamano_vector.value())
        try:
            r = int(self.relacion_inserto.toPlainText())
            j = int(self.relacion_vector.toPlainText())
        except:
            msg = "Has intentado introducir un caracter no valido,\n solo admite numeros enteros para la relacion"
            self.error.setText(msg)
            self.error.setAlignment(QtCore.Qt.AlignCenter)
            resultado = ""
            self.resultado_inserto.setText(resultado)
            self.resultado_vector.setText(resultado)
        else:
            vf = float(self.volumen_final.value())
            msg = ""
            
            
            try:
                x = C_inserto/L_inserto
                y = C_vector/L_vector
            except:
                msg = "Se ha encontrado un 0 en el divisor.\n Asegurese de rellenar bien los campos."
                self.error.setText(msg)
                self.error.setAlignment(QtCore.Qt.AlignCenter)
                resultado = ""
                self.resultado_inserto.setText(resultado)
                self.resultado_vector.setText(resultado)


            
            else:
                volumen = round((vf*r*y)/(j*r*y+x),2)
                v_vector = round(vf-volumen,2)
                salida_inserto = str(volumen)+ " ul"
                salida_vector = str(v_vector)+ " ul"
                self.resultado_inserto.setText(salida_inserto)
                self.resultado_vector.setText(salida_vector)
                self.error.setText(msg)
            
        

if __name__ == "__main__":
    importar_paquetes("PyQt5")
    importar_paquetes("sys")

    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())