from flask import Flask, render_template, request, session

import random

app = Flask(__name__)


@app.route('/')
def index():
  return "<h1>Welcome to My First P5-JS Project !</h1>"


@app.route('/feedbackForm',methods=['GET', 'POST'])
def feedbackForm():
  # GET is when we load the page in our browser
  # POST is when we click the button
    return render_template("feedbackForm.html")

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        madarasShariganEye = request.form['Madaras Sharingan Eye']
        blackCat = request.form['Black Cat']
        froggyFrog = request.form['Froggy Frog']
        absorbingGas = request.form['Absorbing Gas']
        # print('Madaras Sharingan Eye')
    return render_template('success.html')
      # else:
        # print("Not post")
      
 
 


app.run(host="0.0.0.0",port=5001,debug=True)



