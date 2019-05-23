import random

#基础对象操作
i=[1,2,3,4,1,1]
i[0],i[1] = i[1],i[0]
i.append(5)
i.insert(4,8)   #插入一个元素 参数一：index位置 参数二：object
j = i.copy()
i.clear()
print(j.pop(),"删除最后一个值，并打印出来，可指定索引进行删除")
print(j.count(1),"给出1出现的次数")
print(j.remove(2),"删除指定值，左边优先")
print(j.reverse(),"当前列表进行翻转")
print(j.sort(),"列表排序")
print(j.sort(reverse=True),"列表排序，倒序")
print(j.index(3),"打印第N个索引的值")
print("序列正常如下操作")
print(len(j),"打印出列表中的个数")
print(min(j),"打印列表中最小数")
print(max(j),"打印列表中最大数")
print(i,j,"以上为列表常用操作方法")

t1 = ( 5, 8, 24)
t2 = ( 4, 15, 43)
t3 = 5
print( t1 + t2 ,"两个元组相加")
print( t3 in t1 , "t3是否属于t1"  )
print( t3 in t2 , "t3是否属于t2"  )
print(list(t1), "元组转化为列表" , "以上为元组常用操作方法")

d1 = { 'x' : 1, 'y' : [5,8,9] , 'h' : "heihei" }
d2 = d1.copy()
print(d2.get('y') ,"获取字典中某个key的值,没有该key则返回None")
print(d2.get('z','haha') ,"获取字典中某个key的值,没有该key则返回给定字符")
print(d2.keys(),"获取所有key的值")
print(d2.values(),"获取所有value的值")
d2['x'] = 5     #修改key的value值
print(d2.pop('h') , "删除指定keys，将会打印相应的value")
print(d2.popitem(), "随机删除一个" )
d2.clear()      #清除字典
print(d1.items(),"转化成一个伪列表","以上为字典常用操作")

s1 = {'2','4','5','7'}
s2 = {'1','8','5','9'}
a = '4'
print(list(s1),"集合转化为列表")
print( s1 & s2 ,"交集")
print( s1 | s2 ,"并集")
print( s1 - s2 ,"补集")
print( s1 ^ s2 ,"对称补集")
print( s1 < s2 ,"子集，False s1 不是 s2 的子集")
print( a in s1 ,"表示a属于s1")
print( a not in s1 ,"表示a不属于s2")
s1.add('12')    #添加
s1.pop()        #随机删除
print(s1,len(s1),max(s1),min(s1),any(s1),all(s1),"以上为集合常用操作")

b = 5
c = 12
d = b
L2 = [1,4,6,8,7]
print( b + c ,c - b , b * c , b / c )       #计算运算
print( c % b )                              #取模
print( True or False , True and False ,  not True ) #逻辑运算
print( b in L2 , c in L2 , b not in L2 )    #成员关系运算
print( b is c , b is d )                    #对象实例测试
print( b == c , b > c , d <= b, b != c )    #比较运算

#if、for、while
if c >= b :
    print("good")
elif b == c :
    print("to")
else:
    print("pass")
# 1、任何非0数字和非空对象都为真；
# 2、数字0、空对象和特殊对象None均为假；
# 3、比较和相等测试会递归地应用于数据结构中；
# 4、返回值为True或False;

print(b) if b < c else print(c)

for k in range(2,6):
    if k == 3:
        continue
    else:
        print(k)

print(  [ x**2 for x in range(9)]  )

while b < c:
    b = b + 1
    if b == 10 :
        break
    else:
        print(b)
else:
    pass
#基础排序算法
    #冒泡排序
items = [2, 1, 9, 11, 10, 8, 7, 15]
for i in range(len(items) - 1):
    for j in range(len(items) - 1 - i):
        print(i,j)
        if items[j] > items[j + 1]:
            items[j], items[j + 1] = items[j + 1], items[j]
            print(items)
print(items)

    #顺丰面试题，取序列排序后的中位数
