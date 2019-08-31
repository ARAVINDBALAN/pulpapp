
import sys
from PyQt4 import QtCore, QtGui
from pulpui import Ui_Pulpapp

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Pulpapp()
        self.ui.setupUi(self)

if (__name__ == "__main__"):
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())	
