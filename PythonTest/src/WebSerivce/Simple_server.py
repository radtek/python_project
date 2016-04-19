'''
Web服务的入口类
Created on 2016年4月5日
@author: Songge
'''
from wsgiref.simple_server import make_server
from Simple_server_process import processMain
from GetSystemInfo import getPlatform

n_port = 8899

#取系统信息
getPlatform()
#设置服务器地址、端口、响应函数
httpd = make_server('127.0.0.1', n_port, processMain)

#打印监听端口名...
print('Serving Http on port ',n_port,'...')

#开始监听HTTP请求
httpd.serve_forever()