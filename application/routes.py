
from application import app
from flask import Flask, render_template


#
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/biodata')
def biodata():
    return render_template('biodata.html')

@app.route('/divisi')
def divisi():
    return render_template('divisi.html')

@app.route('/about-us')
def aboutUs():
    return render_template('about-us.html')

@app.route('/contact-us')
def contactUs():
    return render_template('contact-us.html')


if __name__ == '__main__':
    app.run(debug=True)