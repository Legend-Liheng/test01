'''
    目标：实现登录接口对象层封装
'''

#导包 requests
import requests

#新建类 登录接口对象
class ApiLogin(object):
    #新建方法 登录方法
    #url，uesrname，password，从data中读取
    def api_post_login(self, url, Content, username, password):
        #headers定义
        headers = {'headers':Content}
        #body定义
        body = {"username":username,"password":password}
        #调用方法并返回响应对象
        return requests.post(url, headers=headers, json=body)



