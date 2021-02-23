# ________________________________Instructions_________________________________
"""
01.- Create a directory and name it Models
02.- Create a directory and name it Views
03.- Create a directory and name it Controllers
04.- Create a directory and name it Config
05.- Create a directory and name it Ui_frms
06.- Create a directory and name it Imgs
07.- Create a file and save it as Config/app.py
08.- Execute the command app in app.py
09.- Create a file and save it as Config/config.py
10.- Execute the command config in config.py
11.- Create a file and save it as Controller/controllerroot.py
12.- Use the live template controller and name it ControllerRoot
13.- Replace jan/01/2021 with date
14.- Check all the class and delete this instructions
"""
# ________________________________Instructions_________________________________
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from Config.config import run_config
from PySide2.QtWidgets import QApplication
from Controllers.controllerroot import ControllerRoot

__email__ = "oscarmtzp93@gmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martinez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "jan/01/2021"

__author__ = "Oscar Martinez"

__credits__ = "AvantZen"


if "__main__" == __name__:
    run_config()
    app = QApplication(sys.argv)
    controller_root = ControllerRoot()
    controller_root.show()
    app.exec_()
