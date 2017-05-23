# -*-coding:utf-8-*-
__author__ = "pawpawDu"
# 60 sec/min,60min/hr,24hr/day
#oython外壳：代码结构
import time
print time.timezone
print time.localtime()
alphabet = ""
alphabet +="abdc"
alphabet +="efgj"
print(alphabet)
#使用\连接，仍是一行
alphabet = "abcd"+\
    "efjk"+\
    "QEWQEQ"+\
    "ddf"
print alphabet
#4.3使用if elif else

print("请输入：True or False")
disaster = input()
if disaster:
    print "WW00!"
else:
    print "wjhjj!"
print disaster