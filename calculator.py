from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui= QUiLoader().load('calculatorUi.ui')
        self.ui.show()
        self.number = 0
        self.current_operation = None
        self.ui.display.setReadOnly(True)
        self.ui.num0.clicked.connect(lambda:self.add_num(0))
        self.ui.num1.clicked.connect(lambda:self.add_num(1))
        self.ui.num2.clicked.connect(lambda:self.add_num(2))
        self.ui.num3.clicked.connect(lambda:self.add_num(3))
        self.ui.num4.clicked.connect(lambda:self.add_num(4))
        self.ui.num5.clicked.connect(lambda:self.add_num(5))
        self.ui.num6.clicked.connect(lambda:self.add_num(6))
        self.ui.num7.clicked.connect(lambda:self.add_num(7))
        self.ui.num8.clicked.connect(lambda:self.add_num(8))
        self.ui.num9.clicked.connect(lambda:self.add_num(9))
        self.ui.plus.clicked.connect(lambda:self.operation('+'))
        self.ui.minus.clicked.connect(lambda:self.operation('-'))
        self.ui.cross.clicked.connect(lambda:self.operation('x'))
        self.ui.div.clicked.connect(lambda:self.operation('/'))
        self.ui.equlas.clicked.connect(self.calculate)
        self.ui.C.clicked.connect(self.clear)


    def append_to_text(self, _str):
        self.ui.display.setText(self.ui.display.toPlainText() + _str)

    def add_num(self,num):
        self.number = self.number * 10 + num
        self.append_to_text(str(num))
    def operation(self,symbol):
        self.append_to_text(symbol)
        self.current_operation = symbol
        self.temp_number = self.number
        self.number = 0

    def calculate(self):
        self.append_to_text('=\n')
        if self.current_operation == '+':
            result = self.temp_number + self.number
        if self.current_operation == '-':
            result = self.temp_number - self.number
        if self.current_operation == 'x':
            result = self.temp_number * self.number
        if self.current_operation == '/':
            result = round(self.temp_number / self.number,10)
        self.append_to_text(str(result))
        self.append_to_text('\n')
        self.number = 0

    def clear(self):
        self.ui.display.clear()
        self.number = 0

app = QApplication([])
my_window = window()
app.exec()

