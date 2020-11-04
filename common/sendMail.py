import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from common.readFile import ReadFile
import json

#将测试报告发送到邮件
def send_mail(latest_report):

    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    config = ReadFile()
    smtpserver = config.readConfig('Email','smtpserver')

    user = config.readConfig('Email','user')
    password = config.readConfig('Email','password')
    #发件人
    sender = config.readConfig('Email','sender')
    #收件人列表(读取ini的文件得到的是str格式，需要用json.loads去掉")
    receives = json.loads(config.readConfig('Email','receives'))
    #抄送人列表
    cc = json.loads(config.readConfig('Email','cc'))
    subject = config.readConfig('Email','subject')
    msg = MIMEMultipart('mixed')
    #邮件内容
    msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

    #添加邮件附件
    att1 = MIMEText(open(latest_report,"rb").read(),"base64","utf-8")
    att1["Content-Type"] = "application/octet-stream"
    att1["Content-Disposition"] = "attachment;filename=" + 'test_report.html'
    msg.attach(att1)

    #邮件主题
    msg['Subject'] = Header(subject, 'utf-8')
    #邮件发送人
    msg['From'] = Header(sender, 'utf-8')
    #邮件接受人
    msg['To'] = ','.join(receives)
    #邮件抄送人
    msg['Cc']=','.join(cc)
    #连接邮箱服务器
    smtp = smtplib.SMTP(smtpserver, 587)
    #创建了安全连接，当SMTP服务必须要加密时使用，端口非25
    smtp.starttls()
    #登录邮箱服务器
    smtp.login(user, password)
    #发送邮件
    smtp.sendmail(sender, receives, msg.as_string())
    smtp.quit()

