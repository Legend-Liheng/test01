#导包 json
import json

#打开json文件并且获取文件流
# file_content = open('../data/login.json', mode='r', encoding='UTF-8')
# print('file_content内容为：', file_content)
#
# data = json.load(file_content)#调用load方法加载数据流
# print('data内容为：', data)

#封装成函数
# def read_json():
#     file_content = open('../data/login.json')
#
#     return  json.load(file_content)

#封装成方法
class ReadJson():
    def __init__(self, filename):
        self.filepath = '../data/' + filename
        # print(self.filepath)

    def read_json(self):
        file_content = open(self.filepath, mode='r', encoding='UTF-8')
        # print(json.load(self.file_content))
        return  json.load(file_content)

        # print(json.load(self.file_content))



if __name__ == '__main__':
    # print(ReadJson('login_more.json').read_json())
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
    # print(datas)
    print(arrs)