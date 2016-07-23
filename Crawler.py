# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
import xlrd
import time

def demo_requests(company_name):
    search = 'https://www.sogou.com/web?query=' + company_name + '+证券代码'
    content = requests.get(search).content
    soup = BeautifulSoup(content, 'html.parser')

    pattern_num = re.compile('\d\d\d\d\d\d')
    # pattern_name = re.compile(ur"[\u8bc1][\u5238][\u7b80][\u79f0][\uff1a]w*")
    number = "NULLNUM"
    # name = "NULLNAME"

    for div in soup.find_all('div',  {'class': 'ft'}):
        raw_text = div.text.strip()
        temp_num = pattern_num.findall(raw_text)
        # temp_name = pattern_name.findall(raw_text)
        if len(temp_num) > 0:
            number = temp_num[0]
        # if len(temp_name) > 0:
        #     name = temp_name[0]
    return number

if __name__ == '__main__':
    fname = "data.xlsx"
    bk = xlrd.open_workbook(fname)
    shxrange = range(bk.nsheets)
    sh = bk.sheet_by_name("1")

    nrows = sh.nrows
    ncols = sh.ncols
    print "nrows %d, ncols %d" % (nrows, ncols)

    row_list = []
    for i in range(1, nrows):
        row_data = sh.row_values(i)
        row_list.append(row_data)


    number = []
    for i in range(0,nrows-1):
        company_name = row_list[i][0]
        company_name = company_name.encode("utf-8")
        temp_num = demo_requests(company_name)
        print company_name, temp_num
        time.sleep(8)
        number.append(temp_num)

    print number