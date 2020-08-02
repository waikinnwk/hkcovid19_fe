from flask import Flask , render_template, url_for
from app import app
from app.config import *
from flask import request

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html',backend_url=backend_url)


@app.route('/casenobymonth')
def case_by_month():
    return render_template('casenobymonth.html',backend_url=backend_url)    


@app.route('/caseinfo')
def case_info():
    return render_template('case_info.html',backend_url=backend_url)    


@app.route('/casenobydistrict')
def case_by_district():
    return render_template('case_district.html',backend_url=backend_url)    
