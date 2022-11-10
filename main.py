import random
import form
import sys
from PyQt5 import QtWidgets


class ExampleApp(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.action_2.triggered.connect(self.open_file)
        self.action.triggered.connect(self.browse_folder)
        self.pushButton.clicked.connect(self.generate_keys)
        self.pushButton_2.clicked.connect(self.encrypt_text)
        self.pushButton_3.clicked.connect(self.decrypt_text)

    def open_file(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        text_file = open(file[0], "r")
        self.lineEdit.setText(text_file.read())
        text_file.close()

    def browse_folder(self):
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        text_file = open(file[0], "w")
        text_file.write(self.lineEdit.text())
        text_file.close()

    def generate_keys(self):
        while True:
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
        for i, word in enumerate(self.textEdit.toPlainText()):
            message += list(word)

        message_ord = []
        for i, letter in enumerate(message):
            message_ord.append(ord(letter))

        for sim in message_ord:
            self.textEdit_2.insertPlainText(f'{str(sim ** int(self.lineEdit_6.text()) % int(self.lineEdit_5.text()))} ')
        return 1

    def decrypt_text(self):
        self.textEdit_4.setText('')
        for sim in self.textEdit_3.toPlainText().split():
            sim = sim if sim[-1] != ',' else sim[:-1]
            self.textEdit_4.insertPlainText(chr(int(sim) ** int(self.lineEdit_8.text()) % int(self.lineEdit_7.text())))
        return 1


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.setFixedSize(392, 803)
    window.show()
    sys.exit(app.exec_())


# clear = lambda: os.system('cls')
# def gen_easy_num(eas_m):
#     num_i = random.randint(0, len(eas_m))
#     return eas_m[num_i]
#
#
# def encrypt_with_key(message_inp, open_exp, open_key):
#     message = []
#     for i, word in enumerate(message_inp):
#         message += list(word)
#
#     message_ord = []
#     for i, letter in enumerate(message):
#         message_ord.append(ord(letter))
#
#     encrypted_message = []
#     for sim in message_ord:
#         encrypted_message.append(sim ** open_exp % open_key)
#     return encrypted_message
#
#
# def decrypt(encrypted_msg, private_k, open_k):
#     decrypted_message = []
#     for sim in encrypted_msg:
#         decrypted_message.append(chr(sim ** int(private_k) % open_k))
#     r = f'Decrypted message: {decrypted_message}'
#     return r
#
#
# eas = []
# for num in range(100, 264):
#     i = 2
#     while i < num:
#         if num % i == 0:
#             break
#         i += 1
#     else:
#         eas.append(num)
# clear()
# MainWindow()
# while True:
#     try:
#         choice = int(input('1 - Encrypt message\n2 - Decrypt message\n3 - Generate keys\n\n0 - Exit\n\nYour choice: '))
#     except Exception as e:
#         clear()
#         continue
#     match choice:
#         case 1:
#             clear()
#             message_input = input('Enter message: ')
#             open_exp = int(input('Enter open_exp: '))
#             open_key = int(input('Enter open_key: '))
#             clear()
#             print(*encrypt_with_key(message_input, open_exp, open_key))
#             print()
#         case 2:
#             clear()
#             encrypted_message = list(map(int, input('Enter encrypted message: ').split()))
#             private_key = int(input('Enter private_key: '))
#             open_key = int(input('Enter open_key: '))
#             clear()
#             print(decrypt(encrypted_message, private_key, open_key))
#             print()
#         case 3:
#             clear()
#             while True:
#                 easy_num1, easy_num2 = gen_easy_num(eas), gen_easy_num(eas)
#                 private_key = 1
#                 open_exp = 1
#                 open_key = easy_num1 * easy_num2
#                 functionEller = (easy_num1 - 1) * (easy_num2 - 1)
#
#                 for i in range(1, 100):
#                     if functionEller % i != 0:
#                         open_exp = i
#                         break
#
#                 for k in range(100):
#                     if (functionEller * k + 1) / open_exp * 10 % 10 == 0:
#                         private_key = (functionEller * k + 1) / open_exp
#                         break
#
#                 if private_key > 1 and easy_num1 != easy_num2:
#                     break
#
#             print(f'Easy nums: {easy_num1} {easy_num2}')
#             print(f'Public key: {open_key} {open_exp}')
#             print(f'Private key: {int(private_key)}')
#             print()
#         case 0:
#             clear()
#             break
