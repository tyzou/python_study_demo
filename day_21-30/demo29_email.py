import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.parse import quote

# 邮件服务器域名（自行修改）
EMAIL_HOST = 'smtp.126.com'
# 邮件服务端口（通常是465）
EMAIL_PORT = 465
# 登录邮件服务器的账号（自行修改）
EMAIL_USER = 'xxxxxxxxx@126.com'
# 开通SMTP服务的授权码（自行修改）
EMAIL_AUTH = '邮件服务器的授权码'

class Demo29:

    @staticmethod
    def demo1():
        print('----------------发送普通邮件-------------------')
        # 创建邮件主体对象
        email = MIMEMultipart()
        # 设置发件人、收件人和主题
        email['From'] = 'xxxxxxxxx@126.com'
        email['To'] = 'yyyyyy@qq.com;zzzzzz@1000phone.com'
        email['Subject'] = Header('上半年工作情况汇报', 'utf-8')
        # 添加邮件正文内容
        content = """据德国媒体报道，当地时间9日，德国火车司机工会成员进行了投票，
        定于当地时间10日起进行全国性罢工，货运交通方面的罢工已于当地时间10日19时开始。
        此后，从11日凌晨2时到13日凌晨2时，德国全国范围内的客运和铁路基础设施将进行48小时的罢工。"""
        email.attach(MIMEText(content, 'plain', 'utf-8'))

        # 创建SMTP_SSL对象（连接邮件服务器）
        smtp_obj = smtplib.SMTP_SSL('smtp.126.com', 465)
        # 通过用户名和授权码进行登录
        smtp_obj.login('xxxxxxxxx@126.com', '邮件服务器的授权码')
        # 发送邮件（发件人、收件人、邮件内容（字符串））
        smtp_obj.sendmail(
            'xxxxxxxxx@126.com',
            ['yyyyyy@qq.com', 'zzzzzz@1000phone.com'],
            email.as_string()
        )

    @staticmethod
    def demo2():
        print('----------------发送带有附件的邮件-------------------')
        # 创建邮件主体对象
        email = MIMEMultipart()
        # 设置发件人、收件人和主题
        email['From'] = 'xxxxxxxxx@126.com'
        email['To'] = 'zzzzzzzz@1000phone.com'
        email['Subject'] = Header('请查收离职证明文件', 'utf-8')
        # 添加邮件正文内容（带HTML标签排版的内容）
        content = """<p>亲爱的前同事：</p>
        <p>你需要的离职证明在附件中，请查收！</p>
        <br>
        <p>祝，好！</p>
        <hr>
        <p>孙美丽 即日</p>"""
        email.attach(MIMEText(content, 'html', 'utf-8'))
        # 读取作为附件的文件
        with open(f'resources/王大锤离职证明.docx', 'rb') as file:
            attachment = MIMEText(file.read(), 'base64', 'utf-8')
            # 指定内容类型
            attachment['content-type'] = 'application/octet-stream'
            # 将中文文件名处理成百分号编码
            filename = quote('王大锤离职证明.docx')
            # 指定如何处置内容
            attachment['content-disposition'] = f'attachment; filename="{filename}"'

        # 创建SMTP_SSL对象（连接邮件服务器）
        smtp_obj = smtplib.SMTP_SSL('smtp.126.com', 465)
        # 通过用户名和授权码进行登录
        smtp_obj.login('xxxxxxxxx@126.com', '邮件服务器的授权码')
        # 发送邮件（发件人、收件人、邮件内容（字符串））
        smtp_obj.sendmail(
            'xxxxxxxxx@126.com',
            'zzzzzzzz@1000phone.com',
            email.as_string()
        )

    @staticmethod
    def demo3():
        print('----------------demo-------------------')




    @staticmethod
    def demo4():
        print('----------------demo-------------------')

    @staticmethod
    def demo5():
        print('----------------demo-------------------')

    @staticmethod
    def demo6():
        print('----------------demo-------------------')



    @staticmethod
    def send_email(*, from_user, to_users, subject='', content='', filenames=[]):
        """发送邮件

        :param from_user: 发件人
        :param to_users: 收件人，多个收件人用英文分号进行分隔
        :param subject: 邮件的主题
        :param content: 邮件正文内容
        :param filenames: 附件要发送的文件路径
        """
        email = MIMEMultipart()
        email['From'] = from_user
        email['To'] = to_users
        email['Subject'] = subject

        message = MIMEText(content, 'plain', 'utf-8')
        email.attach(message)
        for filename in filenames:
            with open(filename, 'rb') as file:
                pos = filename.rfind('/')
                display_filename = filename[pos + 1:] if pos >= 0 else filename
                display_filename = quote(display_filename)
                attachment = MIMEText(file.read(), 'base64', 'utf-8')
                attachment['content-type'] = 'application/octet-stream'
                attachment['content-disposition'] = f'attachment; filename="{display_filename}"'
                email.attach(attachment)

        smtp = smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT)
        smtp.login(EMAIL_USER, EMAIL_AUTH)
        smtp.sendmail(from_user, to_users.split(';'), email.as_string())

if __name__ == '__main__':
    Demo29.demo1()
    Demo29.demo2()
    Demo29.demo3()
    Demo29.demo4()
    Demo29.demo5()
    Demo29.demo6()
