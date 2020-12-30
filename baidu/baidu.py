#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import argv
import requests
import json
import execjs

class BaiduFanyi(object):
    def __init__(self):
        self.s = requests.Session()
        self.request_url ='https://fanyi.baidu.com'
        self.post_url = 'https://fanyi.baidu.com/v2transapi'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
            'origin': 'https://fanyi.baidu.com',
            'referer': 'https://fanyi.baidu.com/',
            'cookie': 'BIDUPSID=EC93DCCEEDD6959BE366802A2B7E5FDF; PSTM=1587979706; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=EC93DCCEEDD6959BB9FB815E94E3121B:SL=0:NR=10:FG=1; MCITY=-131%3A; __yjs_duid=1_87689ab8977348e26ae2c055a5bde4571608799069509; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=EC93DCCEEDD6959BB9FB815E94E3121B:SL=0:NR=10:FG=1; H_PS_PSSID=33425_1424_33420_33306_33256_31254_32973_33284_33351_33313_33347_33312_33311_33310_33274_33413_33309_26350_33308_33307_33389_33385_33370; delPer=0; PSINO=2; BA_HECTOR=8ha521ah010k81209r1fuoodd0r; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1608612715,1608696894,1608870118,1609328401; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1609328401; ab_sr=1.0.0_MmQzOThiMmJlOTFjMWU4ZDE2Nzc1ZDRlYWUxYWM2NGFjNjU5YmU5N2Y2ZDc4ZjgwYmNhM2QzNDY2ZTU4Y2UwN2NhZjdjNDQ1N2UwMDI3Nzc4MTg2ZjVkMWQyODRmOTcy; __yjsv5_shitong=1.0_7_a299f4338b94aacb05298ee9dff7b36192f9_300_1609328401303_114.247.56.202_e044ddad; yjs_js_security_passport=b3ea7ae9bf32fe1b41d850ad70fd602d967b3a19_1609328403_js',
        }
        self.formdata = {
            'from': 'en',
            'to': 'zh',
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'token': 'e456f0f59cb1251bcef0a3d36fac9678',
        }
    def get_sign(self, word):    # 获取签名
        with open('/home/einhep/Tools/gd_plugin/baidu/baidu.js') as f:
            js = f.read()
        sign = execjs.compile(js).call('e', word)
        return sign
    def get_page(self, sign, word):    # 请求网页
        self.formdata['query'] = word
        self.formdata['sign'] = sign
        r = self.s.post(url=self.post_url, headers=self.headers, data=self.formdata)
        if r.status_code == 200:
            return r.text.encode('utf-8').decode('unicode_escape')
    def parse_page(self, html):    # 解析数据
        data = json.loads(html)
        data = data['trans_result']['data'][0]['dst']
        print(data)


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
    baidufanyi = BaiduFanyi()
    sign = baidufanyi.get_sign(d)
    html = baidufanyi.get_page(sign, d)
    baidufanyi.parse_page(html)
