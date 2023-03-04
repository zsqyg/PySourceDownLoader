# -*- coding:utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from .AbstractMainWindow import AbstractMainWindow
from .ui.TitleBar_ui import Ui_TB
from ..core.rcmgr import *
from ..core.UserConfig import getConfigPath, getThemeInt


class MWTitleBar(QWidget, Ui_TB):

    def __init__(self, parent: AbstractMainWindow):
        super(QWidget, self).__init__(parent)
        self._mw = parent
        self.setupUi(self)
        self._color = ''
        self.changeColorTheme(getThemeInt())
        self._isPress: bool = False
        self._lastPos: QPoint = QPoint()
        self.closeBtn.clicked.connect(self._mw.close)
        self.sizeBtn.clicked.connect(self._sizeBtn_clicked_)
        self.minBtn.clicked.connect(self._mw.showMinimized)

    def _sizeBtn_clicked_(self):
        config = QSettings(getConfigPath(), QSettings.IniFormat)
        if self._mw.isMaximized():
            self._mw.showNormal()
            self.sizeBtn.setIcon(getRC_ICON(f'max_radius_{self._color}'))
            config.setValue('win/show_mode', 'normal')
        else:
            self._mw.showMaximized()
            self.sizeBtn.setIcon(getRC_ICON(f'normal_radius_{self._color}'))
            config.setValue('win/show_mode', 'max')

    def changeColorTheme(self, ct: int):
        self._color = 'white' if ct == 0 else 'black'
        self.closeBtn.setIcon(getRC_ICON(f'close_radius_{self._color}'))
        if self._mw.isMaximized():
            self.sizeBtn.setIcon(getRC_ICON(f'normal_radius_{self._color}'))
        else:
            self.sizeBtn.setIcon(getRC_ICON(f'max_radius_{self._color}'))
        self.minBtn.setIcon(getRC_ICON(f'min_radius_{self._color}'))
        self.toolBtn.setIcon(getRC_ICON(f'cho_radius_{self._color}'))
        self.setStyleSheet('''
        QWidget{
            border: none;
            background-color: #303030;
            color: #ffffff;
            font-family: Microsoft YaHei;
            font-size: 12fp;
            font-weight: bold;
            }
        QPushButton#closeBtn:hover{background-color: #ff2020;}
        QPushButton#sizeBtn:hover{background-color: #50607f;}
        QPushButton#minBtn:hover{background-color: #50607f;}
        QToolButton#toolBtn:hover{background-color: #50607f;}
        %s''' if self._color == 'white' else '''
        QWidget{
            border: none;
            background-color: #eeeeee;
            color: #202020;
            font-family: Microsoft YaHei;
            font-size: 12fp;
            font-weight: bold;
            }
        QPushButton#closeBtn:hover{background-color: #ff3f3f;}
        QPushButton#sizeBtn:hover{background-color: #aaaaff;}
        QPushButton#minBtn:hover{background-color: #aaaaff;}
        QToolButton#toolBtn:hover{background-color: #aaaaff;}
        %s''')

    def mousePressEvent(self, m: QMoveEvent):
        self._isPress = True
        self._lastPos = m.pos()

    def mouseMoveEvent(self, m: QMoveEvent):
        if self._isPress:
            self._mw.move(self._mw.pos() + (m.pos() - self._lastPos))

    def mouseReleaseEvent(self, m: QMoveEvent):
        self._isPress = False
        if self._mw.y() < 0:
            self._mw.move(self._mw.x(), 0)

class TitleBar(QWidget, Ui_TB):
    def __init__(self, parent: QWidget):
        super(QWidget, self).__init__(parent)
        self._parent = parent
        self.setupUi(self)
        self._color = ''
        self.changeColorTheme(getThemeInt())
        self._isPress: bool = False
        self._lastPos: QPoint = QPoint()
        self.closeBtn.clicked.connect(self._parent.close)
        self.sizeBtn.clicked.connect(self._sizeBtn_clicked_)
        self.minBtn.clicked.connect(self._parent.showMinimized)

    def _sizeBtn_clicked_(self):
        config = QSettings(getConfigPath(), QSettings.IniFormat)
        if self._parent.isMaximized():
            self._parent.showNormal()
            self.sizeBtn.setIcon(getRC_ICON(f'max_radius_{self._color}'))
            config.setValue('win/show_mode', 'normal')
        else:
            self._parent.showMaximized()
            self.sizeBtn.setIcon(getRC_ICON(f'normal_radius_{self._color}'))
            config.setValue('win/show_mode', 'max')

    def changeColorTheme(self, ct: int):
        self._color = 'white' if ct == 0 else 'black'
        self.closeBtn.setIcon(getRC_ICON(f'close_radius_{self._color}'))
        if self._parent.isMaximized():
            self.sizeBtn.setIcon(getRC_ICON(f'normal_radius_{self._color}'))
        else:
            self.sizeBtn.setIcon(getRC_ICON(f'max_radius_{self._color}'))
        self.minBtn.setIcon(getRC_ICON(f'min_radius_{self._color}'))
        self.toolBtn.setIcon(getRC_ICON(f'cho_radius_{self._color}'))
        self.setStyleSheet('''
        QWidget{
            border: none;
            background-color: #303030;
            color: #ffffff;
            font-family: Microsoft YaHei;
            font-size: 12fp;
            font-weight: bold;
            }
        QPushButton#closeBtn:hover{background-color: #ff2020;}
        QPushButton#sizeBtn:hover{background-color: #50607f;}
        QPushButton#minBtn:hover{background-color: #50607f;}
        QToolButton#toolBtn:hover{background-color: #50607f;}
        %s''' if self._color == 'white' else '''
        QWidget{
            border: none;
            background-color: #eeeeee;
            color: #202020;
            font-family: Microsoft YaHei;
            font-size: 12fp;
            font-weight: bold;
            }
        QPushButton#closeBtn:hover{background-color: #ff3f3f;}
        QPushButton#sizeBtn:hover{background-color: #aaaaff;}
        QPushButton#minBtn:hover{background-color: #aaaaff;}
        QToolButton#toolBtn:hover{background-color: #aaaaff;}
        %s''')

    def mousePressEvent(self, m: QMoveEvent):
        self._isPress = True
        self._lastPos = m.pos()

    def mouseMoveEvent(self, m: QMoveEvent):
        if self._isPress:
            self._parent.move(self._parent.pos() + (m.pos() - self._lastPos))

    def mouseReleaseEvent(self, m: QMoveEvent):
        self._isPress = False
        if self._parent.y() < 0:
            self._parent.move(self._parent.x(), 0)
