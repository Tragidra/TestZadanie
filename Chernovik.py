import ast
import sys
import urllib.request
import sched, time

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
randomstroka = ""

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("UI/main.ui",self)
        s = sched.scheduler(time.time, time.sleep)
        s.enter(5, 1, Main.request, (s,))
        s.run()

    def request(sc):
        global randomstroka
        print("Doing stuff...")
        url = 'http://service.oblako-it.com/test/generateRandomString'
        data = urllib.request.urlopen(url).read()
        dict_str = data.decode("UTF-8")
        stroka = ast.literal_eval(dict_str)
        stroka = stroka.get('randomString')
        randomstroka = stroka
        sc.enter(5, 1, Main.request, (sc,))

    def peresapis(self):
        self.randoms.settext(randomstroka)

app = QApplication(sys.argv)
mainW = Main()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainW)
widget.setFixedWidth(600)
widget.setFixedHeight(500)
widget.show()
app.exec()