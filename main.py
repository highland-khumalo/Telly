import os
import os.path
import subprocess
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(792, 545)
        MainWindow.setStyleSheet("* {\n"
                                 "    background-color:  white;\n"
                                 "    color: rgb(28, 113, 216);\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton {\n"
                                 "    background-color: rgb(28, 113, 216);\n"
                                 "    color: white;\n"
                                 "    border: 2px solid transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QPushButton:hover {\n"
                                 "    background-color: rgb(53, 132, 228);\n"
                                 "    color: white;\n"
                                 "    border: 2px solid transparent;\n"
                                 "}\n"
                                 "\n"
                                 "QLabel {\n"
                                 "    font: 81 20pt \"Cantarell\";\n"
                                 "}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(320, 50, 91, 131))
        self.label.setText("")
        self.label.setPixmap(QPixmap("tely.bk011.png"))
        self.label.setObjectName("label")
        self.logot = QLabel(self.centralwidget)
        self.logot.setGeometry(QRect(410, 80, 211, 71))
        self.logot.setStyleSheet("#logot {\n"
                                 "    font: 81 28pt \"Cantarell\";\n"
                                 "}")
        self.logot.setObjectName("logot")

        self.start = QPushButton(self.centralwidget)
        self.start.setGeometry(QRect(70, 460, 211, 31))
        self.start.setObjectName("pushButton")
        self.start.clicked.connect(self.st)

        self.cont = QPushButton(self.centralwidget)
        self.cont.setGeometry(QRect(290, 460, 211, 31))
        self.cont.setObjectName("pushButton_2")
        self.start.clicked.connect(self.conti)

        self.res = QPushButton(self.centralwidget)
        self.res.setGeometry(QRect(510, 460, 211, 31))
        self.res.setObjectName("pushButton_3")

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setGeometry(QRect(310, 280, 401, 31))
        self.label_2.setObjectName("label_2")

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setGeometry(QRect(310, 240, 401, 31))
        self.label_3.setObjectName("label_3")

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setGeometry(QRect(310, 320, 411, 31))
        self.label_4.setObjectName("label_4")

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setGeometry(QRect(310, 360, 421, 31))
        self.label_5.setObjectName("label_5")

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setGeometry(QRect(70, 140, 51, 51))
        self.label_6.setText("")
        self.label_6.setPixmap(QPixmap("../box1.png"))
        self.label_6.setObjectName("label_6")

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setGeometry(QRect(660, 140, 51, 51))
        self.label_7.setText("")
        self.label_7.setPixmap(QPixmap("../box1.png"))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Telly"))
        self.logot.setText(_translate("MainWindow", "elly"))

        self.start.setText(_translate("MainWindow", "Start"))
        self.cont.setText(_translate("MainWindow", "Continue"))
        self.res.setText(_translate("MainWindow", "Restart"))
        if os.path.isfile("game.one"):
            with open("game.one", "r+") as game:
                game = game.read().split("\n")
                for line in game:
                    if line.startswith("time: "):
                        score = int(line.replace("time: ", ""))
                        self.label_2.setText(
                            _translate("MainWindow", "Latest Score: " + str(score)))
                    elif line.startswith("LEVEL: "):
                        level = int(line.replace("LEVEL: ", ""))
                        self.label_3.setText(
                            _translate("MainWindow", "Level: " + str(level)))
                    elif line.startswith("HIGHSCORE: "):
                        HIGHSCORE = int(line.replace("HIGHSCORE: ", ""))
                        self.label_4.setText(
                            _translate("MainWindow",
                                       "High Score: " + str(HIGHSCORE)))
                    self.label_5.setText(_translate("MainWindow", "6th place"))

    def st(self):
        if os.path.isfile("game.one"):
            os.remove("game.one")
        _translate = QCoreApplication.translate
        import game
        game.game()
        print("end")
        if os.path.isfile("game.one"):
            with open("game.one", "r+") as game:
                game = game.read().split("\n")
                for line in game:
                    if line.startswith("time: "):
                        score = int(line.replace("time: ", ""))
                        self.label_2.setText(
                            _translate("MainWindow", "Latest Score: " + str(score)))
                    elif line.startswith("LEVEL: "):
                        level = int(line.replace("LEVEL: ", ""))
                        self.label_3.setText(
                            _translate("MainWindow", "Level: " + str(level)))
                    elif line.startswith("HIGHSCORE: "):
                        HIGHSCORE = int(line.replace("HIGHSCORE: ", ""))
                        self.label_4.setText(
                            _translate("MainWindow",
                                       "High Score: " + str(HIGHSCORE)))
                    self.label_5.setText(_translate("MainWindow", "6th place"))
    def conti(self):
        import game
        game.game()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_MainWindow()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
