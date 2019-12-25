from bs4 import BeautifulSoup as bs
import os.path
import sys
import csv

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

    tableO[1][0] = '第一节'
    tableO[2][0] = '第二节'
    tableO[3][0] = '第三节'
    tableO[4][0] = '第四节'
    tableO[5][0] = '第五节'
    tableO[6][0] = '第六节'
    tableO[7][0] = '第七节'
    tableO[8][0] = '第八节'
    tableO[9][0] = '第九节'
    tableO[10][0] = '第十节'
    tableO[11][0] = '第十一节'

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

    order = 1
    br = classes[0][0].contents[1]
    for period in classes:
        for oneClass in period:
            classList = []
            classContent = oneClass.contents

            for i in classContent:
                if i != br:
                    classList.append(str(i))
            classList = '\n'.join(classList)

            attrsDict = oneClass.attrs
            if 'rowspan' in attrsDict:
                if attrsDict['rowspan'] == '2':
                    tableO[order][period.index(oneClass)+1] = classList
                    tableO[order+1][period.index(oneClass)+1] = '同前一节'
                else:
                    tableO[order][period.index(oneClass)+1] = classList
                    tableO[order+1][period.index(oneClass)+1] = '同前一节'
                    tableO[order+2][period.index(oneClass)+1] = '同前一节'
            else:
                tableO[order][period.index(oneClass)+1] = classList
        order += 2
    
    with open('classTable.csv', 'w') as fileO:
        myWriter = csv.writer(fileO)
        myWriter.writerows(tableO)
    print('课程表文件保存为classTable.csv')

