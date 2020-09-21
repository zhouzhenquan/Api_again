"""
@项目名称 : api_test
@时间 ： 2020 2020/9/4 17:49
@作者 ： 周振全
@文件名 ：Yaml.py
@IDE ：PyCharm

"""
import yaml

f= open(r'D:\python_study\api_test\Config\config.yaml')
data = f.read()
yaml_ = yaml.load(data,Loader=yaml.SafeLoader)
yaml__ = yaml.safe_load(data)


print(yaml_['log']['level'])
print(yaml__['log']['fh_leve'])