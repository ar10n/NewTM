from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object('config')
mail = Mail(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        body_message = 'Имя: {}. Email: {}. Тема: {}. Сообщение: {}'.format(
            name, email, subject, message)
        email_message = Message(
            body=body_message,
            recipients=['sergey.nikitin@tendermarkt.ru'],
        )
        mail.send(email_message)
    return render_template('index.html', name=index)


if __name__ == '__main__':
    app.run()
