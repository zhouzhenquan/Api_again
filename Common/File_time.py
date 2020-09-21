"""
@项目名称 : api_test
@时间 ： 2020 2020/9/4 16:52
@作者 ： 周振全
@文件名 ：File_time.py
@IDE ：PyCharm

"""

import time


class File_time_(object):
    def time(self):
        return time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime(time.time()))

File_time = File_time_()
