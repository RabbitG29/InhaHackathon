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

def sayhello(max_count = 1): # Image Crawling
    base_url = "http://106.10.34.83:3001/download/1"
    url = "http://www.naver.com/"

    count = 1
    while count <= max_count:
        print(count)
        html = urllib.request.urlopen(url)
        source = html.read()
        soup = bs4.BeautifulSoup(source, "html.parser")

        img = soup.find("img")
        img_src = img.get("src")
        img_url = base_url + img_src
        img_name = img_src.replace("/", "")

        urllib.request.urlretrieve(base_url, "./img/"+img_name)
        count+=1

def sayhow(): # Image Download
    print("굿")
    url = "http://106.10.34.83:3001/download/1"
    with urlopen(url) as res:
        res_data = res.read()
    with open('./img/download1.jpg', 'wb') as f:
        f.write(res_data)

socketio.on('image')
def test_message():
        print('start')
        socketio.emit('image', {'data':data})

if __name__== '__main__':
        sayhow()
        socketio.run(app)
