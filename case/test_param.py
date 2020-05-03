'''
    参数化组件的使用
    安装：pip install parameterized
    使用：@parameterized.expend(参数)
    参数：单个参数：[value1, value2]
          多个参数：[(value1, value2),(value3, value4)]
'''

#导包
import unittest
from parameterized import parameterized

#新建测试类
class TestPara(unittest.TestCase):
    #新建测试方法
    @parameterized.expand([('10000','Aa123456')])
    def test_para(self, username, password):
        print("用户名：", username)
        print("密码：", password)