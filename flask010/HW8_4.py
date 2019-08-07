# 4.
# По адресу /form/user должен принимать POST запрос с
# параментрами: email, пароль и подтверждение пароля.
# Необходимо валидировать email, что обязательно присутствует,
# валидировать пароли, что они минимум 6 символов в длину и совпадают.
# Возрващать пользователю json вида: "status" - 0 или 1 (если ошибка валидации),
# "errors" - список ошибок, если они есть, или пустой список.


from flask import Flask, request
from flask.json import jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError


app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'asdasdasd',
    'DEBUG': True,
    'WTF_CSRF_ENABLED': False
})


def confirm_password(form, field):
    if form.data['password'] != form.data['confirm_password']:
        raise ValidationError('Пароли не совпадают"')


class UserForm(FlaskForm):
    email = StringField(label='E-mail', validators=[
        validators.Length(min=5, max=35), validators.Email()
    ])
    password = StringField(label='password:', validators =[
        validators.Length(min=6, max=12)
    ])
    confirm_password = StringField(label='confirm password:', validators=[
        validators.Length(min=6, max=20), confirm_password
    ])


@app.route('/form/user', methods =['GET', 'POST'])
def post_data():
    if request.method == 'POST':
        user_form = UserForm(request.form)
        status_output = {0:'Проверка пройдена', 1: 'Ошибка валидации'}
        if user_form.validate():
            # print('email:', request.form['email'])
            # print('pass:', request.form['password'])
            status_check = jsonify(status_output[0])
            return status_check
        else:
            status_check = jsonify(status_output[1])
            error_list = jsonify(user_form.errors)
            # print(user_form.errors)
            return status_check and error_list
    return 'Done!'

if __name__ == '__main__':
    app.run()
