from flask import render_template, request, redirect
from app import app
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/sendbsg', methods= ['GET', 'POST'])
def send_bsg():
    if request.method == "GET":
        return "not working"
    else: 
        user_data = request.form
        print(user_data)
        
        month = user_data["month-name"]
        birthstone = model.bsg(month)
        print(birthstone)
        print("For the month of ")
        return(birthstone)