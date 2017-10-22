from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
passwordRegex = re.compile(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{10,}$')

from datetime import datetime, date, time

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
    

    if len(request.form['firstname']) < 1:
        flash("First Name cannot be empty!")
    elif any(char.isdigit() for char in request.form['firstname']) == True:
        flash('First Name cannot have numbers', 'firstNameError')


    if len(request.form['lastname']) < 1:
        flash("Last Name cannot be empty!")
    elif any(char.isdigit() for char in request.form['lastname']) == True:
        flash('Last Name cannot have numbers', 'lastNameError')


    if request.form['password'] == '':
        flash("Password cannot be empty!")
    elif len(request.form['password']) < 8:
        flash('Password must be greater than 8 characters', 'passwordError')
    elif not passwordRegex.match(request.form['password']) == None:
        flash('Password must contain at least one lowercase letter, one uppercase letter, and one digit', 'passwordError')
   


    if request.form['confirmPassword'] == '':
        flash('Please confirm password', 'confirmPasswordError')
    elif request.form['confirmPassword'] != request.form['password']:
        flash('Passwords do not match', 'confirmPasswordError')
    
    else:
        flash("Thanks for submitting your information.")
    

    return redirect('/')

app.run(debug=True)
