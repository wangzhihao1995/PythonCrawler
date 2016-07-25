# -*- coding: utf-8 -*-

import requests, time
import json

stock_num = "600681"
searchkey = "报告书"

# 设置url和需要post的data
url = "http://www.cninfo.com.cn/cninfo-new/announcement/query"
data = {'stock':stock_num,'searchkey':searchkey}

# 发送post请求
r = requests.post(url=url, data=data).content

# print r

json_r = json.loads(r)

# print type(json_r), json_r

announcements = json_r["announcements"][0]

# print type(announcements), announcements

filename = announcements["announcementTitle"]
# filename = announcements["announcementTitle"] + ".pdf"

download_url = announcements["adjunctUrl"]
download_url = "http://www.cninfo.com.cn/" + download_url

print filename, download_url