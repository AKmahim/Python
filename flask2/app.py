from flask import Flask,render_template,request
from models import *
import os
import psycopg2

#DATABASE_URL = 'postgres+psycopg2://postgres:mahim@localhost:5432/lecture'
#SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:mahim@localhost:5432/lecture'

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres+psycopg2://postgres:mahim@localhost:5432/lecture"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)

def main():
    db.create_all()


if __name__ == "__main__":
    with app.app_context():
        main()