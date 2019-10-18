
import sys
from PyQt4 import QtCore, QtGui
from alpha import Ui_Scheduler
from database import  select_date_from_table,delete_dates_from_table,insert_into_work

#global variables 
li=[]

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Scheduler()
        self.ui.setupUi(self)
        self.ui.browse_check.hide()
        self.ui.browse_check.setChecked(False)
        self.ui.Browse.clicked.connect(self.selectFile)
        self.initializedates()
        self.ui.calendarWidget.clicked.connect(self.select_working_days)
        self.ui.confirm_date.clicked.connect(self.confirm_dates)


    @QtCore.pyqtSignature("")
    def selectFile(self):
        self.ui.path.setText(QtGui.QFileDialog.getOpenFileName())
        self.ui.browse_check.show()
        self.ui.browse_check.setChecked(True)


    @QtCore.pyqtSignature("")
    def select_working_days(self):
        select_date = self.ui.calendarWidget.selectedDate()
        if(select_date in li):
            li.remove(select_date.toPyDate())
        else:
            li.append(select_date.toPyDate())
        


    @QtCore.pyqtSignature("")
    def initializedates(self):
        res = select_date_from_table("working_days")
        for i in res:
            self.ui.datelistview.addItem(str(i[0]))
        

    @QtCore.pyqtSignature("")
    def confirm_dates(self):
        global li
        self.ui.datelistview.clear()
        string_dates = []
        for i in range(len(li)):
            string_dates.append(str(li[i]))
        res = select_date_from_table("working_days")
        table_dates = []
        for i in res:
            table_dates.append(i[0])
        print(table_dates)
        for i in table_dates:
            if i in string_dates:
                string_dates.remove(i)  
                delete_dates_from_table(i)
        insert_into_work(string_dates)
        res = select_date_from_table("working_days")

        for i in res:
            self.ui.datelistview.addItem(str(i[0]))
        li=[]





if (__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())	
