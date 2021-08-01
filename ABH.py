#!/usr/bin/ecdie python
# -*- coding: utf-8 -*-

import math
import os
import struct
from binascii import a2b_hex, b2a_hex

from Crypto.Cipher import AES
from PIL import Image
import sys


# 如果text不足16位的倍数就用空格补足为16位
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encrypt(text):
    key = '9999999999999999'.encode('utf-8')
    mode = AES.MODE_CBC
    iv = b'qqqqqqqqqqqqqqqq'
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
    return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text):
    key = '9999999999999999'.encode('utf-8')
    iv = b'qqqqqqqqqqqqqqqq'
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')

def encryption():
    filename = input("请输入要加密的文件(绝对路径): ")
    with open(filename,"r") as f:
        a = f.read()
        f.close()
    #1.aes加密
    e = encrypt(a)  # 加密
    #2.binary处理
    with open("temp.txt", "wb") as f2:
        f2.write(e)
        os.system("g++ binary.cc -o b && ./b")
        f2.close()
    #3.hex处理
    os.system("python3 hex_w.py")

def decryption():
    ###解hex
    os.system("python3 hex_r.py")
    ###解binary
    os.system("g++ read_b.cc -o r ./r ")
    with open("result.txt", "rb") as f2:
        data = f2.read()
        f2.close()
    ###解aes
    d = decrypt(data)  # 解密
    with open("result.txt","w") as f3:
        for i in d:
            f3.write(i)
