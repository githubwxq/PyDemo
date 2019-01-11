import keyword

import random

import sys

import requests
import firstPython
firstPython.printa()

# import test.firstPython

response=requests.get("http://www.baidu.com")
print(response.text)
def sayHello(number1 ,number2):
    """ dadadsasdfadsfadsf"""
    # print(number1+number2)
    return number1+number2
result=  sayHello(sayHello(10,20),sayHello(10,20))  ;
# print(result)
name_list=["wxq","wxm","qwe","zxc"]
name_list.append("2www")
name_list.append("2ww")
name_list.insert(0,"ddd")
del name_list[1]
print(len(name_list))
name ="wxq"
age=18
address="江苏"
print(name_list)
info_tuple=("zhangsan",180,120)

type(info_tuple)
print(type(name_list))

print(info_tuple[2])

single_type=(11111,)
print(type(single_type))

for   x in info_tuple:
    print( "打印元祖%s,%d,%d" % info_tuple)


# 、、字典 hushmap

xiaoming={
    "name":"wxq",
    "age":18,
    "height":1.75
}

xiaoming2={
    "name":"小清清",
    "age2":28,
    "height2":20
}





xiaoming["aihao"]="打乒乓"

print("name"+xiaoming["name"])

xiaoming.pop("aihao")


xiaoming.update(xiaoming2)


# for item in xiaoming.keys():
#     print(xiaoming.get(item))
#
# for item in xiaoming2:
#     print(xiaoming.get(item))
#
#
#


str1="hello1"

str2="hello2"

for char in str2:
    print(char)

print(char)

