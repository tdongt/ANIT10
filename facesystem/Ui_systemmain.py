# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\11299\Desktop\other\try\facesystem\systemmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(822, 489)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 30, 521, 381))
        self.label.setObjectName("label")
        self.facedetect = QtWidgets.QPushButton(Form)
        self.facedetect.setGeometry(QtCore.QRect(30, 130, 141, 71))
        self.facedetect.setObjectName("facedetect")
        self.warningeditt = QtWidgets.QLineEdit(Form)
        self.warningeditt.setGeometry(QtCore.QRect(300, 430, 411, 51))
        self.warningeditt.setObjectName("warningeditt")
        self.guestreg = QtWidgets.QPushButton(Form)
        self.guestreg.setGeometry(QtCore.QRect(30, 230, 141, 71))
        self.guestreg.setObjectName("guestreg")
        self.manager = QtWidgets.QPushButton(Form)
        self.manager.setGeometry(QtCore.QRect(30, 330, 141, 71))
        self.manager.setObjectName("manager")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 30, 171, 91))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FACE DETECT SYSTEM BY D1"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.facedetect.setText(_translate("Form", "人脸检测"))
        self.guestreg.setText(_translate("Form", "访客登记"))
        self.manager.setText(_translate("Form", "管理员界面"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">人脸识别门禁系统</span></p></body></html>"))
