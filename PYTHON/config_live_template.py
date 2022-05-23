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


from config.app import App


def run_config():
    App._name = 'NameApp'
    App.lan('en')
