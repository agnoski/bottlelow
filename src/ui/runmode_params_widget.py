from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal
from .runmode_params_form import Ui_runmode_params_widget

class RunmodeParamsWidget(QWidget, Ui_runmode_params_widget):
    VAL_INCREASE = 1
    
    signal_max_limit = pyqtSignal(int)
    signal_min_limit = pyqtSignal(int)

    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self._connectSignalSlot()

    def _connectSignalSlot(self):
        self.lev_max_plus.clicked.connect(lambda: self._update_max_limit(-self.VAL_INCREASE))
        self.lev_max_minus.clicked.connect(lambda: self._update_max_limit(self.VAL_INCREASE))
        self.lev_min_plus.clicked.connect(lambda: self._update_min_limit(-self.VAL_INCREASE))
        self.lev_min_minus.clicked.connect(lambda: self._update_min_limit(self.VAL_INCREASE))

    def _update_max_limit(self,val):
        self.signal_max_limit.emit(val)

    def _update_min_limit(self,val):
        self.signal_min_limit.emit(val)



    