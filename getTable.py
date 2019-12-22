from bs4 import BeautifulSoup as bs
import os.path
import sys

def getTable(fileLoc):
    if not os.path.exists(fileLoc):
        print('网页文件不存在，退出...')
        sys.exit()
    with open(fileLoc) as fileT:
        content = fileT.read()
    
    tableO = [[''for i in range(8)] for j in range(11)]
    tableO[0][0] = '星期一'
    tableO[0][1] = '星期二'
    tableO[0][2] = '星期三'
    tableO[0][3] = '星期四'
    tableO[0][4] = '星期五'
    tableO[0][5] = '星期六'
    tableO[0][6] = '星期日'
    soup = bs(content, 'lxml')
    table = soup.table
    tr = table.find_all(name = 'tr')


