
#!/usr/bin/env python
# encoding=utf-8
 
import time     #导入定时
import requests  #导入url
import re       #导入正则
import socket
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip
def catch_pic():
    req = requests.get("http://"+get_host_ip()+":8080/?action=snapshot")
    buf = req.content      
    return buf
 

