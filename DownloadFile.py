from os.path import basename
from urllib.parse import urlsplit
import urllib.request


def url2name(url):
    return basename(urlsplit(url)[2])


def download(url, localFileName=None):
    localName = url2name(url)
    req = urllib.request.Request(url)
    r = urllib.request.urlopen(req)
    if 'Content-Disposition' in r.info():
        #  If the response has Content-Disposition, we take file name from it
        localName = r.info()['Content-Disposition'].split('filename=')[1]
        if localName[0] == '"' or localName[0] == "'":
            localName = localName[1:-1]
    elif r.url != url:
        # if we were redirected, the real file name we take from the final URL
        localName = url2name(r.url)
    if localFileName:
        # we can force to save the file as specified name
        localName = localFileName
    f = open(localName, 'wb')
    f.write(r.read())
    f.close()


if __name__ == '__main__':
    download('http://www.cninfo.com.cn/cninfo-new/disclosure/szse_main/download/1202496314?announceTime=2016-07-21')

