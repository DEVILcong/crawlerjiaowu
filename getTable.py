from bs4 import BeautifulSoup as bs
import os.path
import sys

def getTable(fileLoc):
    if not os.path.exists(fileLoc):
        print('网页文件不存在，退出...')
        sys.exit()
    with open(fileLoc) as fileT:
        content = fileT.read()
    
    tableO = [[''for i in range(8)] for j in range(12)]
    tableO[0][0] = '时间'
    tableO[0][1] = '星期一'
    tableO[0][2] = '星期二'
    tableO[0][3] = '星期三'
    tableO[0][4] = '星期四'
    tableO[0][5] = '星期五'
    tableO[0][6] = '星期六'
    tableO[0][7] = '星期日'
    soup = bs(content, 'lxml')
    table = soup.table
    table = table.find_all(name = 'tr')
    table = [table[2], table[4], table[6], table[8], table[10]]

    classes = []
    for period in table:
        classes.append(period.find_all(name = 'td'))

    
    classes[0].pop(0)
    classes[2].pop(0)
    classes[4].pop(0)
    for i in classes:
        i.pop(0)



