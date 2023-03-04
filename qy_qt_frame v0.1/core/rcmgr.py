# -*- coding:utf-8 -*-
import os.path

from .var import frame_abs_path
from PyQt5.QtGui import *


def getRC_ICON(name: str) -> QIcon:
    return QIcon(os.path.join(frame_abs_path, 'source/icon/%s.png' % name))
