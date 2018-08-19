from PyQt5 import QtCore, QtGui, QtWidgets
import pycurl as pc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(674, 370)
        MainWindow.setMinimumSize(QtCore.QSize(674, 370))
        MainWindow.setMaximumSize(QtCore.QSize(674, 370))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 311, 31))
        self.label.setStyleSheet('font: 20pt "Monospace";')
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 40, 201, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 101, 31))
        self.label_3.setObjectName("label_3")
        self.ip = QtWidgets.QLineEdit(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(130, 100, 471, 30))
        self.ip.setStyleSheet('font: 12pt "Monospace";')
        self.ip.setText("")
        self.ip.setObjectName("ip")
        self.set = QtWidgets.QPushButton(self.centralwidget)
        self.set.setGeometry(QtCore.QRect(610, 100, 51, 31))
        self.set.setStyleSheet('font: 10pt "Monospace";')
        self.set.setObjectName("set")
        self.up = QtWidgets.QPushButton(self.centralwidget)
        self.up.setGeometry(QtCore.QRect(310, 180, 51, 31))
        self.up.setStyleSheet('font: 12pt "Monospace";')
        self.up.setObjectName("up")
        self.left = QtWidgets.QPushButton(self.centralwidget)
        self.left.setGeometry(QtCore.QRect(220, 230, 51, 31))
        self.left.setMinimumSize(QtCore.QSize(51, 31))
        self.left.setStyleSheet('font: 12pt "Monospace";')
        self.left.setObjectName("left")
        self.down = QtWidgets.QPushButton(self.centralwidget)
        self.down.setGeometry(QtCore.QRect(310, 230, 51, 31))
        self.down.setStyleSheet('font: 12pt "Monospace";')
        self.down.setObjectName("down")
        self.right = QtWidgets.QPushButton(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(400, 230, 51, 31))
        self.right.setStyleSheet('font: 12pt "Monospace";')
        self.right.setObjectName("right")
        self.br3ak = QtWidgets.QPushButton(self.centralwidget)
        self.br3ak.setGeometry(QtCore.QRect(220, 280, 231, 31))
        self.br3ak.setStyleSheet('font: 12pt "Monospace";')
        self.br3ak.setObjectName("br3ak")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.obj = MainWindow

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GoKart Driver"))
        self.label.setText(_translate("MainWindow", "GoKart Driver Panel"))
        self.label_2.setText(
            _translate(
                "MainWindow",
                '<html><head/><body style="text-align:center">Brought to you by <span style=" font-weight:600;">Gurkirat Singh </span><br>https://tbhaxor.me/godry</body></html>',
            )
        )
        self.label_3.setText(_translate("MainWindow", "Car IP/Hostname"))
        self.set.setText(_translate("MainWindow", "Set"))
        self.up.setText(_translate("MainWindow", "↑"))
        self.left.setText(_translate("MainWindow", "←"))
        self.down.setText(_translate("MainWindow", "↓"))
        self.right.setText(_translate("MainWindow", "→"))
        self.br3ak.setText(_translate("MainWindow", "Break"))

        self.up.setEnabled(False)
        self.down.setEnabled(False)
        self.left.setEnabled(False)
        self.right.setEnabled(False)
        self.br3ak.setEnabled(False)

        self.set.clicked.connect(self.disable)

        self.up.clicked.connect(self.moveUp)
        self.down.clicked.connect(self.moveDown)
        self.left.clicked.connect(self.moveLeft)
        self.right.clicked.connect(self.moveRight)
        self.br3ak.clicked.connect(self.breakDown)
        pass

    def disable(self):
        ip = self.ip.text()
        if ip == "":
            QtWidgets.QMessageBox.information(self.obj, " ", "IP/Hostname is mandatory")
            return
        else:
            self.ip.setReadOnly(True)
            self.set.setEnabled(False)
            QtWidgets.QMessageBox.information(
                self.obj,
                "Ready",
                "You can now use the panel\nTo change ip restart the app",
            )
            self.up.setEnabled(True)
            self.down.setEnabled(True)
            self.left.setEnabled(True)
            self.right.setEnabled(True)
            self.br3ak.setEnabled(True)

    def moveDown(self):
        ip = "http://{}:80/?action=".format(self.ip.text())
        curl = pc.Curl()
        curl.setopt(pc.URL, ip + "bck")
        curl.setopt(pc.NOBODY, True)
        curl.setopt(pc.HEADER, False)
        curl.setopt(pc.CONNECTTIMEOUT_MS, 600)
        curl.perform()
        curl.close()

    def moveUp(self):
        ip = "http://{}:80/?action=".format(self.ip.text())
        curl = pc.Curl()
        curl.setopt(pc.URL, ip + "fwd")
        curl.setopt(pc.NOBODY, True)
        curl.setopt(pc.HEADER, False)
        curl.setopt(pc.CONNECTTIMEOUT_MS, 600)
        curl.perform()
        curl.close()

    def moveLeft(self):
        ip = "http://{}:80/?action=".format(self.ip.text())
        curl = pc.Curl()
        curl.setopt(pc.URL, ip + "lft")
        curl.setopt(pc.NOBODY, True)
        curl.setopt(pc.HEADER, False)
        curl.setopt(pc.CONNECTTIMEOUT_MS, 600)
        curl.perform()
        curl.close()

    def breakDown(self):
        ip = "http://{}:80/?action=".format(self.ip.text())
        curl = pc.Curl()
        curl.setopt(pc.URL, ip + "brk")
        curl.setopt(pc.NOBODY, True)
        curl.setopt(pc.HEADER, False)
        curl.setopt(pc.CONNECTTIMEOUT_MS, 600)
        curl.perform()
        curl.close()

    def moveRight(self):
        ip = "http://{}:80/?action=".format(self.ip.text())
        curl = pc.Curl()
        curl.setopt(pc.URL, ip + "rgt")
        curl.setopt(pc.NOBODY, True)
        curl.setopt(pc.HEADER, False)
        curl.setopt(pc.CONNECTTIMEOUT_MS, 600)
        curl.perform()
        curl.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
