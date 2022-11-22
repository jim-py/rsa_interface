import random
import form
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
import base64

import form2


def check(x, y):
    x, y = int(x), int(y)
    if x == y:
        return False
    else:
        i = 2
        while i < x / 2:
            if x % i == 0:
                return False
            i += 1
        i = 2
        while i < y / 2:
            if y % i == 0:
                return False
            i += 1

        return True


class SaveWindow(QWidget, form2.Ui_Form):
    def __init__(self):
        super(SaveWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Что сохранить?')
        self.pushButton.clicked.connect(self.browse_folder)

    def browse_folder(self):
        file = QtWidgets.QFileDialog.getSaveFileName(self, "Выберите файл")
        text_file = open(file[0], "w")
        save_str = {}
        if self.checkBox.isChecked():
            save_str[self.checkBox.text()] = self.lineEdit.text()
        if self.checkBox_2.isChecked():
            save_str[self.checkBox_2.text()] = self.lineEdit_2.text()
        if self.checkBox_3.isChecked():
            save_str[self.checkBox_3.text()] = self.lineEdit_3.text()
        if self.checkBox_4.isChecked():
            save_str[self.checkBox_4.text()] = self.lineEdit_4.text()
        if self.checkBox_5.isChecked():
            save_str[self.checkBox_5.text()] = self.textEdit.toPlainText()
        if self.checkBox_6.isChecked():
            save_str[self.checkBox_6.text()] = self.textEdit_2.toPlainText()
        for key, values in save_str.items():
            text_file.write(f'{key} --- {values}' + '\n')
        text_file.close()
        SaveWindow.close(self)


class MainRSA(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('~RSA~')
        self.action_2.triggered.connect(self.open_file)
        self.action.triggered.connect(self.open)
        self.pushButton.clicked.connect(self.generate_keys)
        self.pushButton_2.clicked.connect(self.encrypt_text)
        self.pushButton_3.clicked.connect(self.decrypt_text)
        self.action_3.triggered.connect(self.close)
        self.action_4.triggered.connect(self.clean)

    def open(self):
        self.w2 = SaveWindow()
        self.w2.lineEdit.setText(self.lineEdit.text())
        self.w2.lineEdit_2.setText(self.lineEdit_2.text())
        self.w2.lineEdit_3.setText(self.lineEdit_4.text())
        self.w2.lineEdit_4.setText(self.lineEdit_3.text())
        self.w2.textEdit.insertPlainText(self.textEdit_2.toPlainText())
        self.w2.textEdit_2.insertPlainText(self.textEdit_4.toPlainText())
        self.w2.show()

    def close(self):
        MainRSA.close(self)

    def clean(self):
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')
        self.lineEdit_3.setText('')
        self.lineEdit_4.setText('')
        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')
        self.lineEdit_8.setText('')
        self.lineEdit_9.setText('')
        self.lineEdit_10.setText('')
        self.textEdit.setText('')
        self.textEdit_2.setText('')
        self.textEdit_3.setText('')
        self.textEdit_4.setText('')

        return 1

    def open_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        with open(file[0], "r") as file:
            for line in file:
                line = line.split()
                s = f'{line[0]} {line[1]}'
                if len(line) == 5:
                    num = f'{line[3]} {line[4]}'
                else:
                    num = f'{line[3]}'
                num = str(num)
                if s == 'Простые числа':
                    self.lineEdit.setText(num)
                elif s == 'Публичный ключ':
                    self.lineEdit_2.setText(num)
                    self.lineEdit_5.setText(num)
                    self.lineEdit_7.setText(num)
                elif s == 'Открытая экспонента':
                    self.lineEdit_4.setText(num)
                    self.lineEdit_6.setText(num)
                elif s == 'Приватный ключ':
                    self.lineEdit_3.setText(num)
                    self.lineEdit_8.setText(num)
                elif s == 'Зашифрованный текст':
                    self.textEdit_2.insertPlainText(num)
                    self.textEdit_3.insertPlainText(num)
                elif s == 'Расшифрованный текст':
                    self.textEdit.insertPlainText(num)
                    self.textEdit_4.insertPlainText(num)

    def generate_keys(self):
        x = self.lineEdit_9.text()
        y = self.lineEdit_10.text()
        while True:
            if x.isdigit() and y.isdigit() and check(x, y):
                easy_num1, easy_num2 = int(x), int(y)
            else:
                easy_num1, easy_num2 = self.gen_easy_num(), self.gen_easy_num()
            private_key = 1
            open_exp = 1
            open_key = easy_num1 * easy_num2
            functionEller = (easy_num1 - 1) * (easy_num2 - 1)

            for i in range(1, 100):
                if functionEller % i != 0:
                    open_exp = i
                    break

            for k in range(100):
                if (functionEller * k + 1) / open_exp * 10 % 10 == 0:
                    private_key = (functionEller * k + 1) / open_exp
                    break

            if private_key != 1 and easy_num1 != easy_num2:
                break

        self.lineEdit.setText(f'{easy_num1} {easy_num2}')
        self.lineEdit_2.setText(f'{open_key}')
        self.lineEdit_3.setText(f'{int(private_key)}')
        self.lineEdit_4.setText(f'{open_exp}')
        if not self.lineEdit_5.text():
            self.lineEdit_5.setText(f'{open_key}')
        if not self.lineEdit_6.text():
            self.lineEdit_6.setText(f'{open_exp}')
        if not self.lineEdit_7.text():
            self.lineEdit_7.setText(f'{open_key}')
        if not self.lineEdit_8.text():
            self.lineEdit_8.setText(f'{int(private_key)}')

    def gen_easy_num(self):
        eas = []
        for num in range(100, 264):
            i = 2
            while i < num:
                if num % i == 0:
                    break
                i += 1
            else:
                eas.append(num)
        num_i = random.randint(0, len(eas) - 1)
        return eas[num_i]

    def encrypt_text(self):
        message = []
        self.textEdit_2.setText('')
        for i, word in enumerate(self.textEdit.toPlainText()):
            message += list(word)

        message_ord = []
        for i, letter in enumerate(message):
            message_ord.append(ord(letter))

        strok = ''
        for sim in message_ord:
            strok += f'{str(sim ** int(self.lineEdit_6.text()) % int(self.lineEdit_5.text()))} '
        b = base64.b64encode(bytes(strok, 'utf-8'))
        self.textEdit_2.insertPlainText(b.decode('utf-8'))
        return 1

    def decrypt_text(self):
        self.textEdit_4.setText('')
        for sim in base64.b64decode(self.textEdit_3.toPlainText()).decode("utf-8").split():
            sim = sim if sim[-1] != ',' else sim[:-1]
            self.textEdit_4.insertPlainText(chr(int(sim) ** int(self.lineEdit_8.text()) % int(self.lineEdit_7.text())))
        return 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainRSA()
    window.setFixedSize(392, 898)
    window.show()
    sys.exit(app.exec_())
