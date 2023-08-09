# -*- coding: utf-8 -*-
# @Time    : 2023/8/9 18:17
# @Author  : Claire
# @file : test_sendMessage.py
import DingTalk

# Dingtalk Url(钉钉群机器人链接)
ding_conf = {
    "url": "https://oapi.dingtalk.com/robot/send?access_token="
}

# input @Specific people phone number(通过群成员手机号@特定的人)
Account = ["phone number", "phone number"]

ding_url = ding_conf["url"]

text = "automation send message"
print(text)
# send DingTalk group message(发送群消息)
DingTalk.DingTalk2(ding_url, text, Account)


