from flask import Flask,render_template

app = Flask(__name__)
@app.route("/")
def  index():
    return render_template("index.html")

texts = ["The software industry has seen no shortage of new web frameworks over the years, but I certainly wouldn't be alone in saying that none. Discovering Flask is to rediscover instant gratification itself: all it takes is a mere few seconds for anybody to deploy a Python application, alive and well on a development server. I believe the cliche that the hardest part of anything is getting started, so it's no surprise that Flaks can get the imagination brewing.","Configuring apps isn't the sexiest topic to cover in the realm of hot new frameworks, which is precisely why most newcomers skip over this aspect of Flask development entirely. This level of short-term procrastination seems harmless to the untrained eye. From my perspective, it's like watching a generation of grown professionals postponing their child's potty-training by one more day: both cases ultimately end with grown adults shitting their pants.","Every web app needs to be configured with things like database URIs and secret keys to enable critical functionality. Unlike Django, there's no monolithic settings.py file in Flask (thank god). Instead, we can choose to configure Flask via several methods. Today we're covering two topics in Flask configuration: best practices in configuration structure and configuration settings themselves."]

@app.route("/first")
def first():
    return texts[0]
@app.route("/second")
def second():
    return texts[1]

@app.route("/third")
def third():
    return texts[2]