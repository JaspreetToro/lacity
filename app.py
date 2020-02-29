from flask import Flask, render_template, request
from uszipcode import SearchEngine
search = SearchEngine(simple_zipcode=True) # set simple_zipcode=False to use rich info database



app = Flask(__name__)

sp_name = "Charter"
sp_tech = "Fibre Optics"
sp_down = 340
sp_up = 50

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
	zipcode = request.form['zipcode']
	zpcode = search.by_zipcode(zipcode)
	return render_template('pass.html', zp=zpcode.to_json(), sp_name=sp_name, sp_tech=sp_tech, sp_down=sp_down, sp_up=sp_up)

if __name__ == '__main__':
	app.run(debug = True)