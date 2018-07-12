from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/<string:num_A>/<string:num_B>')
def show_post(num_A, num_B):
	if num_A.isdigit() and num_B.isdigit():
		result = int(num_A) * int(num_B)
		return '%d' % result
	else:
		return 'only int is accepted'
	