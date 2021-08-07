from PyQt5 import QtWidgets


class Error(QtWidgets.QMessageBox):

    def __init__(self, summary, details):
        super().__init__()
        self.setIcon(QtWidgets.QMessageBox.Critical)
        self.setText(summary)
        self.setInformativeText(details)
        self.setWindowTitle("Error")

    def show(self):
        self.exec_()
