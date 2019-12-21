from bs4 import BeautifulSoup as bs
import os.path
import sys

def getTable(fileLoc):
    if not os.path.exists(fileLoc):
        print('网页文件不存在，退出...')
        sys.exit()
    with open(fileLoc) as fileT:
        content = fileT.read()
    
    table = [[''for i in range(8)] for j in range(11)]
    soup = bs(content, 'lxml')
