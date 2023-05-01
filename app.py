from peewee import *
from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)
app.secret_key = "3209djno3eu98u3e"
db = SqliteDatabase('wbb.db')

class TeamTotal(Model):
    