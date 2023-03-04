# -*- coding:utf-8 -*-
import os.path
import sys

from PyQt5.QtWidgets import QApplication

app: QApplication = QApplication(sys.argv)
frame_abs_path = os.path.abspath(__file__).replace('core\\var.py', '')
