from app.app import App
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow

import logging
import sys

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s][%(levelname)s][%(name)s] %(message)s')

    app = App("config.yaml")
    app.start()

    ui_app = QApplication([])

    window = MainWindow(app.get_controller())
    window.show()

    sys.exit(ui_app.exec_())