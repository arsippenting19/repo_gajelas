import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
import zipfile

class ZipPasswordCracker(QWidget):
    def __init__(self):
        super().__init__()

        # Membuat widget UI
        self.label_wordlist = QLabel('Pilih file wordlist:')
        self.wordlist_input = QLineEdit()
        self.button_browse = QPushButton('Pilih')
        self.button_browse.clicked.connect(self.browse_wordlist)
        self.label_zip = QLabel('Masukkan nama file zip:')
        self.zip_input = QLineEdit()
        self.label_result = QLabel()
        self.button_crack = QPushButton('Coba Buka File Zip')
        self.button_crack.clicked.connect(self.crack_zip)

        # Membuat layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_wordlist)
        layout.addWidget(self.wordlist_input)
        layout.addWidget(self.button_browse)
        layout.addWidget(self.label_zip)
        layout.addWidget(self.zip_input)
        layout.addWidget(self.label_result)
        layout.addWidget(self.button_crack)
        self.setLayout(layout)

    def browse_wordlist(self):
        wordlist_file, _ = QFileDialog.getOpenFileName(self, 'Pilih File Wordlist', '', 'Text Files (*.txt);;All Files (*)')
        self.wordlist_input.setText(wordlist_file)

    def crack_zip(self):
        wordlist_file = self.wordlist_input.text()
        zip_filename = self.zip_input.text()

        try:
            with open(wordlist_file, 'r', encoding='utf-8') as wordlist:
                for password in wordlist:
                    password = password.strip()
                    try:
                        with zipfile.ZipFile(zip_filename) as zip_file:
                            zip_file.extractall(pwd=password.encode())
                            self.label_result.setText(f'Kata sandi berhasil ditemukan: {password}')
                            return
                    except Exception as e:
                        pass
                self.label_result.setText('Kata sandi tidak ditemukan dalam wordlist.')
        except Exception as e:
            QMessageBox.warning(self, 'Gagal', f'Gagal membuka file wordlist: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ZipPasswordCracker()
    window.show()
    sys.exit(app.exec_())
