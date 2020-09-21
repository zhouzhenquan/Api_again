"""
@项目名称 : api_test
@时间 ： 2020 2020/9/4 16:46
@作者 ： 周振全
@文件名 ：Run.py
@IDE ：PyCharm

"""

import unittest
from Common.Path import CASEDIR, REPORTDIR
from BeautifulReport import BeautifulReport
from Common.File_time import File_time

# 创建套件
suite = unittest.TestSuite()
# 加载套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR))

br = BeautifulReport(suite)
br.report("测试报告", filename=File_time.time() + 'report.html', report_dir=REPORTDIR,theme='theme_candy')
