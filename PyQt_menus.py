# Bu uygulama PyQt5 ile Uygulama arayüzü hazırlanmasını içerir.
# Dosya,Düzenle ve Yardım menüleri içerikleri ile erişilebilmektedir.
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtGui import QKeySequence


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Python Menus & Toolbars")
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.resize(400, 200)
        self.centralWidget = QLabel(" ")
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setAlignment(Qt.AlignHCenter)
        self.Action()
        self.Menu()
        self.Tool()
        self.Sag_tik()
        self.cikis()


    def Menu(self):
        menuBar = self.menuBar() # ana menü çubuğu
        dosyaMenu = menuBar.addMenu("&Dosya")
        dosyaMenu.addAction(self.yeni)
        dosyaMenu.addAction(self.ac)
        sonKullanilan = dosyaMenu.addMenu("Son Kullanılan")
        dosyaMenu.addAction(self.kaydet)
        dosyaMenu.addAction(self.cik)
        duzenMenu = menuBar.addMenu("&Düzenle")
        duzenMenu.addAction(self.kopyala)
        duzenMenu.addAction(self.yapistir)
        duzenMenu.addAction(self.kes)
        bulMenu = duzenMenu.addMenu("Bul ve Değiştir")
        bulMenu.addAction("Bul")
        bulMenu.addAction("Değiştir")
        yardimMenu = menuBar.addMenu("&Yardım")
        yardimMenu.addAction(self.hakkinda)

    def Tool(self):
        dosyaTool = self.addToolBar("Dosya")
        dosyaTool.setMovable(False)
        duzenTool = self.addToolBar("Düzenle")
        yardimTool = self.addToolBar("Yardim")
        self.yaziboyut = QSpinBox()
        self.yaziboyut.setFocusPolicy(Qt.NoFocus)
        dosyaTool.addWidget(self.yaziboyut)

    def Action(self):
        self.yeni = QAction("&Yeni",self)
        self.yeni.setShortcut("Ctrl+N")
        self.ac = QAction("&Aç",self)
        self.ac.setShortcut("Ctrl+O")
        self.kaydet = QAction("&Kaydet",self)
        self.kaydet.setShortcut("Ctrl+S")
        self.cik = QAction("&Çık",self)
        self.kopyala = QAction("&Kopyala",self)
        self.kopyala.setShortcut(QKeySequence.Copy)
        self.yapistir = QAction("&Yapıştır",self)
        self.yapistir.setShortcut(QKeySequence.Paste)
        self.kes = QAction("&Kes",self)
        self.kes.setShortcut(QKeySequence.Cut)
        self.hakkinda = QAction("&Hakkında",self)

    def Sag_tik(self):
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.addAction(self.yeni)
        self.addAction(self.ac)
        self.addAction(self.kaydet)
        ayir = QAction(self)
        ayir.setSeparator(True)
        self.addAction(ayir)
        self.addAction(self.kopyala)
        self.addAction(self.yapistir)
        self.addAction(self.kes)

    def cikis(self):
        self.cik.triggered.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
