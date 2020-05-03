import requests

#定义类
class Information_list():
    def get_information_list(self, url, page):
        query = {}

        return requests.get(url, params=query)
