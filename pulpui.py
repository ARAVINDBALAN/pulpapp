# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pulpapp.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Pulpapp(object):
    def setupUi(self, Pulpapp):
        Pulpapp.setObjectName(_fromUtf8("Pulpapp"))
        Pulpapp.resize(696, 551)
        self.buttonBox = QtGui.QDialogButtonBox(Pulpapp)
        self.buttonBox.setGeometry(QtCore.QRect(280, 390, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.KMTracker = QtGui.QPushButton(Pulpapp)
        self.KMTracker.setGeometry(QtCore.QRect(70, 180, 161, 29))
        self.KMTracker.setObjectName(_fromUtf8("KMTracker"))
        self.Indent_Input = QtGui.QPushButton(Pulpapp)
        self.Indent_Input.setGeometry(QtCore.QRect(70, 220, 161, 29))
        self.Indent_Input.setObjectName(_fromUtf8("Indent_Input"))
        self.KMTracker_3 = QtGui.QPushButton(Pulpapp)
        self.KMTracker_3.setGeometry(QtCore.QRect(510, 250, 161, 29))
        self.KMTracker_3.setObjectName(_fromUtf8("KMTracker_3"))
        self.KMTracker_4 = QtGui.QPushButton(Pulpapp)
        self.KMTracker_4.setGeometry(QtCore.QRect(290, 200, 161, 29))
        self.KMTracker_4.setObjectName(_fromUtf8("KMTracker_4"))
        self.KMTracker_2 = QtGui.QPushButton(Pulpapp)
        self.KMTracker_2.setGeometry(QtCore.QRect(510, 170, 161, 29))
        self.KMTracker_2.setObjectName(_fromUtf8("KMTracker_2"))
        self.KMTracker_5 = QtGui.QPushButton(Pulpapp)
        self.KMTracker_5.setGeometry(QtCore.QRect(510, 210, 161, 29))
        self.KMTracker_5.setObjectName(_fromUtf8("KMTracker_5"))

        self.retranslateUi(Pulpapp)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Pulpapp.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Pulpapp.reject)
        QtCore.QMetaObject.connectSlotsByName(Pulpapp)

    def retranslateUi(self, Pulpapp):
        Pulpapp.setWindowTitle(_translate("Pulpapp", "Pulp Application", None))
        self.KMTracker.setText(_translate("Pulpapp", "Import KM Tracker", None))
        self.Indent_Input.setText(_translate("Pulpapp", "Import Indent", None))
        self.KMTracker_3.setText(_translate("Pulpapp", "Truck Schedule", None))
        self.KMTracker_4.setText(_translate("Pulpapp", "Proceed", None))
        self.KMTracker_2.setText(_translate("Pulpapp", "Process Schedule", None))
        self.KMTracker_5.setText(_translate("Pulpapp", "Blend Schedule", None))
