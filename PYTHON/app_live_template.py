# ________________________________Instructions_________________________________
"""
                    VARIABLES
DAY:        , example -> 01
MONTH:      , example -> jan
YEAR:       , example -> 2021
CREDITS:    , example -> AvantZen

                    PROCESS:
01.- Check all the class and delete this instructions
"""
# ________________________________Instructions_________________________________
#!/usr/bin/python3
# -*- coding: utf-8 -*-

__email__ = "oscarmtzp93@gmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martinez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "//"

__author__ = "Oscar Martinez"

__credits__ = ""


class App:
    """Set general application settings."""

    # ____________________________Class attributes_____________________________

    _languages = ['en', 'es']
    _text = dict()
    _name = ''
    _lan = 'en'
    _version = '1.0'

    # ____________________________Class attributes_____________________________

    # ______________________________Class methods______________________________

    @classmethod
    def lan(cls, lan: str) -> None:
        """Sets the application configuration language."""
        App._lan = lan
        App.__private_method()

    @classmethod
    def name(cls, name: str) -> None:
        """Sets the name application."""
        App._name = name

    @classmethod
    def __private_method(cls):
        """Set the app texts"""
        if App._lan == 'en':
            App._text = {
                'roots': App._name,
                'close_root': 'Close program',
                'msg_close_root': 'Do you want to close the program?',
                'yes': 'Yes',
                'no': 'No',
                'close_window': 'Close window',
                'msg_close_window': 'Do you want to close this window?'
            }

        elif App._lan == 'es':
            App._text = {
                'roots': App._name,
                'close_root': 'Cerrar programa',
                'msg_close_root': '¿Quiéres cerrar el programa?',
                'yes': 'Si',
                'no': 'No',
                'close_window': 'Cerrar ventana',
                'msg_close_window': '¿Quiéres cerrar esta ventana?'
            }

    # ______________________________Class methods______________________________

    # ______________________________MAGIC METHODS______________________________

    # _____________________________Generic methods_____________________________

    def __init__(self, name: str):
        """Method description  (DocString)"""
        pass

    def __str__(self):
        """Return the app name
        return App._name"""
        return App._name

    # _____________________________Generic methods_____________________________

    # ______________________________MAGIC METHODS______________________________

    # ______________________________Inner classes______________________________

    class AppError(Exception):
        def __init__(self, msg: str):
            super().__init__(msg)

    # ______________________________Inner classes______________________________


if __name__ == "__main__":
    import doctest
    doctest.testmod()
