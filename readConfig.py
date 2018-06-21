#!/usr/bin/python
#coading:utf-8

import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir,"config.ini")

class