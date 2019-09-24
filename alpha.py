# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scheduler_main.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from datetime import datetime,date
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

class Ui_Scheduler(object):
    def setupUi(self, Scheduler):
        Scheduler.setObjectName(_fromUtf8("Scheduler"))
        Scheduler.resize(835, 605)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Scheduler.setWindowIcon(icon)
        self.modify_sku = QtGui.QPushButton(Scheduler)
        self.modify_sku.setGeometry(QtCore.QRect(610, 160, 181, 29))
        self.modify_sku.setObjectName(_fromUtf8("modify_sku"))
        self.line = QtGui.QFrame(Scheduler)
        self.line.setGeometry(QtCore.QRect(540, 20, 20, 571))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.path = QtGui.QLineEdit(Scheduler)
        self.path.setGeometry(QtCore.QRect(40, 100, 211, 29))
        self.path.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);"))
        self.path.setObjectName(_fromUtf8("path"))
        self.Browse = QtGui.QPushButton(Scheduler)
        self.Browse.setGeometry(QtCore.QRect(270, 100, 100, 29))
        self.Browse.setObjectName(_fromUtf8("Browse"))
        self.modify_machine = QtGui.QPushButton(Scheduler)
        self.modify_machine.setGeometry(QtCore.QRect(610, 220, 181, 29))
        self.modify_machine.setObjectName(_fromUtf8("modify_machine"))
        self.Blend_calc = QtGui.QPushButton(Scheduler)
        self.Blend_calc.setGeometry(QtCore.QRect(610, 280, 181, 29))
        self.Blend_calc.setObjectName(_fromUtf8("Blend_calc"))
        self.schedule = QtGui.QPushButton(Scheduler)
        self.schedule.setGeometry(QtCore.QRect(130, 560, 181, 29))
        self.schedule.setObjectName(_fromUtf8("schedule"))
        self.calendarWidget = QtGui.QCalendarWidget(Scheduler)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 260, 448, 174))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.label = QtGui.QLabel(Scheduler)
        self.label.setGeometry(QtCore.QRect(120, 220, 261, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.date = QtGui.QLabel(Scheduler)
        self.date.setGeometry(QtCore.QRect(730, 10, 141, 20))
        self.date.setObjectName(_fromUtf8("date"))
        self.day = QtGui.QLabel(Scheduler)
        self.day.setGeometry(QtCore.QRect(730, 30, 141, 20))
        self.day.setObjectName(_fromUtf8("day"))
        self.browse_check = QtGui.QCheckBox(Scheduler)
        self.browse_check.setGeometry(QtCore.QRect(10, 100, 21, 31))
        self.browse_check.setText(_fromUtf8(""))
        self.browse_check.setObjectName(_fromUtf8("browse_check"))
        self.browse_check_2 = QtGui.QCheckBox(Scheduler)
        self.browse_check_2.setGeometry(QtCore.QRect(390, 220, 96, 20))
        self.browse_check_2.setText(_fromUtf8(""))
        self.browse_check_2.setObjectName(_fromUtf8("browse_check_2"))
        self.confirm_date = QtGui.QPushButton(Scheduler)
        self.confirm_date.setGeometry(QtCore.QRect(200, 470, 100, 29))
        self.confirm_date.setObjectName(_fromUtf8("confirm_date"))

        self.retranslateUi(Scheduler)
        QtCore.QMetaObject.connectSlotsByName(Scheduler)

    def retranslateUi(self, Scheduler):
        Scheduler.setWindowTitle(_translate("Scheduler", "Scheduler Application for PULP", None))
        self.modify_sku.setText(_translate("Scheduler", "Modify  SKUs", None))
        self.Browse.setText(_translate("Scheduler", "Browse", None))
        self.modify_machine.setText(_translate("Scheduler", "Modify Machine Config", None))
        self.Blend_calc.setText(_translate("Scheduler", "Blend Calculation", None))
        self.schedule.setText(_translate("Scheduler", "Schedule", None))
        self.label.setText(_translate("Scheduler", "Select working days from the calender", None))
        self.date.setText(_translate("Scheduler", str(date.today()), None))
        self.day.setText(_translate("Scheduler", str(datetime.today().strftime("%A")), None))
        self.confirm_date.setText(_translate("Scheduler", "Confirm date", None))

