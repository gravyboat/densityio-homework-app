#!/usr/bin/python

from flask import Flask, request, redirect, url_for
import psycopg2

application = Flask(__name__)

hostname = 'dd1cgjf7dvsomrz.ckh4iv9iog58.us-east-2.rds.amazonaws.com'
dbusername = 'density'
password = 'PASSHERE'
database = 'MyDatabase'

@application.route('/')
def hello_world():
    return('Hello, World!')


@application.route('/success')
def success():
    return('Success!')


@application.route('/fail')
def fail():
    return('Something went wrong.')


@application.route('/create', methods=['POST'])
def create():
    try:
        username = request.form['username']
        con = psycopg2.connect(host = hostname,
                               user = dbusername,
                               password = password,
                               dbname = database)
        cur = con.cursor()
        cur.execute("INSERT INTO users (username) VALUES (%s)", (username, ))
        con.commit()
        con.close()
        return(redirect(url_for('success')))
    except:
        print("nope")

if __name__ == "__main__":
    application.run(host='0.0.0.0')