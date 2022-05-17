from flask_mail import Mail, Message
from flask import Flask, request, render_template

# 참고로 기존 서버에 사용되는 모듈은 이전과 같습니다.
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jeongminji58@gmail.com'
app.config['MAIL_PASSWORD'] = 'ImMinig9295!@'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


def email_test():
    if request.method == 'POST':
        senders = request.form['email_sender']
        receiver = request.form['email_receiver']
        content = request.form['email_content']
        receiver = receiver.split(',')

        for i in range(len(receiver)):
            receiver[i] = receiver[i].strip()

        print
        receiver

        result = send_email(senders, receiver, content)

        if not result:
            return render_template('email.html', content="Email is sent")
        else:
            return render_template('email.html', content="Email is not sent")

    else:
        return render_template('email.html')
