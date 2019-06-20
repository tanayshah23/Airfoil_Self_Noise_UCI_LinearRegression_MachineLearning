# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'airfoil.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 384)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 70, 81, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 130, 91, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 160, 131, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(50, 190, 131, 31))
        self.label_5.setObjectName("label_5")
        self.r1 = QtWidgets.QLabel(Dialog)
        self.r1.setGeometry(QtCore.QRect(200, 270, 91, 31))
        self.r1.setText("")
        self.r1.setObjectName("r1")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(60, 270, 111, 31))
        self.label_7.setObjectName("label_7")
        self.f1 = QtWidgets.QLineEdit(Dialog)
        self.f1.setGeometry(QtCore.QRect(211, 75, 133, 20))
        self.f1.setObjectName("f1")
        self.a1 = QtWidgets.QLineEdit(Dialog)
        self.a1.setGeometry(QtCore.QRect(211, 105, 133, 20))
        self.a1.setObjectName("a1")
        self.cl1 = QtWidgets.QLineEdit(Dialog)
        self.cl1.setGeometry(QtCore.QRect(211, 135, 133, 20))
        self.cl1.setObjectName("cl1")
        self.fsv1 = QtWidgets.QLineEdit(Dialog)
        self.fsv1.setGeometry(QtCore.QRect(211, 165, 133, 20))
        self.fsv1.setObjectName("fsv1")
        self.dt1 = QtWidgets.QLineEdit(Dialog)
        self.dt1.setGeometry(QtCore.QRect(211, 195, 133, 20))
        self.dt1.setObjectName("dt1")
        self.b1 = QtWidgets.QPushButton(Dialog)
        self.b1.setGeometry(QtCore.QRect(160, 240, 75, 23))
        self.b1.setObjectName("b1")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(90, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(60, 300, 111, 31))
        self.label_8.setObjectName("label_8")
        self.r2 = QtWidgets.QLabel(Dialog)
        self.r2.setGeometry(QtCore.QRect(200, 300, 91, 31))
        self.r2.setText("")
        self.r2.setObjectName("r2")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 350, 371, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(140, 361, 131, 21))
        self.label_10.setObjectName("label_10")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 340, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Frequency (Hz)"))
        self.label_2.setText(_translate("Dialog", "Angle (degrees)"))
        self.label_3.setText(_translate("Dialog", "Chord Lenght (m)"))
        self.label_4.setText(_translate("Dialog", "Free Stream Velocity (m/s)"))
        self.label_5.setText(_translate("Dialog", "Displacement Thickness (m)"))
        self.label_7.setText(_translate("Dialog", "Sound Pressure Level"))
        self.b1.setText(_translate("Dialog", "Enter"))
        self.label_6.setText(_translate("Dialog", "Airfoil Self Noise"))
        self.label_8.setText(_translate("Dialog", "**Mean Absolute Error"))
        self.label_9.setText(_translate("Dialog", "** This mean absolute error is found from the predictions made from X_test."))
        self.label_10.setText(_translate("Dialog", "(Check jupyter notebook)"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
