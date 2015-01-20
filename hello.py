from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
   import urllib
   from bs4 import BeautifulSoup
   url=urllib.urlopen('http://music.bugs.co.kr/chart/bugs/newrealtime?wl_ref=sub_gnb')
   soup=BeautifulSoup(url)
   music=soup.find_all('dl')
   return render_template('1.html',soup=soup, music=music)

@app.route('/test')
def hello():
	byonsuda='hello'
	listda=['shanghyup','jiyoon','all']
	return render_template('2.html',byonsuda=byonsuda,listda=listda)
 
@app.route('/media')
def media():
	import urllib
	from bs4 import BeautifulSoup
	url1=urllib.urlopen('http://besuccess.com/')
	url2=urllib.urlopen('http://platum.kr/')
	url3=urllib.urlopen('http://www.venturesquare.net/')
	soup1=BeautifulSoup(url1)
	soup2=BeautifulSoup(url2)
	soup3=BeautifulSoup(url3)
	return render_template('3.html',soup1=soup1,soup2=soup2,soup3=soup3)

@app.route('/list')
def list():
	import urllib
	from bs4 import BeautifulSoup
	url4=urllib.urlopen('http://www.appstory.co.kr/rank/?p=gappstore_rank')
	soup4=BeautifulSoup(url4)
	return render_template('4.html',soup4=soup4)

@app.route('/book')
def book():
	import urllib
	from bs4 import BeautifulSoup
	url5=urllib.urlopen('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=4db')
	url6=urllib.urlopen('http://www.bandinlunis.com/front/display/listBest.do')
	url7=urllib.urlopen('http://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1')
	soup5=BeautifulSoup(url5)
	soup6=BeautifulSoup(url6)
	soup7=BeautifulSoup(url7)
	return render_template('5.html',soup5=soup5,soup6=soup6,soup7=soup7)


if __name__== '__main__':
   app.run(debug=True, host='0.0.0.0') 