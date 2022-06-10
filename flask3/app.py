from flask import Flask,render_template,request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres+psycopg2://postgres:mahim@localhost:5432/lecture"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html",flights=flights)

@app.route("/book",methods=["POST"])
def book():
    """book a flight."""
    name = request.form.get("name")

    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html",message="Invalid flight number.")
    
    #Make sure the flight exists
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html",message="No such flight wtih that id.")

    #add passenger
    # passenger = Passenger(name=name,flight_id=flight_id)
    # db.session.add(passenger)
    # db.session.commit()
    flight.add_passenger(name)
    return render_template("success.html")


@app.route("/flights")
def flights():
    """list all flights."""
    flights = Flight.query.all()
    return render_template("flights.html",flights=flights)
@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """list details about a single flight."""

    #Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html",message="No such file")
    #Get all passengers.
    # passengers = Passenger.query.filter_by(flight_id=flight.id).all()
    passenger= flight.passengers
    return render_template("flight.html",flight=flight,passengers=passengers)

@app.route("/api/flights/<int:flight_id>")
def flight_api(flight_id):
    """Return details about a single flight."""

    #Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return jsonify({"error":"Invalid flight_id"}),422
    
    #Get all passengers.

    passengers = flight.passengers
    names = []
    for passenger in passengers:
        names.append(passenger.name)
    return jsonify(
        {
            "origin": flight.origin,
            "destination":flight.destination,
            "duration":flight.duration,
            "passengers":names
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
