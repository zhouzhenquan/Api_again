"""
@项目名称 : api_test
@时间 ： 2020 2020/9/4 15:14
@作者 ： 周振全
@文件名 ：excel.py
@IDE ：PyCharm

"""

import openpyxl

# 打开Excel
wb = openpyxl.load_workbook(r"D:\python_study\api_test\复习\test.xlsx")
# 选择表单
sh = wb["测试"]

# 获取所有表单数据
datas = list(sh.rows)
# 获取第一行数据
li1 = [i.value for i in datas[0]]

# 获取第二行数据
li2 = [i.value for i in datas[1]]

li3 = [i.value for i in datas[2]]

data = dict(zip(li1,li2))
data2 = dict(zip(li1,li3))
print(li1)
print(data)
print(data2)