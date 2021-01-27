from PyQt5 import QtWidgets
from Python_projeleri.hesap_makinesi.hm_arayuz import Ui_MainWindow

class Hm_Arayuz(QtWidgets.QMainWindow,Ui_MainWindow):
    ilksayi = None
    ikincisayi = False
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

        # artimetiksel işlemler buyonları etkileşimi

        self.pushButton_arti.clicked.connect(self.faritmetik)
        self.pushButton_eksi.clicked.connect(self.faritmetik)
        self.pushButton_carp.clicked.connect(self.faritmetik)
        self.pushButton_bol.clicked.connect(self.faritmetik)

        self.pushButton_arti.setCheckable(True)
        self.pushButton_eksi.setCheckable(True)
        self.pushButton_carp.setCheckable(True)
        self.pushButton_bol.setCheckable(True)

        #eşittir butonuna basıldığında
        self.pushButton_esittir.clicked.connect(self.fsonuc)
        self.pushButton_esittir.setCheckable(True)

        #temizle butonu basıldığında
        self.pushButton_temizle.clicked.connect(self.ftemizle)

     # herhangi bir rakam butonuna basıldığında çalışacak fonksiyon
    def frakam_basma(self):
        buton = self.sender()
        if ((self.ikincisayi) and (self.pushButton_esittir.isChecked())):
            self.label.setText(format(float(buton.text()), '.15g'))
            self.ikincisayi = True
            self.pushButton_esittir.setChecked(False)
        elif ((self.pushButton_arti.isChecked() or self.pushButton_eksi.isChecked() or self.pushButton_carp.isChecked() or self.pushButton_bol.isChecked())and (not self.ikincisayi)):
            self.label.setText(format(float(buton.text()), '.15g'))
            self.ikincisayi = True
        else:
            if (('.' in self.label.text()) and buton.text() == "0"):
                self.label.setText(format(float(self.label.text() + buton.text()), '.15'))
            else:
                self.label.setText(format(float(self.label.text() + buton.text()), '.15g'))


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

    def faritmetik(self):
        buton = self.sender()
        self.ilksayi = float(self.label.text())
        buton.setChecked(True)


    def fsonuc(self):
        ikincideger = float(self.label.text())

        if self.pushButton_arti.isChecked():
            yenideger = self.ilksayi + ikincideger
            self.label.setText(format(yenideger, '.15g'))
            self.pushButton_arti.setChecked(False)
        elif self.pushButton_carp.isChecked():
            yenideger = self.ilksayi * ikincideger
            self.label.setText(format(yenideger, '.15g'))
            self.pushButton_carp.setChecked(False)
        elif self.pushButton_eksi.isChecked():
            yenideger = self.ilksayi - ikincideger
            self.label.setText(format(yenideger, '.15g'))
            self.pushButton_eksi.setChecked(False)
        elif self.pushButton_bol.isChecked():
            yenideger = self.ilksayi / ikincideger
            self.label.setText(format(yenideger, '.15g'))
            self.pushButton_bol.setChecked(False)

        self.ilksayi = yenideger
        self.pushButton_esittir.setChecked(True)

    def ftemizle(self):
        self.ilksayi = 0
        self.ikincisayi = False
        self.label.setText("0")
        self.pushButton_arti.setChecked(False)
        self.pushButton_eksi.setChecked(False)
        self.pushButton_esittir.setChecked(False)
        self.pushButton_carp.setChecked(False)
        self.pushButton_bol.setChecked(False)
