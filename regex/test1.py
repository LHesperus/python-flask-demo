# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:17:05 2019

@author: KB520
"""

from flask import Flask
from werkzeug.routing import BaseConverter

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

class RegexConverter(BaseConverter):
   
    def __init__(self, url_map, regex):
        super(RegexConverter,self).__init__(url_map)
        self.regex = regex
   

        
app.url_map.converters["re"]=RegexConverter

@app.route("/send/<re(r'1[23578]\d{9}'):mobile>") #������ʽ����һλ������1���ڶ�λ�Ƿ��������������������9������
def send_sms(mobile):
    return "send sms to %s" % mobile

if __name__=='__main__':
    print(app.url_map)
    app.run(debug=True)