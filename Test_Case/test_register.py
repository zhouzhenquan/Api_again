"""
@项目名称 : api_test
@时间 ： 2020 2020/9/4 14:48
@作者 ： 周振全
@文件名 ：test_register.py
@IDE ：PyCharm

"""

"""
注册用例
"""
import os
import unittest
from Library.ddt import data, ddt
from Common.ReadExcel import read_excel
from Common.Path import DATADIR
from Common.Log import log
from register import register

file_name = os.path.join(DATADIR, "apicases.xlsx")


@ddt
class TestRegister(unittest.TestCase):
    excel = read_excel(file_name, "register")
    cases = excel.read_excel()

    @data(*cases)
    def test_register(self, case):

        """准备数据"""
        data = eval(case["data"])
        row = case["case_id"]+1

        """实际结果"""
        res = register(*data)

        """预期结果"""
        expected = eval(case["expected"])

        """断言"""
        try:
            self.assertAlmostEqual(expected,res)
        except Exception as e:
            self.excel.writer_excel(row=row,column=5,value="未通过")
        else:
            self.excel.writer_excel(row=row, column=5, value="通过")
