import sys
import hashlib
import pyaes
from gui.gui import Ui_Form
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QInputDialog, QApplication
from PyQt5 import uic
        
        
def not_empty_decorator(obj_dict):
    attributes = ["text", "toPlainText"]
    def wrapper(method):
        def _wrapper(self, *args, **kwargs):
            for obj_name, field_name in obj_dict.items():
                obj = getattr(self, obj_name)
                if not any(getattr(obj, attr, lambda: "")() for attr in attributes):
                    msg = "{} field cannot be empty.".format(field_name).capitalize()
                    return QMessageBox.information(self, 'Secret editor', msg, QMessageBox.Ok)
            return method(self, *args, **kwargs)
        return _wrapper
    return wrapper
    

class MainWindow(QWidget, Ui_Form):
    """
    QTextEdit: teContent
    QPushButton: pbOpen
    QPushButton: pbSave
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pbOpen.clicked.connect(self.open_secret)
        self.pbSave.clicked.connect(self.save_secret)
        self.file_dialog = QFileDialog()
        self.file_dialog.setDefaultSuffix(".sk")
        self.show()
        self.init_open()
    
    def init_open(self):
        if len(sys.argv) > 1:
            filepath = sys.argv[1]
            self.load_file(filepath)
        
    def open_secret(self, checked):
        filepath = self.file_dialog.getOpenFileName(self, "Open file", "", "Secret text files (*.sk)")
        
        if filepath:
            self.load_file(filepath)
  
    def load_file(self, filepath):
        try:
            with open(filepath, "rb") as file:
                content = file.read()
            if content[0] == 0:
                text = content[1:].decode()
            else:
                psw, ok = QInputDialog.getText(self, 'File protection', 'This file is protected, please enter password:')
                if ok:
                    key = hashlib.sha256(psw.encode()).digest()
                    aes = pyaes.AESModeOfOperationCTR(key)
                    text = aes.decrypt(content[1:]).decode()
                else:
                    return
                
        except UnicodeError:
            QMessageBox.information(self, 'Open secret', "Invalid file format or password.", QMessageBox.Ok)
       
        except Exception as e:
            QMessageBox.information(self, 'Open secret', str(e), QMessageBox.Ok)
        
        else:
            self.teContent.setPlainText(text)
            QMessageBox.information(self, 'Open secret', "Secret successfully loaded.", QMessageBox.Ok) 
    
    
    @not_empty_decorator({"teContent": "text"})
    def save_secret(self, checked):
        psw, ok = QInputDialog.getText(self, 'File protection', 'If you want to protect this file, please enter a password. Otherwise leave it blank.')
    
        if not ok:
            return
            
        try:    
            filepath, filetype = QFileDialog.getSaveFileName(self, "Save file", "", "Secret text files (*.sk)")
            if not filepath:
                return
            text = self.teContent.toPlainText()
            if psw == "":
                ciphertext = b"\x00" + text.encode()
            else:
                key = hashlib.sha256(psw.encode()).digest()
                aes = pyaes.AESModeOfOperationCTR(key)
                ciphertext = b"\x01" + aes.encrypt(text.encode())
            with open(filepath, "wb") as file:
                file.write(ciphertext)
                
        except Exception as e:
            QMessageBox.information(self, 'Save secret', str(e), QMessageBox.Ok)
            
        else:
            QMessageBox.information(self, 'Save secret', "Secret successfully stored.", QMessageBox.Ok)

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())