import urllib.request
import urllib.parse
import urllib.error
import re
import sys
import os.path
from PIL import Image

class login:

    def __init__(self, username, password):
        self._userName = username
        self._password = password

    def getHidden(self):
        '''
        获取cookie、viewstat、viewstatGenerator
        '''
        headers = self._headersPage
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

    def getCheckCode(self):
        '''
        获取验证码，保存在工作目录
        '''
        dest = ''.join((self._httpStr, self._url2))
        dest = ''.join((dest, 'CheckCode.aspx'))

        headers = self._headersCheckCode
        headers['Cookie'] = self._Cookie
        headers['Host'] = self._url2

        req = urllib.request.Request(url = dest, headers = headers)
        CheckCodeData = urllib.request.urlopen(req, timeout = 3)
        CheckCodeData = CheckCodeData.read()
        fileCheckCode = open(self._CheckCode, 'wb')
        fileCheckCode.write(CheckCodeData)
        fileCheckCode.close()
    
    def postData(self):
        '''
        上传用户名、密码及验证码进行登录
        '''
        headers = self._headersPage
        formData = self._formData

        img = Image.open(self._CheckCode)
        img.show()
        formData['txtSecretCode'] = input('请输入验证码')
        formData['__VIEWSTATE'] = self._viewstat
        formData['__VIEWSTATEGENERATOR'] = self._viewstatGen
        formData['txtUserName'] = self._userName
        formData['TextBox2'] = self._password
        
        headers['Cookie'] = self._Cookie
        headers['Content-Type'] = r'application/x-www-form-urlencoded'
        headers['Host'] = self._url2
        headers['Origin'] = 'null'
        headers['Sec-Fetch-Site'] = 'same-origin'
        headers['Content-Length'] = '%d'%len(urllib.parse.urlencode(formData))

        dest = ''.join((self._httpStr, self._url2))
        formDataFin = urllib.parse.urlencode(formData).encode()

        request = urllib.request.Request(url = dest, headers = headers)
        response = urllib.request.urlopen(request, data = formDataFin)

        if response.geturl() == self._url2:
            print('登录失败，退出...')
            sys.exit()
        
        pat = '"(xskbcx.+?)"'
        self._urlTable = re.findall(pat, str(response.read()))[0]

    def outPut(self):
        '''
        打印相关结果
        '''
        print(self._Cookie)
        print(self._viewstat)
        print(self._viewstatGen)



    

    _headersPage = {
        'Accept':r'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding':r'gzip, deflate, br',
	'Accept-Language':r'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
	'Connection':r'keep-alive',
	'Cookie':r'',
	'Host':r'',
	'Sec-Fetch-Mode':r'navigate',
	'Sec-Fetch-Site':r'none',
	'Sec-Fetch-User':r'?1',
	'Upgrade-Insecure-Requests':r'1',
	'User-Agent':r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
    }
    
    _headersCheckCode = {
        'Accept':r'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding':r'gzip, deflate, br',
        'Accept-Language':r'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,pt;q=0.6,ca;q=0.5',
        'Connection':r'keep-alive',
        'Cookie':r'',
        'Host':r'',
        'Sec-Fetch-Mode':r'no-cors',
        'Sec-Fetch-Site':r'same-origin',
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
    
    _userName = ''
    _password = ''
    _url1 = 'jw.ahu.ConnectionError'
    _url2 = 'jwxt3.ahu.edu.cn'
    _urlTable = ''
    _httpStr = 'https://'
    _Cookie = ''
    _viewstat = ''
    _viewstatGen = ''
    _CheckCode = 'CheckCode.aspx'

