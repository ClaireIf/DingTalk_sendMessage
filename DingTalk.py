# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 18:08
# @Author  : Claire
# @file : send_message.py

import json
import urllib.request
import time
import hmac
import hashlib
import base64
import urllib.parse


# Send party messages by verifying the signature(通过验证签名发送群消息)
def DingTalk(ding_url, secret, content_text, atMobiles):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    send_url = "%s&timestamp=%s&sign=%s" % (ding_url, timestamp, sign)

    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": content_text

        },
        "at": {
            "atMobiles": [
                atMobiles
            ],
            "isAtAll": False     #@All members(Here you can set @ specific someone)
        }
    }
    sendData = json.dumps(data)
    sendData = sendData.encode("utf-8")
    request = urllib.request.Request(url=send_url, data=sendData, headers=header)
    opener = urllib.request.urlopen(request)
    return opener

# Send party messages through keyword matching @Specific people(通过关键字@特定的人)
def DingTalk2(ding_url, content_text, atMobiles):
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": content_text

        },
        "at": {
            "atMobiles":
                atMobiles,
            "isAtAll": False
        }
    }
    sendData = json.dumps(data)
    sendData = sendData.encode("utf-8")
    request = urllib.request.Request(url=ding_url, data=sendData, headers=header)
    opener = urllib.request.urlopen(request)
    return opener


# @All members(通过关键字@所有人)
def DingTalk_ALL(ding_url, content_text):
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": content_text

        },
        "at": {
            "isAtAll": True
        }
    }
    sendData = json.dumps(data)
    sendData = sendData.encode("utf-8")
    request = urllib.request.Request(url=ding_url, data=sendData, headers=header)
    opener = urllib.request.urlopen(request)
    return opener
