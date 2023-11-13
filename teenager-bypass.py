import hashlib
import urllib.parse
import json
import requests
import time
import urllib
import random
import string
import uuid
import re
import base64

class Config:
    # 创建一个类属性来存储header
    header = None
    def __init__(self, cid=44):
        self.cid = cid
        self.appkey = "1d8b6e7d45233436"
        self.appsec = "560c52ccd288fed045859ed18bffd973"
        self.header = self.generate_header()          

    def generate_header(self):
        """生成请求头，以下这些是你需要填的"""
        header = {
            "Buvid": "1",
            "user-agent": "ua",
            "Device-Id": "",
            "Fp_local": "",
            "Fp_remote": "",
            "Session_id": "", 
            "Connection": "close"
        }
        return header
        
def appsign(params, appkey, appsec):
    """生成app签名"""
    params.update({'appkey': appkey})
    params = dict(sorted(params.items()))
    query = urllib.parse.urlencode(params)
    sign = hashlib.md5((query + appsec).encode()).hexdigest()
    params.update({'sign': sign})
    return params
    

url = "https://app.biliapi.net/x/v2/account/teenagers/update"
url_1 = "https://app.biliapi.com/x/v2/account/teenagers/update"
data = {
    "access_key": "你的key",#要改
    "appkey": "1d8b6e7d45233436",
    "build": "6270200",
    "c_locale": "zh_CN",
    "channel": "yingyongbao",#要改
    "device_model": "samsung%7CSM-G955N",#要改
    "mobi_app": "android",
    "platform": "android",
    "pwd": "", 
    "s_locale": "zh_CN",
    "statistics": "%7B%22appId%22%3A1%2C%22platform%22%3A3%2C%22version%22%3A%226.27.0%22%2C%22abtest%22%3A%22%22%7D", #是否需要url编码，存疑,
    "teenagers_mode": "1",
    "teenagers_status": "0",
    "ts": int(time.time())
}
data = appsign(params=data, appkey=Config().appkey, appsec=Config().appsec)
print(data)
r = requests.post(url=url, data=data, headers=Config().header)
print("响应正文:", r.text)
query = urllib.parse.urlencode(data)
print(query)
