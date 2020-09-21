"""
@项目名称 : api_test
@时间 ： 2020 2020/9/4 14:56
@作者 ： 周振全
@文件名 ：ReadExcel.py
@IDE ：PyCharm

"""

import openpyxl


class read_excel(object):
    def __init__(self, Filename, Sheetname):
        self.Filename = Filename
        self.Sheetname = Sheetname

    """选择打开excel"""
    def open_excel(self):
        self.wb = openpyxl.load_workbook(self.Filename) # 选择工作簿
        self.sh = self.wb[self.Sheetname]   # 选择表单名

    """读数据"""
    def read_excel(self):
        self.open_excel()
        data = list(self.sh.rows)
        li = [i.value for i in data[0]] # 这是Excel的第一行数据
        cases = [] # 遍历除第一行以外的数据

        for i in data[1:]:
            """
            读取该行数据的值，与第一行数据进行打包处理，后转化为字典
            将字典添加到列表中
            随后返回整个列表
            """
            values = [c.value for c in i ]
            case = dict(zip(li,values))
            cases.append(case)
        return cases

    """写数据"""
    def writer_excel(self,row,column,value):
        self.open_excel()
        """
        打开文件
        按着 行 列 写入 数据
        保存文件
        """
        self.sh.cell(row=row,column=column,value=value)
        self.wb.save(self.Filename)
