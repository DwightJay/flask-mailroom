import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import db, Donor, Donation

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/create', methods=['GET', 'POST'])
def create():

	if request.method == 'POST':

		#db.close()
		#db.connect()
		#db.close()
		#dname = Donor(name=request.form['name'])
		#evie.save()
		#evie = "Evie"
		#print(evie)
		evie = Donor(name=request.form['name'])
		evie.save()
		#db.connect()
		#donors = [evie]
		#4print(request.form['name'])

		#Donation(donor=evie,value=150).save()
		Donation(donor=evie,value=int(request.form['value'])).save()

		
		#Donation(name=evie,value=int(150)).save()

		#Donation(donor=evie, value=int(request.form['value'])).save()
		#Donation(name=evie, value=int(request.form['value'])).save()
		#Donation(name=donors, value=int(1000)).save()
		#task.save()
		#db.close()

		return redirect(url_for('all'))
	else:
		return render_template('create.jinja2')
    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

