#!usr/bin/python
#coading:utf-8

import requests
import readConfig as readConfig
from common.Log import MyLog as log

localReadConfig = readConfig.ReadConfig()

class ConfigHttp:
    def __init__(self):
        global host,port,timeout
        host = localReadConfig.get_http("baseurl1")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self,url):
        self.url = host + url

    def set_headers(self,header):
        self.headers = header

    def set_params(self,param):
        self.params = param

    def set_data(self,data):
        self.data = data

    def set_files(self,file):
        self.files = file

    #defined 

