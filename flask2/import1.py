import csv
import os
import psycopg2

from flask import Flask,render_template,request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres+psycopg2://postgres:mahim@localhost:5432/lecture"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)


def main():
    f = open("flights.csv")
    reader = csv.reader(f)
    for origin,destination,duration in reader:
        flight = Flight(origin=origin,destination=destination,duration=duration)
        db.session.add(flight)
        print(f"Added flight from {origin} to {destination} lasting {duration} min")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()

