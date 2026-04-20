from PyQt5 import QtWidgets, uic,QtCore
import sys

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("untitled.ui")


flags = QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint
window.setWindowFlags(flags)
window.show()


sys.exit(app.exec_())