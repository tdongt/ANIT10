# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QTextEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(728, 490)
        font = QFont()
        font.setFamilies([u"\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53"])
        Form.setFont(font)
        self.faceget = QPushButton(Form)
        self.faceget.setObjectName(u"faceget")
        self.faceget.setGeometry(QRect(30, 70, 191, 61))
        self.facetrain = QPushButton(Form)
        self.facetrain.setObjectName(u"facetrain")
        self.facetrain.setGeometry(QRect(30, 150, 191, 61))
        self.guestcheck = QPushButton(Form)
        self.guestcheck.setObjectName(u"guestcheck")
        self.guestcheck.setGeometry(QRect(20, 230, 111, 51))
        self.picture = QPushButton(Form)
        self.picture.setObjectName(u"picture")
        self.picture.setGeometry(QRect(30, 330, 191, 61))
        self.hostcheck = QPushButton(Form)
        self.hostcheck.setObjectName(u"hostcheck")
        self.hostcheck.setGeometry(QRect(30, 400, 191, 61))
        self.textEdityes = QTextEdit(Form)
        self.textEdityes.setObjectName(u"textEdityes")
        self.textEdityes.setGeometry(QRect(263, 63, 431, 301))
        self.textEdityes.setReadOnly(True)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 20, 151, 20))
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(130, 230, 101, 51))
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(275, 390, 411, 81))
        self.chaxun = QLineEdit(Form)
        self.chaxun.setObjectName(u"chaxun")
        self.chaxun.setGeometry(QRect(60, 290, 131, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u7ba1\u7406\u5458\u754c\u9762", None))
        self.faceget.setText(QCoreApplication.translate("Form", u"\u4eba\u8138\u5f55\u5165", None))
        self.facetrain.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8bad\u7ec3", None))
        self.guestcheck.setText(QCoreApplication.translate("Form", u"\u8bbf\u5ba2\u4fe1\u606f\u67e5\u8be2", None))
        self.picture.setText(QCoreApplication.translate("Form", u"\u56fe\u50cf\u68c0\u6d4b(\u6d4b\u9a8c\uff09", None))
        self.hostcheck.setText(QCoreApplication.translate("Form", u"\u4e1a\u4e3b\u4fe1\u606f\u67e5\u8be2", None))
        self.textEdityes.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\">\u6ce8\u610f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u4eba\u8138\u5f55\u5165\u524d\u8bf7\u5148\u8f93\u5165\u4e2a\u4eba\u4fe1\u606f\uff0c\u786e\u4fdd\u4e2a\u4eba\u4fe1\u606f\u65e0\u8bef</p>\n"
"<p style=\" margin-top:0px; "
                        "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u5728\u6b64\u663e\u793a\u67e5\u8be2\u7ed3\u679c</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-style:italic;\"><br /></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; font-style:italic;\">\u7ba1\u7406\u5458\u754c\u9762</span></p></body></html>", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u65b9\u6b63\u7c97\u9ed1\u5b8b\u7b80\u4f53'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic; text-decoration: underline;\">\u5f00\u53d1\u8005\uff1addd</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic; text-decoration: underline;\">\u652f\u6301"
                        "\uff1addd</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic; text-decoration: underline;\">\u7248\u672c\uff1a0.0.2(\u6d4b\u8bd5)</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt; font-style:italic; text-decoration: underline;\"><br /></p></body></html>", None))
        self.chaxun.setText("")
    # retranslateUi

