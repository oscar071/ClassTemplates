#!/usr/bin/python3
# -*- coding: utf-8 -*-

__email__ = "oscarmtzp93@gmail.com"
__license__ = "GPL"
__maintainer__ = "Oscar Martinez"
__status__ = "Developing"

__version__ = "1.0"

__date__ = "feb/09/2021"

__author__ = "Oscar Martinez"

__credits__ = "AvantZen"


from Config.app import App

def run_config():
    App._name = 'NameApp'
    App.lan('en')
