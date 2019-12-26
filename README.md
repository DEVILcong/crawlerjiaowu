# 教务系统的爬虫
## 说明
    针对安徽大学新版教务系统，实现传入用户名，自动登录教务系统，得到当前学期的课程表，并将其保存成csv文件

## 运行环境
    Linux 5.3.15-1-MANJARO
    Python 3.8.0
    gcc 9.2.0
    依赖BeautifulSoup4
    依赖lxml

## 文件功能描述
    文件夹
        doc ----保存项目用到的阶段报告等文件
        __pycache__ ----python运行时的缓存
        webPages  ----保存新版教务系统的一些网页
    文件
        imgProcess.py  ----程序初期想实现自动识别验证码，但是最后没搞
        login.py  ----登陆及获取网页部分相关功能的实现
        getTableFile.py  ----根据网页源代码生成CSV
        test.py ----主程序，将上面两个主要的部分结合起来

## 使用方法
    1.打开test.py，在对象的初始化中输入你的学号及密码；
    2.执行'python3 test.py'

## 进一步说明
    程序执行过程中会产生三个文件，分别是：
        CheckCode.aspx  登陆界面二维码
        testT  课程表界面的网页源代码，可以加后缀名‘.html’然后用浏览器打开
        classTable.csv  最终的课程表

## bug反馈
    邮箱：liangyuecong@sina.com(不常看)
    QQ：2424878279
