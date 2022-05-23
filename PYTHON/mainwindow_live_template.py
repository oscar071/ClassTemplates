# ________________________________Instructions_________________________________
"""
                    VARIABLES
DAY:        $DAY$, example -> 01
MONTH:      $MONTH$, example -> jan
YEAR:       $YEAR$, example -> 2021
CREDITS:    $CREDITS$, example -> AvantZen

                    PROCESS:
01.- Create a Python package and name it model
02.- Create a Python package and name it view
03.- Create a Python package and name it controller
04.- Create a Python package and name it config
05.- Create a Python package and name it uifrm
06.- Create a directory and name it img
07.- Create a file and save it as config/app.py
08.- Use the live template <app> in app.py
09.- Create a file and save it as config/config.py
10.- Use the live template <config> in config.py
11.- Create a file and save it as controller/controllerroot.py
12.- Use the live template <controller> and name it ControllerRoot
13.- Check all the class and delete this instructions
"""
# ________________________________Instructions_________________________________
#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from config.config import run_config
from PySide2.QtWidgets import QApplication
from controller.controllerroot import ControllerRoot

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

