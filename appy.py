from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/dashboard', methods=['POST'])
def home():
	if request.method == 'POST':
		admin_pass = '123456'
		user_name = request.form['username']
		user_password = request.form['pass']

		if user_name == 'admin':
			if user_password == admin_pass:
				return '<h1>Welcome to admin Dashboard</h1>'
			else:
				return '<h1>Credentials doesnot match. Please try again</h1>'

		return f'<h3>Hello!!</h3><h1>{user_name} : {user_password}</h1>'
	else:
		return render_template('home.html', flag = '')
		# True and Flase
		# flag --> True
		# 	- Login
		# 	- Register
		# flag --> False
		# 	- contact, home, about

		# additiopnally
		# error page
		# 	- error msg
		# 	- button --> login

@app.route('/login')
def login():
	return render_template('login.html')

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=8080)

