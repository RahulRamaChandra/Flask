from flask import Flask, request, jsonify

import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host = "localhost", user = "root", password = "Password#123")
cursor = mydb.cursor()
cursor.execute("create database if not exists tasksql")
cursor.execute("create table if not exists tasksql.mysqltable(name varchar(30), number int)")