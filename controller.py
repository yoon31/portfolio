from flask import request, redirect, render_template, Flask, session
from flask.ext.sqlalchemy import SQLAlchemy
import logging

from __init__ import app 

db = SQLAlchemy(app)

from models import *

@app.route('/')
def hello_world():
	return render_template("home.html")

@app.route('/jiyoon')
def jiyoon_page():
	return render_template("jiyoon.html")

@app.route('/minah')
def minah_page():
	return render_template("minah.html")

@app.route('/jaehyo')
def jaehyo_page():
	return render_template("jaehyo.html")

@app.route('/jeonghyun')
def jeonghyun_page():
	return render_template("jeonghyun.html")

@app.route('/jaeyoon')
def jaeyoon_page():
	return render_template("jaeyoon.html")

@app.route('/webtest')	
def index():
	import urllib


@app.route('/test/<tempvar>')	
def test(tempvar):
	import urllib
	from bs4 import BeautifulSoup
	url=urllib.urlopen('http://www.naver.com')
	soup=BeautifulSoup(url)
	return render_template('home.html', soup=soup)

@app.route('/login', methods=['POST'])
def login():
		user_id = request.form['user_id']
		user_pw = request.form['password']
		if user_id == 'jiyoon':
			if user_pw == '1234':
					session['logged_in'] = True
					return 'login success'
			else: 
					return 'wrong password'
		else:
			return 'wrong id' 


if __name__=='__main__':
	app.secret_key = 'sdifjsdoijffj'
	app.run(debug=True,host='0.0.0.0')
