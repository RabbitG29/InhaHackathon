# -*- coding: utf-8 -*-
from urllib.request import urlopen, Request
from flask import Flask
from flask_socketio import SocketIO, emit
import urllib
import bs4
import requests
import threading
import sys
import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app)

global data
data = []

def sayhi():
        global data
        threading.Timer(600.0, sayhi).start()
        location = '인천 용현1.4동'
        enc_location = urllib.parse.quote(location + '+날씨')
        url = 'https://search.naver.com/search.naver?ie=utf8&query='+enc_location
        req = Request(url)
        page = urlopen(req)
        html = page.read()
        soup = bs4.BeautifulSoup(html, 'html5lib')
        temperature = soup.find('p', class_='info_temperature').find('span', class_='todaytemp').text # 기온
        weather = soup.find('p', class_='cast_txt').text # 날씨
        mise = soup.find('dl', class_='indicator').text # 미세먼지+초미세먼지+오존지수
        morning = soup.find('li', class_='date_info today').find('span', class_='point_time morning').find('span', class_='rain_rate').find('span', class_='num').text
        afternoon = soup.find('li', class_='date_info today').find('span', class_='point_time afternoon').find('span', class_='rain_rate').find('span', class_='num').text
        print('현재 ' + location + ' 기온은 ' + temperature + '도 입니다.')
        print('날씨는 ' + weather)
        print(mise)
        print('오늘 오전의 강수확률은 '+morning+'% 입니다.')
        print('오늘 오후의 강수확률은 '+afternoon+'% 입니다.')

        data2 = []
        data2.append(temperature)
        data2.append(weather)
        data2.append(mise)
        data2.append(morning)
        data2.append(afternoon)
        data = data2

        socketio.emit('mise', {'data': data})

def test_message():
        print('start')
        socketio.emit('mise', {'data':data})

if __name__== '__main__':
        sayhi()
        socketio.run(app)
