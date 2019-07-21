import functools
import json
import os
import flask
from flask import Flask, redirect, url_for, session, request,render_template
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('a.json', scope)

gc = gspread.authorize(credentials)
# print(gc)
wks = gc.open("test1").sheet1

# Extract and print all of the values
# list_of_hashes = sheet.get_all_records()
# print(list_of_hashes)
app = Flask(__name__)  
@app.route('/')

def form():
    return render_template('contact.html')
@app.route('/', methods=['POST'])
def sub():
    text=['1']*13
    text[0] = request.form['name']
    text[1] = request.form['email']
    text[2] = request.form['mem1']
    text[3] = request.form['email0']
    text[4] = request.form['mem2']
    text[5] = request.form['email1']
    text[6] = request.form['mem3']
    text[7] = request.form['email2']
    text[8] = request.form['mem4']
    text[9] = request.form['email3']
    text[10] = request.form['mem5']
    text[11] = request.form['email4']
    text[12] = request.form['message']
    wks.insert_row(text)

    return text[4]


if __name__ == "__main__":  
  
    #app.run(debug=True) 
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)