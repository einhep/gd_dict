#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
post 方式提交数据
参考：http://blog.csdn.net/serverxp/article/details/6963059
'''

import urllib, time, random, hashlib, json
from urllib import request
from sys import argv

def getMd5(v):
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8"))
    sign1 = md5.hexdigest()
    return sign1

def getsign(key, salt):
    sign2 = "fanyideskweb" + key + salt + "Tbh5E8=q6U3EXe+&L[4c@"
    sign2 = getMd5(sign2)
    return sign2

if __name__ == "__main__":
    word = argv[1]
    word = word.replace("/","／")       # url 方式要过滤掉 / 换成全角
    word = word.replace("\n -","")
    word = word.replace("\n-","")
    word = word.replace("\n","")
    word = word.replace("- ","")
    word = word.replace("\xe2\x80\x8e", '')  #resovle the Zero-width-space issue
    word = word.replace("\xe2\x80\x8c", '')  # resovle the Zero-width-space issue
    word = word.replace("\xe2\x80\x8d", '')  # resovle the Zero-width-space issue
    d = word
    u = 'fanyideskweb'
    lts = str(round(time.time(), 3)).replace(".", "")
    f = lts + str(random.randint(0, 9))
    data = {
        'i': d,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': u,
        'salt': f,
        "sign": getsign(d, f),
        'lst': lts,
        "bv": 'fc080c3cd240f5000b593381aec25d12',
        ##'sign': sign,
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        #'Accept-Encoding': 'gzip, deflate',   # 注意这一行，如果有这一行，返回的响应是压缩的可能不能正常输出
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '996',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-558886715@10.108.160.19; OUTFOX_SEARCH_USER_ID_NCOO=166980140.2794344; _ntes_nnid=2bb7ce9f0dbc2e9b076181178219e855,1607336314370; JSESSIONID=aaaop-_2Q8j7Chi22fZAx; ___rl__test__cookies=1609322453799',
        'Host': 'fanyi.youdao.com',
        'Origin': 'https://fanyi.youdao.com',
        'Referer': 'https://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    postdata = urllib.parse.urlencode(data)
    postdata = postdata.encode('utf-8')
    #headers = urllib.parse.urlencode(headers)
    #headers = headers.encode('utf-8')  
    req = urllib.request.Request(url, headers=headers)
    res = urllib.request.urlopen(req, data=postdata)

    #print(res.status, 're:',res.reason)  
    json1 = res.read().decode('utf-8', errors='ignore')
    #print(json1)
    obj1 = json.loads(json1)

    # for res in obj1['translateResult'][0]:
    #     print(res['src'])
    for res in obj1['translateResult'][0]:
        print(res['tgt'], end='')