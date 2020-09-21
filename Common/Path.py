
"""
@项目名称 : api_test
@时间 ： 2020 2020/9/4 15:43
@作者 ： 周振全
@文件名 ：Path.py
@IDE ：PyCharm

"""

import os

"""
os.path.dirname  --- 返回文件路径
os.path.abspath  --- 返回绝对路径
os.path.join     --- 路径拼接
"""

"""项目目录路径"""
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""测试模块目录"""
CASEDIR = os.path.join(BASEDIR,"Test_Case")
"""测试数据目录"""
DATADIR = os.path.join(BASEDIR,'Data')
"""测试报告目录"""
REPORTDIR = os.path.join(BASEDIR,'Reports')
"""配置文件目录"""
CONFDIR= os.path.join(BASEDIR,'Config')
"""日志文件目录"""
LOGDIR = os.path.join(BASEDIR,'Log')

