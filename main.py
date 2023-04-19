import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import zipfile

class ZipPasswordCracker(QWidget):
    def __init__(self):
        super().__init__()

        # Membuat widget UI
        self.label = QLabel('Masukkan kata sandi file zip:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.button = QPushButton('Buka File Zip')
        self.button.clicked.connect(self.crack_zip)
        
        # Membuat layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def crack_zip(self):
        password = self.password_input.text()

        # Mengambil nama file zip yang ingin dibuka
        zip_filename = 'file.zip'  # Ganti dengan nama file zip yang ingin Anda buka

        try:
            # Membuka file zip dengan kata sandi yang dimasukkan
            with zipfile.ZipFile(zip_filename) as zip_file:
                zip_file.extractall(pwd=password.encode())
            QMessageBox.information(self, 'Berhasil', 'File zip berhasil dibuka!')
        except Exception as e:
            QMessageBox.warning(self, 'Gagal', f'Gagal membuka file zip: {str(e)}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ZipPasswordCracker()
    window.show()
    sys.exit(app.exec_())
