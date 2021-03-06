import requests
import json
import re

# 导入bmob模块
from bmob import *

class Gank:

    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36",
    }

    def __init__(self):
        self.appinnUrl="http://gank.io/api/xiandu/data/id/appinn/count/{}"+"/page/{}"
        # http://gank.io/api/data/福利/10/1  http://gank.io/api/data/数据类型/请求个数/第几页
        self.dataUrl="http://gank.io/api/data/{}/{}/{}"
        self.parmer=["福利","android","IOS","休息视频"]
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
        filePath = "../data/{}.json".format(name)
        with open(filePath, "w",encoding="utf-8") as  f:
            f.write(htmlStr)


    def saveImage(self, name, htmlStr):
        filePath = "../image/{}".format(name)
        rps=requests.get(htmlStr)
        with open(filePath, "wb") as  f:
            f.write(rps.content)


    def saveVideo(self, name, htmlStr):
        respText = requests.get(htmlStr,headers=self.headers).text
        # playAddressIndex=respText.index("playAddr:")
        # coverIndex=respText.index("cover: ")
        # videoUrl=respText[playAddressIndex+len("playAddr:"):coverIndex].replace(" ","")[1:-3]
        videoList = re.findall(r'playAddr: "(.+?)"', respText)
        if len(videoList) > 0:
            videoContent=requests.get(videoList[0],headers=self.headers).content
            filePath = "../video/{}.mp4".format(name)
            with open(filePath, "wb") as  f:
                f.write(videoContent)


    def getUrls(self):
        response = requests.get("http://gank.io/api/today")
        print(response.content.decode())


# 例如： http://gank.io/api/xiandu/data/id/appinn/count/10/page/1
    def getappinn(self,page,count):
        url=self.appinnUrl.format(count,page)
        response = requests.get(url)
        self.saveFile(page,response.content.decode())
        print(response.content.decode())

# 数据类型： 福利 | Android | iOS | 休息视频 | 拓展资源 | 前端 | all
    def getFuLi(self,type,page,count):
        url=self.dataUrl.format(type,count,page)
        response = requests.get(url)
        self.saveFile(type+page,response.content.decode())
        return json.loads(response.content.decode())





if __name__ == '__main__':
    # gankApi = Gank();
    # gankApi.getLastTodayData();
    # result=gankApi.getFuLi(gankApi.parmer[3],str(3),"10")
    # print( len(result["results"]))
    # for item in result["results"]:
    #     print(item["desc"])
    #     gankApi.saveVideo(item["desc"],item["url"])

    # 新建一个bmob操作对象
    b = Bmob("ea796f59c1a3d4a34f0b18b7626dd291", "6fe04b6e18174dc1fcacae5685c48046")
    # 插入一行数据，原子计数、Pointer
    print(
        b.insert(
            'Feedback', # 表名
            BmobUpdater.increment(
                "count", # 原子计数key
                2, # 原子计数值
                { # 额外信息
                    "content": "测试python",
                    "user": BmobPointer("_User", "0dc0356307"), # Pointer类型
                    "date": BmobDate(1545098009351) ## Date类型
                }
            )
        ).jsonData # 输出json格式的内容
    )

    bmobInsertUrl="https://api2.bmob.cn/1/classes/TableName"





