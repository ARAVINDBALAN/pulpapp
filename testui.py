
import sys
from PyQt4 import QtCore, QtGui
from alpha import Ui_Scheduler

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Scheduler()
        self.ui.setupUi(self)
        self.ui.Browse.connect().clicked(selectFile)

def selectFile(self):
    self.ui.path.setText(QtGui.QFileDialog.getOpenFileName())

if (__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())	
