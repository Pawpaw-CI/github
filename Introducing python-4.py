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
#单值真假输入：0,1
#print("请输入：True or False")
#disaster = input()#输入参数：False假，输入数字或布尔值0,1
disaster = 1
if disaster:
    print "正确的选择!"
else:
    print "错误的选择!"
print disaster
#多层嵌套
#双值，4中关系，00,01,10,11
furry = False
small = True

if furry:
    if small:
        print ("11，it's a cat.")
    else:
        print ("10，it' a bear")
else:
    if small:
        print ("01，it's a skink")
    else:
        print ("00，it's a human ,or a hairless bear")

#三个条件以上的判定if\elif \else

color ="puce"
if color == "red":
    print "it's a tomato"
elif color=="green":
    print "it's a grenn pepper"
elif color =="bee purple":
    print "I don't what it is ,but only bees can see it "
else:
    print "I've never heard of the color",color

#4.4 while循环
#从1打印至5
count =1
while count <=5:
    print count
    count +=1

