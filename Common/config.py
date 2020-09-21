"""
@项目名称 : api_test
@时间 ： 2020 2020/9/18 20:40
@作者 ： 周振全
@文件名 ：config.py
@IDE ：PyCharm

"""

import os
import yaml
from configparser import ConfigParser
from Common.Path import CONFDIR


class config(ConfigParser):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.read(filename, encoding='utf-8')

    def write_data(self, section, option, content):
        self.set(section, option, content)
        self.write(fp=open(self.filename, "w"))


f = open(CONFDIR + os.sep + 'config.yaml')
data = f.read()
conf = yaml.safe_load(data)
print(conf['log']['level'])
