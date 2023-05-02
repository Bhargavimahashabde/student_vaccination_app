from flask import Flask, render_template, request
import requests
import mysql.connector

app = Flask(_name_)

connection = mysql.connector.connect(
    user='root', password='root', host='db', port="3306", database='db')
print("Database connected")
cursor = connection.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vaccination_status', methods=['POST'])
def vaccination_status():
    reg_no = request.form['reg_no']
    cursor.execute(f"SELECT * FROM students WHERE RegNo = '{reg_no}'")
    student = cursor.fetchone()
    
    if student is None:
        message = 'Student not in database'
        
    else:
        message = f"{reg_no} is {student['vaccinated']} vaccinated"
    cursor.close()
    
    return render_template('index.html', message=message)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
