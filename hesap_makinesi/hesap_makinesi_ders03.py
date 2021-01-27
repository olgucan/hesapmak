from PyQt5 import QtWidgets
from Python_projeleri.hesap_makinesi.hm_arayuz import Ui_MainWindow

class Hm_Arayuz(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        #rakam butonları etkileşimi
        self.pushButton_1.clicked.connect(self.frakam_basma)
        self.pushButton_2.clicked.connect(self.frakam_basma)
        self.pushButton_3.clicked.connect(self.frakam_basma)
        self.pushButton_4.clicked.connect(self.frakam_basma)
        self.pushButton_5.clicked.connect(self.frakam_basma)
        self.pushButton_6.clicked.connect(self.frakam_basma)
        self.pushButton_7.clicked.connect(self.frakam_basma)
        self.pushButton_8.clicked.connect(self.frakam_basma)
        self.pushButton_9.clicked.connect(self.frakam_basma)
        self.pushButton_0.clicked.connect(self.frakam_basma)

        #nokta butonu etkileşimi
        self.pushButton_nokta.clicked.connect(self.fondalik)

        #işaret ve yüzde buton etkileşimi
        self.pushButton_isaret.clicked.connect(self.fisaret_yuzde)
        self.pushButton_yuzde.clicked.connect(self.fisaret_yuzde)



     # herhangi bir rakam butonuna basıldığında çalışacak fonksiyon
    def frakam_basma(self):
        buton = self.sender()
        self.label.setText(format(float(self.label.text() + buton.text()),'.15g'))

    def fondalik(self):
        self.label.setText(self.label.text()+".")
        #koşullu durum oluştur noktaya iki kere basılmasın ???


    def fisaret_yuzde(self):
        buton = self.sender()

        deger = float(self.label.text())

        if buton.text()=="+/-":
            deger = deger*-1
        else:
            deger = deger*0.01

        self.label.setText(format(deger,'.15g'))


