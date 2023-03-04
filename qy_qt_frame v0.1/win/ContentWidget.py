# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from .AbstractContent import AbstractContent


class ContentWidget(AbstractContent):
    def __init__(self, parent: QWidget):
        super(QWidget, self).__init__(parent)
