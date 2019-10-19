
import sys
from PyQt4 import QtCore, QtGui
from alpha import Ui_Scheduler
from database import  select_date_from_table,delete_dates_from_table,insert_into_work,insert_into_skudim,select_from_skudimpath
import skuaddgui
from nooftruck import tenative,volume_or_weight_map,schedule_two_week_truck,depo_day_map,depo_list,depo_truck,dummy,map_list,schedule_list
import tenativegui
from get_sku_format_with_depo import get_format_from_dim_km
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
        self.ui.proceedtonexttext.hide()
        self.ui.next.hide()
        self.ui.calendarWidget.clicked.connect(self.select_working_days)
        self.ui.confirm_date.clicked.connect(self.confirm_dates)
        self.skuaddguipy = skuaddgui.MyDialog()
        self.ui.modify_sku.clicked.connect(self.goto_skuaddgui)
        self.ui.datelistview.setSelectionMode(QtGui.QListWidget.MultiSelection)
        self.ui.datedeletebutton.clicked.connect(self.delete_dates)
        self.tenativegiu = tenativegui.MyDialog()
        self.ui.next.clicked.connect(self.show_tenative)
        self.ui.inputskudimension.clicked.connect(self.inputskuhere)
        self.ui.get_sku_format.clicked.connect(self.generate_op_from_km)


    @QtCore.pyqtSignature("")
    def goto_skuaddgui(self):
        self.skuaddguipy.show()
        
    @QtCore.pyqtSignature("")
    def inputskuhere(self):
        path = QtGui.QFileDialog.getOpenFileName()
        insert_into_skudim(str(path))


    @QtCore.pyqtSignature("")
    def show_tenative(self):
        self.tenativegiu.show()




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


    @QtCore.pyqtSignature("")
    def generate_op_from_km(self):
        datesfromtable = select_date_from_table("working_days")
        scheduledates = []
        for i in datesfromtable:
            scheduledates.append(str(i[0]))
        dm = select_from_skudimpath()
        for i in dm:
            pathtodm = i[1]
        print(pathtodm)
        get_format_from_dim_km(str(self.ui.path.text()),str(pathtodm))
        self.ui.next.show()
        self.ui.proceedtonexttext.show()



    @QtCore.pyqtSignature("")
    def delete_dates(self):
        dates_to_delete = self.ui.datelistview.selectedItems()
        for i in dates_to_delete:
            delete_dates_from_table(i.text())
        self.ui.datelistview.clear()
        res = select_date_from_table("working_days")
        for i in res:
            self.ui.datelistview.addItem(str(i[0]))


if (__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())	
