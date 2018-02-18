from flask import Flask
from flask_mail import Mail
app = Flask(__name__)
app.config['SECRET_KEY'] = 'enter some random passphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '465'
app.config['MAIL_USERNAME'] = 'enter your mailtrap username'
app.config['MAIL_PASSWORD'] = 'enter your mailtrap password'
mail = Mail(app)
from app import views