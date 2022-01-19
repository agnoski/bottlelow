from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
import logging

from .run_ui import Ui_runmode_widget


class RunWidget(QWidget, Ui_runmode_widget):
    VAL_INCREASE = 1
    
    signal_max_limit = pyqtSignal(int)
    signal_min_limit = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)

        #init Ui_runmode_widget
        self.setupUi(parent)

        self.logger = logging.getLogger(self.__class__.__name__)

    def _connectSignalSlot(self):
        self.lev_max_plus.clicked.connect(lambda: self._update_max_limit(-self.VAL_INCREASE))
        self.lev_max_minus.clicked.connect(lambda: self._update_max_limit(self.VAL_INCREASE))
        self.lev_min_plus.clicked.connect(lambda: self._update_min_limit(-self.VAL_INCREASE))
        self.lev_min_minus.clicked.connect(lambda: self._update_min_limit(self.VAL_INCREASE))

        self.settingButton.clicked.connect(self._show_settings)
        self.saveButton.clicked.connect(self._save_settings)
        self.cancelButton.clicked.connect(self._cancel_setting)

    def _update_max_limit(self,val):
        self.signal_max_limit.emit(val)

    def _update_min_limit(self,val):
        self.signal_min_limit.emit(val)
    
    def _show_settings(self):
        self.stackedWidget.setCurrentIndex(1)

    def _save_settings(self):
        #update configs
        self.logger.info("Configs updated")
        self.stackedWidget.setCurrentIndex(0)

    def _cancel_setting(self):
        self.stackedWidget.setCurrentIndex(0)