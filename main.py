import sys
from UI.Setting.index import Ui_Setting
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Ui_Setting()
    ui.show()
    sys.exit(app.exec_())

