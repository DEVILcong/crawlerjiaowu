import urllib.request
import urllib.parse
import urllib.error
import re
import sys

class login:

    def __init__(self):
        pass
    def getHidden(self):
        headers = self._headers
        headers['Host'] = self._url2
        url = ''.join((self._httpStr, self._url2))
        req = urllib.request.Request(url = url, headers = headers)

        try:
            response = urllib.request.urlopen(req, timeout = 4)
        except urllib.error.URLError:
            print(r'website error, exiting')
            sys.exit()

        except urllib.error.HTTPError as e:
            print(r'network error, error code is', e,getcode(),r',exiting')
            sys.exit()
        else:
            print(r'got web page, finding hidden message...')
            rawCookie = response.getheader('Set-Cookie')
            self._Cookie = rawCookie[:rawCookie.index(';'):]

            content = response.read().decode('utf-8')
            pat1 = r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*)" />'
            pat2 = r'<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="(.*)" />'
            self._viewstat = re.findall(pat1, content)[0]
            self._viewstatGen = re.findall(pat2, content)[0]
            print(r'got hidden message')

    def outPut(self):
        print(self._Cookie)
        print(self._viewstat)
        print(self._viewstatGen)

    

    _headers = {
        'Accept':r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':r'gzip, deflate, br',
	'Accept-Language':r'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
	'Connection':r'keep-alive',
	'Cookie':r'',
	'Host':r'',
	'Referer':r'',
	'Sec-Fetch-Mode':r'navigate',
	'Sec-Fetch-Site':r'none',
	'Sec-Fetch-User':r'?1',
	'Upgrade-Insecure-Requests':r'1',
	'User-Agent':r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }

    _formData = {
	'__LASTFOCUS': '', 
	'__VIEWSTATE':r'',
	'__VIEWSTATEGENERATOR':'',
	'__EVENTTARGET':'', 
	'__EVENTARGUMENT':'', 
	'txtUserName':'',
	'TextBox2':'',
	'txtSecretCode':'',
	'RadioButtonList1':'学生',
	'Button1':'登录'
    }
    _url1 = 'jw.ahu.cn'
    _url2 = 'jwxt3.ahu.edu.cn'
    _httpStr = 'https://'
    _Cookie = ''
    _viewstat = ''
    _viewstatGen = ''

