# encoding:utf-8
import os
from PIL import Image


def resize(file, max_len=1136, min_len=640):
    try:
        img = Image.open(file)
    except:
        print('failed to open the file', file)
        return
    while max(img.size) > max_len or min(img.size) > min_len:
        img = img.resize((int(img.size[0] * 0.9), int(img.size[1] * 0.9)))
    if len(img.split()) == 3:
        r, g, b = img.split()
    else:
        r, g, b, a = img.split()
    img = Image.merge("RGB", (r, g, b))
    print('changed the resolution of', file, 'to', img.size[0], 'x', img.size[1], 'named', 'changed_' + file)
    img.save(file)


def main():
    print('do you want to input your own resolution? (y/n)')
    if input() == 'y':
        print('please input the resolution you expecting')
        print('input the longer side:')
        x = int(input())
        print('input the shorter side:')
        y = int(input())
    else:
        x = 1136
        y = 640
    for file in os.listdir():
        if not 'changed' in file:
            resize(file, x, y)


