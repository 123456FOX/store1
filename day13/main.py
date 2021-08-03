# 报告：
# 1.
# 加载器：加载所有测试用例并得到所有用例
# 2.
# 使用运行器运行这些测试用例并生成报告
from email.mime.application import MIMEApplication

from HTMLTestRunner import HTMLTestRunner
import unittest
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

# 加载所有用例
tests = unittest.defaultTestLoader.discover(r'C:\Users\a\PycharmProjects\pythonProject\day13',
                                            pattern='test.py')
# 使用运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title='计算机测试报告',
    description='这是减乘除运算报告',
    verbosity=1,
    stream=open('jisuanji.html', mode='w+', encoding='utf-8')
)
# 运行所有用例
runner.run(tests)

sender = '1483221745@qq.com'  # 发件人邮箱账号
my_pass = 'rxoxseiefynxbacd'  # 发件人邮箱授权码
user = '717813873@qq.com'  # 收件人邮箱账号

msg = MIMEMultipart()  # 创建一个邮件
msg['From'] = formataddr(["", sender])  # 括号里对应发件人邮箱昵称、发件人邮箱账号
msg['To'] = formataddr(["呵呵", user])  # 括号里对应收件人邮箱昵称、收件人邮箱账号
msg['Subject'] = "发送邮件测试"  # 邮件的主题，也可以说是标题

server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，SMTP端口是25
server.login(sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

# 发送附件
att = MIMEText(open(r'C:\Users\a\PycharmProjects\pythonProject\day13\jisuanji.txt', 'rb').read(), 'base64', 'utf-8')  # 构造附件，三个参数：第一个为附件路径，第二个附件格式，第三个附件设置编码utf-8
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = "attachment; filename=test.html"  # filename为文件名字
msg.attach(att)


try:
    server.sendmail(sender, user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.quit()  # 关闭连接
    print("邮件发送成功")
except smtplib.SMTPException:
    print("邮件发送失败")