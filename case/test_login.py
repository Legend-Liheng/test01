'''
    目标：完成登录业务层实现
'''

#导包
import unittest
from api.api_login import ApiLogin
from parameterized import parameterized
# from tool.read_json import read_data
from tool.read_json import ReadJson

def read_data():
    # print(ReadJson('filename').read_json())

    datas = ReadJson('login_more.json').read_json()
     # 新建空列表，添加读取到的json数据
    arrs = []
    for data in datas.values():
        arrs.append((data.get('url'),
                     data.get('Content'),
                     data.get('username'),
                     data.get('password'),
                     data.get('expect_result'),
                     data.get('status_code')))
    return arrs
    print(arrs)
#新建测试类
class TestLogin(unittest.TestCase):
    #新建测试方法
    @parameterized.expand(read_data())
    def test_Login(self, url, Content, username, password, expect_result, status_code):
        #暂时存放数据url,username,password
        # url = "https://test-crmapi.xiaomawang.com/user/index/login"
        # username = '10000'
        # password = 'Aa123456'
        #调用登录方法
        result = ApiLogin().api_post_login(url, Content, username, password)

        #打印响应信息
        print("响应结果为：", result.json())
        print('我执行了1')
        #断言、响应信息及状态码
        # self.assertEqual(20000, result.json()['code'])
        # print('返回结果类型为：', result.json()['code'])

        print(self.assertEqual(expect_result, result.json()['message']))
        print('返回结果为：', result.json()['message'])

        print(self.assertTrue(status_code, result.status_code))
        print('状态码为：', result.status_code)


    print('我执行了2')
print('我执行了3')
if __name__ == '__main__':
    unittest.main()

print('我执行了4')
