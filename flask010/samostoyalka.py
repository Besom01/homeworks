from flask import Flask
app = Flask(__name__)

@app.route('/quest1/<user>')
def quest1(user):
	return 'hello user: ' + user

@app.route('/quest2/<int:x>/<int:y>')
def quest2(x, y):
	z = x + y
	return 'summa ravna: ' + str(z)

@app.route('/quest3/<str1>/<str2>/<str3>')
def quest3(str1, str2, str3):
	if len(str1) > len(str2) and len(str1) > len(str3):
		x = str1
	elif len(str2) > len(str3) and len(str2) > len(str1):
		x = str2
	else:
		x = str3
	return x

if __name__ == '__main__':
	app.run()