#Реализовать на Flask

#+1. По адресу /locales должен возвращаться массив в формате json с тремя локалями: ['ru', 'en', 'it']
#+2. По адресу /sum/<int:first>/<int:second> должен получать в url-адресе два числа, возвращать их сумму
#+3. По адресу /greet/<user_name> должен получать имя пользователя, возвращать текст 'Hello, имя_которое_прислали'
#+4. По адресу /form/user должен принимать POST запрос с параментрами: email, пароль и подтверждение пароля. 
#Необходимо валидировать email, что обязательно присутствует, валидировать пароли, что они минимум 6 символов в длину и совпадают. Возрващать пользователю json вида: 
# "status" - 0 или 1 (если ошибка валидации),
# "errors" - список ошибок, если они есть,
# или пустой список.
#5. По адресу /serve/<path:filename> должен возвращать содержимое запрашиваемого файла из папки ./files. Файлы можно туда положить любые текстовые. А если такого нет - 404.

from flask import Flask, request
from threading import Lock
from flask_wtf import FlaskForm
from wtforms import StringField, validators, DateField
import json
from flask.json import jsonify

app = Flask(__name__)


@app.route('/locales')
def jsoner():
    return json.dumps(['ru', 'en', 'it'])


@app.route('/sum/<int:first>/<int:second>')
def summ(first, second):
    z = first + second
    return 'summa ravna: ' + str(z)

@app.route('/greet/<user_name>')
def quest1(user_name):
    return 'Hello,' + user_name

def checkpassf(form, field):
    if form.data['pass1'] != form.data['pass2']:
        raise ValueError('Passwords dont so match')

class UsersF(FlaskForm):
    email = StringField(label='email', validators=[
        validators.Length(min=6, max=35),
        validators.Email()
    ])
    pass1 = StringField(label='pass1', validators=[
        validators.Length(min=6, max=35),
    ])
    pass2 = StringField(label='pass2', validators=[
        validators.Length(min=6, max=35),
        checkpassf
    ])

@app.route('/form/user', methods=['POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        user_form = UsersF(request.form)
        status_output = {0:'All right', 1: 'validate error'}
        if user_form.validate():
            return json.dumps(status_output[0])
        else:
            return json.dumps(status_output[1]) and json.dumps(user_form.errors)
        

@app.route('/serve/<path:filename>')
def open_file(filename):
    fullpath = './files/' + filename
    with open(fullpath) as file:
        return file.read()





app.config.update(
    DEBUG=True,
    SECRET_KEY='This key must be secret!',
    WTF_CSRF_ENABLED=False,
)



if __name__ == '__main__':
    app.run()
