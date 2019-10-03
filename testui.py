
import sys
from PyQt4 import QtCore, QtGui
from alpha import Ui_Scheduler
import skuaddgui
#global variables
global li 
li = []

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Scheduler()
        self.ui.setupUi(self)
        self.ui.Browse.clicked.connect(self.selectFile)
        self.ui.calendarWidget.clicked.connect(self.select_working_days)
        self.sku_modify = skuaddgui.MyDialog()
        self.ui.modify_sku.clicked.connect(self.goto_modify_sku) 
        self.ui.confirm_date.clicked.connect(self.confirm_date_fun)


    @QtCore.pyqtSignature("")
    def selectFile(self):
        self.ui.path.setText(QtGui.QFileDialog.getOpenFileName())
        #self.ui.browse_check.setEnabled(True)
        self.ui.browse_check.setChecked(True)
    
    

    @QtCore.pyqtSignature("")
    def select_working_days(self):
        select_date = self.ui.calendarWidget.selectedDate()
        if(select_date in li):
            li.remove(select_date.toPyDate())
        else:
            li.append(select_date.toPyDate())
        
        #self.ui.calendarWidget.paintCell(self.paintEvent(),QtCore.QRect(10,10,10,10),self.ui.calendarWidget.selectedDate())

    @QtCore.pyqtSignature("")
    def goto_modify_sku(self):
        self.sku_modify.show()
    

    @QtCore.pyqtSignature("")
    def confirm_date_fun(self):
        choice = li
        print(choice)


if (__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())	
