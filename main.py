import ast
import sys
import urllib.request
import logging
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
randomstroka = ""

logger = logging.getLogger('')  # записываем строку в логи
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
file_handler = logging.FileHandler('logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("UI/main.ui",self)

    def update_label(self): #Берём данные с сайта с помощью запроса в байтовом виде, конвертируем в слоарь и достаём строку по ключу
        url = 'http://service.oblako-it.com/test/generateRandomString'
        data = urllib.request.urlopen(url).read()
        dict_str = data.decode("UTF-8")
        stroka = ast.literal_eval(dict_str)
        stroka = stroka.get('randomString')
        self.randoms.setText(stroka)
        logger.info(stroka)

app = QApplication(sys.argv)
ex = Main()
widget = QtWidgets.QStackedWidget()
widget.addWidget(ex)
widget.setFixedWidth(600)
widget.setFixedHeight(300)
widget.show()
timer = QTimer()
timer.timeout.connect(ex.update_label)
timer.start(60000)
sys.exit(app.exec_())