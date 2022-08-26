import random
from time import localtime
from requests import get, post
from datetime import datetime, date
from zhdate import ZhDate
import sys
import os
import http.client, urllib
import json

with open("config.txt", encoding="utf-8") as f:
    config = eval(f.read())

key = config["tian_api"]
key = config["tian_api"]
conn = http.client.HTTPSConnection('api.tianapi.com')  # 接口域名
params = urllib.parse.urlencode({'key': key})
headers = {'Content-type': 'application/x-www-form-urlencoded'}
conn.request('POST', '/saylove/index', params, headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data)
data = data["newslist"][0]["content"]
print(data)

