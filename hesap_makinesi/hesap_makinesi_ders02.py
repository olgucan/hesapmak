from PyQt5 import QtWidgets
from Python_projeleri.hesap_makinesi.hm_arayuz import Ui_MainWindow

class Hm_Arayuz(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()




