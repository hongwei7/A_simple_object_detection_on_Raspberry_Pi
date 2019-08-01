
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

    return '192.16.9.101'
def catch_pic():
    req = requests.get("http://"+get_host_ip()+":8080/?action=snapshot")
    buf = req.content
    return buf
def test():
    f = open('keychain.jpg','wb')
    print('test')
    f.write(catch_pic())
    f.close()

if __name__ == '__main__':
    test()