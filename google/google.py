#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from googletrans import Translator
from sys import argv

if __name__ == "__main__":
    word = argv[1]
    word = word.replace("/","／")       # url 方式要过滤掉 / 换成全角 #
    word = word.replace("\n -","")
    word = word.replace("\n-","")
    word = word.replace("\n","")


    ts = Translator(service_urls=['translate.google.cn'])
    print(ts.translate("this is an apple", dest='zh-CN').text)
