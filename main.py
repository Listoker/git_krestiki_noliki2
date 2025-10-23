import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class Krestiki(QWidget):
    def __init__(self):
        self.x = 600
        self.y = 800
        self.znaki = [[''],[''],[''],[''],[''],[''],[''],[''],['']]
        self.nomer = 0
        self.hods = 0
        super().__init__()
        self.setupUI()


    def setupUI(self):
        self.setGeometry(int(30), int(50), int(self.x), int(self.y))
        self.setWindowTitle('Крестики нолики')

        self.blok = QPushButton(''.join(self.znaki[0]), self)
        self.blok.move(0, 0)
        self.blok.resize(200, 200)
        self.blok.clicked.connect(self.hod)

        self.blok1 = QPushButton(''.join(self.znaki[1]), self)
        self.blok1.move(200, 0)
        self.blok1.resize(200, 200)
        self.blok1.clicked.connect(self.hod1)

        self.blok2 = QPushButton(''.join(self.znaki[2]), self)
        self.blok2.move(400, 0)
        self.blok2.resize(200, 200)
        self.blok2.clicked.connect(self.hod2)

        self.blok3 = QPushButton(''.join(self.znaki[3]), self)
        self.blok3.move(0, 200)
        self.blok3.resize(200, 200)
        self.blok3.clicked.connect(self.hod3)

        self.blok4 = QPushButton(''.join(self.znaki[4]), self)
        self.blok4.move(200, 200)
        self.blok4.resize(200, 200)
        self.blok4.clicked.connect(self.hod4)

        self.blok5 = QPushButton(''.join(self.znaki[5]), self)
        self.blok5.move(400, 200)
        self.blok5.resize(200, 200)
        self.blok5.clicked.connect(self.hod5)

        self.blok6 = QPushButton(''.join(self.znaki[6]), self)
        self.blok6.move(0, 400)
        self.blok6.resize(200, 200)
        self.blok6.clicked.connect(self.hod6)

        self.blok7 = QPushButton(''.join(self.znaki[7]), self)
        self.blok7.move(200, 400)
        self.blok7.resize(200, 200)
        self.blok7.clicked.connect(self.hod7)

        self.blok8 = QPushButton(''.join(self.znaki[8]), self)
        self.blok8.move(400, 400)
        self.blok8.resize(200, 200)
        self.blok8.clicked.connect(self.hod8)

        self.label1 = QLabel(" Нажимайте по очереди. Кто первый соберет 3 Х или 0 в ряд(или по диагонали), тот победил.\n Кнопка рестарт очищает поле.", self)
        self.label1.move(0, 600)
        self.label1.resize(600, 100)

        self.restar = QPushButton('рестарт', self)
        self.restar.move(0, 700)
        self.restar.resize(600, 100)
        self.restar.clicked.connect(self.restart)

    def hod(self):
        if self.znaki[0] == ['']:
            self.hods += 1
            if self.nomer == 0:
                self.znaki[0] = ['x']
                self.blok.setText('X')
                self.nomer = 1
                self.pobed_x()
            elif self.nomer == 1:
                self.znaki[0] = ['0']
                self.blok.setText('0')
                self.nomer = 0
                self.pobed_0()

    def hod1(self):
        if self.znaki[1] == ['']:
            self.hods += 1
            if self.nomer == 0:
                self.znaki[1] = ['x']
                self.blok1.setText('X')
                self.nomer = 1
                self.pobed_x()
            elif self.nomer == 1:
                self.znaki[1] = ['0']
                self.blok1.setText('0')
                self.nomer = 0
                self.pobed_0()

    def hod2(self):
        if self.znaki[2] == ['']:
            self.hods += 1
            if self.nomer == 0:
                self.znaki[2] = ['x']
                self.blok2.setText('X')
                self.nomer = 1
                self.pobed_x()
            elif self.nomer == 1:
                self.znaki[2] = ['0']
                self.blok2.setText('0')
                self.nomer = 0
                self.pobed_0()

    def hod3(self):
        if self.znaki[3] == ['']:
            self.hods += 1
            if self.nomer == 0:
                self.znaki[3] = ['x']
                self.blok3.setText('X')
                self.nomer = 1
                self.pobed_x()
            elif self.nomer == 1:
                self.znaki[3] = ['0']
                self.blok3.setText('0')
                self.nomer = 0
                self.pobed_0()

    def hod4(self):
        if self.znaki[4] == ['']:
            self.hods += 1
            if self.nomer == 0:
                self.znaki[4] = ['x']
                self.blok4.setText('X')
                self.nomer = 1
                self.pobed_x()
            elif self.nomer == 1:
                self.znaki[4] = ['0']
                self.blok4.setText('0')
                self.nomer = 0
                self.pobed_0()

    def hod5(self):
        if self.znaki[5] == ['']:
            self.hods += 1
            if self.nomer == 0:
                self.znaki[5] = ['x']
                self.blok5.setText('X')
                self.nomer = 1
                self.pobed_x()
            elif self.nomer == 1:
                self.znaki[5] = ['0']
                self.blok5.setText('0')
                self.nomer = 0
                self.pobed_0()

    def hod6(self):
        if self.znaki[6] == ['']:
            self.hods += 1
            if self.nomer == 0:
                self.znaki[6] = ['x']
                self.blok6.setText('X')
                self.nomer = 1
                self.pobed_x()
            elif self.nomer == 1:
                self.znaki[6] = ['0']
                self.blok6.setText('0')
                self.nomer = 0
                self.pobed_0()

    def hod7(self):
        if self.znaki[7] == ['']:
            self.hods += 1
            if self.nomer == 0:
                self.znaki[7] = ['x']
                self.blok7.setText('X')
                self.nomer = 1
                self.pobed_x()
            elif self.nomer == 1:
                self.znaki[7] = ['0']
                self.blok7.setText('0')
                self.nomer = 0
                self.pobed_0()

    def hod8(self):
        if self.znaki[8] == ['']:
            self.hods += 1
            if self.nomer == 0:
                self.znaki[8] = ['x']
                self.blok8.setText('X')
                self.nomer = 1
                self.pobed_x()
            elif self.nomer == 1:
                self.znaki[8] = ['0']
                self.blok8.setText('0')
                self.nomer = 0
                self.pobed_0()


    def pobed_x(self):
        if self.znaki[0] == self.znaki[1] == self.znaki[2] == ['x']:
            self.label1.setText("Победили Х")
            self.nomer = 3
        elif self.znaki[3] == self.znaki[4] == self.znaki[5] == ['x']:
            self.label1.setText("Победили Х")
            self.nomer = 3
        elif self.znaki[6] == self.znaki[7] == self.znaki[8] == ['x']:
            self.label1.setText("Победили Х")
            self.nomer = 3
        elif self.znaki[0] == self.znaki[3] == self.znaki[6] == ['x']:
            self.label1.setText("Победили Х")
            self.nomer = 3
        elif self.znaki[1] == self.znaki[4] == self.znaki[7] == ['x']:
            self.label1.setText("Победили Х")
            self.nomer = 3
        elif self.znaki[2] == self.znaki[5] == self.znaki[8] == ['x']:
            self.label1.setText("Победили Х")
            self.nomer = 3
        elif self.znaki[0] == self.znaki[4] == self.znaki[8] == ['x']:
            self.label1.setText("Победили Х")
            self.nomer = 3
        elif self.znaki[2] == self.znaki[4] == self.znaki[6] == ['x']:
            self.label1.setText("Победили Х")
            self.nomer = 3
        elif self.hods >= 8:
            self.label1.setText("Ничья")
            self.nomer = 3


    def pobed_0(self):
        if self.znaki[0] == self.znaki[1] == self.znaki[2] == ['0']:
            self.label1.setText("Победили 0")
            self.nomer = 3
        elif self.znaki[3] == self.znaki[4] == self.znaki[5] == ['0']:
            self.label1.setText("Победили 0")
            self.nomer = 3
        elif self.znaki[6] == self.znaki[7] == self.znaki[8] == ['0']:
            self.label1.setText("Победили 0")
            self.nomer = 3
        elif self.znaki[0] == self.znaki[3] == self.znaki[6] == ['0']:
            self.label1.setText("Победили 0")
            self.nomer = 3
        elif self.znaki[1] == self.znaki[4] == self.znaki[7] == ['0']:
            self.label1.setText("Победили 0")
            self.nomer = 3
        elif self.znaki[2] == self.znaki[5] == self.znaki[8] == ['0']:
            self.label1.setText("Победили 0")
            self.nomer = 3
        elif self.znaki[0] == self.znaki[4] == self.znaki[8] == ['0']:
            self.label1.setText("Победили 0")
            self.nomer = 3
        elif self.znaki[2] == self.znaki[4] == self.znaki[6] == ['0']:
            self.label1.setText("Победили 0")
            self.nomer = 3



    def restart(self):
        self.znaki = [[''],[''],[''],[''],[''],[''],[''],[''],['']]
        self.blok.setText('')
        self.blok1.setText('')
        self.blok2.setText('')
        self.blok3.setText('')
        self.blok4.setText('')
        self.blok5.setText('')
        self.blok6.setText('')
        self.blok7.setText('')
        self.blok8.setText('')
        self.nomer = 0
        self.hods = 0
        self.label1.setText(" Нажимайте по очереди. Кто первый соберет 3 Х или 0 в ряд(или диагонали), тот победил.\n Кнопка рестарт очищает поле.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Krestiki()
    example.show()
    sys.exit(app.exec())