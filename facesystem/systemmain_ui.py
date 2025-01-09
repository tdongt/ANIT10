# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'systemmain.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(822, 489)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 30, 521, 381))
        self.facedetect = QPushButton(Form)
        self.facedetect.setObjectName(u"facedetect")
        self.facedetect.setGeometry(QRect(30, 130, 141, 71))
        self.warningeditt = QLineEdit(Form)
        self.warningeditt.setObjectName(u"warningeditt")
        self.warningeditt.setGeometry(QRect(300, 430, 411, 51))
        self.guestreg = QPushButton(Form)
        self.guestreg.setObjectName(u"guestreg")
        self.guestreg.setGeometry(QRect(30, 230, 141, 71))
        self.manager = QPushButton(Form)
        self.manager.setObjectName(u"manager")
        self.manager.setGeometry(QRect(30, 330, 141, 71))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 171, 91))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"FACE DETECT SYSTEM BY D1", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.facedetect.setText(QCoreApplication.translate("Form", u"\u4eba\u8138\u68c0\u6d4b", None))
        self.guestreg.setText(QCoreApplication.translate("Form", u"\u8bbf\u5ba2\u767b\u8bb0", None))
        self.manager.setText(QCoreApplication.translate("Form", u"\u7ba1\u7406\u5458\u754c\u9762", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">\u4eba\u8138\u8bc6\u522b\u95e8\u7981\u7cfb\u7edf</span></p></body></html>", None))
    # retranslateUi

