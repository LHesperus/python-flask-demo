# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:17:05 2019

@author: KB520
"""

from flask import Flask,request
from werkzeug.routing import BaseConverter

app = Flask(__name__)

@app.route("/")
def index():
    return "hello"

@app.route("/upload",methods=["POST"])
def upload():
    fil_obj = request.files.get("pic")
    if fil_obj is None:
        return  "δ�ϴ�"
    # ����1
    """
    f=open("./demo.jpg","wb")
    data =fil_obj.read()
    f.write(data)
    f.close()
    """
    #����2
    fil_obj.save("./demo2.png")
    return "�ϴ��ɹ�"


if __name__=='__main__':
   # print(app.url_map)
    app.run(debug=True)