if len(items) % 2 == 1:
    print( items[( len(items) - 1 ) // 2]  )
else:
    print( items[(len(items)) // 2 - 1 ] , items[(len(items)) // 2 ])


#接口调用---查看某个域名是否已被注册
import json
from urllib import request
# domain='baidu'
# url = 'https://whois.ename.net/index.php/ajax/recommendtrans/%s.com' % domain   #url
# req = request.Request(url)          #发起请求，并保持返回对象保持到变量中
#     # request.Request(url, header, data)    #可详明请求地址,请求头，请求参数
# result = request.urlopen(req)       #从内存地址中获取该信息
# response = result.read()            #读取返回信息，此时还未解码
# page = response.decode('utf-8')     #对获取到的数据进行解码
# page = json.loads(page)             #将解码数据转化为json格式
# result.close()                      #主动关闭连接
# register_status = page['data'][domain + '.com']['Code']  #从json中获取具体的数据
# #1表示未注册、0表示已注册
# print(register_status)
# #时间操作
# import time
# time.sleep(2)               #延时2秒，否则会被屏蔽
# print( time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) )   #获取当前时间

#定义类与方式、并实现调用、匿名函数
class Zabbix():
    #参数初始化
    def __init__(self):
        #配置Zabbix
        self.ZABBIX_URL = "http://zabbix.mabeyx.com"
        self.ZABBIX_USERNAME = "admin"
        self.ZABBIX_PASSWORD = "C7waCW659bgoPqiQsV5p"

        self.url = "{}/api_jsonrpc.php".format(self.ZABBIX_URL)
        self.header = {"Content-Type": "application/json"}
        self.authID = self.User_login()
    #相同操作抽取为一个函数，减少代码冗余
    def RequestFun(self,data):
        value = json.dumps(data).encode('utf-8')
        req = request.Request(self.url, headers=self.header, data=value)
        try:
            result = request.urlopen(req)
        except Exception as e:
            print("Auth Failed, Please Check Your Name And Password:", e)
        else:
            response = result.read()
            page = response.decode('utf-8')
            page = json.loads(page)
            result.close()
            return page
    # 操作接口、获取auth认证信息
    def User_login(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.ZABBIX_USERNAME,
                "password": self.ZABBIX_PASSWORD
            },
            "id": 1,
        }
        message = self.RequestFun(data)
        #获取返回信息，并将auto值提取出来，作为返回结果
        return message.get('result')
    def Get_data(self):
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": [
                    "hostid",
                    "host"
                ],
                "selectInterfaces": [
                    "interfaceid",
                    "ip"
                ]
            },
            "id": 2,
            "auth": self.authID
        }
        message = self.RequestFun(data)
        return message.get('result')

x = Zabbix()    #实例化类
length = len(x.Get_data())  #使用类中的方法
context = {'status': 1, 'messages': x.Get_data(), 'length' : length }
print( context )
#返回http数据
# from django.http import JsonResponse
# return JsonResponse(context)

#文件操作
import os
f = open( r"C:\Users\Administrator\Desktop\cmdb\myapp\base.txt" , 'r+')
print(f.read())
f.close()

f = open( r"C:\Users\Administrator\Desktop\cmdb\myapp\base.txt" , 'r+')
print(f.readline())     #打印一行数据
print(f.tell())         #打印目前文件指针的位置
print(f.flush())        #用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件,一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法
print(f.seek(0))        #将文件指针指向起始位置
print(f.readline())
f.close()               #关闭文件，将缓存区内容写入磁盘。

#创建文件或追加内容。
f = open( r"C:\Users\Administrator\Desktop\cmdb\myapp\base.txt" , 'a')
f.write("\n1011123")
f.close()

#创建文件或写入数据并原有覆盖内容
# f = open( r"C:\Users\Administrator\Desktop\cmdb\myapp\base.txt" , 'w')
# f.write("1011123")
# f.close()

#异常捕获
try:
    pass
    print("没异常就执行这里")
except KeyError:
    pass
    print("捕获到EeyError异常就执行这里")


#数据库操作


#主要模块使用


#高级算法使用






