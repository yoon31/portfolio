from flask import Flask, render_template, request, session

app = Flask(__name__)

from controller import *

if __name__=='__main__':
	app.secret_key = 'sdifjsdoijffj'
	app.run(debug=True,host='0.0.0.0')
