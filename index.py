# 导入模块
import time, requests, easygui

friends = easygui.enterbox('输入好友名称')
city = easygui.enterbox('输入城市名')

def getToday(cityName):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + cityName
    response = requests.get(url)
    weatherDict = response.json()
    if weatherDict['desc'] == 'OK':
        # 获取城市名
        global city, wendu,month,forecast,tips
        city = weatherDict['data']['city']
        # 获取当前温度
        wendu = weatherDict['data']['wendu'] + '℃ '
        # 获取月份
        month = time.strftime('%m')
        forecast = weatherDict['data']['forecast']
        tips = weatherDict['data']['ganmao']
        # 获取日期
        global date, type, high, low
        date = month + '月' + forecast[0]['date']
        # 获取天气类型
        type = forecast[0]['type']
        # 获取最高温度
        high = forecast[0]['high']
        # 获取最低温度
        low = forecast[0]['low']

getToday(city)

result = '今天' + city + '的天气是：' + type + '，温度是：' + wendu + '，' + tips + '♥'

from wxpy import *
# 初始化机器人，扫码登陆
bot = Bot()

my_friend = bot.friends().search(friends)[0]
my_friend.send(result)
