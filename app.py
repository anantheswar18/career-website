from flask import Flask,render_template,jsonify

app = Flask(__name__)


JOBS = [
    {
        "id":1,
        "name" : "Deepak Prabhu",
        "job title" : "Database Architect",
        "location" : "Kochi,Kerala"
    },
    {
        "id":2,
        "name" : "Titto Bobby",
        "job title" : "Database Developer",
        "location" : "Kochi,Kerala"
    },
    {
        "id":3,
        "name" : "Vivek",
        "job title" : "Quality Analyst",
        "location" : "Kochi,Kerala"
    },
    {
        "id":4,
        "name" : "Sulekha Naidu",
        "job title" : "Backend Senior Developer",
        "location" : "Bangalore,Karnataka"
    },
    {
        "id":5,
        "name" : "Aswin V S",
        "job title" : "Devops Engineer",
        "location" : "Kochi,Kerala"
    },
]

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/carrer")
def Second():
    return render_template("proHome.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

@app.route("/sreeja")
def forSreeja():
    return "Hey, Sreeja you are great.You are a great tutor,WOnderful,fantastic,elastic,gymnastic.......Advance Merry Christmas and Happy New Year 🎅🥳🍾🎇"


@app.route("/reema")
def forReema():
    return "Hey, Reema you are great.You are a great tutor,WOnderful,fantastic,elastic,gymnastic.......Advance Merry Christmas and Happy New Year 🎅🥳🍾🎇"

@app.route("/sadhika")
def forsadhika():
    return "Hey Sadhika Chechi, You are sooo good and sooo caring we love you sooo much espeaciallly me.Keep going like this. You are always in my prayers God bless you.Merry Christmas and Happy New Year 🥳🎅🍾😘🎇"



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
