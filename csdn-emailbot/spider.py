#!/bin/python
#Coding="utf-8"

import sys
import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 爬取访问量、排名等信息
def getResult(CSDN_ID):
   

        return "Holle World"


# 生成信息
def formatMessage(result):
    message = result
   
    return message


# 发送邮件
def sendEmail(content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = "GitHub Actions<" + sender + ">"
    message['To'] = "<" + receiver + ">"

    subject = "CSDN Report"
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
        smtpObj.login(mail_user, mail_password)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print("邮件发送成功")

    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


# 保存email内容
def saveEmail(email_path, message):
    with open(email_path, 'w', encoding="utf-8") as email:
        email.writelines(message)


if __name__ == "__main__":

    CSDN_ID = sys.argv[1]

    res = getResult(CSDN_ID)
    message = formatMessage(res)
    email_path = "email.txt"
    saveEmail(email_path, message)
