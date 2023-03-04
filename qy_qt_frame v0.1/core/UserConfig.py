# -*- coding:utf-8 -*-
import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from .var import frame_abs_path


def getConfigPath() -> str:
    return os.path.join(frame_abs_path, 'config.ini')


def isUserConfigNoExist() -> bool:
    if os.path.exists(getConfigPath()):
        return False
    else:
        return True


def createConfig():
    if isUserConfigNoExist():
        config = QSettings(getConfigPath(), QSettings.IniFormat)
        config.setValue('win/show_mode', 'normal')
        config.setValue('win/normal_size_rate', 0.8)
        config.setValue('win/theme', 'black')


def getThemeInt() -> int:
    config = QSettings(getConfigPath(), QSettings.IniFormat)
    if config.value('win/theme') == 'black':
        return 0
    else:
        return 1
