# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from .UserConfig import *
from .var import app


def isConfig_NormalSize() -> bool:
    config = QSettings(getConfigPath(), QSettings.IniFormat)
    if str(config.value('win/show_mode')) == 'normal':
        return True
    else:
        return False


def getNormalSize() -> QSize:
    config = QSettings(getConfigPath(), QSettings.IniFormat)
    rate = float(config.value('win/normal_size_rate'))
    dw: QDesktopWidget = app.desktop()
    rect: QRect = dw.availableGeometry()
    size = QSize(int(rect.width() * rate), int(rect.height() * rate))
    return size


def getCenterPos() -> QPoint:
    config = QSettings(getConfigPath(), QSettings.IniFormat)
    rate = float(config.value('win/normal_size_rate'))
    dw: QDesktopWidget = app.desktop()
    rect: QRect = dw.availableGeometry()
    size = QSize(int(rect.width() * rate), int(rect.height() * rate))
    pos = QPoint(int((rect.width() - size.width()) / 2),
                 int((rect.height() - size.height()) / 2))
    return pos
