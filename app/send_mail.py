from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def send_mail(recipients, subject, data):
    content = MIMEMultipart()  # 建立MIMEMultipart物件
    content["subject"] = subject + " 申告郵件通知"  # 郵件標題
    content["from"] = "yuxp0130@gmail.com"  # 寄件者
    content["to"] = recipients  # 收件者
    content.attach(MIMEText(data))  # 郵件內容

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("yuxp0130@gmail.com", "rvdb gluy kjbq nboo")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)

