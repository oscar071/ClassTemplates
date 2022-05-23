# ________________________________Instructions_________________________________
"""
                    VARIABLES
DAY:                , example -> 01
MONTH:              , example -> jan
YEAR:               , example -> 2021
CREDITS:            , example -> AvantZen
NAME_FILE:          , example -> worker
NAME_CLASS:         , example -> Worker
PUBLIC_METHOD:      , example -> show_window
PATH_ICON:          , example -> img/.png

                    PROCESS:
01.- Create a file and name it as uifrm/ui.ui in Qt Designer
02.- Rename the window object as  in Qt Designer
03.- Save the window icon image in the directory 
04.- Use the command nameProject>pyside2-uic uifrm/ui.ui > view/ui.py
05.- Check all the class and delete this instructions
"""
# ________________________________Instructions_________________________________
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from config.app import App
from PySide2.QtCore import *
from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtGui import QIcon
from view.ui import Ui_

__email__ = "oscarmtzp93@gmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martinez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "//"

__author__ = "Oscar Martinez"

__credits__ = ""


class Controller(QMainWindow):
    """Class description (DocString)"""

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, parent=None):
        """Method description  (DocString)"""
        super(Controller, self).__init__(parent=parent)

        self.__setup = Ui_()
        self.__setup.setupUi(self)
        self.__design()
        self.__listen_events()

    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Private methods_____________________________

    def __design(self):
        """Create or modify the initial design of the form."""
        icon = QIcon("")
        self.setWindowIcon(icon)

        self.setWindowTitle(QCoreApplication.translate("", App._text[''], None))

    def __listen_events(self):
        """Puts all the events of the form to listen."""
        # self.__setup.spn_origin_x.valueChanged.connect(self.public_method)
        #
        # self.__setup.btn_add.clicked.connect(self.public_method)
        #
        # self.__setup.rdb_speed.clicked.connect(self.public_method)
        #
        # self.__setup.act_open.triggered.connect(self.public_method)
        #
        # self.__setup.txt_search.returnPressed.connect(self.public_method)
        # self.__setup.txt_search.textEdited.connect(self.public_method)
        #
        # self.__setup.ckb_next.stateChanged.connect(self.public_method)
        # self.__setup.cbo_id.currentIndexChanged.connect(self.public_method)
        # self.__setup.sld_size.valueChanged.connect(self.public_method)
        pass

    # _____________________________Private methods_____________________________

    # _____________________________Public methods______________________________

    def closeEvent(self, event):
        """It requests the user's confirmation to close the system."""
        box = QMessageBox(self)
        box.setIcon(QMessageBox.Question)
        box.setWindowTitle(App._text['close_window'])
        box.setText(App._text['msg_close_window'])
        box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        btn_y = box.button(QMessageBox.Yes)
        btn_y.setText(App._text['yes'])
        btn_n = box.button(QMessageBox.No)
        btn_n.setText(App._text['no'])
        box.exec_()

        if box.clickedButton() == btn_y:
            event.accept()
        else:
            event.ignore()

    def (self):
        """Method description (DocString)"""
        pass

    # _____________________________Public methods______________________________
