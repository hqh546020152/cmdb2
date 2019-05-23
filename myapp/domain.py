import json
from urllib import request
import random
import time



#定义要搜索的域名个数
domain_number = 200
#定义域名的长度
domain_len = 5
#定义域名中可出现字符
codeList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


#code
j = 0
while j <= domain_number:
    #在集合中成一个N位的随机数
    randCode=''
    for i in range(domain_len):
        Num = random.randint(0, len(codeList)-1)
        randCode += codeList[Num]
    #打印生成的随机数
    # print(randCode)

    domain=randCode
    url = 'https://whois.ename.net/index.php/ajax/recommendtrans/%s.com' % domain
    req = request.Request(url)
    result = request.urlopen(req)
    response = result.read()
    page = response.decode('utf-8')
    page = json.loads(page)
    result.close()
    #打印请求返回数据
    # print(page)
    register_status = page['data'][domain + '.com']['Code']
    #1表示未注册、0表示已注册
    # print(register_status)


    if register_status == 0 :

        print(domain + '.com' + ' 已被注册')
    else:
        print(domain + '.com' + ' 未注册')
        #win打印到文本中
        # fout = open(r'C:\Users\Administrator\Desktop\domain.txt', 'w+', encoding='utf8')
        # fout.write(domain + '.com' + ' 未注册')
        # fout.write('\n')
        # fout.close()
        j += 1
    #延时2秒，否则会被屏蔽
    time.sleep(2)
