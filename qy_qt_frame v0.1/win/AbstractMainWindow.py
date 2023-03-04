# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import QWidget
from ..core.UserConfig import *
from ..core.policy import *


class AbstractMainWindow(QWidget):
    def setupConfig(self):
        if isUserConfigNoExist():
            createConfig()
        self.resize(getNormalSize())
        self.move(getCenterPos())

    def show_cfg(self):
        if isConfig_NormalSize():
            self.resize(getNormalSize())
            self.move(getCenterPos())
            self.show()
        else:
            self.showMaximized()
