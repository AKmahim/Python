from flask import Flask,render_template,request
import psycopg2

con = psycopg2.connect(
	database = "cs50",
	host = "localhost",
	user = "postgres",
	password = "mahim",
	port ="5432"
)
db = con.cursor()
app = Flask(__name__)



@app.route("/")

def index():
	db.execute("SELECT * FROM flights")
	fl = list(db.fetchall())

	return render_template("index.html",flights=fl)

@app.route("/book",methods=["POST"])

def book():
	"""Book a flight"""

	name = request.form.get("name")

	try:
		flight_id = int(request.form.get("flight_id"))
	except ValueError:
		return render_template("error.html",message="Invalid flight Number.")
	
	#make sure the flight exists.
	res = "SELECT * FROM flights WHERE id = {}"
	res = res.format(flight_id)
	db.execute(res)
	res1 = db.fetchall()
	if res1 == None:
		return render_template("error.html",message="No such flight with that id.")
	db.execute("INSERT INTO passengers (name,flight_id) VALUES ('"+ name + " ',' " + str(flight_id) + "')",(name,flight_id))
	con.commit()
	return render_template("success.html")

@app.route("/flights")
def flights():
	"""lists all flights."""
	db.execute("SELECT * FROM flights")
	flights = db.fetchall()
	return render_template("flights.html",flights=flights)

@app.route("/flights/<int:flights_id>")

def flight(flight_id):
	"""Lists details about a single flight."""

	d = "SELECT * FROM flights WHERE id = {}"
	d = d.format(flight_id)
	db.execute(d)
	flight = db.fetchone()
	if flight is None:
		return render_template("error.html",message="No such flight.")
	pd = "SELECT name FROM passengers WHERE flight_id = {}"
	pd = pd.format(flight_id)
	db.execute(pd)
	passengers = db.fetchall()
	return render_template("flight.html",flight=flight,passengers=passengers)