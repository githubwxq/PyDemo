import requests
import json


class Gank:
    def __init__(self):
        self.appinnUrl="http://gank.io/api/xiandu/data/id/appinn/count/{}"+"/page/{}"


        pass



    # 获取最新一天的干货  http://gank.io/api/today
    def getLastTodayData(self):
        response = requests.get("http://gank.io/api/today")
        # print(response.content.decode())
        dict_ret= json.loads(response.content.decode())
        ret=dict_ret["results"]["Android"][0]["who"]
        android=dict_ret["category"][1]
        print(android)


    def saveFile(self, name, htmlStr):
        filePath = "{}数据.json".format(name)
        with open(filePath, "w") as  f:
            f.write(htmlStr)

    def getUrls(self):
        response = requests.get("http://gank.io/api/today")
        print(response.content.decode())


# 例如： http://gank.io/api/xiandu/data/id/appinn/count/10/page/1

    def getappinn(self,page,count):
        url=self.appinnUrl.format(count,page)
        response = requests.get(url)
        self.saveFile(page,response.content.decode())
        print(response.content.decode())




if __name__ == '__main__':
    gankApi = Gank();
    gankApi.getLastTodayData();
    # gankApi.saveFile("wxq", "dddddd");
    for i in range(10):
        gankApi.getappinn(str(i),"10")




