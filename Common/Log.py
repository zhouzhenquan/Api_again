"""
@项目名称 : api_test
@时间 ： 2020 2020/9/4 16:59
@作者 ： 周振全
@文件名 ：Log.py
@IDE ：PyCharm

"""

import os
import logging
from Common.config import conf
from Common.Path import LOGDIR


class My_Log(object):

    @staticmethod
    def My_log():
        # 创建收集器
        mylog = logging.getLogger('zzq')
        mylog.setLevel(conf['log', 'level'])

        # 控制台
        sh = logging.StreamHandler()
        sh.setLevel(conf['log', 'sh_level'])
        mylog.addHandler(sh)

        # 文件
        fh = logging.FileHandler(filename=os.path.join(LOGDIR, "log.log"), encoding='utf-8') #生成的指定路径
        fh.setLevel(conf['log', 'fh_level'])
        mylog.addHandler(fh)

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息：%(message)s')
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        return mylog


log = My_Log.My_log()