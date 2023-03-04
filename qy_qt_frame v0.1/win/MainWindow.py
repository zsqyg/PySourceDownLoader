# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from .AbstractMainWindow import AbstractMainWindow
from .TitleBar import MWTitleBar
from .ContentWidget import ContentWidget
from ..core.UserConfig import *
from ..core.policy import *


class MainWindow(AbstractMainWindow):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.setupConfig()
        self.setObjectName("MainWindow")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        self.titleBar = MWTitleBar(self)
        self.contentWidget = ContentWidget(self)
        self.mainLayout.addWidget(self.titleBar, alignment=Qt.AlignTop)
        self.mainLayout.addWidget(self.contentWidget, alignment=Qt.AlignBottom)
        self.setLayout(self.mainLayout)
        self.setWindowTitle("QingYang IDE python version")

    def setWindowTitle(self, p_str):
        super().setWindowTitle(p_str)
        self.titleBar.titleLabel.setText(p_str)
