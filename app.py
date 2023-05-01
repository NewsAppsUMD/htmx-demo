from peewee import *
from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = "3209djno3eu98u3e"
db = SqliteDatabase('testudo.db')

class Course(Model):
    id = CharField()
    title = CharField()
    description = TextField()
    term = CharField()
    department = CharField()
    instructors = CharField()
    seats = IntegerField()

    class Meta:
        table_name = "courses"
        database = db

@app.route('/')
def index():
    terms = Course.select().order_by(Course.term.desc())
    return render_template('index.html', terms=terms)
